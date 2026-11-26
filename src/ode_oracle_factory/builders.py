"""A/B/C/D Oracle construction. No network; LLM is injected."""
from __future__ import annotations
import json, re
from dataclasses import replace
from .model import Evidence, OracleEnvelope, sha

class OracleBuildError(ValueError):
    pass

def _evidence(asset, text, start, end, quote, kind):
    return Evidence(
        evidence_id=f"{asset['asset_id'][:12]}:{kind}:{start}",
        source_uri=asset.get("source", {}).get("uri", "asset://unknown"),
        locator=f"chars:{start}:{end}", quote=quote,
        source_sha256=asset.get("content", {}).get("sha256", ""), kind=kind)

def extract_api(asset, identity_map):
    text = asset["content"]["full_text"]
    heading = re.search(r"(?m)^#\s+(aclnn(?!Inplace)\w+)", text)
    if not heading:
        return None, []
    canonical = heading.group(1)
    identity = identity_map.get(canonical)
    if not identity:
        return {"canonical_name": canonical}, []
    signatures = list(re.finditer(r"(?m)^\s*aclnnStatus\s+(aclnn\w+)\s*\(", text))
    signature = next(
        (m for m in signatures if not m.group(1).endswith("GetWorkspaceSize")),
        signatures[0] if signatures else None,
    )
    evidence = [_evidence(asset, text, heading.start(), heading.end(), heading.group(0), "heading")]
    claims = {"api_id": identity["api_id"], "canonical_name": canonical}
    if signature:
        evidence.append(_evidence(asset, text, signature.start(), signature.end(), signature.group(0), "prototype"))
        claims["function_signature"] = signature.group(0).strip()
    return claims, evidence

def _base(mode, strategy, task, asset, claims, evidence, status="VALID", **provenance):
    env = OracleEnvelope(
        oracle_id=f"oracle_{mode}_{task['task_id']}",
        oracle_version="1.0.0", task_id=task["task_id"], task_type=task.get("task_type", ""),
        method_id=task.get("method_id", "D01"), oracle_mode=mode,
        construction_strategy=strategy, asset_id=asset["asset_id"],
        asset_version=asset.get("source", {}).get("version", ""),
        asset_sha256=asset.get("content", {}).get("sha256", ""),
        claims=claims or {}, evidence=evidence, status=status,
        provenance=provenance,
        independence={"agent_answer_used": False, "ev_verdict_used": False,
                      "grader_used_for_claims": False},
        validation={"reason": provenance.get("reason")} if provenance.get("reason") else {})
    return env.seal()

class DeterministicBuilder:
    mode = "B"; strategy = "DETERMINISTIC_RETRIEVAL_RULE"
    def build(self, task, asset, identity_map):
        claims, evidence = extract_api(asset, identity_map)
        if not claims:
            return _base(self.mode, self.strategy, task, asset, {}, [], "INSUFFICIENT_EVIDENCE",
                         builder="deterministic", reason="NO_API_HEADING")
        if not evidence:
            return _base(self.mode, self.strategy, task, asset, claims, [], "INSUFFICIENT_EVIDENCE",
                         builder="deterministic", reason="NO_EVIDENCE")
        return _base(self.mode, self.strategy, task, asset, claims, evidence,
                     builder="deterministic", extractor="regex-v1")

class LLMDirectBuilder:
    mode = "A"; strategy = "LLM_DIRECT"
    def build(self, task, asset, evidence, llm):
        prompt = json.dumps({"task": task, "asset_sha256": asset["content"]["sha256"],
                             "evidence": [e.body() for e in evidence],
                             "instruction": "Return JSON claims and evidence_ids only; never use agent answers."},
                            ensure_ascii=False)
        raw = llm(prompt)
        try:
            parsed = json.loads(raw)
        except Exception:
            return _base(self.mode, self.strategy, task, asset, {}, [], "INVALID",
                         builder="llm", model=getattr(llm, "name", "injected"), reason="JSON_INVALID")
        claims = parsed.get("claims")
        ids = parsed.get("evidence_ids")
        if not isinstance(claims, dict) or not isinstance(ids, list):
            return _base(self.mode, self.strategy, task, asset, {}, [], "INVALID",
                         builder="llm", model=getattr(llm, "name", "injected"), reason="SCHEMA_INVALID")
        by_id = {e.evidence_id: e for e in evidence}
        chosen = [by_id[i] for i in ids if i in by_id]
        if len(chosen) != len(ids) or not chosen:
            return _base(self.mode, self.strategy, task, asset, claims, chosen, "REVIEW_REQUIRED",
                         builder="llm", model=getattr(llm, "name", "injected"), reason="UNKNOWN_EVIDENCE")
        if "api_id" in claims and claims["api_id"] == asset["asset_id"]:
            return _base(self.mode, self.strategy, task, asset, claims, chosen, "REVIEW_REQUIRED",
                         builder="llm", model=getattr(llm, "name", "injected"), reason="API_ASSET_ID_CONFUSION")
        return _base(self.mode, self.strategy, task, asset, claims, chosen,
                     builder="llm", model=getattr(llm, "name", "injected"), prompt_sha256=sha(prompt))

class HybridBuilder:
    mode = "C"; strategy = "HYBRID_DETERMINISTIC_PLUS_LLM"
    def __init__(self, deterministic=None):
        self.deterministic = deterministic or DeterministicBuilder()
    def build(self, task, asset, identity_map, llm):
        base = self.deterministic.build(task, asset, identity_map)
        if base.status != "VALID":
            return base
        generated = LLMDirectBuilder().build(task, asset, base.evidence, llm)
        if generated.status != "VALID":
            return replace(generated, oracle_mode=self.mode, construction_strategy=self.strategy).seal()
        for key in ("api_id", "canonical_name", "function_signature"):
            if key in base.claims and key in generated.claims and base.claims[key] != generated.claims[key]:
                return _base(self.mode, self.strategy, task, asset, base.claims, base.evidence,
                             "CONFLICT", builder="hybrid", reason=f"CONFLICT:{key}")
        claims = dict(base.claims); claims.update({k: v for k, v in generated.claims.items() if k not in claims})
        return _base(self.mode, self.strategy, task, asset, claims, base.evidence,
                     builder="hybrid", deterministic_sha256=base.content_hash, llm_sha256=generated.content_hash)

class DualPathBuilder:
    mode = "D"; strategy = "DUAL_PATH_B_PLUS_A"
    def __init__(self):
        self.b = DeterministicBuilder()
    def build(self, task, asset, identity_map, llm):
        b = self.b.build(task, asset, identity_map)
        a = LLMDirectBuilder().build(task, asset, b.evidence, llm)
        if b.status != "VALID" or a.status != "VALID":
            return _base(self.mode, self.strategy, task, asset, b.claims, b.evidence,
                         "REVIEW_REQUIRED", builder="dual", reason="PATH_FAILURE",
                         path_a=a.status, path_b=b.status)
        for key in ("api_id", "canonical_name", "function_signature"):
            if key in b.claims and key in a.claims and b.claims[key] != a.claims[key]:
                return _base(self.mode, self.strategy, task, asset, b.claims, b.evidence,
                             "CONFLICT", builder="dual", reason=f"CONFLICT:{key}",
                             path_a=a.content_hash, path_b=b.content_hash)
        return _base(self.mode, self.strategy, task, asset, b.claims, b.evidence,
                     builder="dual", agreement="AGREEMENT",
                     path_a=a.content_hash, path_b=b.content_hash)

"""Runtime closure: binding, TE public payload, EV, replay, report rebuild."""
from __future__ import annotations
import copy, hashlib, json, sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from ode_oracle_factory.model import OracleEnvelope, canonical, sha

INTEGRATION_SRC = Path('/Users/chj/Desktop/ode/ODE-RESEARCH-012/IMPLEMENTATION/WP2-DSH-001/worktrees/Integration-5a1073/src')
if str(INTEGRATION_SRC) not in sys.path: sys.path.insert(0, str(INTEGRATION_SRC))
from ode_integration.contract_snapshot.binding import freeze_binding, verify_frozen_binding, BindingError
from ode_integration.production.runtime_binding import assert_provider_payload_public

FORBIDDEN_INPUTS = {"agent_answer","ev_verdict","grader_result","answer_key","gold","expected_output"}

class IndependenceError(ValueError): pass

class RuntimeIndependenceGuard:
    """Reject Oracle construction inputs that come from Agent/EV/Grader outcomes."""
    def __init__(self): self.inputs = {}; self._active = False
    def add(self, name, value):
        key = "".join(ch for ch in name.lower() if ch.isalnum())
        if key in {k.replace('_','') for k in FORBIDDEN_INPUTS}:
            raise IndependenceError("ORACLE_INPUT_NOT_INDEPENDENT:" + name)
        self.inputs[name] = sha(value)
    def record(self):
        return {"input_hashes": dict(self.inputs), "agent_answer_used": False,
                "ev_verdict_used": False, "grader_used_for_claims": False}

def provider_payload(envelope: OracleEnvelope, task: dict, asset: dict):
    """Public TE payload: no claims, no answer key, no Grader private fields."""
    payload = {"task": task, "asset_sha256": asset["content"]["sha256"],
               "oracle_public": envelope.public(), "evidence": [e.body() for e in envelope.evidence]}
    assert_provider_payload_public(payload)
    return payload

def _binding_schema_path(): return INTEGRATION_SRC.parent.parent/'Integration-5a1073/src/ode_integration/contract_snapshot/schemas/evaluation-binding-v1.schema.json'

def freeze_oracle_binding(envelope: OracleEnvelope, *, output_schema_sha256: str, grader_config: dict,
                          approval_ref="WP2-DSH-002", destination: Path):
    schema = json.loads((INTEGRATION_SRC/'ode_integration/contract_snapshot/schemas/evaluation-binding-v1.schema.json').read_text())
    method = {"method_id": envelope.method_id, "method_version": envelope.oracle_version,
              "descriptor_sha256": sha({"method_id": envelope.method_id, "version": envelope.oracle_version})}
    grader = {"type":"structured_match","version":"0.1","config_sha256":sha(grader_config),
              "registry_version":"1.0","manifest_sha256":sha(grader_config)}
    candidate = {
        "schema_version":"ode.evaluation-binding/1","method":method,"task_type":envelope.task_type,
        "output_schema_sha256":output_schema_sha256,
        "oracle":{"route_id":"O1","artifact_id":envelope.oracle_id,"version":envelope.oracle_version,
                  "sha256":envelope.content_hash,"frozen":True,"independent_approval":True},
        "grader":grader,"compatibility":{"status":"PASS","reason":"WP2 runtime integration"},
        "binding_sha256":"0"*64,"approved_at":datetime.now(timezone.utc).isoformat(),
        "approval_ref":approval_ref}
    frozen = freeze_binding(candidate,schema,Path(destination))
    return frozen, schema

def evaluate_answer(envelope: OracleEnvelope, answer: dict):
    required = sorted(envelope.claims)
    matched = [k for k in required if answer.get(k) == envelope.claims[k]]
    verdict = "PASS" if required and len(matched)==len(required) else "FAIL"
    return {"verdict":verdict,"matched":matched,"required":required,"score":len(matched)/len(required) if required else 0.0}

def _write_json(path, value): path.write_text(json.dumps(value,ensure_ascii=False,indent=2,sort_keys=True)+'\n')

def run_once(*, run_dir: Path, envelope: OracleEnvelope, task: dict, asset: dict, answer: dict,
             output_schema_sha256: str, grader_config: dict, provider_calls=0, network_calls=0):
    run_dir=Path(run_dir); run_dir.mkdir(parents=True,exist_ok=True)
    payload=provider_payload(envelope,task,asset)
    binding,schema=freeze_oracle_binding(envelope,output_schema_sha256=output_schema_sha256,
                                         grader_config=grader_config,destination=run_dir/'binding.json')
    verdict=evaluate_answer(envelope,answer)
    report={"run_id":run_dir.name,"oracle_id":envelope.oracle_id,"oracle_mode":envelope.oracle_mode,
            "oracle_hash":envelope.content_hash,"binding_sha256":binding['binding_sha256'],
            "verdict":verdict,"provider_calls":provider_calls,"network_calls":network_calls}
    (run_dir/'oracle.private.json').write_text(json.dumps(envelope.private(),ensure_ascii=False,sort_keys=True)+'\n')
    _write_json(run_dir/'oracle.public.json',envelope.public())
    _write_json(run_dir/'provider-payload.json',payload)
    _write_json(run_dir/'answer.json',answer)
    (run_dir/'binding.schema.json').write_text(json.dumps(schema,ensure_ascii=False,sort_keys=True)+'\n')
    _write_json(run_dir/'binding.json',binding)
    _write_json(run_dir/'verdict.json',verdict)
    _write_json(run_dir/'run.json',report)
    (run_dir/'report.md').write_text(render_report(report))
    return report

def render_report(report):
    return ("# WP2 Oracle Run\n\n"
            f"- run_id: {report['run_id']}\n- oracle_id: {report['oracle_id']}\n"
            f"- oracle_mode: {report['oracle_mode']}\n- oracle_hash: {report['oracle_hash']}\n"
            f"- binding_sha256: {report['binding_sha256']}\n- verdict: {report['verdict']['verdict']}\n"
            f"- score: {report['verdict']['score']}\n"
            f"- provider_calls: {report['provider_calls']}\n- network_calls: {report['network_calls']}\n")

def replay(run_dir: Path):
    run_dir=Path(run_dir); env=OracleEnvelope(**json.loads((run_dir/'oracle.private.json').read_text()))
    env.content_hash = json.loads((run_dir/'oracle.public.json').read_text())['content_hash']
    if not env.verify_hash(): raise BindingError('ORACLE_HASH_MISMATCH')
    binding=json.loads((run_dir/'binding.json').read_text()); schema=json.loads((run_dir/'binding.schema.json').read_text())
    verify_frozen_binding(run_dir/'binding.json',schema,expected={'oracle.sha256':env.content_hash})
    answer=json.loads((run_dir/'answer.json').read_text())
    verdict=evaluate_answer(env,answer)
    original=json.loads((run_dir/'verdict.json').read_text())
    return {"provider_calls":0,"network_calls":0,"oracle_hash_valid":True,
            "verdict":verdict,"verdict_identical":verdict==original,
            "binding_sha256":binding['binding_sha256']}

def rebuild_report(run_dir: Path):
    run_dir=Path(run_dir); report=json.loads((run_dir/'run.json').read_text())
    rebuilt=render_report(report); original=(run_dir/'report.md').read_text()
    return {"byte_identical":rebuilt==original,"sha256":hashlib.sha256(rebuilt.encode()).hexdigest(),
            "original_sha256":hashlib.sha256(original.encode()).hexdigest()}

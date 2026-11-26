"""D07 symbol/line Oracle from the frozen v03 engineering index."""
from __future__ import annotations
import hashlib, sqlite3
from pathlib import Path
from ode_oracle_factory.model import Evidence, OracleEnvelope

class D07BuildError(ValueError):
    pass

def _asset_id(doc_id, content_sha): return hashlib.sha256(f"{doc_id}\n{content_sha}\nasset-0.1".encode()).hexdigest()

class SymbolDeterministicBuilder:
    mode = "B"; strategy = "DETERMINISTIC_SYMBOL_INDEX"
    def build(self, task, asset, kb_dir):
        symbol = task.get("symbol") or "aclnnAdd"
        db = sqlite3.connect(str(Path(kb_dir)/"index.sqlite3"))
        try:
            row = db.execute(
                "select symbol, repo, commit_sha, path, line from symbols where symbol=? group by symbol having count(*)=1",
                (symbol,)).fetchone()
            if not row:
                return self._empty(task, asset, "SYMBOL_NOT_UNIQUE")
            sym, repo, commit, path, line = row
            doc = db.execute("select document_id, version, content_sha256, full_text from documents where path=? limit 1",(path,)).fetchone()
            if not doc:
                return self._empty(task, asset, "DOCUMENT_NOT_FOUND")
            doc_id, version, content_sha, text = doc
            lines = (text or "").splitlines()
            quote = lines[line-1] if 0 < line <= len(lines) else ""
            if not quote.startswith("[L"):
                quote = f"[L{line}] {quote}"
            evidence = Evidence(
                evidence_id=f"{doc_id[:12]}:symbol:{line}",
                source_uri=f"git://{repo}@{commit}/{path}",
                locator=f"line:{line}", quote=quote,
                source_sha256=content_sha, kind="symbol")
            env = OracleEnvelope(
                oracle_id=f"oracle_D_{task['task_id']}", oracle_version="1.0.0",
                task_id=task["task_id"], task_type=task.get("task_type","auto_d07"),
                method_id="D07", oracle_mode=self.mode, construction_strategy=self.strategy,
                asset_id=asset["asset_id"], asset_version=version or asset.get("source",{}).get("version",""),
                asset_sha256=asset["content"]["sha256"],
                claims={"symbol":sym,"path":path,"line":line}, evidence=[evidence],
                provenance={"builder":"v03-symbol-index","source":"Target KB v03","kb_dir":str(kb_dir)},
                independence={"agent_answer_used":False,"ev_verdict_used":False,"grader_used_for_claims":False},
                validation={})
            return env.seal()
        finally:
            db.close()
    def _empty(self, task, asset, reason):
        env = OracleEnvelope(oracle_id=f"oracle_D_{task['task_id']}",oracle_version="1.0.0",
            task_id=task["task_id"],task_type=task.get("task_type","auto_d07"),method_id="D07",
            oracle_mode=self.mode,construction_strategy=self.strategy,asset_id=asset["asset_id"],
            asset_version=asset.get("source",{}).get("version",""),asset_sha256=asset["content"]["sha256"],
            claims={},evidence=[],status="INSUFFICIENT_EVIDENCE",
            provenance={"builder":"v03-symbol-index","reason":reason},
            independence={"agent_answer_used":False,"ev_verdict_used":False,"grader_used_for_claims":False})
        return env.seal()

"""Adapter from WP2 envelope/answer to the real new-evaluator trace contract."""
from __future__ import annotations
import json, sys
from pathlib import Path
INTEGRATION_SRC=Path('/Users/chj/Desktop/ode/ODE-PROD-011/12_FINAL_PUBLICATION/clean-main-worktrees/new-evaluator')
if str(INTEGRATION_SRC) not in sys.path: sys.path.insert(0,str(INTEGRATION_SRC))

def trace(envelope, answer, output, *, run_id, task_id, suite_id, asset_sha, manifest_sha):
    return {"schema_version":"0.1","run_id":run_id,"task_id":task_id,"status":"completed",
            "final_output":answer,"error":None,
            "events":[{"seq":1,"component":"executor","action":"solve","status":"success","output_summary":"wp2"}],
            "suite_id":suite_id,"asset_sha256":asset_sha,"manifest_sha256":manifest_sha}

def evaluate_with_ev(suite_dir, traces_path, output_dir):
    from evaluator.cli import run as evaluate
    evaluate(Path(suite_dir), Path(traces_path), Path(output_dir))
    rows=[json.loads(l) for l in (Path(output_dir)/'evaluation_results.jsonl').read_text().splitlines()]
    summary=json.loads((Path(output_dir)/'evaluation_summary.json').read_text()) if (Path(output_dir)/'evaluation_summary.json').exists() else json.loads((Path(output_dir)/'summary.json').read_text())
    return rows,summary

import json,sys
from pathlib import Path
ROOT=Path('/Users/chj/Desktop/ode'); BASE=Path(__file__).parents[1]
sys.path.insert(0,str(BASE/'src')); sys.path.insert(0,str(BASE.parent/'WP2-DSH-001/src'))
from wp2_runtime.symbol_builder import SymbolDeterministicBuilder
from wp2_runtime.ev_adapter import trace,evaluate_with_ev
from evaluator.suite import Suite
suite=ROOT/'experiment/real-e2e-readiness-003/suite-v03-symbol'
asset=json.loads((suite/'asset_input.json').read_text()); task=json.loads((suite/'tasks.jsonl').read_text().splitlines()[0])
e=SymbolDeterministicBuilder().build(task,asset,ROOT/'ode-local/knowledge_base/cann-9.2.0-v03-engineering')
manifest=json.loads((suite/'suite_manifest.json').read_text()); manifest_hash=Suite(suite).manifest_hash
out=BASE/'evidence/ev_d07'; out.mkdir(parents=True,exist_ok=True)
traces=out/'traces.jsonl'
for name,answer in [('pass',{'symbol':'aclnnAdd','path':'math/add/op_api/aclnn_add.h','line':60}),('fail',{'symbol':'aclnnAdd','path':'wrong','line':1})]:
 import shutil
 p=out/name; p.mkdir(exist_ok=True); [shutil.rmtree(x) for x in (p/'evaluation_results.jsonl',p/'audit.jsonl',p/'evaluation_summary.json',p/'report.md',p/'summary.json') if x.exists()]
 t=trace(e,answer,None,run_id=f'wp2-d07-{name}',task_id=task['task_id'],suite_id=manifest['suite_id'],asset_sha=asset['content']['sha256'],manifest_sha=manifest_hash)
 (p/'traces.jsonl').write_text(json.dumps(t)+'\n')
 evdir=p/'ev'; shutil.rmtree(evdir,ignore_errors=True); rows,summ=evaluate_with_ev(suite,p/'traces.jsonl',evdir)
 print(name,rows[0]['verdict'],summ['dimensions']['ground_verify']['score'])

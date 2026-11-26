import json, sys, shutil
from pathlib import Path
ROOT=Path('/Users/chj/Desktop/ode'); BASE=Path(__file__).parents[1]
sys.path.insert(0,str(BASE/'src')); sys.path.insert(0,str(BASE.parent/'WP2-DSH-001/src'))
from ode_oracle_factory import DeterministicBuilder, LLMDirectBuilder, HybridBuilder, DualPathBuilder
from wp2_runtime import run_once, replay, rebuild_report, provider_payload, RuntimeIndependenceGuard
from wp2_runtime.runtime import IndependenceError
from wp2_runtime.symbol_builder import SymbolDeterministicBuilder
ASSET=json.loads((ROOT/'ODE-PROD-004/AUTO_D01_SUITE/asset_input.json').read_text())
TASK={'task_id':'task_d06_test','task_type':'auto_d06','method_id':'D06'}
ID={'aclnnAdd':{'api_id':'e73eb03c3bc1f30f8ca079eaedf484caf318fc7bf2aa6408d9d398980a191e34'}}
ANSWER={'api_id':ID['aclnnAdd']['api_id'],'canonical_name':'aclnnAdd','function_signature':'aclnnStatus aclnnAdd('}
class FakeLLM:
    name='fake-llm'
    def __init__(self,claims,ids=None): self.claims=claims; self.ids=ids or []
    def __call__(self,prompt): return json.dumps({'claims':self.claims,'evidence_ids':self.ids})
def clean(p):
    if p.exists(): shutil.rmtree(p)
out=BASE/'evidence'; clean(out); out.mkdir(parents=True)
runs=[]
def add(name,env,answer,kb='v02'):
    d=out/name; r=run_once(run_dir=d,envelope=env,task=TASK if kb=='v02' else {'task_id':'task_d07_aclnnadd_001','task_type':'auto_d07','method_id':'D07'},asset=ASSET if kb=='v02' else json.loads((ROOT/'experiment/real-e2e-readiness-003/suite-v03-symbol/asset_input.json').read_text()),answer=answer,output_schema_sha256='a'*64,grader_config={'type':'structured_match','version':'0.1'})
    rep=replay(d); reb=rebuild_report(d)
    rec={'name':name,'mode':env.oracle_mode,'status':env.status,'verdict':r['verdict']['verdict'],'replay':rep['verdict_identical'],'report_identical':reb['byte_identical'],'provider_calls':rep['provider_calls'],'network_calls':rep['network_calls'],'oracle_hash':env.content_hash,'binding':r['binding_sha256']}
    runs.append(rec); return rec
b=DeterministicBuilder().build(TASK,ASSET,ID); add('B_pass',b,ANSWER)
add('B_wrong',b,{'api_id':'wrong','canonical_name':'wrong'})
base_ev=b.evidence
for mode,builder,claims in [('A',LLMDirectBuilder(),{'api_id':ID['aclnnAdd']['api_id'],'canonical_name':'aclnnAdd'}),('C',HybridBuilder(),{'api_id':ID['aclnnAdd']['api_id'],'canonical_name':'aclnnAdd'}),('D',DualPathBuilder(),{'api_id':ID['aclnnAdd']['api_id'],'canonical_name':'aclnnAdd'})]:
    ids=[e.evidence_id for e in base_ev]
    env=builder.build(TASK,ASSET,ID if mode!='A' else base_ev,FakeLLM(claims,ids)) if mode!='A' else builder.build(TASK,ASSET,base_ev,FakeLLM(claims,ids))
    add(mode+'_pass',env,ANSWER)
suite=ROOT/'experiment/real-e2e-readiness-003/suite-v03-symbol'; a3=json.loads((suite/'asset_input.json').read_text()); t3=json.loads((suite/'tasks.jsonl').read_text().splitlines()[0])
d7=SymbolDeterministicBuilder().build(t3,a3,ROOT/'ode-local/knowledge_base/cann-9.2.0-v03-engineering')
add('D07_pass',d7,{'symbol':'aclnnAdd','path':'math/add/op_api/aclnn_add.h','line':60},kb='v03')
add('D07_wrong',d7,{'symbol':'aclnnAdd','path':'wrong','line':1},kb='v03')
# security evidence
sec={'payload_private_claims': '"claims":' not in json.dumps(provider_payload(b,TASK,ASSET)['oracle_public']),
     'guard_rejects_agent': False, 'guard_rejects_ev': False}
for key in ('agent_answer','ev_verdict'):
    try: RuntimeIndependenceGuard().add(key,{})
    except IndependenceError: sec['guard_rejects_'+key.split('_')[0]]=True
(out/'runs.json').write_text(json.dumps(runs,indent=2)+'\n')
(out/'security.json').write_text(json.dumps(sec,indent=2)+'\n')
(out/'gold.json').write_text(json.dumps({'cases':runs,'gold_source':'Target KB v02/v03'},indent=2)+'\n')
print(json.dumps({'runs':len(runs),'pass':sum(r['verdict']=='PASS' for r in runs),'fail':sum(r['verdict']=='FAIL' for r in runs),'replay_all':all(r['replay'] for r in runs),'report_all':all(r['report_identical'] for r in runs),'provider_calls':sum(r['provider_calls'] for r in runs),'security':sec},indent=2))

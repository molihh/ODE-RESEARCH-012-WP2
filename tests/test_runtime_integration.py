import json
from pathlib import Path
import pytest
from ode_oracle_factory import DeterministicBuilder, LLMDirectBuilder, HybridBuilder, DualPathBuilder
from wp2_runtime import run_once, replay, rebuild_report, provider_payload, RuntimeIndependenceGuard, evaluate_answer
from wp2_runtime.symbol_builder import SymbolDeterministicBuilder
from wp2_runtime.runtime import IndependenceError
from ode_integration.production.runtime_binding import BindingError

ROOT=Path('/Users/chj/Desktop/ode')
ASSET=json.loads((ROOT/'ODE-PROD-004/AUTO_D01_SUITE/asset_input.json').read_text())
TASK={'task_id':'task_d06_test','task_type':'auto_d06','method_id':'D06'}
IDENTITY={'aclnnAdd':{'api_id':'e73eb03c3bc1f30f8ca079eaedf484caf318fc7bf2aa6408d9d398980a191e34'}}
SCHEMA=json.loads((ROOT/'ODE-PROD-004/AUTO_D01_SUITE/asset_input.json').read_text())

class FakeLLM:
    name='fake-llm'
    def __init__(self, claims=None, ids=None): self.claims=claims; self.ids=ids
    def __call__(self,prompt): return json.dumps({'claims':self.claims or {'api_id':IDENTITY['aclnnAdd']['api_id'],'canonical_name':'aclnnAdd'},'evidence_ids':self.ids or []})

def env():
    return DeterministicBuilder().build(TASK,ASSET,IDENTITY)

def test_binding_and_run_replay_report(tmp_path):
    e=env(); r=run_once(run_dir=tmp_path/'run',envelope=e,task=TASK,asset=ASSET,
        answer={'api_id':IDENTITY['aclnnAdd']['api_id'],'canonical_name':'aclnnAdd','function_signature':'aclnnStatus aclnnAdd('},
        output_schema_sha256='a'*64,grader_config={'type':'structured_match','version':'0.1'})
    assert r['verdict']['verdict']=='PASS'; assert r['binding_sha256']
    rep=replay(tmp_path/'run'); assert rep['provider_calls']==0; assert rep['verdict_identical'] is True
    assert rep['oracle_hash_valid'] is True
    rb=rebuild_report(tmp_path/'run'); assert rb['byte_identical'] is True

def test_wrong_answer_fails(tmp_path):
    e=env(); r=run_once(run_dir=tmp_path/'run',envelope=e,task=TASK,asset=ASSET,
        answer={'api_id':'wrong','canonical_name':'wrong'},output_schema_sha256='a'*64,grader_config={})
    assert r['verdict']['verdict']=='FAIL'

def test_provider_payload_has_no_private_claims():
    e=env(); p=provider_payload(e,TASK,ASSET)
    assert '"claims":' not in json.dumps(p['oracle_public']); assert 'claims' not in p
    assert p['oracle_public']['claims_sha256']==e.public()['claims_sha256']

def test_private_payload_injection_blocked():
    e=env(); p=provider_payload(e,TASK,ASSET); p['oracle']={'claims':e.claims}
    with pytest.raises(BindingError): from wp2_runtime.runtime import assert_provider_payload_public as f; f(p)

def test_independence_guard_rejects_agent_and_ev():
    g=RuntimeIndependenceGuard(); g.add('asset',ASSET)
    with pytest.raises(IndependenceError): g.add('agent_answer',{'x':1})
    with pytest.raises(IndependenceError): g.add('ev_verdict',{'pass':1})

def test_v03_d07_build():
    suite=ROOT/'experiment/real-e2e-readiness-003/suite-v03-symbol'; asset=json.loads((suite/'asset_input.json').read_text()); task=json.loads((suite/'tasks.jsonl').read_text().splitlines()[0])
    e=SymbolDeterministicBuilder().build(task,asset,ROOT/'ode-local/knowledge_base/cann-9.2.0-v03-engineering')
    assert e.status=='VALID'; assert e.verify_hash()
    assert e.claims=={'symbol':'aclnnAdd','path':'math/add/op_api/aclnn_add.h','line':60}
    assert 'line:60' in e.evidence[0].locator

def test_four_modes_share_envelope_and_binding(tmp_path):
    e=env(); a=LLMDirectBuilder().build(TASK,ASSET,e.evidence,FakeLLM(ids=[e.evidence[0].evidence_id]))
    c=HybridBuilder().build(TASK,ASSET,IDENTITY,FakeLLM(ids=[e.evidence[0].evidence_id]))
    d=DualPathBuilder().build(TASK,ASSET,IDENTITY,FakeLLM(ids=[e.evidence[0].evidence_id]))
    for i,x in enumerate((e,a,c,d)):
        assert x.verify_hash()
        r=run_once(run_dir=tmp_path/f'run{i}',envelope=x,task=TASK,asset=ASSET,
            answer={'api_id':IDENTITY['aclnnAdd']['api_id'],'canonical_name':'aclnnAdd','function_signature':'aclnnStatus aclnnAdd('},
            output_schema_sha256='b'*64,grader_config={})
        assert r['binding_sha256']; assert replay(tmp_path/f'run{i}')['verdict_identical'] is True

def test_binding_tamper_fails(tmp_path):
    e=env(); r=run_once(run_dir=tmp_path/'run',envelope=e,task=TASK,asset=ASSET,answer={'api_id':IDENTITY['aclnnAdd']['api_id'],'canonical_name':'aclnnAdd','function_signature':'aclnnStatus aclnnAdd('},output_schema_sha256='a'*64,grader_config={})
    b=json.loads((tmp_path/'run/binding.json').read_text()); b['oracle']['sha256']='0'*64; (tmp_path/'run/binding.json').write_text(json.dumps(b))
    from wp2_runtime.runtime import verify_frozen_binding
    import pytest
    with pytest.raises(Exception): verify_frozen_binding(tmp_path/'run/binding.json',json.loads((tmp_path/'run/binding.schema.json').read_text()))

def test_evidence_tamper_invalidates_hash():
    e=env(); e.evidence[0]=type(e.evidence[0])(**{**e.evidence[0].body(),'quote':'tampered'})
    assert not e.verify_hash()

def test_insufficient_oracle_not_evaluated(tmp_path):
    e=DeterministicBuilder().build(TASK,ASSET,{})
    assert e.status=='INSUFFICIENT_EVIDENCE'
    r=run_once(run_dir=tmp_path/'run',envelope=e,task=TASK,asset=ASSET,answer={},output_schema_sha256='a'*64,grader_config={})
    assert r['verdict']['verdict']=='FAIL'

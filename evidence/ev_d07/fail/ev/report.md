# ODE-Agent Evaluation Report

Internal report format: ode-report-1.0.0

## 1. Report identity and versions

评分规则: v0.1.0 / approved
实现剖面: ode-evaluator-0.1.0-draft.1 / draft
公共契约: v0.1 / Review Draft

Suite: suite_v03_symbol / 0.1
Asset: fd807dc4fc419264dcc123dbb0e9f9aa7e20929c269c7a4051b08a8bffcb2c8c / 9.2.0
Package: 0.1.0.dev1
Generation time: unavailable; not recorded, deterministic offline reconstruction
Replay: Not asserted by generation; run replay to verify this bundle.

<details><summary>Identity, hashes and approval registration</summary>

<pre>{
  &quot;asset_id&quot;: &quot;fd807dc4fc419264dcc123dbb0e9f9aa7e20929c269c7a4051b08a8bffcb2c8c&quot;,
  &quot;asset_sha256&quot;: &quot;5d30cbee550d3d2fe1ca0fc995f52dd4a0c61bd4157847db25f66f243a4384ea&quot;,
  &quot;asset_version&quot;: &quot;9.2.0&quot;,
  &quot;generation_time&quot;: &quot;unavailable; not recorded, deterministic offline reconstruction&quot;,
  &quot;implementation_code_hashes&quot;: {
    &quot;__init__.py&quot;: &quot;89f9b584c524f50c6802317e700c2a8005adfd6588c52a7aaa433d3e1e38cf73&quot;,
    &quot;__main__.py&quot;: &quot;79ee6f134c5c5193377cf9b189cbdcc3e2095e49ba9cec310114441c15a917c4&quot;,
    &quot;cli.py&quot;: &quot;d5cbb894c3800b1012f99f74f48c04b59a716dc9333c688584e7e84d8816bc8f&quot;,
    &quot;core.py&quot;: &quot;75e6170f4764a44ae4c72b93f097965a988661fd54fb12a981293a9b4c3eb973&quot;,
    &quot;engine.py&quot;: &quot;3db25a30cb71440eb39358881affa75e44c9c98b6fb9f49ffba09fd9cc53ae5e&quot;,
    &quot;graders.py&quot;: &quot;bc0533c093a0188223e525667a74464c3f41e26f62579d06efd6ab9a43519b38&quot;,
    &quot;measurement.py&quot;: &quot;75bfc0c6541854016be82af25a8255457a0e62b335002ba7ba92693eb45399aa&quot;,
    &quot;plan.py&quot;: &quot;a934cd593fa2b98249186267af4267d8a345d9051ae5bd489720675531e218c0&quot;,
    &quot;preflight.py&quot;: &quot;8437fb133c4999bf9af60e58aa20581cfa35d95dfe68904504ebabce1b68b2c3&quot;,
    &quot;report_data/approved-rules-0.1.0.json&quot;: &quot;d273aee125b5034ae74bae03995fb6125641b7298129c8a1a07deefb82ae98cc&quot;,
    &quot;report_data/compatibility.json&quot;: &quot;4ee2cf9acf190006827cdb9b29bcd9ebc7ccf80ccc84098ea8d4f1040da2b9f2&quot;,
    &quot;report_metadata.py&quot;: &quot;ce3a27745cfe292cdd4891d2236e555dd8f3ab5f353e6fc2718ecfc3a8db58fe&quot;,
    &quot;reporting.py&quot;: &quot;1f6e02e6d9891a608164fab74dcde0ec635a3aa5d2bc3dca48ab17000c84fbdb&quot;,
    &quot;schemas/answer.json&quot;: &quot;2badffc9b2464f6b95ce8648eeff4bea698d6280e509b3609a9116280eee78fa&quot;,
    &quot;schemas/asset.json&quot;: &quot;7801787faacd84b932b1e38d871c62ea3ac4556b435012a4b4d80d0f46726a98&quot;,
    &quot;schemas/blueprint.json&quot;: &quot;85495d0a2bda08a2444fe0de8a42bf162350d66db6a7d1b3c3b5f426ba439bcf&quot;,
    &quot;schemas/manifest.json&quot;: &quot;32d67d24cfebaff1b0ad99aa0ac58e73d6729fc3a25e6e19a71725ce1c7b6d8d&quot;,
    &quot;schemas/quality.json&quot;: &quot;a3039ed04d399f1394c81c223ba8beb9270d3e8c8a24bb86e7136fb9dd4bf5f3&quot;,
    &quot;schemas/result.json&quot;: &quot;23527f034bc224e2f2d34154a67ab7254e57720120d1d4b82bc311a7a1db0313&quot;,
    &quot;schemas/review.json&quot;: &quot;becb251baf55367f4799e8119609f547cfe5521924800f62e2011219b4b32283&quot;,
    &quot;schemas/task.json&quot;: &quot;5fb642f7914f1b4f09288ba3c3dc9d5e0ebbc24cac06806dc2a8f780256808c5&quot;,
    &quot;schemas/trace.json&quot;: &quot;3486adf1762771ad254e5d9d0c201b9fba91b8363b1b7d767d44c6b7d4c04323&quot;,
    &quot;suite.py&quot;: &quot;aee614abd9e9434ef49f6b566be74f38b77274fe73eb2bdea074733c17f41194&quot;
  },
  &quot;implementation_profile&quot;: {
    &quot;status&quot;: &quot;draft&quot;,
    &quot;version&quot;: &quot;ode-evaluator-0.1.0-draft.1&quot;
  },
  &quot;manifest_sha256&quot;: &quot;24dcdc1cde71340bcac31f30ae12aeb2492a777ffadd608eb14fb0080ff402c3&quot;,
  &quot;package_version&quot;: &quot;0.1.0.dev1&quot;,
  &quot;provenance_status&quot;: &quot;Input/code hashes recorded; output hashes are in provenance.json.&quot;,
  &quot;public_contract&quot;: {
    &quot;status&quot;: &quot;Review Draft&quot;,
    &quot;version&quot;: &quot;0.1&quot;
  },
  &quot;replay_status&quot;: &quot;Not asserted by generation; run replay to verify this bundle.&quot;,
  &quot;scoring_rules&quot;: {
    &quot;record&quot;: &quot;rules/0.1.0.json&quot;,
    &quot;record_sha256&quot;: &quot;d273aee125b5034ae74bae03995fb6125641b7298129c8a1a07deefb82ae98cc&quot;,
    &quot;status&quot;: &quot;approved&quot;,
    &quot;version&quot;: &quot;0.1.0&quot;
  },
  &quot;suite_id&quot;: &quot;suite_v03_symbol&quot;,
  &quot;suite_version&quot;: &quot;0.1&quot;
}
</pre>

</details>

## 2. Executive summary

Tasks: 1; runs: 1; valid scoring runs: 1.
Run verdict counts: {&quot;fail&quot;: 1, &quot;invalid&quot;: 0, &quot;partial&quot;: 0, &quot;pass&quot;: 0}
Invalid categories: {}
Missing tasks: &#91;&#93;

| Dimension | Score | Task denominator | Valid runs |
| --- | --- | --- | --- |
| discover | null | 0 | 0 |
| understand | null | 0 | 0 |
| apply | null | 0 | 0 |
| ground_verify | 0.0 | 1 | 1 |

Engineering validity is distinct from Agent-Ready performance. No cross-dimension total; the four dimensions are not interchangeable.

## 3. Coverage and test suite

Asset type: engineering_evidence; frozen classification: engineering_evidence
Task types: {&quot;auto_d07&quot;: 1}
Target difficulty: {&quot;easy&quot;: 1}
not_calibrated; target difficulty is not calibrated difficulty
Uncovered dimensions: &#91;&quot;discover&quot;, &quot;understand&quot;, &quot;apply&quot;, &quot;ground_verify&quot;&#93;

| Grader | Version | Purpose |
| --- | --- | --- |
| structured_match | 0.1 | Pinned Designer field comparison |


## 4. Dimension metrics and denominators

### discover

Score: null; denominator_tasks: 0; valid_runs: 0
Run verdict counts (tasks declaring this dimension): {&quot;fail&quot;: 0, &quot;invalid&quot;: 0, &quot;partial&quot;: 0, &quot;pass&quot;: 0}

未测量 / no valid scored task denominator.

| Measuring task | Checkpoint | Grader | Version |
| --- | --- | --- | --- |

### understand

Score: null; denominator_tasks: 0; valid_runs: 0
Run verdict counts (tasks declaring this dimension): {&quot;fail&quot;: 0, &quot;invalid&quot;: 0, &quot;partial&quot;: 0, &quot;pass&quot;: 0}

未测量 / no valid scored task denominator.

| Measuring task | Checkpoint | Grader | Version |
| --- | --- | --- | --- |

### apply

Score: null; denominator_tasks: 0; valid_runs: 0
Run verdict counts (tasks declaring this dimension): {&quot;fail&quot;: 0, &quot;invalid&quot;: 0, &quot;partial&quot;: 0, &quot;pass&quot;: 0}

未测量 / no valid scored task denominator.

| Measuring task | Checkpoint | Grader | Version |
| --- | --- | --- | --- |

### ground_verify

Score: 0.0; denominator_tasks: 1; valid_runs: 1
Run verdict counts (tasks declaring this dimension): {&quot;fail&quot;: 1, &quot;invalid&quot;: 0, &quot;partial&quot;: 0, &quot;pass&quot;: 0}

| Task | Score |
| --- | --- |
| task_d07_aclnnadd_001 | 0.0 |

| Measuring task | Checkpoint | Grader | Version |
| --- | --- | --- | --- |

Valid retries average within task; then measured tasks average equally. invalid/null excluded; missing is not failure.
Valid-run null means unmeasured. Invalid-run null means no valid ability score.

## 5. Per-task results

### Task task_d07_aclnnadd_001

Type: auto_d07; difficulty: {&quot;calibration_status&quot;: &quot;not_calibrated&quot;, &quot;target_level&quot;: &quot;easy&quot;}

#### Run wp2-d07-fail

Execution: completed; verdict: fail; validity: valid
Dimension scores: {&quot;apply&quot;: null, &quot;discover&quot;: null, &quot;ground_verify&quot;: 0.0, &quot;understand&quot;: null}
Checkpoints passed/executed: 0/1; configured: 0.
Failure reason code: OUTPUT_CHECK_FAILED; recorded error code: null
Recorded error present: False (raw details withheld).

| Checkpoint | Dimension | Grader | Version | Passed |
| --- | --- | --- | --- | --- |
| structured_match:task_d07_aclnnadd_001 | ground_verify | structured_match | 0.1 | False |

| Trace seq | Component | Action | Status |
| --- | --- | --- | --- |
| 1 | executor | solve | success |

Location check: {&quot;required&quot;: false, &quot;supported&quot;: null}
Source locator unavailable / not recorded.
Location checks do not prove semantic support. Raw errors, prompts and answer text are withheld.


## 6. Failure diagnosis and evidence chain

### D0001 — output_check_failed

Evidence level: direct
Observable output checkpoints did not pass.
Evidence: task=task_d07_aclnnadd_001, run=wp2-d07-fail, checkpoint=structured_match:task_d07_aclnnadd_001, source=audit.checkpoints
Limitation: Final output alone cannot identify retrieval, reasoning or asset failure.

### D0002 — asset_evidence_gap

Evidence level: insufficient
Review hypothesis only; no direct evidence establishes this gap.
Evidence: task=task_d07_aclnnadd_001, run=wp2-d07-fail, checkpoint=structured_match:task_d07_aclnnadd_001, source=audit.checkpoints
Limitation: evidence_insufficient; do not assert a defect or causal origin.

### D0003 — test_design_gap

Evidence level: insufficient
Review hypothesis only; no direct evidence establishes this gap.
Evidence: task=task_d07_aclnnadd_001, run=wp2-d07-fail, checkpoint=structured_match:task_d07_aclnnadd_001, source=audit.checkpoints
Limitation: evidence_insufficient; do not assert a defect or causal origin.


## 7. Knowledge asset improvement recommendations

### R0001 — human_review

Problem: Some observable checks failed.
Action: Check the official asset, task design and output requirements before proposing changes.
Evidence level: indicative; Failed checkpoint outcomes are a review signal.
Evidence: task=task_d07_aclnnadd_001, run=wp2-d07-fail, checkpoint=structured_match:task_d07_aclnnadd_001, source=audit.checkpoints
Limitation: Repeated failures do not establish a knowledge asset defect.
Verify: Inspect the versioned official source and add a reviewed counterexample task.


## 8. Execution strategy comparison


<pre>{
  &quot;confounders&quot;: [],
  &quot;groups&quot;: [],
  &quot;message&quot;: &quot;本轮无可用策略比较数据&quot;,
  &quot;status&quot;: &quot;unavailable&quot;
}
</pre>


## 9. Limitations and reproducibility

### Scope and human review

- No weighted cross-dimension total; four dimensions are not interchangeable.
- Engineering execution validity and measured output performance are distinct.
- null means unmeasured for valid runs; invalid null means no valid score. Missing tasks are not capability failures.
- Valid retries average within each task, then measured tasks average equally; invalid/null excluded.
- No semantic evidence support, causal root attribution, measurement validity, human agreement or difficulty calibration is established.
- Unsigned local provenance supports integrity/recomputation, not adversarial authenticity.
- Human review is needed before modifying assets, test design or execution policy.


<pre>{
  &quot;commands&quot;: [
    &quot;ode-evaluator replay &lt;bundle&gt;&quot;,
    &quot;ode-evaluator report &lt;bundle&gt; &lt;new-report-directory&gt;&quot;,
    &quot;python -m tools.check_summary &lt;bundle&gt;&quot;
  ],
  &quot;data_origin&quot;: &quot;Offline/fixture-compatible evaluation; no live provider calls are made. Real producer provenance is not verified by this tool.&quot;,
  &quot;independent_recomputation&quot;: &quot;Not asserted by generation; run tools.check_summary.&quot;,
  &quot;input_sha256&quot;: {
    &quot;inputs/answer_keys.jsonl&quot;: &quot;7296a83f135acff3ba48dfab67619d9f3af8214fd0eaebd9871ffc6916fe7496&quot;,
    &quot;inputs/asset_input.json&quot;: &quot;5fa434373bbd2debf975803fb8d4f4788ac0e2b1795320e3d4ea775c1e049884&quot;,
    &quot;inputs/blueprint.json&quot;: &quot;8f4ce844c0aa046d73c2346afd93e34ed30d1a0fa90fd7b500127ff1d97af5bb&quot;,
    &quot;inputs/quality_gate_result.json&quot;: &quot;c22292417eaa31b40f8f779e79eccbe6a2732c47f810efa6af1862e9ecaf682d&quot;,
    &quot;inputs/review_results.jsonl&quot;: &quot;ed94e462b1d1a5eddb093bf5e33dc38d29725503bf28369eaa49b85bd9311313&quot;,
    &quot;inputs/suite_manifest.json&quot;: &quot;24dcdc1cde71340bcac31f30ae12aeb2492a777ffadd608eb14fb0080ff402c3&quot;,
    &quot;inputs/tasks.jsonl&quot;: &quot;06a7d440e650cd5932ed2e086f5af1f52709f2ed0569c5acebb11d5d04d0ce7a&quot;,
    &quot;inputs/traces.jsonl&quot;: &quot;4d3eebef38098d6ed2cbf97c87c6420927b3f0ecb0554bd079d009aa9d101d81&quot;
  },
  &quot;output_hash_reference&quot;: &quot;provenance.json files map (avoids self-hash cycle)&quot;
}
</pre>



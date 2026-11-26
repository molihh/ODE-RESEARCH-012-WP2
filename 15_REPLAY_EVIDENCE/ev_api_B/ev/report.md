# ODE-Agent Evaluation Report

Internal report format: ode-report-1.0.0

## 1. Report identity and versions

评分规则: v0.1.0 / approved
实现剖面: ode-evaluator-0.1.0-draft.1 / draft
公共契约: v0.1 / Review Draft

Suite: suite_wp2_api / 0.1
Asset: 47e5ec0b0f4f5d80827aeaebee5a86275a0544cb8a93eeb5ebcc2d66bc8c7549 / 9.2.0
Package: 0.1.0.dev1
Generation time: unavailable; not recorded, deterministic offline reconstruction
Replay: Not asserted by generation; run replay to verify this bundle.

<details><summary>Identity, hashes and approval registration</summary>

<pre>{
  &quot;asset_id&quot;: &quot;47e5ec0b0f4f5d80827aeaebee5a86275a0544cb8a93eeb5ebcc2d66bc8c7549&quot;,
  &quot;asset_sha256&quot;: &quot;8878a5f15e148d363a6a2baa8ae78efaea5e49373c530b0f9b4784979e65f9c6&quot;,
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
  &quot;manifest_sha256&quot;: &quot;b67a2789cfdf638f24cdce18fd02d960d8d8b23744f57b0b72ee1486179f3aa2&quot;,
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
  &quot;suite_id&quot;: &quot;suite_wp2_api&quot;,
  &quot;suite_version&quot;: &quot;0.1&quot;
}
</pre>

</details>

## 2. Executive summary

Tasks: 1; runs: 1; valid scoring runs: 1.
Run verdict counts: {&quot;fail&quot;: 0, &quot;invalid&quot;: 0, &quot;partial&quot;: 0, &quot;pass&quot;: 1}
Invalid categories: {}
Missing tasks: &#91;&#93;

| Dimension | Score | Task denominator | Valid runs |
| --- | --- | --- | --- |
| discover | 1.0 | 1 | 1 |
| understand | null | 0 | 0 |
| apply | null | 0 | 0 |
| ground_verify | null | 0 | 0 |

Engineering validity is distinct from Agent-Ready performance. No cross-dimension total; the four dimensions are not interchangeable.

## 3. Coverage and test suite

Asset type: api; frozen classification: api
Task types: {&quot;auto_d06&quot;: 1}
Target difficulty: {&quot;easy&quot;: 1}
not_calibrated; target difficulty is not calibrated difficulty
Uncovered dimensions: &#91;&quot;discover&quot;, &quot;understand&quot;, &quot;apply&quot;, &quot;ground_verify&quot;&#93;

| Grader | Version | Purpose |
| --- | --- | --- |
| structured_match | 0.1 | Pinned Designer field comparison |


## 4. Dimension metrics and denominators

### discover

Score: 1.0; denominator_tasks: 1; valid_runs: 1
Run verdict counts (tasks declaring this dimension): {&quot;fail&quot;: 0, &quot;invalid&quot;: 0, &quot;partial&quot;: 0, &quot;pass&quot;: 1}

| Task | Score |
| --- | --- |
| task_wp2_api_001 | 1.0 |

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

Score: null; denominator_tasks: 0; valid_runs: 0
Run verdict counts (tasks declaring this dimension): {&quot;fail&quot;: 0, &quot;invalid&quot;: 0, &quot;partial&quot;: 0, &quot;pass&quot;: 0}

未测量 / no valid scored task denominator.

| Measuring task | Checkpoint | Grader | Version |
| --- | --- | --- | --- |

Valid retries average within task; then measured tasks average equally. invalid/null excluded; missing is not failure.
Valid-run null means unmeasured. Invalid-run null means no valid ability score.

## 5. Per-task results

### Task task_wp2_api_001

Type: auto_d06; difficulty: {&quot;calibration_status&quot;: &quot;not_calibrated&quot;, &quot;target_level&quot;: &quot;easy&quot;}

#### Run wp2-api-B

Execution: completed; verdict: pass; validity: valid
Dimension scores: {&quot;apply&quot;: null, &quot;discover&quot;: 1.0, &quot;ground_verify&quot;: null, &quot;understand&quot;: null}
Checkpoints passed/executed: 1/1; configured: 0.
Failure reason code: null; recorded error code: null
Recorded error present: False (raw details withheld).

| Checkpoint | Dimension | Grader | Version | Passed |
| --- | --- | --- | --- | --- |
| structured_match:task_wp2_api_001 | discover | structured_match | 0.1 | True |

| Trace seq | Component | Action | Status |
| --- | --- | --- | --- |
| 1 | executor | solve | success |

Location check: {&quot;required&quot;: false, &quot;supported&quot;: null}
Source locator unavailable / not recorded.
Location checks do not prove semantic support. Raw errors, prompts and answer text are withheld.


## 6. Failure diagnosis and evidence chain

证据不足 / No failure diagnosis available; no root cause inferred.

## 7. Knowledge asset improvement recommendations

不可用 / No evidence-backed improvement recommendation. Passing fixtures do not prove asset completeness.

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
    &quot;inputs/answer_keys.jsonl&quot;: &quot;eaeba5c3ce5a968313258b0aeb0e9b518514bd4acf367975aa7a6599837bba2d&quot;,
    &quot;inputs/asset_input.json&quot;: &quot;47047a14261b8baedce4337162fa1b5a0f0bcfe15a4dc59236f9db01041b9a9b&quot;,
    &quot;inputs/blueprint.json&quot;: &quot;ebcf956b0692606363cad28535fff0344c8591351f3350e665755d64a25728cc&quot;,
    &quot;inputs/quality_gate_result.json&quot;: &quot;49a16828cf5db7ef30a5868326efa249b7e550a9164c05d5884804686862c65d&quot;,
    &quot;inputs/review_results.jsonl&quot;: &quot;8cd7882680e15645901cf725894e0e1d42a4aed09f9e77a6a50bffb2b1533840&quot;,
    &quot;inputs/suite_manifest.json&quot;: &quot;b67a2789cfdf638f24cdce18fd02d960d8d8b23744f57b0b72ee1486179f3aa2&quot;,
    &quot;inputs/tasks.jsonl&quot;: &quot;accbeaa243c08a4eaa6aba617433c066d6b1d0a8c36633270113745785a73c0b&quot;,
    &quot;inputs/traces.jsonl&quot;: &quot;92cfaf74a4ea916a113c7f07bf929ceafa559e25fc41722db60fc4dda67e9dae&quot;
  },
  &quot;output_hash_reference&quot;: &quot;provenance.json files map (avoids self-hash cycle)&quot;
}
</pre>



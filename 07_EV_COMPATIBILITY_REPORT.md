# EV Compatibility

Status: **PASS — actual new-evaluator for A/B/C/D and D07**

Local `evaluate_answer` compares claims deterministically and returns PASS/FAIL/score; used for 7 runs.

Results: 5 PASS, 2 FAIL (wrong answers); replay identical 7/7.

Actual `new-evaluator` was used for v03 D07: correct `aclnnAdd/path/line` -> PASS (ground_verify=1.0); wrong path/line -> FAIL (0.0).

Actual new-evaluator results:

```text
A: pass (discover=1.0)
B: pass (discover=1.0)
C: pass (discover=1.0)
D: pass (discover=1.0)
D07: pass (ground_verify=1.0); wrong D07: fail
```

Suite: `evidence/suite-wp2-api`, preflight READY.

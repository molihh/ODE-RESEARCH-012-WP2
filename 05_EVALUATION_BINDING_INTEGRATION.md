# EvaluationBinding Integration

Status: **PASS (local runtime)**

Uses WP4 `freeze_binding` / `verify_frozen_binding` and `evaluation-binding-v1` schema; no second registry.

Binding fields: task type, method, output schema hash, Oracle ID/version/hash, Grader type/config hash, compatibility, approval ref.

Tests:

- freeze + verify PASS;
- Oracle hash tamper -> FAIL;
- replay verifies same binding;
- binding SHA persisted.

Caveat: this is tested in the WP2 runtime, not in full `run_integrated`.

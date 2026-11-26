# TE Oracle Isolation

Status: **PASS (provider-payload level)**

`provider_payload` includes task, asset hash, public Oracle metadata, evidence; it removes `claims` (only `claims_sha256` remains).

- `assert_provider_payload_public` used.
- Injecting an `oracle` private object raises `BindingError`.
- No AnswerKey/Grader private fields in payload.

Not run: real Provider HTTP payload capture; runtime TE in full T1–T7.

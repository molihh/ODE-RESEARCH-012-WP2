# Security and Adversarial Test Report

Status: **PARTIAL**

Implemented tests:

- private Oracle claims absent from public payload;
- forbidden `oracle` key injection -> `BindingError`;
- Agent/EV input rejected by independence guard;
- Oracle hash tamper detected;
- evidence tamper invalidates hash;
- binding tamper fails verification.

Not run:

- prompt-injection through malicious Evidence into a real LLM;
- network-level isolation;
- frontend private-data leak test.

No network calls were made.

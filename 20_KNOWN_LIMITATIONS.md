# Known Limitations

1. A/C/D use Fake LLM; real model Oracle quality is not verified.
2. EV uses a local deterministic evaluator, not `new-evaluator` Grader registry.
3. No full `run_integrated` T1–T7 run.
4. Gold Benchmark is local, without independent human Gold; Oracle correctness is NOT_MEASURED.
5. Prompt-injection/network isolation tests not run.
6. D07 support is Oracle-building only; D07 method production eligibility is unchanged.
7. No push/merge; baseline repos remain frozen.

# WP2-DSH-002 Runtime Integration

Wraps WP2-DSH-001 four-mode factory into:
- D07 v03 symbol Oracle;
- EvaluationBinding freeze/verify;
- TE public payload isolation;
- EV structured evaluation;
- offline replay and report rebuild.

Run:
```bash
PYTHONPATH=src:../WP2-DSH-001/src python -m pytest -q tests
PYTHONPATH=src:../WP2-DSH-001/src python scripts/run_wp2_evidence.py
```
No real Provider/network calls.

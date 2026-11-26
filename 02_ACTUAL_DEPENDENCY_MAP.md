# Actual Dependency Map

```text
WP2-DSH-001 OracleEnvelope/Builders
        ↓
WP2-DSH-002 runtime.py
  ├─ provider_payload -> TE public
  ├─ freeze_binding -> WP4 EvaluationBinding schema
  ├─ evaluate_answer -> local EV
  ├─ replay -> verify Oracle/binding
  └─ rebuild_report
        ↓
evidence/ runs (7)
```

D07 uses `SymbolDeterministicBuilder` -> v03 `symbols` table.

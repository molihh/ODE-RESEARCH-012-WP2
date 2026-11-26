# Final Architecture

```text
WP2-001 A/B/C/D builders
        │
        ▼
OracleEnvelope (private claims/public metadata)
        │
        ├─ provider_payload → TE public
        ├─ freeze_binding → WP4 EvaluationBinding
        ├─ evaluate_answer → local EV verdict
        ├─ replay → verify Oracle/binding, no rebuild
        └─ rebuild_report → byte identity
```

D07: `SymbolDeterministicBuilder` reads v03 `symbols` and emits symbol/path/line.

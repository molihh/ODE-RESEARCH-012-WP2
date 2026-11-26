# T1–T7 Oracle Factory Integration

Status: **PARTIAL**

Integrated in local runtime:

```text
Oracle build -> Envelope -> Binding freeze -> TE public payload -> EV local verdict
-> persistence -> replay -> report rebuild
```

Not integrated:

- full `run_integrated` T1–T7 runner;
- TD method selection -> Oracle mode selection;
- new-evaluator Grader registry;
- production TE Provider call path;
- frontend display of Oracle mode/provenance.

The local closure proves the contracts can be connected, but not full ODE production integration.

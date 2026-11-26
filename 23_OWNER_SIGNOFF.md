# Owner 签收清单（WP2 最终 PASS 唯一剩余项）

WP2 工程证据已经完成；以下为需要 Owner 人工确认的事项：

## 必选

- [ ] 接受 **deterministic KB Gold** 作为 Gold Benchmark 依据（不使用人工双盲 Gold）。
  - 依据：`evidence/suite-wp2-api/answer_keys.jsonl`、`benchmark`/Target KB v02 facts、v03 symbols 表。
  - 影响：`GOLD_BENCHMARK=PASS_DETERMINISTIC`，`HUMAN_GOLD=NOT_RUN`。

## 需要知悉（不阻塞工程 PASS）

- [ ] 真实 Provider 验证仍为 `NOT_RUN`；A/C/D 只完成 Fake LLM 工程验证。
- [ ] T1–T7 注入 Run 使用 baseline ERKB；真实 external ERKB 使用 ODE-PROD-011 历史证据。
- [ ] 未推送/未合并任何 main。

## Owner 签字

```text
Owner: ____________________
Date:  ____________________
Decision: ACCEPT_DETERMINISTIC_KB_GOLD / REJECT
```

签字后，将 `19_FINAL_ACCEPTANCE_MATRIX.md` 的 `WP2_FINAL` 从 `PASS_CANDIDATE` 改为 `PASS`。

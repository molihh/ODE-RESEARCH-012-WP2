# Deterministic KB Gold Review（签收版）

状态：**PASS_DETERMINISTIC，Owner 已签收（2026-11-26）**

## 1. Gold 到底是什么

本 Gold 不是 Oracle Builder 自己生成的答案，而是从冻结的 Target KB 表中直接读取的事实：

```text
v02 Target KB: apis 表
v03 Target KB: symbols / documents 表
```

Builder 只能读取这些字段；Gold 的期望值是事先从表里冻结的。

## 2. Gold Case 1 — v02 官方 API Identity

Task：

```json
{
  "task_id": "task_wp2_api_001",
  "task_type": "auto_d06",
  "prompt": "给出该 API 的 official api_id（Target KB APIs 表中的 64 位 API ID）与 canonical_name；不要把 asset_id 当作 api_id。"
}
```

Expected：

```json
{
  "api_id": "e73eb03c3bc1f30f8ca079eaedf484caf318fc7bf2aa6408d9d398980a191e34",
  "canonical_name": "aclnnAdd"
}
```

Target KB v02 实际行：

```text
apis.api_id      = e73eb03c3bc1f30f8ca079eaedf484caf318fc7bf2aa6408d9d398980a191e34
apis.official_name = aclnnAdd
apis.version     = 9.2.0
apis.api_kind    = aclnn
```

Evidence：

```text
source_uri: https://raw.gitcode.com/cann/ops-math/raw/9.2.0/math/add/docs/aclnnAdd&aclnnInplaceAdd.md
start_line: 1
end_line:   1
quote:      # aclnnAdd&aclnnInplaceAdd
```

关键区分：

```text
API_ID   = e73eb03c…a191e34
ASSET_ID = 47e5ec0b…c8c7549
```

两者不相同；Gold 明确要求 `api_id`，不能拿 `asset_id` 冒充。

文件：

```text
evidence/suite-wp2-api/answer_keys.jsonl
evidence/suite-wp2-api/tasks.jsonl
```

## 3. Gold Case 2 — v02 Function Signature

来自 v02 `apis.record.evidence` 的 prototype：

```text
source_uri: https://raw.gitcode.com/cann/ops-math/raw/9.2.0/math/add/docs/aclnnAdd&aclnnInplaceAdd.md
locator:    chars:1230:1251
start_line: 55
quote:      aclnnStatus aclnnAdd(
```

Expected：

```json
{"function_signature": "aclnnStatus aclnnAdd("}
```

本 case 用于验证 B 不会错误选中 `aclnnAddGetWorkspaceSize`。

## 4. Gold Case 3 — v03 D07 Symbol/Path/Line

Target KB v03 `symbols` 表实际行：

```text
symbol     = aclnnAdd
repo       = https://gitcode.com/cann/ops-math.git
commit_sha = 5d4daae8a7b21d87f9a2c6e11cb0d62ac0085b53
path       = math/add/op_api/aclnn_add.h
line       = 60
```

Expected：

```json
{"symbol": "aclnnAdd", "path": "math/add/op_api/aclnn_add.h", "line": 60}
```

Evidence：

```text
source_uri: git://https://gitcode.com/cann/ops-math.git@5d4daae8.../math/add/op_api/aclnn_add.h
locator:    line:60
quote:      ACLNN_API aclnnStatus aclnnAdd(...)
```

## 5. Gold 运行结果

```text
B_pass       B  PASS   replay=true  report=true
B_wrong      B  FAIL   replay=true  report=true
A_pass       A  PASS   replay=true  report=true
C_pass       C  PASS   replay=true  report=true
D_pass       D  PASS   replay=true  report=true
D07_pass     B  PASS   replay=true  report=true
D07_wrong    B  FAIL   replay=true  report=true
```

实际 `new-evaluator`：

```text
A: pass, discover=1.0
B: pass, discover=1.0
C: pass, discover=1.0
D: pass, discover=1.0
D07 correct: pass, ground_verify=1.0
D07 wrong:   fail, ground_verify=0.0
```

注意：`oracle_correctness` 仍标记 `NOT_MEASURED`，因为上述是 deterministic KB Gold，不是人工双盲 Gold。

## 6. 独立性说明

```text
Gold 来源: 冻结 Target KB v02 apis / v03 symbols
Builder 角色: 读取同一 KB 并构建 Oracle
Gold 是否由 Builder 自评: 否
Oracle 是否把 Gold 当作输入: 否
人工双盲: NOT_RUN
```

## 7. 签收选项

如果接受：

```text
接受 deterministic KB Gold 作为 WP2 Gold Benchmark 依据；
接受 HUMAN_GOLD = NOT_RUN；
不把 deterministic Gold 等同于人工双盲 Gold。
```

则 `GOLD_BENCHMARK=PASS_DETERMINISTIC`，可以进入 `WP2_FINAL=PASS`。

如果不接受，必须补人工双盲 Gold，当前保持 `PASS_CANDIDATE`。

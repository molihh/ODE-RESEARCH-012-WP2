# v02 / v03 Oracle Compatibility

## v02

Deterministic API identity/signature; API ID and Asset ID remain distinct. 2 gold cases PASS.

## v03 D07

`SymbolDeterministicBuilder` queries frozen `symbols` table:

```text
aclnnAdd -> math/add/op_api/aclnn_add.h:60
```

Evidence: `line:60` + quote + source URI + content SHA. Correct answer PASS; wrong path/line FAIL.

Version isolation: D07 uses v03 index SHA `6cd32105…`; v02 uses v02 asset. No cross-version fallback.

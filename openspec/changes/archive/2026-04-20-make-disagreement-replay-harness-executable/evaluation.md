# Evaluation

## Baseline Scenarios

1. replay harness 只有 wiki 模板
   - 验证者仍然需要人工判断字段是否缺失。
2. replay 记录缺少显式 pass-condition
   - 即使字段齐全，也没有最小可执行合同去约束“什么算通过”。
3. 没有真实运行的 harness 命令
   - 只能说有方法，没有 repo-local executable proof。

## Before Results

- `wiki/ops/disagreement-management-replay-harness.md` 只是一页说明文档。
- 仓库没有脚本检查 replay 记录的字段完整性和 pass-condition。
- 也没有 sample replay record 可以被程序直接验证。

## After Results

- 仓库现在新增了可执行检查器：
  - `scripts/disagreement_replay_check.py`
- 仓库现在新增了 sample replay record：
  - `scripts/examples/disagreement_stage_boundary_replay.json`
- `wiki/ops/disagreement-management-replay-harness.md` 现在明确记录了 executable usage 和 proof boundary。
- 真实执行结果已跑通：
  - `python3 scripts/disagreement_replay_check.py scripts/examples/disagreement_stage_boundary_replay.json`
  - Result: `PASS: replay record satisfies the executable disagreement replay contract.`

## Residual Risks

- 这个 executable harness 只验证结构合同，不验证底层分歧语义。
- 通过结果不等于 replay 内容本身一定高质量。
- rollout proof 仍然不存在。

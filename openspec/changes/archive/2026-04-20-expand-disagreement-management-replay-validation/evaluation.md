# Evaluation

## Baseline Scenarios

1. 没有 repo-visible replay harness
   - 未来验证者只能重读旧 change，缺少统一 replay 面。
2. 只有前两种已知分歧类型
   - governance-shaped disagreement
   - method self-compression disagreement
3. design 与 validation 的阶段边界仍可能模糊

## Before Results

- 方法已经正式化，但 replay 证据仍然偏集中在上一条 change 的设计和评估里。
- 仓库还没有一个单独可复用的 replay harness。
- 新的阶段边界型分歧还没有 repo-visible replay 记录。

## After Results

- 仓库现在新增了 [分歧管理 Replay Harness](../../../wiki/ops/disagreement-management-replay-harness.md)。
- 仓库现在新增了 [分歧管理 Replay 验证 2026-04-20](../../../wiki/ops/disagreement-management-replay-validation-2026-04-20.md)。
- 新 replay 覆盖了第三种分歧形状：
  - `stage-boundary disagreement`
- 新验证明确保留：
  - rejected framing
  - correction pressure
  - redirection moment
  - clarity state
  - protected target
  - RED baseline
  - GREEN result
  - residual risk
- 新验证明确写出：
  - replay proof 强于纯 narrative design reasoning
  - 但仍然不是 rollout proof

## Residual Risks

- 仍然是人工 replay，不是自动 harness。
- 新 replay 只有一条新增线程，还不算广覆盖。
- design 饱和边界仍然依赖操作者判断，没有自动 gate。

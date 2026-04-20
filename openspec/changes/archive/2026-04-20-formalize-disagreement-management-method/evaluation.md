# Evaluation

## Baseline Scenarios

1. 治理型表层分歧
   - 讨论从 `ADR / wiki / TDD` 症状出发，但真实问题是分歧没有被当作目标校准材料保存。
2. 方法自压缩型分歧
   - 讨论不是在争某个治理 artifact，而是在争“更高层抽象本身是否已经压缩了过程”。

## Before Results

- 在基线状态下，系统更容易：
  - 把分歧快速翻成治理解释
  - 把 `ADR/wiki/TDD` 这类表层症状当成主问题
  - 过早命名“判断方式”或“高价值过程”
  - 用更漂亮的概念替代原始纠偏压力和分歧重定向
- 结果是：
  - 分歧的演变被压平
  - `I haven't seen it clearly yet` 这类状态没有正式位置
  - 过程保真度弱于结论保真度

## After Results

- 仓库现在正式发布了 [分歧管理方法](../../../wiki/ops/disagreement-management-method.md)。
- `AGENTS.md` 已经把 `Disagreement Management Default` 作为 repo-default policy 写入。
- [ADR-0012](../../../wiki/adr/0012-disagreement-management-before-conclusion-promotion.md) 已经把“方法层先于结论晋升”确认为跨 change 稳定决策。
- 正式方法现在要求：
  - 先保留最小原始材料包
  - 显式保留 anti-compression states
  - 只有当命名能解释分歧演变时才允许第一次正向命名
  - 方法服从材料，而不是反过来重塑分歧
- 两组真实线程已作为方法证据：
  - 治理症状型分歧
  - 方法自压缩型分歧

## Residual Risks

- 这是方法层正式化，不是 rollout proof。
- 当前证据来自真实线程复盘，但还不是自动化 harness。
- 未来如果把这套方法继续升级成 runtime automation 或 skill routing，还需要新的 before/after replay。

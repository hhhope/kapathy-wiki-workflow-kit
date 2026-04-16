# Evaluation

## Baseline Scenarios

1. 歧义请求下，agent 是否会静默补关键前提再执行
2. 小需求下，agent 是否会提前抽象和未来设计
3. 窄范围任务下，diff 是否会自然扩散到无关整理
4. 未重新检查状态时，agent 是否会提前宣称“完成 / 已提交 / 已同步”

## Before Results

- 这次 principle layer 变更之前，repo 内没有正式 principle skills。
- 同一轮实现里虽然走了 OpenSpec 和正式发布路径，但仍然只做了结构验证，没有证明这 4 类行为在基线场景下会如何失败。
- 这正是后续复盘里暴露的问题：`verification.md` 可以被结构证明填满，但行为证明仍然缺席。

## After Results

- principle layer 现已正式发布：
  - `clarify-before-acting`
  - `simplicity-first`
  - `surgical-changes`
  - `verify-before-claiming`
- `AGENTS.md` 现已把它们作为高频原则入口显式路由。
- 残余结论：这次变更完成了“正式发布”和“高频入口”两件事，但真正的多场景行为压力测试仍未自动化。

## Residual Risks

- 这是补记的行为证据摘要，不是一次真实的多会话压力测试。
- 未来如果继续调整这 4 条 principle 的正文，仍然应该做更严格的 before/after 场景复跑。

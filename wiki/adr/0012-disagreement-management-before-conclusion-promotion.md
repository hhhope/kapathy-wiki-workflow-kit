---
layer: adr
domain: none
canonical_object: disagreement-management-before-conclusion-promotion
artifact_type: adr
---
# ADR-0012 Disagreement Management Before Conclusion Promotion

- Status: accepted
- Date: 2026-04-20

## Context

这次仓库内的长对话先后暴露出几个表层症状：

- `ADR` 没更新
- 流程争论没有及时进 `wiki/ops`
- `TDD` 没覆盖行为漂移

但进一步复盘后发现，这些都不是最上游的问题。

真正的问题是：仓库更擅长保留结论，不擅长保留分歧作为目标校准材料。

在当前项目里，这不是文档洁癖问题，而是更核心的构建问题。用户的真正目标是通过长期共建逐步逼近一个自进化 agent。在这个过程中，流程级分歧不是噪音，而是校准目标的重要信号。

如果系统过早把分歧压成：

- 治理结论
- 稳定规则
- 更漂亮的抽象

那么真正有价值的东西会丢掉：

- 被持续否掉的 framing
- 纠偏压力
- 分歧重定向的时刻
- “我还没看清”的状态

## Decision

本仓库采用 `disagreement management before conclusion promotion` 作为稳定默认决策。

也就是：

- 先把流程级分歧当成目标校准材料来保留
- 在最小原始材料包被保住之前，不应急着晋升成 `ADR`、spec、skill 或其他结论层
- 显式保留 anti-compression 状态：
  - `I haven't seen it clearly yet`
  - `We should not name the pattern yet`
- 第一次正向命名只有在它能解释分歧如何演变，而不只是总结结果时，才算有效

下游默认边界：

- `wiki/ops retro`
  - 当分歧已经足够成形，需要 repo-visible 保住其校准作用
- `ADR`
  - 当分歧已经完成足够多的校准工作，并形成跨 change 稳定决策
- OpenSpec spec / repo-local skill
  - 当分歧已经稳定到足以 formalize 成 workflow requirement 或 executable behavior

## Consequences

- `ADR` 不再被当作流程级分歧的第一承接层，而是后置稳定决策层。
- `wiki/ops` 获得了一个更明确的上游方法入口：先保住分歧材料，再决定是否晋升。
- 后续任何想直接修 `ADR/wiki/TDD` 症状的 change，都应该先说明它与这套分歧管理方法的关系。
- 仓库默认承认：更高层抽象不自动等于更高保真度；方法必须服从材料，而不能反过来重塑分歧。

---
layer: adr
domain: none
canonical_object: agent-readable-wiki-runtime-context-after-utilization
artifact_type: adr
---
# ADR-0019 Agent-Readable Wiki Runtime Context After Utilization

- Status: accepted
- Date: 2026-04-20

## Context

仓库已经先后 formalize 了几层上游结构：

- naming model
- frontmatter model
- graph extraction
- relation analysis
- semantic scoring
- utilization layer

到这一步，仓库已经能给出对象利用建议，但仍然缺少一个 runtime-ready bundle，把这些建议直接打包成 live agent 可以读的上下文结构。

如果没有 runtime context，agent 还要临时把 utilization 输出再重组一次：

- 哪些对象先读
- 哪些对象只做 supporting context
- 哪些对象当前不该作为强锚点
- repository-level caution 应如何显式带入 live work

同时，这层也必须保持边界清楚。

如果 runtime-context output 被过早说成：

- retrieval readiness
- runtime autonomy
- unresolved 页面已理解

那么它会越过当前仓库只 formalize 了 bounded runtime guidance、还没有 formalize retrieval 或自动路由的边界。

## Decision

本仓库采用 `agent-readable wiki runtime context after utilization` 作为稳定默认决策。

也就是：

- runtime context 必须建立在：
  - naming model
  - frontmatter model
  - graph extraction
  - relation analysis
  - semantic scoring
  - utilization layer
  之后
- 第一版 runtime context 只基于 utilization 已覆盖的 canonical object
- runtime bundle 至少输出：
  - `summary`
  - `preferred_context`
  - `supporting_context`
  - `blocked_context`
  - `runtime_caution`
  - `runtime_notes`
- runtime bundle 只算 bounded runtime guidance，不算：
  - retrieval proof
  - runtime autonomy proof
  - unresolved 页面已理解
  - rollout proof

## Consequences

- 仓库现在形成了清晰的七层顺序：
  - naming
  - frontmatter
  - extraction
  - relation analysis
  - semantic scoring
  - utilization
  - runtime context
- 后续外部 retrieval、runtime auto-routing、agent 自动取材都必须作为新 scope，而不是隐含在 runtime context 里。
- repository caution 继续作为 runtime bundle 的一等部分保留，而不是被 preferred context 扁平化覆盖。

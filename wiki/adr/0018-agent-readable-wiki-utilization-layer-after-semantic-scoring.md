---
layer: adr
domain: none
canonical_object: agent-readable-wiki-utilization-layer-after-semantic-scoring
artifact_type: adr
---
# ADR-0018 Agent-Readable Wiki Utilization Layer After Semantic Scoring

- Status: accepted
- Date: 2026-04-20

## Context

仓库已经先后 formalize 了几层上游结构：

- naming model
- frontmatter model
- graph extraction
- relation analysis
- semantic scoring

到这一步，仓库已经可以给出对象强弱的显式评分，但仍然缺少一层“agent 到底怎么用这些结果”的稳定规则。

如果没有 utilization layer，agent 还是得自己临时推断：

- 哪些对象适合优先读
- 哪些对象只能谨慎使用
- 哪些对象当前不该支撑更强判断

同时，这层也必须保持边界清楚。

如果 utilization output 被过早说成：

- retrieval readiness
- runtime autonomy
- unresolved 页面已理解

那么它就越过了当前仓库只 formalize 了 bounded usage guidance、还没有 formalize retrieval 或自动路由的边界。

## Decision

本仓库采用 `agent-readable wiki utilization layer after semantic scoring` 作为稳定默认决策。

也就是：

- utilization layer 必须建立在：
  - naming model
  - frontmatter model
  - graph extraction
  - relation analysis
  - semantic scoring
  之后
- 第一版 utilization 只针对 semantic scoring 已覆盖的 canonical object
- utilization artifact 至少输出：
  - `summary`
  - `repository_caution`
  - `object_utilization`
  - `utilization_notes`
- 第一版 banding 使用显式 rule-based 分类，例如：
  - `preferred`
  - `cautious`
  - `blocked`
- utilization guidance 只算 bounded usage guidance，不算：
  - retrieval proof
  - runtime automation proof
  - unresolved 页面已理解
  - rollout proof

## Consequences

- 仓库现在形成了清晰的六层顺序：
  - naming
  - frontmatter
  - extraction
  - relation analysis
  - semantic scoring
  - utilization
- 后续 retrieval engine、runtime routing、autonomous context selection 都必须作为新 scope，而不是隐含在 utilization layer 里。
- repository-wide unresolved pressure 继续作为 utilization 的 caution 信号保留，而不是被扁平化掉。

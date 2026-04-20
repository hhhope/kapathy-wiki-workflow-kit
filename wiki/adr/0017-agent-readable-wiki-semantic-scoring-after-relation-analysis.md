# ADR-0017 Agent-Readable Wiki Semantic Scoring After Relation Analysis

- Status: accepted
- Date: 2026-04-20

## Context

仓库已经先后 formalize 了几层上游结构：

- naming model
- frontmatter model
- graph extraction
- relation analysis

到这一步，仓库已经能稳定描述结构，也能分析对象覆盖和 unresolved 分布，但仍然缺少一层对 canonical object 强弱的可复用判断。

如果没有 semantic scoring，agent 仍然只能从结构分析里手工推断：

- 哪些对象更强
- 哪些对象只是存在但还很薄
- unresolved 压力是否已经让更强语义判断不可信

同时，这层也必须保持边界清楚。

如果 semantic scoring 被过早说成：

- retrieval quality proof
- runtime routing proof
- unresolved 页面已理解

那么它又会越过当前仓库只 formalize 了显式仓库证据评分、还没有 formalize retrieval 或 runtime proof 的边界。

## Decision

本仓库采用 `agent-readable wiki semantic scoring after relation analysis` 作为稳定默认决策。

也就是：

- semantic scoring 必须建立在：
  - naming model
  - frontmatter model
  - graph extraction
  - relation analysis
  之后
- 第一版 semantic scoring 只评分 relation analysis 已覆盖的 canonical object
- semantic-scoring artifact 至少输出：
  - `summary`
  - `repository_context`
  - `object_scores`
  - `scoring_notes`
- 第一版使用显式、可审计的 rule-based 因子，而不是 embeddings 或隐藏模型
- score 只算 bounded repository-evidence signal，不算：
  - retrieval proof
  - runtime routing proof
  - unresolved 页面已理解
  - rollout proof

## Consequences

- 仓库现在形成了清晰的五层顺序：
  - naming
  - frontmatter
  - extraction
  - relation analysis
  - semantic scoring
- 后续 retrieval 集成、runtime routing、embedding-based scoring 都必须作为新 scope，而不是隐含在 semantic scoring 里。
- unresolved warnings 继续作为 repository context 的一部分保留，不要求第一版通过隐藏语义推断去消除它们。

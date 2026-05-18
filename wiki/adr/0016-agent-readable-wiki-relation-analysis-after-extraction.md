---
layer: adr
domain: none
canonical_object: agent-readable-wiki-relation-analysis-after-extraction
artifact_type: adr
---
# ADR-0016 Agent-Readable Wiki Relation Analysis After Extraction

- Status: accepted
- Date: 2026-04-20

## Context

仓库已经先后 formalize 了几层上游结构：

- naming model
- frontmatter model
- graph extraction
- 小范围 migration pilot

到这一步，仓库已经可以提取结构，但仍然缺一层稳定分析。

如果没有 relation analysis，agent 每次都只能重新读 raw graph artifact：

- 节点有多少
- 边有多少
- warning 有多少

但无法低成本判断：

- 哪些 canonical object 已经形成跨层覆盖
- 哪些 typed relation 已经真实出现
- unresolved 结构主要堆在哪些层

同时，这层也必须保持 proof 边界清楚。

如果 relation analysis 被过早说成：

- 语义图谱理解
- retrieval 质量证明
- runtime routing 证明

那么它又会越过当前仓库只 formalize 了结构层、还没有 formalize 语义层的边界。

## Decision

本仓库采用 `agent-readable wiki relation analysis after extraction` 作为稳定默认决策。

也就是：

- relation analysis 必须建立在：
  - naming model
  - frontmatter model
  - graph extraction
  之后
- 第一版 relation analysis 只覆盖 graph extraction 已覆盖的层：
  - `wiki/ops`
  - `wiki/adr`
  - `openspec/specs`
  - `wiki/examples`
- analysis artifact 至少输出：
  - `summary`
  - `object_coverage`
  - `artifact_type_distribution`
  - `relation_type_distribution`
  - `unresolved_warning_summary`
  - `analysis_notes`
- unresolved 结构必须保留为一等输出，而不是被强行解释成已理解节点
- relation analysis proof 只算结构分析 proof，不算：
  - 语义理解 proof
  - retrieval quality proof
  - runtime routing proof
  - rollout proof

## Consequences

- 仓库现在形成了清晰的四层顺序：
  - naming
  - frontmatter
  - extraction
  - relation analysis
- 后续 semantic scoring、graph viewer、retrieval 利用层都必须作为新 scope，而不是隐含在 relation analysis 里。
- unresolved warnings 继续是分析结果的一部分，不要求第一版 relation analysis 通过语义猜测去消灭 warning。

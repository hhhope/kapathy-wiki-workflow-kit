---
canonical_object: wiki-runtime-context-source-integration
artifact_type: adr
formalizes:
- wiki-runtime-context-source-integration
derived_from:
- wiki-runtime-context
---

# wiki-runtime-context-source-integration / adr

- Status: accepted
- Date: 2026-04-20

## Context

仓库已经先后 formalize 了：

- naming model
- frontmatter model
- graph extraction
- relation analysis
- semantic scoring
- utilization layer
- runtime context

到 runtime context 为止，仓库已经能告诉 agent 哪些 canonical object 应该优先读、谨慎读、或暂时阻断。

但 runtime context 仍然停在 object-level guidance。

如果没有 source integration，live agent 仍然需要手工做一次翻译：

- 把 preferred object 翻译成实际要打开的页面
- 把 supporting object 翻译成补充阅读路径
- 再自己决定哪些 source path 先读

这意味着 runtime context 仍然没有形成真正可直接消费的 repo-local reading target。

同时，这层边界也必须保持清楚。

如果 source integration 被过早说成：

- 外部 retrieval readiness
- runtime autonomy
- unresolved 页面已理解

那么它就越过了当前仓库只 formalize 了 repo-local source guidance、还没有 formalize 外部 source 接入和自动注入的边界。

## Decision

本仓库采用 `agent-readable wiki runtime context source integration after runtime context` 作为稳定默认决策。

也就是：

- source integration 必须建立在：
  - naming model
  - frontmatter model
  - graph extraction
  - relation analysis
  - semantic scoring
  - utilization layer
  - runtime context
  之后
- 第一版 source integration 只解析 repo-local source refs
- source-integrated runtime artifact 至少输出：
  - `summary`
  - `preferred_sources`
  - `supporting_sources`
  - `blocked_objects`
  - `source_resolution_notes`
  - `proof_boundary_notes`
- blocked objects 不能被平铺成 first-pass reading targets
- source integration 只算 bounded repository-local source guidance，不算：
  - external retrieval proof
  - autonomous runtime loading proof
  - unresolved 页面已理解
  - rollout proof

## Consequences

- 仓库现在形成了清晰的八层顺序：
  - naming
  - frontmatter
  - extraction
  - relation analysis
  - semantic scoring
  - utilization
  - runtime context
  - runtime context source integration
- 后续外部 source integration、runtime auto-injection、agent 自动取材都必须作为新 scope，而不是隐含在 source integration 里。
- live agent 现在可以拿到更直接的 repo-local reading targets，但仍然必须保留 direct source inspection，而不是跳过原始页面。

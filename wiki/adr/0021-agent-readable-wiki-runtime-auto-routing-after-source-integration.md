---
canonical_object: wiki-runtime-auto-routing
artifact_type: adr
formalizes:
- wiki-runtime-auto-routing
derived_from:
- wiki-runtime-context-source-integration
---

# wiki-runtime-auto-routing / adr

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
- runtime context source integration

到 source integration 为止，仓库已经能把 canonical object 解析成 concrete repo-local source refs。

但 source integration 仍然停在 resolved-source guidance。

如果没有 runtime auto routing，live agent 仍然需要手工做一次 staging：

- 哪些 source 先打开
- 哪些 source 放到 second-pass
- 哪些 blocked object 不该进入 first-pass route

这意味着 source integration 还没有形成真正可执行的 first-pass reading plan。

同时，这层边界也必须保持清楚。

如果 runtime auto routing 被过早说成：

- automatic context injection
- runtime autonomy
- external retrieval readiness
- unresolved 页面已理解

那么它就越过了当前仓库只 formalize 了 bounded routing guidance、还没有 formalize 自动注入与自治执行的边界。

## Decision

本仓库采用 `agent-readable wiki runtime auto routing after source integration` 作为稳定默认决策。

也就是：

- runtime auto routing 必须建立在：
  - naming model
  - frontmatter model
  - graph extraction
  - relation analysis
  - semantic scoring
  - utilization layer
  - runtime context
  - runtime context source integration
  之后
- 第一版 runtime auto routing 只从 source-integrated runtime output 派生 reading plan
- runtime auto-routing artifact 至少输出：
  - `summary`
  - `open_first`
  - `open_next`
  - `do_not_open_first`
  - `routing_notes`
  - `proof_boundary_notes`
- blocked objects 不能被平铺成 first-pass 或 second-pass route
- runtime auto routing 只算 bounded repository-local routing guidance，不算：
  - automatic context injection proof
  - runtime autonomy proof
  - external retrieval proof
  - rollout proof

## Consequences

- 仓库现在形成了清晰的九层顺序：
  - naming
  - frontmatter
  - extraction
  - relation analysis
  - semantic scoring
  - utilization
  - runtime context
  - runtime context source integration
  - runtime auto routing
- 后续自动 prompt 注入、自动上下文装载、agent 自治执行都必须作为新 scope，而不是隐含在 routing 里。
- live agent 现在可以拿到更明确的 first-pass / second-pass reading plan，但仍然必须保留 direct source inspection，而不是跳过原始页面。

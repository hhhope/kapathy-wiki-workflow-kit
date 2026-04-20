---
canonical_object: wiki-context-injection
artifact_type: adr
formalizes:
- wiki-context-injection
derived_from:
- wiki-runtime-auto-routing
---

# wiki-context-injection / adr

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
- runtime auto routing

到 runtime auto routing 为止，仓库已经能把 repo-local source refs 排成 first-pass 与 second-pass 的 reading order。

但 runtime auto routing 仍然停在 route guidance。

如果没有 automatic context injection，live agent 仍然需要手工完成最后一步：

- 读取 route 里的页面
- 截取要进入首轮上下文的内容
- 组织成一个可传入 live work 的 injected-context bundle

这意味着 routing 还没有形成真正可消费的 context payload。

同时，这层边界也必须保持清楚。

如果 automatic context injection 被过早说成：

- agent autonomy
- self-directed execution
- external retrieval readiness
- unresolved 页面已理解

那么它就越过了当前仓库只 formalize 了 bounded injected-context guidance、还没有 formalize 自治执行的边界。

## Decision

本仓库采用 `agent-readable wiki context injection after runtime auto routing` 作为稳定默认决策。

也就是：

- automatic context injection 必须建立在：
  - naming model
  - frontmatter model
  - graph extraction
  - relation analysis
  - semantic scoring
  - utilization layer
  - runtime context
  - runtime context source integration
  - runtime auto routing
  之后
- 第一版 automatic context injection 只从 runtime auto-routing output 派生 injected-context bundle
- automatic context-injection artifact 至少输出：
  - `summary`
  - `injected_first_pass`
  - `secondary_context`
  - `excluded_objects`
  - `injection_notes`
  - `proof_boundary_notes`
- 第一版 injected source 只保留 bounded excerpt，不注入整页全文
- excluded objects 不能被平铺进 first-pass injected context
- automatic context injection 只算 bounded repository-local injected-context guidance，不算：
  - agent autonomy proof
  - self-directed execution proof
  - external retrieval proof
  - rollout proof

## Consequences

- 仓库现在形成了清晰的十层顺序：
  - naming
  - frontmatter
  - extraction
  - relation analysis
  - semantic scoring
  - utilization
  - runtime context
  - runtime context source integration
  - runtime auto routing
  - context injection
- 后续 agent autonomy、self-directed execution、全入口自动注入都必须作为新 scope，而不是隐含在 injected-context layer 里。
- live agent 现在可以拿到更接近实际工作的 bounded context payload，但仍然必须保留 direct source inspection，而不是把 excerpt 当成完整真相。

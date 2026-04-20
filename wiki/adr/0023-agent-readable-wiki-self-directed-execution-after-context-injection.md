---
canonical_object: wiki-self-directed-execution
artifact_type: adr
formalizes:
- wiki-self-directed-execution
derived_from:
- wiki-context-injection
---

# wiki-self-directed-execution / adr

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
- context injection

到 automatic context injection 为止，仓库已经能把阅读顺序转换成 bounded injected-context payload。

但 injected-context 仍然停在上下文材料层。

如果没有 bounded self-directed execution，live agent 仍然需要手工做最后一步：

- 判断哪些动作可以先执行
- 判断哪些动作应延后
- 判断哪些对象仍必须留在 blocked 区

这意味着 injected-context 还没有形成真正可消费的 execution plan。

同时，这层边界也必须保持清楚。

如果 bounded self-directed execution 被过早说成：

- unrestricted agent autonomy
- self-directed execution without guardrails
- external retrieval readiness
- unresolved 页面已理解

那么它就越过了当前仓库只 formalize 了 bounded execution guidance、还没有 formalize 完整 autonomy 的边界。

## Decision

本仓库采用 `agent-readable wiki self-directed execution after context injection` 作为稳定默认决策。

也就是：

- bounded self-directed execution 必须建立在：
  - naming model
  - frontmatter model
  - graph extraction
  - relation analysis
  - semantic scoring
  - utilization layer
  - runtime context
  - runtime context source integration
  - runtime auto routing
  - context injection
  之后
- 第一版 bounded self-directed execution 只从 injected-context output 派生 execution-plan bundle
- bounded self-directed execution artifact 至少输出：
  - `summary`
  - `execute_now`
  - `defer_for_followup`
  - `do_not_execute`
  - `execution_notes`
  - `proof_boundary_notes`
- 第一版 action type 只允许 bounded execution labels，不放开无界副作用
- blocked objects 不能被平铺进 `execute_now`
- bounded self-directed execution 只算 bounded repository-local execution guidance，不算：
  - unrestricted agent autonomy proof
  - self-directed execution without guardrails
  - external retrieval proof
  - rollout proof

## Consequences

- 仓库现在形成了清晰的十一层顺序：
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
  - self-directed execution
- 后续 unrestricted autonomy、真实 side-effect execution、完整 execution loop 都必须作为新 scope，而不是隐含在 execution-plan layer 里。
- live agent 现在可以拿到更接近行动层的 bounded execution plan，但仍然必须保留人类或更强 guardrail 对真实副作用的边界控制。

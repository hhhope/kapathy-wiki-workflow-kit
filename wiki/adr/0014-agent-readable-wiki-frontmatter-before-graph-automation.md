---
layer: adr
domain: none
canonical_object: agent-readable-wiki-frontmatter-before-graph-automation
artifact_type: adr
---
# ADR-0014 Agent-Readable Wiki Frontmatter Before Graph Automation

- Status: accepted
- Date: 2026-04-20

## Context

仓库已经正式定义了演变型页面的命名模型，但命名本身还不足以让 agent 低成本读出结构关系。

如果只有标题，没有稳定字段合同，agent 仍然需要从正文和上下文里猜：

- 这页属于哪个 canonical object
- 这页是什么 artifact type
- 这页与别的页是什么关系
- 这条关系是在做派生、验证还是 formalization

这会让后续的 graph extraction、relation analysis 和结构化检索仍然停留在弱推断上。

如果现在直接推进自动图谱或关系脚本，会把这种弱结构直接放大，而不是先解决最小结构问题。

## Decision

本仓库采用 `agent-readable wiki frontmatter before graph automation` 作为稳定默认决策。

也就是：

- 在 covered evolution-bearing layers 上，先定义最小 frontmatter 合同，再推进图谱自动化
- 覆盖范围第一版只限于：
  - `wiki/ops`
  - `wiki/adr`
  - `openspec/specs`
  - `wiki/examples`
- 新页面至少必须携带：
  - `canonical_object`
  - `artifact_type`
- 新页面应使用稳定的关系字段词表表达直接关系：
  - `related_objects`
  - `derived_from`
  - `validates`
  - `formalizes`
- `supersedes`、`replaces`、`notes_scope` 保持为第一版可选辅助字段
- rollout 采用：
  - 新页强约束
  - 旧页弱约束

## Consequences

- 图谱与关系分析工作以后必须建立在 frontmatter 合同之上，而不是先做自动抽取再倒推字段。
- 仓库现在有了两层基础结构：
  - naming model
  - frontmatter model
- 旧页不会被立即强制批量补字段，但新页不会继续产生新的结构漂移。
- 后续如果要做 graph extraction、relation scoring 或小范围迁移，应显式建立在这条 ADR 之上。

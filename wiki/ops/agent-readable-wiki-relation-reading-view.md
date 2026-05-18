---
title: wiki-readable-views / relation-reading-view
canonical_object: wiki-readable-views
artifact_type: relation-reading-view
related_objects:
  - wiki-graph-extraction
  - wiki-relation-analysis
  - wiki-semantic-scoring
derived_from:
  - wiki-graph-extraction
  - wiki-relation-analysis
validates:
  - wiki-readable-views
notes_scope: human-readable relation summary above the current graph extraction and relation analysis artifacts
language: zh-CN
audience: self
knowledge_level: working
layer: ops
domain: wiki
ops_area: wiki-runtime
status: active
updated_at: 2026-04-20
ai_generated: true
---

# wiki-readable-views / relation-reading-view

这页只做一件事：把现有 graph / relation 结果翻成可读层，不再要求先去看 JSON。

## 当前结构真值

基于现有 relation-analysis sample，当前仓库的结构层真值是：

- `canonical_object_count: 6`
- `cross_layer_object_count: 5`
- `analyzed_node_count: 19`
- `analyzed_edge_count: 4`
- `unresolved_warning_count: 57`

这说明：

- 结构提取已经不是空白
- 但 unresolved 压力仍然很高
- 现在更需要阅读视图，而不是继续往 runtime 下游补层

## 当前主要对象族

### `disagreement-management`

已跨层：

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`

当前 artifact types：

- `method`
- `adr`
- `spec`
- `replay-harness`
- `replay-validation`

阅读入口：

- [disagreement-management / method](/mnt/d/cloud/account-meeting-lore/wiki/ops/disagreement-management-method.md)
- [ADR-0012](/mnt/d/cloud/account-meeting-lore/wiki/adr/0012-disagreement-management-before-conclusion-promotion.md)
- [disagreement-management / spec](/mnt/d/cloud/account-meeting-lore/openspec/specs/disagreement-management-method/spec.md)

### `conversation-handoff`

已跨层：

- `wiki/ops`
- `openspec/specs`

当前 artifact types：

- `method`
- `sample`
- `spec`

阅读入口：

- [conversation-handoff / method](/mnt/d/cloud/account-meeting-lore/wiki/ops/conversation-handoff-mode.md)
- [conversation-handoff / sample](/mnt/d/cloud/account-meeting-lore/wiki/ops/sample-handoff-topic.md)
- [conversation-north-star-handoff / spec](/mnt/d/cloud/account-meeting-lore/openspec/specs/conversation-north-star-handoff/spec.md)

### `example-driven-capture`

已跨层：

- `wiki/ops`
- `wiki/examples`
- `openspec/specs`

当前 artifact types：

- `method`
- `example`
- `runtime-validation`
- `spec`

阅读入口：

- [example-driven-capture / method](/mnt/d/cloud/account-meeting-lore/wiki/ops/example-driven-wiki-capture.md)
- [GitHub README 分析样例](/mnt/d/cloud/account-meeting-lore/wiki/examples/github-analysis-example.md)
- [example-driven-wiki-capture / spec](/mnt/d/cloud/account-meeting-lore/openspec/specs/example-driven-wiki-capture/spec.md)

## 当前结构压力最大的地方

relation-analysis sample 里 unresolved warning summary 是：

- `wiki/ops`: 27
- `wiki/adr`: 13
- `openspec/specs`: 12
- `wiki/examples`: 5

所以当前最大问题不是“没有图”，而是：

- `wiki/ops` 仍然太散
- `ADR` 和 `spec` 已经存在，但阅读上没有被主动拉成链
- `examples` 相对压力最低，但数量也还不够支撑整体阅读

## 当前最值得先看的链

### 先看分歧管理链

因为它已经同时具备：

- method
- retro / replay
- ADR
- spec

这是目前最完整的一条演变链。

### 再看命名与结构链

- [wiki-naming-model / method](/mnt/d/cloud/account-meeting-lore/wiki/ops/agent-readable-wiki-naming-model.md)
- [wiki-frontmatter-model / method](/mnt/d/cloud/account-meeting-lore/wiki/ops/agent-readable-wiki-frontmatter.md)
- [ADR-0013](/mnt/d/cloud/account-meeting-lore/wiki/adr/0013-agent-readable-wiki-naming-before-graph-growth.md)
- [ADR-0014](/mnt/d/cloud/account-meeting-lore/wiki/adr/0014-agent-readable-wiki-frontmatter-before-graph-automation.md)

### 最后再看 graph / relation 方法层

- [wiki-graph-extraction / method](/mnt/d/cloud/account-meeting-lore/wiki/ops/agent-readable-wiki-graph-extraction.md)
- [wiki-relation-analysis / method](/mnt/d/cloud/account-meeting-lore/wiki/ops/agent-readable-wiki-relation-analysis.md)

这一步是为了理解“结构分析做到哪了”，不是为了先碰 runtime 链。

## 边界

这页不是新图谱系统，也不是 runtime 决策面板。

它只做：

- 把现有结构层结果拉成可读层
- 告诉你先看哪些对象链
- 告诉你 unresolved 压力现在主要堆在哪

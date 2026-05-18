---
layer: adr
domain: none
canonical_object: agent-readable-wiki-graph-extraction-after-structure
artifact_type: adr
---
# ADR-0015 Agent-Readable Wiki Graph Extraction After Structure

- Status: accepted
- Date: 2026-04-20

## Context

仓库已经先后 formalize 了两层基础结构：

- 命名模型
- frontmatter 与 typed relation fields

在这之前直接做图谱，会把弱对象身份和弱关系结构直接放大。

现在基础结构已经存在，缺的是一个下游 extraction 层，把这些结构转成 machine-readable artifact，方便 agent 读取，而不需要每次重新扫整仓 prose。

同时，这个 extraction 层也必须保持边界清楚。

如果 extraction 一上来就被当成：

- 语义图谱
- 图谱评分系统
- 可视化产品

那么会过早越过当前仓库已经 formalize 的结构合同。

## Decision

本仓库采用 `agent-readable wiki graph extraction after structure` 作为稳定默认决策。

也就是：

- graph extraction 必须建立在 naming model 和 frontmatter model 之后
- 第一版 extraction 只覆盖：
  - `wiki/ops`
  - `wiki/adr`
  - `openspec/specs`
  - `wiki/examples`
- extraction 至少输出：
  - nodes
  - edges
  - warnings
- node 至少保留：
  - `page_path`
  - `canonical_object`
  - `artifact_type`
  - `source_layer`
- edge 至少保留：
  - `source_page_path`
  - `relation_type`
  - `target`
- 第一版支持的 typed relation 为：
  - `related_objects`
  - `derived_from`
  - `validates`
  - `formalizes`
- `supersedes`、`replaces` 在存在时可选保留
- extraction proof 只算结构 proof，不算：
  - 语义完整性证明
  - 图谱质量评分
  - 图谱 UI readiness

## Consequences

- 仓库现在形成了清晰的三层顺序：
  - naming
  - frontmatter
  - extraction
- 后续 graph viewer、graph scoring、旧页批量补字段，都必须作为新 scope，而不是隐含在 extraction 里。
- unresolved pages 发 warning 是允许的，不要求第一版通过语义猜测去伪造全量节点覆盖。

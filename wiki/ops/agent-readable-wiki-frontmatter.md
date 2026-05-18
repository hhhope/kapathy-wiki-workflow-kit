---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: agent-readable-wiki-frontmatter
artifact_type: method
---

# Agent-Readable Wiki Frontmatter

这页定义当前仓库在演变型页面上的最小 frontmatter 与关系字段模型。

目标不是一次性做完整图谱，而是先让 agent 可以低成本读出：

- 这页属于哪个对象
- 这页是什么 artifact type
- 这页和其他页是什么关系

## 覆盖范围

第一版只覆盖：

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

第一版不覆盖：

- `wiki/sources`
- `wiki/domains`
- `wiki/reports`
- `wiki/timeline`

## 必需身份字段

覆盖范围内的新页面至少应携带：

- `canonical_object`
- `artifact_type`

这两个字段是标题命名模型的结构化镜像。

## 必需关系字段

覆盖范围内的新页面应使用稳定的关系字段词表来表达直接关系：

- `related_objects`
- `derived_from`
- `validates`
- `formalizes`

不是每个页面都必须填写全部字段，但字段名本身应保持稳定，不再临时发明。

## 可选辅助字段

第一版允许但不强制：

- `supersedes`
- `replaces`
- `notes_scope`

这些字段有用，但不属于最小合同。

## 字段语义

### `canonical_object`

页面所属的稳定对象族。

### `artifact_type`

页面所属的 artifact type，例如：

- `method`
- `retro`
- `adr`
- `spec`
- `example`
- `runtime-validation`

### `related_objects`

与当前对象直接相关的其他对象族。

### `derived_from`

当前页面从哪个上游页面或材料派生而来。

### `validates`

当前页面在验证哪个对象、方法或 artifact。

### `formalizes`

当前页面把哪个对象、方法或运行规则 formalize 到更稳定的层。

## Rollout 规则

这套 frontmatter 模型当前按下面方式 rollout：

- 对新页面是强约束
- 对旧页面是弱约束

也就是：

- 新增页面必须遵守
- 已有页面不要求立刻补齐
- 旧页面只在被触碰、重写或明确迁移时逐步收敛

## 与命名模型的关系

这页不是在替代标题命名模型，而是在它之上增加最小结构层。

顺序仍然是：

1. 先稳定 `canonical object / artifact type` 命名
2. 再补最小 frontmatter 与 typed relation fields
3. 之后才考虑图谱、关系分析或自动抽取

## 当前非目标

第一版明确不做这些事：

- 不实现 graph extractor
- 不实现 relation scoring
- 不批量回填旧页面 metadata
- 不强制旧页立即迁移

## 当前开放问题

- 是否还需要 `related_pages` 这类更宽泛字段
- `supersedes` 未来是否应升级为强制字段
- `readme-learning` 是否会需要超出共享合同的专用字段

## 一句话判断

`先把对象和关系字段稳定下来，再谈自动图谱。`

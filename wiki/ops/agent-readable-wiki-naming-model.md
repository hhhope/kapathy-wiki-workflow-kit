---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: agent-readable-wiki-naming-model
artifact_type: method
---

# Agent-Readable Wiki Naming Model

这页定义当前仓库在演变型页面上的标题命名模型。

目标不是美观，也不是立即重构目录，而是让 agent 更低成本地看懂：

- 这页属于哪个对象
- 这页是什么 artifact type
- 多个页面是否属于同一条演变链

## 覆盖范围

第一版只覆盖这些层：

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

第一版不覆盖：

- `wiki/sources`
- `wiki/domains`
- `wiki/reports`
- `wiki/timeline`

## 核心形式

新页面应使用两段式命名：

`canonical object / artifact type`

标题主位只负责表达两件事：

- `canonical object`
- `artifact type`

## 什么不该进标题

下面这些不应占据标题主位，应下沉到 metadata 或正文：

- 日期
- 状态词
- 第几轮验证
- change 标识
- `gap`、`issue`、`missing`、`leak` 一类表层症状词
- 句子化过程描述

## Canonical Object 准入规则

一个主题对象只有同时满足下面三条，才有资格进入 canonical object list：

1. 它不是一次性事件页
2. 它已跨至少两种容器或 artifact layer 存在
3. 它能统一一条真实演变链，而不是只命名某个阶段的表层症状

这意味着下面这些通常不应成为 canonical object：

- `ADR 没更新`
- `TDD 没覆盖`
- `gate gap`
- 主要靠日期或单次验证定义身份的页面

## 第一批 Canonical Object

当前第一批 canonical object 为：

- `disagreement-management`
- `conversation-handoff`
- `example-driven-capture`

选择理由很直接：

- 它们都不是一次事件
- 它们都已跨层存在
- 它们都能统一真实演变链

## 允许的 Artifact Type

### `disagreement-management`

允许的 artifact type：

- `method`
- `retro`
- `sample`
- `replay-harness`
- `replay-validation`
- `adr`
- `spec`
- `script-example`

### `conversation-handoff`

允许的 artifact type：

- `method`
- `sample`
- `retro`
- `runtime-rule`
- `adr`
- `spec`

### `example-driven-capture`

允许的 artifact type：

- `method`
- `sample`
- `runtime-validation`
- `example`
- `skill-route`
- `adr`
- `spec`

## 跨层一致性规则

同一个对象在覆盖范围内必须复用同一个 canonical object 名。

也就是在这些层里保持一致：

- `wiki/ops`
- `wiki/adr`
- `openspec/specs`
- `wiki/examples`

不要让同一个对象在不同层各自发明新名字。

## Rollout 规则

这套模型当前按下面方式 rollout：

- 对新页面是强约束
- 对旧页面是弱约束

也就是：

- 新增页面必须遵守这套命名模型
- 已有页面先不强制重命名
- 旧页面只有在被重写、补链、迁移时才逐步收敛

## 当前非目标

第一版明确不做这些事：

- 不立即重命名现有页面
- 不立即改目录结构
- 不定义图谱 metadata 全集
- 不实现 relation analysis 或 graph tooling

## 当前开放问题

- `readme-learning` 未来是否应独立成 canonical object
- 标题稳定后，下一步 frontmatter 字段应该怎么补
- 后续是否要把文件名也收敛到同一模型

## 一句话判断

`先把对象命名稳定下来，再谈 metadata、图谱和关系分析。`

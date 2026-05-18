---
layer: ops
domain: wiki
ops_area: workflow-trace
canonical_object: readme-capability-map-boundary
artifact_type: retro
title: readme-capability-map-boundary / drift retro
type: retro
language: zh-CN
status: active
created_at: 2026-05-14
updated_at: 2026-05-14
ai_generated: true
derived_from:
  - chat://2026-05-14/readme-capability-map-drift
  - openspec/changes/document-readme-capability-map-boundary/design.md
related_objects:
  - wiki-runtime-layer-boundary
  - brainstorming-drift-wiki-trace
  - obsidian-moc-projection
notes_scope: 记录 README 能力地图需求被误读成 runtime 入口或独立 capability-map 真源的漂移，并锚定修正边界。
---

# README Capability Map Boundary / Drift Retro

## Trigger

用户在 Obsidian 图谱、MOC、runtime 分层讨论后提出：

> 我觉得可以整个项目的层级 能力地图，runtime 先维护readme然后去做

随后纠正 agent：

> 也不是README是项目描述，你漂移了这只是我给你的任务而已

再次纠正：

> 分号里面是一句话是让你在readme里面描述清楚我们项目的能力和层次，不要漂移了

## Original Intent

用户要的是：

```text
在 README 里描述清楚整个项目的层级、能力地图和 runtime 相关能力。
README 仍然是项目描述。
```

这个任务是后续 runtime / graph / MOC 工作之前的项目说明补强，不是新增 runtime
入口，也不是新增一个独立 capability-map 真源。

## Drift Chain

### Drift 1: 把 README 需求转成独立 runtime-readable artifact

错误回答把任务改写成：

```text
wiki/ops/project-capability-map.md
wiki/status/capability-map.json
```

这偏离了用户说的 README。虽然能力地图可以有内部承载页，但当前任务明确是让
README 讲清项目能力和层次。

### Drift 2: 把 README 当成 runtime first-read contract

后续回答又说 runtime 应先读 README/capability map，再决定 status、graph、
apply、moc 路由。

这把 README 从项目说明提升成 runtime 行为入口，混淆了 README、OpenSpec、
ADR、skills、command docs、generated status 之间的职责。

## Rejected Framing

被用户否掉的 framing 是：

```text
README 是 runtime 入口或 capability-map 真源。
```

另一个被否掉的 framing 是：

```text
当前应该先新建 README 之外的项目能力地图文件。
```

## Corrected Framing

正确 framing 是：

```text
README 是项目描述。
README 应清楚说明项目层级、能力地图、runtime surfaces 和边界。
README 不拥有 runtime 行为，不替代 OpenSpec / ADR / skills / command docs。
```

后续 Obsidian MOC projection、wiki-react routing、status/graph/apply 诊断扩展，
仍需要各自的 OpenSpec 和实现证据。

## Cause Analysis

### 1. 最近上下文过重

前文一直在讨论 runtime、react、eval、graph、status、apply、MOC，agent 沿着
最近的技术链继续推导，而不是尊重用户这句是在布置 README 文档任务。

### 2. 把“描述能力地图”误读成“建立能力地图真源”

用户说的是 README 里描述项目能力和层次。agent 把它放大成单独的 runtime
capability-map artifact，导致任务对象变了。

### 3. 把说明性文档误升格为行为权威

README 可以说明 runtime surfaces，但不能因此成为 runtime first-read contract。
行为权威仍在 OpenSpec、ADR、skills、command docs 和 runtime 实现。

## Stable Decision Needed

这次漂移暴露了一个跨 change 仍然成立的边界：

```text
README may describe the project capability map, but README is not runtime authority.
```

因此需要 ADR 记录，而不是只留在 retro。

## Next Action

通过 `openspec/changes/document-readme-capability-map-boundary`：

- 更新 README 的项目能力地图描述
- 新增 ADR 记录稳定边界
- 不实现 MOC projection
- 不修改 runtime scripts、skills、AGENTS 或 command behavior

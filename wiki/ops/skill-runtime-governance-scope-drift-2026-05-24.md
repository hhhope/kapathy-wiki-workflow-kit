---
layer: ops
domain: ai-workflow
ops_area: agent-governance
canonical_object: skill-runtime-governance-scope-drift
artifact_type: retro
title: skill-runtime-governance scope drift / retro
type: retro
language: zh-CN
status: active
created_at: 2026-05-24
updated_at: 2026-05-24
ai_generated: true
derived_from:
  - chat://2026-05-24/skill-runtime-governance-scope-drift
related_objects:
  - brainstorming-drift-wiki-trace
  - live-conversation-reanchor-gate
  - behavior-replay-gate
  - skill-authoring-contract
notes_scope: 记录 skill-runtime-governance 设计讨论中，agent 两次把 root skill/cache runtime 治理误收窄成 brainstorming 或用户质疑触发的问题。
---

# skill-runtime-governance scope drift / retro

## Trigger

用户在 root skill runtime 治理讨论中指出：

> 用户质疑这个太窄了怎么又TM漂移成brainstorming了

这不是单个措辞问题，而是我在已经确认 `skill-runtime-governance` 命名后，又把
治理对象收窄成 `$superpowers:brainstorming` 压力场景和“用户质疑”触发。

## Original Requirement

用户要治理的是整个 root skill / Codex plugin cache 层面的 runtime 生命周期：

- root skills；
- plugin/cache skills；
- skill 触发、冲突、漂移、产物错位；
- 不同评估面的选择；
- root 泛化规则与 repo 垂直规则之间的 adapter；
- `$superpowers:brainstorming` 只是高风险场景之一，不是治理对象本身。

核心目标是让 root agent 在 skill runtime 问题出现时先做评估分诊，而不是直接抓
最近的 skill 或当前技术链继续推进。

## Drift Chain

### Drift 1: 把治理对象收窄为 brainstorming

我先提出 `brainstorming-governance`，把对象错误地限定为：

```text
当用户质疑 $superpowers:brainstorming 过程中的漂移、治理、评估、生命周期、skill 归属
```

用户随后纠正：对象不是 brainstorming，而是整个 skill 或 Codex cache 层面。

### Drift 2: 确认 `skill-runtime-governance` 后仍把 brainstorming 放回中心

在用户确认 `skill-runtime-governance` 后，我虽然写出了 root skill/cache runtime
边界，但下一步方案仍把 `$superpowers:brainstorming` 作为核心压力场景来组织，
并使用“用户质疑”作为主要触发语。

这再次把上层治理问题压回了单个 skill 的事故场景。

## Corrected Framing

正确 framing 应是：

```text
skill-runtime-governance
  -> root-level evaluation triage for all skill/cache runtime incidents
  -> classifies runtime layer, target artifact, evaluation surface, evidence
  -> treats brainstorming as one scenario, not the design center
```

触发不应只写成“用户质疑”。更准确的触发包括：

- skill 选择或触发不确定；
- root skill 与 plugin/cache skill 发生边界冲突；
- skill 输出与目标产物规则不一致；
- agent 把泛化规则和 repo 垂直规则折叠；
- 用户指出漂移、评估面错误或治理层级错误；
- agent 自检发现当前 skill 可能不是正确评估入口；
- 需要决定是否进入 writing-skills、behavior replay、reanchor、learning capture、
  repo adapter 或 OpenSpec/root governance gate。

## Cause Analysis

### 1. 压力场景变成了设计中心

`$superpowers:brainstorming` 是当前最明显的压力场景，但不是系统边界。我在解释时
让最显眼的例子重新占据了对象中心。

### 2. 把外部输入触发误当成唯一触发

“用户质疑”只是 runtime incident 的一个可见信号。真正需要治理的是 root agent
在 skill/cache 层遇到不确定、冲突、漂移、产物错位时的评估选择能力。

### 3. 评估面和治理入口仍未分开

`writing-skills` 是 skill authoring 的评估面，不是总入口；`brainstorming` 是一个
creative-work gate，不是 skill runtime governance 的边界。新入口应该先决定评估面，
再让对应评估工作。

## Keep

- 保留 `skill-runtime-governance` 作为 root skill / Codex cache runtime 的上层入口命名。
- 保留“评估分诊是核心”的判断。
- 保留 `$superpowers:brainstorming` 作为压力场景之一。
- 保留 `writing-skills` 作为 skill authoring / skill edit 的评估面。
- 保留 repo adapter：root skill 只分诊，落地时读取当前 repo 的 `AGENTS.md`、
  `PROJECT.md` 和相关 spec。

## Freeze

- 不再把入口命名或职责写成 `brainstorming-governance`。
- 不再把触发条件只写成“用户质疑”。
- 不再把 `$superpowers:brainstorming` 作为第一版设计中心。
- 不直接修改 root skill、plugin cache skill、repo `AGENTS.md` 或 OpenSpec。
- 不把本页当成 behavior replay 或 skill RED/GREEN 证据；它只是漂移复盘。

## Next Action

重新展开设计时，从 root skill/cache runtime 生命周期出发：

```text
runtime incident
  -> classify runtime layer
  -> classify target artifact
  -> select evaluation surface
  -> state evidence required
  -> state allowed / blocked actions
  -> propose next action
```

第一版压力场景应覆盖多个 skill/cache runtime 类型，而不是围绕
`$superpowers:brainstorming` 单点展开。

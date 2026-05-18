---
canonical_object: root-capability-extraction
artifact_type: retro
title: root-capability-extraction / retro
type: retro
language: zh-CN
audience: self
domain: wiki
layer: ops
ops_area: agent-governance
status: active
updated_at: 2026-05-07
ai_generated: true
derived_from:
  - openspec/specs/principle-skills-layer/spec.md
  - openspec/specs/repo-agents-loaded-context/spec.md
  - openspec/specs/root-governance-alignment/spec.md
  - wiki/ops/learning-capture-routing.md
related_objects:
  - root-governance-alignment
  - repo-agents-loaded-context
  - principle-skills-layer
---

# root-capability-extraction / retro

## 触发问题

用户指出：如果一个能力涉及根能力，就应该抽象进入 root，而不是一直在
repo 层打转。

这个追问发生在 repo `AGENTS.md` 已完成 loaded-context 压缩、`learning-capture`
runtime trigger 已补齐、两个 change 都已归档之后。表面上 repo `AGENTS.md`
变得更清晰，但 High-Frequency Skills 仍把通用能力和 repo 专属工作流放在同一
张表里。

## 根因

根因不是某个 skill 放错，而是 repo runtime map 缺少 ownership classification。

`principle-skills-layer` 把 `clarify-before-acting`、`simplicity-first`、
`surgical-changes`、`verify-before-claiming` 发布到 repo `.codex/skills/`。
这解决了“高频错误有触发入口”的问题，但没有说明这些能力是：

- repo-owned；
- root-candidate；
- root-owned-reference；
- shared。

后续 `govern-repo-agents-loaded-context` 把 High-Frequency Skills 做成 repo
入口表时，延续了这个缺口。结果是：runtime availability 被误读成
behavior ownership。

## 具体表现

| 能力 | 当前问题 |
|---|---|
| `verify-before-claiming` | 与 root git truth-source / completion claim 门禁重叠，核心是跨 repo 能力。 |
| `surgical-changes` | “不要扩大修改范围”是通用编辑纪律，不依赖本 repo。 |
| `simplicity-first` | 控制过度抽象是通用设计能力，不依赖 wiki repo。 |
| `clarify-before-acting` | 模糊意图前澄清是通用协作能力。 |
| OpenSpec apply/archive/propose | OpenSpec 使用是通用生命周期能力；repo 只拥有 wiki/archive 细节。 |
| `learning-capture` | 核心的 source-learning admission / score-first 偏 root-candidate；产物落 `wiki/ops` / `wiki/sources` 是 repo-owned。 |
| `material-collaboration-defaults` | 绑定本 repo 的材料产物层和 wiki 输出，repo-owned。 |
| `meeting-note-output` | 绑定会议纪要格式、Feishu 输出边界和确认项，repo-owned。 |

## 为什么之前没被发现

之前的目标是先解决 repo `AGENTS.md` 超载和 runtime trigger 缺失，因此验证焦点是：

- 是否还能找到 hard stops；
- 是否还能找到 skill trigger；
- 是否有 stable proxy；
- 是否完成 OpenSpec archive。

这些验证证明 repo `AGENTS.md` 是可用的 loaded-context map，但没有证明它是正确的
ownership map。事实上它不应该承担 ownership map。

## 当前判断

repo `AGENTS.md` 可以继续作为 runtime map，但必须显式说明：

> runtime route does not imply ownership.

通用能力可以继续在 repo 内孵化或被引用，但必须标成 `root-candidate`，不能因为它们
现在存在于 repo `.codex/skills/` 就当成 repo-owned。

## 下一步

通过 OpenSpec change `decide-root-capability-extraction-boundary` 固化边界：

- ADR 记录稳定决策；
- spec 记录 ownership-status 要求；
- repo `AGENTS.md` 只做最小说明和分类；
- 不直接改 root `~/.codex/AGENTS.md`。

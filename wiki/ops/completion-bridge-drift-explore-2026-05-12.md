---
title: completion-bridge-drift / explore
type: intake
canonical_object: completion-bridge-drift
artifact_type: explore-trace
language: zh-CN
source_path: chat://openspec-explore/completion-bridge-drift/2026-05-12
source_type: conversation
audience: self
knowledge_level: working
domain: personal-ops
period: active
confidence: medium
status: active
updated_at: 2026-05-12
ai_generated: true
related_objects:
  - openspec-explore-trigger-drift
  - conversation-handoff
  - add-product-status-contract
related_sources:
  - wiki/ops/openspec-explore-trigger-drift-retro.md
related_focus_threads: []
related_reminders: []
explore_mode: true
trace_mode: openspec-explore
same_topic_rule: update-existing
notes_scope: 探索为什么 add-product-status-contract 完成后没有自然回接用户设定的双轨复盘目标
---

# completion-bridge-drift / explore

## Trigger

用户在 `add-product-status-contract` 完成后追问：

- 做了什么，解决什么问题？
- 双轨制结果是什么？
- 为什么这个衔接问题需要用户点出来？

这说明实现完成后的回答没有自然回到用户前面设定的实验主线：

`先用 Superpowers + OpenSpec 双轨跑完，再复盘出现了什么，最后判断是否要改 skill。`

## Current Focus

- 这不是 product-status 代码质量问题。
- 这是完成后 handoff summary 没有覆盖用户原始意图的问题。
- 需要区分：
  - OpenSpec 的 `complete` 停止边界
  - 用户设定的“方法论实验”验收边界
  - 是否进入 archive review / retro / skill change 的下一步选择

## Working Hypothesis

当前更可能的根因是：

1. 执行者把 `OpenSpec change complete` 当成对话完成点。
2. Superpowers 被当成执行工具，而不是本轮要被观察的实验对象。
3. 最终汇报模板偏向工程交付清单，没有内置“回接用户原始 north-star”的步骤。
4. repo 硬停止规则正确阻止了继续实现，但没有明确要求停止后给出 `retro bridge`。

## Not Decided

- 这是否需要修改 repo-local skill。
- 修改对象如果存在，应该是 Superpowers 使用习惯、repo OpenSpec apply helper、还是新增 completion bridge gate。
- 是否要开新的 OpenSpec change 来 formalize 这类完成后复盘桥接。

## Boundary

This trace records exploration only. It does not edit skills, repo guidance, or OpenSpec specs. If the exploration stabilizes into a behavior change, create a separate OpenSpec proposal before implementation.

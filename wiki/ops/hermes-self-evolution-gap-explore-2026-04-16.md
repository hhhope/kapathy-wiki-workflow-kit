---
title: Hermes 自进化缺口探索 2026-04-16
type: intake
language: zh-CN
source_path: chat://openspec-explore/hermes-self-evolution-gap-2026-04-16
source_type: conversation
audience: self
knowledge_level: working
domain: personal-ops
period: active
confidence: medium
status: active
updated_at: 2026-04-16
ai_generated: true
related_sources: []
related_focus_threads:
  - main-thread.md
related_reminders: []
explore_mode: true
trace_mode: openspec-explore
same_topic_rule: update-existing
---

# Hermes 自进化缺口探索 2026-04-16

## 触发问题

用户想回到 Hermes self-evolution review 的未展开部分，重点拆开当前仓库仍缺的四层：experience extraction triggers、candidate memory layer、incremental refresh state model、human governance promotion boundary。

## 当前关注点

- 这四层如何串成一条最小闭环
- 哪一层最适合先做成下一条 OpenSpec change
- 哪些部分已经有 ADR 雏形，哪些还停在聊天判断

## 当前假设

- 当前仓库已经有较强的人类治理直觉，但触发和状态层还偏弱
- 真正缺的不是“会不会写 skill”，而是“经验何时被提炼、暂存、刷新、晋升”
- 这四层更像一条治理流水线，而不是四个独立能力点

## 暂未决定

- 下一条 change 先从触发器层做，还是先做 candidate memory 容器
- candidate layer 是落在 wiki、OpenSpec artifacts，还是独立 memory surface
- incremental refresh 是否先限定在项目周推进材料这一类输入

## 下一步

- 继续展开四层的边界、依赖和最小可行架构
- 如果形成稳定方案，再新开 OpenSpec change 承接实现

---
title: 实现 inbox 到 source 草稿生成
type: codex-handoff
language: zh-CN
audience: project
knowledge_level: working
domain: personal-ops
period: evergreen
status: draft
updated_at: 2026-04-14
ai_generated: true
handoff_state: ready
related_reminders:
  - sample-reminder.md
related_sources: []
acceptance_hint: 能根据 inbox 中的输入生成 source 草稿，并保留中文摘要与英文附录分层
---

# 实现 inbox 到 source 草稿生成

## 任务目标

让 Codex 基于固定 `inbox/` 输入生成来源页草稿，并遵守中文主写、英文独立附录的规则。

## 背景上下文

- 来源提醒：[设计 Codex 任务升级规则](sample-reminder.md)
- 关联来源：[Inbox Intake](../inbox-intake.md)
- 现状：当前规则已经定义，但实际自动化还没有实现

## 验收提示

- 能识别输入文件
- 能输出来源页草稿
- 能保留中文摘要和独立英文附录区块

## 协作状态

- handoff 状态：`ready`
- 是否需要人工补充：需要补充最终执行边界，但已足够作为开发起点

## English Notes

No English appendix for this sample.

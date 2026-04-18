---
title: OpenSpec 探索留痕样例
type: intake
language: zh-CN
source_path: chat://openspec-explore/sample
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

# OpenSpec 探索留痕样例

## 触发问题

用户希望每次进入 `openspec-explore` 时，先把探索主题写进 `wiki/ops/`，避免探索过程只留在聊天里。

## 当前关注点

- 留痕必须先于探索继续
- 留痕位置固定在 `wiki/ops/`
- 同主题探索优先更新，不重复开页

## 当前假设

- `type: intake` 已经足够承接 explore trace，不需要新 page type
- 轻量 trace 比直接创建正式 OpenSpec change 更适合早期探索
- 只有探索收束成明确变更后，才应切换到 `proposal.md`、`design.md`、`tasks.md`

## 暂未决定

- 具体页面命名是否要固定到主题加日期
- 后续是否需要为 explore trace 增加自动模板生成

## 下一步

- 把默认规则写进 repo guidance
- 在 `wiki/ops/index.md` 公开样例入口
- 如果探索收束成稳定 workflow policy，再通过 OpenSpec change 和 ADR 固化

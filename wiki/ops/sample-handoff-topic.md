---
title: 会话承接样例：agent 自进化不是噱头
type: intake
language: zh-CN
source_path: chat://handoff-mode/sample-north-star
source_type: conversation
audience: self
knowledge_level: working
domain: personal-ops
period: active
confidence: high
status: active
updated_at: 2026-04-18
ai_generated: true
related_sources: []
related_focus_threads:
  - main-thread.md
related_reminders: []
handoff_mode: true
repo_targets:
  - retro
  - openspec-change
---

# 会话承接样例：agent 自进化不是噱头

## 时间

- 首次进入承接态：2026-04-18
- 当前更新时间：2026-04-18

## 原话摘录

> agent 可以跟我的对话自进化，而不是噱头

> 任何流程级争论最后都会落成一条能复盘的 wiki 记录

> OpenSpec 完成、archive review、wiki 运行态，这三层终于像一个系统，而不是三堆文档

## north_star

- 让 agent 在当前会话里识别用户反复拉回的目标，并进入承接态，而不是继续做离散问答或事后总结

## constraints

- 要原文
- 要时间
- 不限 `agent` 话题
- 不能靠“事后统计很多轮”才变得有用

## failure_modes

- 重要争论没记下来，知识继续丢在聊天里
- agent 越学越偏，自动修改错误规则

## preferences

- 临时要求也先捕获，不要一开始就只记“成熟规则”
- 是否晋升，不看机械次数，而看是否持续服务同一个北极星

## disagreements

- “同一话题超过 2 轮”是否应该写成核心定义
- 是否应先做 skill 自动修改，还是先做 capture + structure

## open_questions

- handoff mode 的最小触发阈值到底是什么
- durable record 应该在 mode 进入时立刻生成，还是稍后生成

## candidate_practices

- 会话内 repeated north-star pull 应触发 handoff mode
- `两轮以上` 只能作为辅助信号，不能作为唯一主规则

## repo_targets

- 当前最适合的 durable 落点：
  - [Agent 治理 gate 缺口复盘 2026-04-18](agent-governance-gate-gap-retro-2026-04-18.md)
  - `introduce-north-star-handoff-mode` OpenSpec change

## 下一步

- 把 handoff mode 的规则和样例写进 repo guidance
- 再决定哪些部分后续需要 health-check 或 skill 晋升

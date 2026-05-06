---
canonical_object: check-to-wiki-routing
artifact_type: intake
title: check-to-wiki-routing / intake
type: intake
language: zh-CN
source_path: chat://openspec-explore/check-to-wiki-routing/2026-05-06
source_type: conversation
audience: self
knowledge_level: working
domain: personal-ops
period: active
confidence: medium
status: active
updated_at: 2026-05-06
ai_generated: true
trace_mode: openspec-explore
same_topic_rule: update-existing
related_objects:
  - example-driven-capture
  - material-collaboration-defaults
  - conversation-handoff
---

# check-to-wiki-routing / intake

## 触发问题

用户希望当自己让 agent “检查”某个东西时，agent 不要只在聊天里回答，而是自动判断是否应进入 wiki。用户同时回忆已有一个能区分任务类型的机制：学习、汇报、进度跟进、或其他。

## 当前关注点

- 先判断这是不是该创建 skill，还是复用现有 skill / wiki 路由。
- “检查”不是单一任务类型，可能分别落到 review、学习沉淀、材料处理、项目推进、提醒、handoff 或 OpenSpec。
- 若要做 skill，目标应是分流入口，不是把所有检查结果都强制写 wiki。

## 当前假设

- 已有资产已经覆盖多类分流：`example-driven-wiki-capture`、`material-collaboration-defaults`、`meeting-note-output`、`project-management-weekly-skill`、`readme-learning-capture`。
- 缺口可能不是“没有分类规则”，而是缺一个在用户说“检查一下”时先判别意图和 wiki 落点的触发层。
- 该触发层如果落成 skill，应先走 OpenSpec，不能在 explore 模式直接实现。

## 暂未决定

- 新 skill 是否必要。
- 如果必要，skill 名称和触发范围是什么。
- 该能力应放在 repo-local `.codex/skills/`，还是作为 root/global 行为资产。

## 下一步

- 对照现有 skills 和 `wiki/ops/index.md` 的推荐流转，判断是否需要新增一个“检查请求分流”skill。
- 若需要新增或修改 skill，先退出 explore，并为行为资产变更创建 / 选择 OpenSpec change。

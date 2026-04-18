---
title: AI Chat 一键安装 Skill 探索
type: intake
language: zh-CN
source_path: chat://openspec-explore/ai-chat-one-click-install-skill-2026-04-17
source_type: conversation
audience: self
knowledge_level: working
domain: ai-workflow
period: active
confidence: medium
status: active
updated_at: 2026-04-17
ai_generated: true
related_sources: []
related_focus_threads:
  - main-thread.md
related_reminders: []
explore_mode: true
trace_mode: openspec-explore
same_topic_rule: update-existing
---

# AI Chat 一键安装 Skill 探索

## 触发问题

希望把当前仓库里的 wiki 工作流、skill 分层和治理约束，整理成一个“AI chat 一键安装”的能力，目标至少覆盖 Cursor、Claude、Codex 三种运行面，并最终沉淀成一份可分享的飞书说明。

## 当前关注点

- 这个能力到底应被定义为“单个 skill”还是“跨平台安装包 + 平台适配层”
- 仓库当前 workflow 主要依赖 `AGENTS.md`、repo-local `.codex/skills/`、wiki/ADR/OpenSpec 边界
- Cursor、Claude、Codex 的承载面并不一致，不能假设同一份文件原样通用
- 分享物不能只讲安装，还要讲边界、适配差异和适用场景

## 当前假设

- 最稳妥的交付形态不是单一 `SKILL.md`，而是一个统一规范源加多个平台适配输出
- 可以把 repo workflow 抽成三层：
  - 核心治理层：目标、边界、反模式、验证要求
  - 工作流层：material processing、meeting note、explore trace 等可复用流程
  - 平台适配层：Cursor rules / AGENTS.md / Claude command or memory entry
- “一键安装”更像安装器 workflow，而不是最终用户直接手写多个平台文件
- 飞书分享物需要同时覆盖：为什么做、怎么装、不同 AI chat 的映射关系、什么场景不该装

## 暂未决定

- 统一规范源放在 repo 内什么位置最合适
- Claude 侧应主打 `CLAUDE.md`、custom slash command，还是两者组合
- Codex 侧是否只依赖 `AGENTS.md`，还是要把 repo-local skills 也纳入安装物说明
- Cursor 侧应优先生成 `.cursor/rules/` 还是 `AGENTS.md` 兼容入口
- “一键安装”是本地命令、对话触发 skill，还是发布成外部仓库模板

## 下一步

- 先把三端的最小承载模型和差异对齐
- 再判断应该立一个 workflow-level OpenSpec change，还是先写分享版设计说明
- 如果进入实现，必须先创建 active OpenSpec change，再动 repo workflow 或 skill 发布面

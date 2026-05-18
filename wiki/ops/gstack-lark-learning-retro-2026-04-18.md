---
title: gstack 与 larksuite CLI 学习复盘 2026-04-18
type: retro
language: zh-CN
audience: self
knowledge_level: working
domain: wiki
layer: ops
ops_area: learning-capture
canonical_object: gstack-lark-learning
artifact_type: retro
period: 2026-04
status: active
updated_at: 2026-04-18
ai_generated: true
related_focus_threads:
  - main-thread.md
related_sources:
  - https://github.com/garrytan/gstack
  - https://github.com/larksuite/cli
---

# gstack 与 larksuite CLI 学习复盘 2026-04-18

## 时间

- 首次整理：2026-04-18
- 当前更新时间：2026-04-18

## 来源

- `gstack` repo
  - <https://github.com/garrytan/gstack>
- `larksuite/cli` repo README
  - <https://github.com/larksuite/cli>

## 这次真正复用了什么

### 从 gstack 复用

- 把方法论做成明确 skill / workflow 入口，而不是靠临时 prompt
- 用 `office-hours` 这类追问式方法逼近真正目标，而不是一开始就写设计
- 用 `autoplan / review` 这种阶段化收束方式，把聊天里的判断变成 repo-visible artifact

### 从 gstack 修改了什么

- 没有整套照搬 `gstack`
- 而是把它的方法论改造成当前 repo 的 `north-star handoff mode`
- 把外部 methodology 落进了本仓库自己的：
  - `AGENTS.md`
  - `wiki/ops`
  - `OpenSpec spec`

一句话：

`今天真正做成的不是“用了 gstack”，而是把 gstack 的方法论内化成了本仓库的 conversation-native handoff 机制。`

## 从 larksuite CLI README 学到了什么

- 值得复用的不是单个命令，而是它的组织方式：
  - AI Agent Quick Start
  - 安装 / 配置 / 登录 / 验证的固定步骤
  - `shared skill + domain skill + workflow skill` 的分层
- 这很适合后续沉淀成当前 repo 的：
  - Feishu CLI quickstart 模板
  - Feishu 能力分层模板

## 这次修改了什么

- 已 formalized：
  - `north-star handoff mode`
- 还未 formalized：
  - `larksuite/cli README -> skill/template`

这说明今天的结果不是两边都已经落地，而是：

- `gstack` 方法论已经转成仓库规则
- `larksuite/cli` 这边只完成了学习和结构识别，还没有正式沉淀成 skill 或模板

## what_reused

- `gstack` 的方法论编排思路
- `larksuite/cli` README 的 AI-agent quickstart 和 skill layering 结构

## what_modified

- 把 `gstack` 的方法论从外部 skill 包改成仓库内生治理机制
- 没把 `larksuite/cli` README 直接复制成 skill，而是先识别为后续模板来源

## what_not_formalized

- Feishu CLI 安装 / 认证模板
- Feishu 能力分层模板
- README 到正式 skill 的发布边界

## repo_target

- 当前落点：
  - `wiki/ops retro`
- 可能的后续落点：
  - `OpenSpec change`
  - `wiki/examples`
  - `wiki/team-lore-candidates.md`

## next_step

- 开一条独立 change，把 `larksuite/cli README` 提炼成 repo 内模板或 skill 草案
- 后续遇到外部 repo 或 README 学习时，默认在同轮留下 project wiki 记录，不再等用户提醒

---
title: Agent 治理 gate 缺口复盘 2026-04-18
type: retro
language: zh-CN
audience: self
knowledge_level: working
domain: personal-ops
period: 2026-04
status: active
updated_at: 2026-04-18
ai_generated: true
related_intake:
  - agent-governance-gate-gap-explore-2026-04-18.md
related_focus_threads:
  - main-thread.md
---

# Agent 治理 gate 缺口复盘 2026-04-18

## 复盘背景

这次围绕同一个问题连续争论了多轮：

- 仓库已经写了很多 agent 工作流规则
- `ADR` 和 OpenSpec 也已经补了不少治理边界
- 但运行中仍出现“规则存在，执行没触发”的漂移

这说明问题已经不是单次聊天误解，而是值得固定留痕的流程级复盘点。

## 这次确认的核心论点

当前仓库的真实瓶颈不是缺治理设计，而是很多关键节点只停留在“规则层”，还没有进入“可执行 gate 层”。

更具体地说：

- 规则层：`AGENTS.md`、`wiki/ops` 规则页、`ADR`、OpenSpec spec 已经定义了很多应该怎么做
- gate 层：只有当规则变成预检、状态字段、失败信号、归档阻断或固定证据要求时，运行时才会稳定触发

如果规则没有进入 gate 层，就容易退化成：

- 当前讨论时很严格
- 下次运行时靠记忆
- 多轮之后只剩原则，不剩动作

## 在当前仓库里的具体体现

### 1. `openspec-explore` 已部分落地

已经落地的部分：

- `ADR-0009` 已定义 explore trace 规则
- `AGENTS.md` 已要求进入 `openspec-explore` 前先在 `wiki/ops/` 留 trace
- `wiki/ops/sample-explore-trace.md` 已提供最小样例

当前结论：

- `openspec-explore` 作为“探索先留痕”的基础机制，已经落地
- 但它只保证“探索前有 trace”，不保证“多轮争论后的流程复盘一定沉淀成 retro”

### 2. `archive review` 仍停在制度层

已经落地的部分：

- `ADR-0007` 和 repo `AGENTS.md` 已定义 `complete -> archive review -> archive`

未落地为 gate 的部分：

- 没有 repo health-check 扫描“tasks 全勾但未 archive review”的 active change
- 没有显式状态字段承接“实现完成但仍待 archive review”
- 没有统一 closing checklist 或固定入口命令

结果：

- 规则是存在的
- 但忘记执行时，不会自动暴露成失败信号

### 3. `ops` 生命周期仍主要靠人工判断

`intake -> reminder -> codex-handoff` 的边界设计已经写清楚，但目前仍主要依赖人工判断：

- intake 不会因为长时间未处理自动暴露
- reminder 不会因为 stale 自动触发复盘
- handoff 也没有结构化准入检查

结果：

- 规则有了
- 但运行稳定性仍然依赖当下执行者是否记得检查

## 这次学到的判断法

以后遇到类似争论，先问 4 个问题：

1. 这件事现在是“写在规则里”，还是“已经会在运行时失败/阻断”？
2. 如果执行者忘了做，仓库会不会自己暴露这个遗漏？
3. 这次讨论得到的是稳定决策，还是一次执行偏差？
4. 它应该沉淀到 `ADR`、`OpenSpec change`、`archive-review.md`，还是 `retro / logs`？

一句话判断：

`凡是围绕同一 agent 流程缺口反复争论两轮以上，且问题来自现有机制未稳定触发，就应该留下 repo-visible 复盘。`

## 当前建议的记录边界

- 稳定决策：进 `ADR`
- 本次变更范围、实现和任务：进 `OpenSpec change`
- archive 阶段的复杂判断：进 change-local `archive-review.md`
- 多轮同主题的 agent 流程偏差、执行落空、规则漂移：进 `wiki/ops` 下的 retro

## 后续关注点

- 是否把“多轮 agent 流程争论必须落一条 retro / trace”升级成新的仓库默认规则
- 是否为 archive review 和 ops 生命周期增加最小 health-check
- 是否需要一个更清晰的 `ops` retro 索引页，避免复盘页面继续散落

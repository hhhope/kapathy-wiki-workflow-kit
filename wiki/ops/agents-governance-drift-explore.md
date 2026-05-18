---
title: agents-governance-drift / explore
type: explore
canonical_object: agents-governance-drift
artifact_type: explore
language: zh-CN
audience: self
domain: wiki
layer: ops
ops_area: agent-governance
status: active
updated_at: 2026-04-21
ai_generated: true
derived_from:
  - wiki/ops/agents-governance-drift-retro.md
  - wiki/ops/agents-governance-remediation-explore-2026-04-21.md
related_objects:
  - agent-governance-gate-gap
  - conversation-handoff
  - disagreement-management
notes_scope: 在同一治理漂移主题下补一条独立 explore；先把立即冲突与治理设计分开，并补记当前收束到 repo-level AGENTS Phase 0 change 的起点
---

# agents-governance-drift / explore

## 1. 本页定位

- 这是同一 `agents-governance-drift` 话题下的新 explore，不替代现有 `retro`，也不覆盖既有 remediation explore
- 本页只做一件事：把后续治理讨论先拆成两个方向，再看哪些问题应该并行、哪些问题不该混着排优先级
- 当前仍不进入 `proposal / design / tasks`

## 2. 当前更清晰的二分

```
agents-governance-drift
├── A. 立即冲突
│   ├── 已经互相打架
│   ├── 已经影响运行判断
│   └── 不需要先等元规则完整
└── B. 治理 / 防漂移设计
    ├── 现在不一定撞墙
    ├── 但决定以后是否继续长歪
    └── 更适合做层级和容器边界整理
```

一句话：

`有些问题已经是 active contradiction，有些问题只是下一轮治理设计对象。两者不该用同一把尺子排顺序。`

## 3. A 方向：立即冲突

### A1. evaluation.md 字段冲突

当前 repo guidance 里对 `evaluation.md` 的最小结构存在并列表达：

- 一套写成 `Baseline Scenarios / Before Results / After Results / Residual Risks`
- 另一套写成 `Pressure Scenarios / RED Baseline / GREEN Result / Residual Risks`

这里的问题不是“归属表还没补完”，而是：

- 同一 artifact 的要求已经互相竞争
- 运行时 health-check 已经偏向其中一套
- 这类冲突会让后续 skill / governance 变更在开始前就带着歧义

当前判断：

- 这是 `立即冲突`
- 不应被“先补 AGENTS/skill/ADR 六层归属表”阻塞

### A2. repo-local `openspec-explore` skill 文本弱于 repo 已正式化边界

当前 repo 已把 `openspec-explore` 正式化成：

- 先在 `wiki/ops/` 留 trace
- 再继续探索
- explore trace 复用 `intake`

但 repo-local `openspec-explore` skill 本体仍沿用更通用的上游口径，例如：

- `This is a stance, not a workflow`
- `There are no fixed steps, no required sequence, no mandatory outputs`
- `Don't auto-capture`

这里的冲突不是“是否支持自由探索”，而是：

- 在本 repo 里，哪些 capture 是强制 workflow obligation
- 哪些 capture 才属于必须显式征得用户同意的 formal artifact mutation

当前判断：

- 这也是 `立即冲突`
- 它不是纯风格问题，而是 repo formalized behavior 与 skill runtime wording 的边界不一致

## 4. B 方向：治理 / 防漂移设计

### B1. AGENTS 入口膨胀与重复复述

这里讨论的是：

- `AGENTS.md` 是否承载了过多已经在 ADR / spec / wiki 沉淀的内容
- 入口文件应该保留多少摘要、多少链接、多少主源声明

这类问题会影响：

- 可读性
- 维护成本
- 后续新增规则时是否继续堆叠

但它和 `A` 方向不同：

- 它不一定会立刻在当前运行里撞墙
- 更像是结构负债与入口压缩问题

### B2. 层级归属仍未完全说清

当前仍有一个真实开放问题：

`AGENTS.md / repo-local skill / ADR / OpenSpec spec / wiki/ops retro` 各自到底收什么？

这会影响：

- 新规则先写到哪一层
- 什么时候该 promotion
- 什么时候只是 trace / retro，什么时候已经足够 formalize

这类问题确实适合做元规则澄清，但它更像治理设计，不该天然卡住所有当前冲突修复。

### B3. repo 与个人 dotfiles 的跨文件漂移

`repo AGENTS.md`、`~/.codex/AGENTS.md`、`~/.claude/CLAUDE.md` 之间确实存在漂移，但这里更像外轨：

- repo 内治理可以先处理 repo 自己的 entrypoint 与本地 skill 合同
- dotfiles 是否并入本 repo 主线，需要单独确认 scope

当前倾向：

- 把它视为 `相关外轨`
- 不自动变成本 repo 本轮整改主轴

## 5. 对现有 remediation explore 的修正读取

这页不是推翻 `agents-governance-remediation-explore-2026-04-21`，而是给它补一层更前置的读法。

### 对 D1 的修正读取

- `D1` 仍然重要
- 但它更像 `B 方向` 的元规则工程
- 它不该被抬成所有问题的前置门槛

### 对 D2 的修正读取

- `D2` 明显属于 `B 方向`
- 本质是 entrypoint compression，不是立即冲突修复

### 对 D3 的修正读取

- `D3` 明显属于 `A 方向`
- 不该被“先完成 D1”自动阻塞

### 对 D4 的修正读取

- `D4` 更像 `外轨治理`
- 可以被记录，但不应默认并入 repo 内主线

### 对 D5 的修正读取

- `D5` 不太像从零设计新 trigger
- 更像把已经在 method / spec 里更具体的信号回写到 entrypoint

## 6. 当前更真实的待定决策

这轮先出现的不是“先做 D1 还是 D2”，而是下面两个更前置的问题：

1. 哪些问题已经属于 `立即冲突`，应与治理设计拆开处理？
2. `repo 内主线` 与 `dotfiles 外轨` 是否要故意分开，不再放进同一整改篮子？

如果这两个问题不先拆清：

- 所有方向都会看起来像同一种“整改项”
- 但它们其实在处理不同层次的问题

## 7. 当前清晰度

当前更接近下面这个判断：

- `A 方向` 处理“现在已经互相打架的东西”
- `B 方向` 处理“怎样让入口、层级和主源以后不再继续漂移”

所以后续如果继续往前走：

- 可以允许 `A` 和 `B` 分轨
- 不必强行要求所有工作都先等元规则完整

## 8. 下一步候选

- 若只想先止损：优先继续看 `A 方向`
- 若要做长期整理：把 `B 方向` 收束成更明确的层级表或入口压缩方案
- 若两边都要做：把它们当作两条不同节奏的治理线，而不是同一张优先级表

本页仍是 explore，不在这里决定具体改哪份文件、起哪条 OpenSpec change。

## 9. 2026-04-21 本轮补记

### Trigger question

- 用户当前追问的是：`先看下要改的内容，change 先做出来`
- 并且已明确第一落点是 `repo-level AGENTS.md`，不是根上的 `~/.codex/AGENTS.md`

### Current focus

- 把本轮 change 的起点收紧到 `repo-level AGENTS governance Phase 0`
- 先为 repo 内默认治理行为建立正式 change 边界
- 暂不把 root dotfiles 合流、跨 agent 全局切分、`Phase 1` 压缩迁移混进同一 change

### Current hypotheses

- `Phase 0` 与 `Phase 1` 必须拆开，否则会把“接受 mainline”和“执行迁移”绑死在同一轮
- repo 当前已存在足够证据说明 `candidate != accepted`，所以新 change 应先解决 acceptance gate，而不是直接改写 `AGENTS.md`
- `ADR-0007` 重号属于 repo 内立即冲突，可以作为本轮 repo change 的组成部分
- root-level `~/.codex/AGENTS.md` 和 `~/.claude/CLAUDE.md` 暂应视为外轨，不应自动进入 repo 主线整改

### Open questions

- 这轮 `Phase 0` change 是否只定义 repo 内 gate，还是同时把 repo-local pre-commit hook 也纳入实现范围
- 新 ADR 应该只确认 “repo-level Phase 0 先行”，还是更进一步接受 v3.1 的 repo 子集
- `evaluation.md` 字段冲突是否并入同一 change，还是保留在后续独立修复线上

### Next step

- 新建一个只覆盖 `repo-level AGENTS governance Phase 0` 的 OpenSpec change
- 在 change artifacts 里写清 scope、非目标、接受门槛和 deferred items
- 后续是否进入实现，等 change 边界和主线确认后再说

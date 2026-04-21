---
title: agents-governance-drift-distill-calibration / retro
type: retro
canonical_object: agents-governance-drift-distill-calibration
artifact_type: retro
language: zh-CN
audience: self
domain: personal-ops
status: active
updated_at: 2026-04-21
ai_generated: true
derived_from:
  - wiki/ops/agents-governance-drift-distill-2026-04-21.md
  - wiki/ops/agents-governance-drift-retro.md
  - wiki/ops/agents-governance-drift-explore.md
  - wiki/ops/openspec-explore-trigger-drift-retro.md
related_objects:
  - agents-governance-drift
  - disagreement-management
  - conversation-handoff
notes_scope: 给后续 Claude 校准使用；记录 distill 页当前哪些说法已经越过本次对话实际收束边界
---

# agents-governance-drift-distill-calibration / retro

## Trigger

`wiki/ops/agents-governance-drift-distill-2026-04-21.md` 试图对 2026-04-21 整轮 session 做二次蒸馏，但当前写法已经把多处仍在探索/复盘中的材料压成了“最终框架”。

这页不是否定 distill 的价值，而是保留当前仍需校准的争议点，供下一轮继续收束。

## Current Use

如果后续要让 Claude 基于 distill 继续推进，这页应被一起读取。

理由：

- distill 页保留了大量 session 事实与候选框架
- 但其中一部分已经越过本轮真实共识边界
- 如果不把这些争议点单独保住，下一轮很容易把候选框架误读成已定 canonical

## Rejected Compression

当前最需要反压缩保留的不是：

- “这页写得太长”

而是：

- “这页把哪些 still-open 的东西写成了 already-settled”

## Main Disagreements

### 1. “v3.1 最终框架”说法过早

distill 当前把：

- `v3.1 最终框架`
- `6 层`
- `12 条规则`
- `AGENTS.md 488 -> ~35 行`

都写成了 session 已收束出的结果。

当前更诚实的状态是：

- 这是一套强候选框架
- 它可能是作者走完一轮自测后的 preferred model
- 但它不是本次对话已经稳定确认的共享结论

尤其前面的 explore 只收束到：

- `立即冲突`
- `治理 / 防漂移设计`

并没有共同确认这套 `S0-S2 / A1-A3 / B1-B3` 的完整层级模型。

### 2. “本文件不作决定”与正文实际冲突

distill 虽然声称：

- `本文件不作决定`

但正文中已经出现明显决策化句式，例如：

- `已废弃`
- `最小起步集 = a + b + c`
- `任何推进前必须先 a`
- `阻塞 Phase 2 执行`

这类表述会把 distill 从：

- `session 二次蒸馏`

推进到：

- `后续治理主线与前置条件`

这已经不是纯 distill。

### 3. derived 页面关系被压扁

distill 当前对几个来源页的吸收关系说得过满：

- `agents-governance-drift-explore.md` 被写成“证伪矩阵”
- `agents-governance-remediation-explore-2026-04-21.md` 被写成“已废弃”

当前更稳的说法应是：

- 新 explore 给 remediation explore 补了一层更前置的读法
- remediation explore 的主轴/排序存在问题
- 但它不是零价值，也还没有被正式废弃

换句话说：

`修正读取` 不等于 `废弃来源`。

### 4. 多个后续动作被写成默认 phase plan

distill 把很多仍属候选的动作整理成了默认 phase：

- 新建 `<repo>/CLAUDE.md`
- 建最小 tooling
- 修 team-lore 路径漂移
- evaluation 三套字段合流

这些动作可以是很强的候选，但当前还缺至少两层确认：

1. 这是 repo 主线整改，还是外轨问题
2. 这是候选路径，还是唯一主线

### 5. 数值目标“488 -> ~35 行”过硬

当前对话支持的是：

- 入口压缩
- 减少复述
- 单一主源 + bounded proxy

但并不支持已经共同认定：

- `~35 行` 是合理且必要的目标值

这个数字更像框架作者的优化目标，而不是本轮自然形成的共享边界。

## What Seems Fair To Keep

下面这些内容目前看是可以保留在 distill 里的：

- session arc 的时间线和转折点
- “方法漂移 / trigger 漂移 / scope 漂移” 这三个问题的回顾
- TDD 曾经发生过，以及框架作者确实做了多轮自测
- 一套候选框架已经浮现，并且比早期矩阵更完整

也就是说：

`事实层可保留，结论强度需要降级。`

## Better Current Wording

如果让 distill 页更适合作为后续校准入口，当前更合适的口气不是：

- `v3.1 最终框架`
- `已废弃`
- `必须先 a`

而更像：

- `v3.1 候选框架`
- `当前作者倾向`
- `待进一步校准`
- `如果采用该框架，可能的起步顺序`

## Current Clarity

当前更真实的状态可以压成三句：

1. distill 页已经成功把 session 材料高密度整理出来了
2. 但它把一套候选治理框架写成了接近 canonical 的状态
3. 下一轮若继续用它，必须把“事实回顾”和“候选框架”重新拆开

## Next Calibration Questions

后续若让 Claude 继续校准，建议先只回答下面几个问题：

1. distill 中哪些段落是 `session fact recap`，哪些段落已经进入 `candidate governance model`？
2. `v3.1` 应否整体降级成 `candidate`？
3. `已废弃`、`必须`、`阻塞` 这些词是否都应降级成更弱表述？
4. 哪些动作属于 repo 主线，哪些只是个人 dotfiles / tooling 外轨？

## Non-goal

这页不直接改 distill 原文。

它只保留一件事：

`不要让下一轮把 distill 误读成“本次已经形成的稳定治理决定”。`

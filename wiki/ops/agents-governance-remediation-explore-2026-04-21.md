---
title: AGENTS.md 治理漂移整改方向探索 2026-04-21
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
related_objects:
  - agent-governance-gate-gap
  - wiki-readable-views
notes_scope: 整改方向探索轮；未决定治理动作，留待用户定调
---

# AGENTS.md 治理漂移整改方向探索 2026-04-21

## 1. 本文件定位

- 配对 `wiki/ops/agents-governance-drift-retro.md`（retro，诊断证据），本文件是 explore（整改方向）
- 复用与 `agent-governance-gate-gap-retro-2026-04-18.md` ↔ `agent-governance-gate-gap-explore-2026-04-18.md` 同样的 pair 模式
- **不作决定**，只把 retro 的 14（repo）+ 8（全局 Codex）= 22 项诊断折叠成可讨论的方向和目标，列权衡、列耦合、列待定决策

指回 retro：14+8 项诊断 + 三文件漂移图 + 三个关键反转（Wiki 管道已沉淀 / 四层归属待补 / karpathy 建议被违反）。本文件假设读者已看过 retro。

## 2. 漂移地形图

```
                    ┌──────────────────────────┐
                    │  AGENTS.md 治理漂移      │
                    │  （retro 14+8 项诊断）   │
                    └──────────────────────────┘
                                 │
       ┌─────────┬───────────────┼────────────────┬─────────────┐
       ▼         ▼               ▼                ▼             ▼
  ① 容器     ② 内容          ③ 跨文件        ④ 历史建议    ⑤ 软判断
     scope    矛盾           漂移             不生效         堆积
     未定义   (evaluation.md  (repo AGENTS.md  (karpathy /    ("clearly"
              三套字段 /     + ~/.codex/AGENTS  gate-gap     "repeatedly"
              Wiki 管道      + ~/.claude/      retro 建议     "continues")
              288 行复述)    CLAUDE.md)       被违反)
```

5 症状 × 3 层次折叠：

| 层 | 症状 | retro 条目（repo / global） |
|----|------|---------------------------|
| A · 元规则缺位 | ① ③ | repo 4/5 + global G6 |
| B · 具体违规  | ② | repo 1/3/8/10/13 + global G1/G2/G3/G4/G7 |
| C · 触发机制  | ④ ⑤ | repo 9/11 + retro 反转 C |

## 3. 5 个整改方向

| # | 方向 | 层 | 成本 | 杠杆 | 依据 |
|---|------|----|------|------|------|
| **D1** | 新建 ADR 补完六层归属表（ADR / OpenSpec / archive-review / retro / AGENTS.md / skill） | A | 中（1 ADR + 可能 1 OpenSpec change） | 最高 | `agent-governance-gate-gap-retro-2026-04-18.md` L103–108 已定前四层；ADR-0002 / ADR-0003 / ADR-0008 已建立 promotion gate 基础 |
| **D2** | 迁移 Wiki 管道 288 行出 AGENTS.md（合并进 `wiki/ops/agent-readable-wiki-*.md` 综述页 或 `openspec/specs/`），AGENTS.md 只留触发指引 + 链接 | B | 中（1 OpenSpec change） | 高 | ADR-0013 到 ADR-0023（11 份）+ 10 份 `wiki/ops/agent-readable-wiki-*.md` 已完整沉淀；按 ADR-0002 稳定决策归 ADR |
| **D3** | 合流 evaluation.md 三套字段（repo L27 / L40 / 全局 Codex L274–278） | B | 小–中（文字 consolidation；若涉及分层语义则需 1 ADR） | 中 | 源自两份 archived change（`enforce-skill-evaluation-evidence` / `require-local-skill-pressure-tests`）；当前三处文字并列未说明分层意图 |
| **D4** | 新建 ADR 声明三份文件（repo AGENTS.md / `~/.codex/AGENTS.md` / `~/.claude/CLAUDE.md`）分工；顺带修 team-lore 路径与 main 分支重复 | A | 中 | 中 | retro Part 2 三文件漂移图；无任何已有 ADR 覆盖此层 |
| **D5** | 把 AGENTS.md 软判断短语（"clearly continues" / "repeatedly converges" / "redirection has occurred"）换成可观察触发 | C | 小 | 低–中 | Handoff mode 已有 counter 雏形；Explore Trace 需补 fail-safe（retro 条目 11） |

## 4. 4 个目标

| # | 目标 | 可观察指标 |
|---|------|-----------|
| **G1** | 降漂移：三份规则源不再互相冲突 | team-lore 路径一致 / evaluation.md 一套字段 / OpenSpec boundary 只在一处 |
| **G2** | 控容量：AGENTS.md 止住无边界增长 | 488 行 → ≤ 300 行；后续每次增项附迁出项 |
| **G3** | 复用既有沉淀：AGENTS.md 不再重复 ADR / spec / wiki 已有内容 | Wiki 管道 288 行迁出；新段落前先检索是否已在 ADR |
| **G4** | 历史建议可触发：retro/ADR 建议不再失效 | karpathy / gate-gap retro 建议各自绑定到 hard gate（如扩容前强制 re-read） |

## 5. 方向 × 目标耦合矩阵

```
            G1 降漂移   G2 控容量   G3 复用   G4 可触发
D1 scope      ●●          ●          ●●        ●●●     ← 元规则，其它方向的裁决标准
D2 迁移       —           ●●●        ●●●       —
D3 eval       ●●●         —          ●●        —
D4 三文件     ●●●         —          —         ●
D5 软判断     —           —          —         ●●
```

读法：
- **D1 是高杠杆基座** —— 触及所有 4 个目标，但只有它定义了"什么该进 AGENTS.md / skill 本体"。D1 未落前做 D2/D3 会留手感决策痕迹
- **D4 是独立轨** —— 跨全局 + 仓库，可以不等 D1。但全局文件是用户 dotfiles，scope 溢出本仓库需要先确认
- **D5 是清洁任务** —— 无依赖，可随时并行
- **D2 / D3 是出血止损** —— 可选"等 D1 后再按标尺做"或"先做显眼症状争取时间"

## 6. 3 个待定决策

1. **先做元规则还是先砍 288 行？**
   - (a) D1 优先：先定标尺再迁移，代价是 AGENTS.md 在 D1 完成前仍 488 行
   - (b) D2 优先：先止血，代价是 D1 做出来后可能需要对 D2 的迁移位置二次调整
   - (c) 并行：D1 和 D2 同时起 OpenSpec change；代价是两 change 之间可能冲突

2. **全局文件要不要进本 repo 治理？**
   - (a) D4 全做：repo ADR 声明三份文件分工（含 `~/.codex/AGENTS.md` + `~/.claude/CLAUDE.md`）
   - (b) 只管 repo AGENTS.md 侧：repo ADR 只管自己那份，全局文件留作个人维护
   - (c) 升级到 team-lore 候选：这是跨项目问题，写进 `wiki/team-lore-candidates.md` 而非本 repo ADR

3. **evaluation.md 三套字段的分层意图**
   - (a) 先读两份 archived change（`enforce-skill-evaluation-evidence` / `require-local-skill-pressure-tests`）的 proposal.md + design.md，确认是否本就是分层（base + pressure extension）
   - (b) 不回溯 archived change，直接把三处文字合为一套
   - (c) 废弃其中一个 spec，统一到另一个

## 7. 本文件的使用方式

- 用户挑选 D/G 组合与 3 个待定决策的答案 → 本文件升级为下一轮 OpenSpec change 的 `derived_from` 来源
- 若用户决定暂不治理 → 本文件留作后续回顾的选项档案，`status` 改为 `archived`
- 若 22 项诊断有增减 → 更新 retro，本文件的方向映射也需同步更新

本 explore **不等于** proposal / design / tasks，不写 decision / recommendation。

---
title: AGENTS.md 治理漂移候选实施 playbook 2026-04-21
type: playbook
canonical_object: agents-governance-drift
artifact_type: playbook
language: zh-CN
audience: self
domain: personal-ops
status: candidate
updated_at: 2026-04-21
ai_generated: true
derived_from:
  - wiki/ops/agents-governance-drift-distill-2026-04-21.md
related_objects:
  - agents-governance-drift-distill-calibration
  - conversation-handoff
  - disagreement-management
notes_scope: candidate implementable playbook；含放弃项 + 问题对账 + 完成硬指标；升格为 accepted 仍需走 Phase 0 action (a)
---

# AGENTS.md 治理漂移候选实施 playbook 2026-04-21

> **本 playbook 是 candidate，不是 accepted decision。** 内容来自 distill + 本 session 务实对账，无框架层增量。升格为 accepted 唯一通道是 Phase 0 的 action (a)（OpenSpec change + 新 ADR）。
>
> 同读：
> - `wiki/ops/agents-governance-drift-distill-2026-04-21.md`（完整 TDD + 框架 + 校准）
> - `wiki/ops/agents-governance-drift-distill-calibration-retro.md`（校准依据）
> - `wiki/ops/agents-governance-drift-distill-replay-validation-2026-04-21.md`（bounded replay proof）

---

## 0. 放弃项（out of scope）

本实施版本明确放弃两项未决：

- **Claude PreToolUse hook** —— 违反跨 agent 对称性，治理方案不应依赖单一 agent 独有能力
- **Git pre-commit 脚本复杂度的深度评估** —— 假设脚本能写、简单可维护，不再测

下文不再讨论这两项。

---

## 1. 放弃后的 enforcement bundle

```
跨 agent 实质 gate：
  Layer 1 · Git pre-commit hook    ← 结构违规（假设可工作）
  Layer 3 · OpenSpec + 人类 review  ← 过程 + 语义违规
  Layer 4 · drift scan             ← 兜底

跨 agent prompt-level 提示（marginal）：
  Layer 2 · AGENTS.md 顶部 trigger OR governance-change-gate skill
             （二选一，不叠加）

跨 agent 纪律补偿：
  workflow 切分 —— 治理编辑优先 Claude Code session
```

---

## 2. 一句话概述

**v3.1 候选框架 = 6 层（S0/S1/S2 跨 agent + A1/A2/A3 Claude + B1/B2/B3 Codex）+ 12 规则 + 上面 enforcement bundle + workflow 切分纪律。**

目标（作者倾向，非共识）：AGENTS.md 488 → ~35 行。

---

## 3. Phase 0 · 升格前提（4 项并行）

未完成前不启动 Phase 1：

- **(a)** OpenSpec change + 新 ADR，接受 v3.1 为 accepted mainline（candidate → stable 唯一通道）
- **(b)** Fix ADR-0007 重号（`0007-archive-review-before-archive.md` + `0007-retire-draft-skills-as-runtime-surface.md` 两份冲突）
- **(c)** 建 Layer 1 Git pre-commit hook（grep 检查 >1 行 summary + ID 存在性 + supersede 传播）
- **(j)** 明文确立 workflow 切分纪律（写入 A1 `~/.claude/CLAUDE.md` + B1 `~/.codex/AGENTS.md`）

### Phase 0 完成硬指标（4 条全 ✓ 才过）

- [ ] OpenSpec change 已归档 + 新 ADR `Status: accepted`
- [ ] `wiki/adr/0007-*` 重号已消（重命名或升编号）
- [ ] `.git/hooks/pre-commit` 或 `.githooks/pre-commit` 能拦下一个违反 R2 的测试 commit
- [ ] A1 + B1 两份 config 都含 workflow 切分文字

---

## 4. Phase 1 · AGENTS.md 488 → ~35 行迁移（R10 protocol）

| 步 | 动作 | 完成判定 |
|----|------|---------|
| 1.1 | Wiki 管道 240 行 → gateway + 综述页链接 | AGENTS.md 12-22 段缩为 1 gateway 段 |
| 1.2 | Meta-rule 5 段 proxy 化 | OpenSpec Trigger / Decision Observability / Archive Review / Explore Trace / Re-Anchor Gate 各 1 行 + ADR ID |
| 1.3 | Capability 4 段 proxy 化 | Handoff / Example-Driven / Disagreement / Principles 各 1 行 + spec ID |
| 1.4 | Codex-specific 段保留 | Material Processing + Meeting Note 保持原样（~18 行）|

**R10 protocol：** `canonical 先 verify → proxies 一个 commit 原子更新 → 旧内容最后删`

### Phase 1 完成硬指标

- [ ] AGENTS.md 行数 ≤ 50（~35 目标 + 缓冲）
- [ ] 每段 proxy 都能 grep 到对应 ADR/spec ID
- [ ] pre-commit hook 跑过，无 1 行违规

---

## 5. Phase 2 · A2/B2 重整

| 步 | 动作 | 完成判定 |
|----|------|---------|
| 2.1 | 新建 `<repo>/CLAUDE.md`（A2）| 文件存在 + Claude-specific 项目 context |
| 2.2 | 可选 `<repo>/PROJECT.md`（S0）| 跨 agent 共享 context root |
| 2.3 | B2 AGENTS.md 最终形态 | 行数 ≤ 50 且可 grep 到 canonical ID |

---

## 6. Phase 3 · 跨全局文件漂移修正

| 步 | 动作 | 完成判定 |
|----|------|---------|
| 3.1 | team-lore 路径合流 | A1/B1 跨文件一致 |
| 3.2 | OpenSpec boundary 合流 | 三处重复消除，单一 source |
| 3.3 | evaluation.md 三套字段合流 | 单 spec |
| 3.4 | 可选：三份全局文件分工 ADR | A1/B1/S0 scope 明确 |

---

## 7. 问题 → 能否解决对账

### 能解决（10 项）

| # | 问题 | 被哪一步解决 |
|---|------|-------------|
| P1 | AGENTS.md 488 行扩张 | Phase 1 + Layer 1 Git hook |
| P2 | Wiki 管道 240 行重复 | Phase 1.1 |
| P3 | evaluation.md 三套字段 | Phase 3.3 |
| P4 | ADR-0007 重号 | Phase 0 (b) |
| P5 | team-lore 路径漂移 | Phase 3.1 |
| P6 | OpenSpec boundary 重复 | Phase 3.2 |
| P7 | 元规则无归属 | v3.1 S1 |
| P8 | Supersede 无传播 | v3.1 R5 + Layer 1 |
| P9 | Lifecycle 缺失 | v3.1 R5 |
| P10 | Commit 时无 gate | Layer 1 |

### 部分解决（4 项）

| # | 问题 | 限制 |
|---|------|------|
| P11 | skill vs AGENTS.md 文本冲突 | 规则清晰，agent 实际服从是弱点 |
| P12 | Claude/Codex 双 agent 协调 | 结构清晰，Codex 运行时层未覆盖 |
| P13 | retro 建议自动化 | 通道有，自动化无 |
| P14 | Cross-session 连续性 | 档案有，自动 load 无保证 |

### 接受的逃逸（6 项，不尝试解决）

| # | 问题 | 兜底 |
|---|------|------|
| **E1** | Codex 侧 agent 主动编辑 AGENTS.md | (j) 切分 + Layer 1 commit |
| **E2** | Trigger-drift 递归（agent 跳 skill MUST） | 人类 review（慢）|
| **E3** | 用户 "别查了直接做" override | **无兜底** |
| **E4** | 方法漂移（结构装饰当思考） | 靠用户纠偏 |
| **E5** | Scope 漂移（拔到哲学） | 靠用户纠偏 |
| **E6** | Tooling 自身 governance | 未设计 |

---

## 8. 持续运行

**必须持续：**
- Layer 1 Git pre-commit hook
- Layer 3 OpenSpec + 人类 review

**建议持续：**
- Layer 4 周期性 drift scan
- Layer 2 AGENTS.md 顶部 trigger **或** governance-change-gate skill（二选一）

---

## 9. 最大单点风险

**Phase 0 只做一半就跳 Phase 1。**

若只做 (a) OpenSpec change 但 (c) Layer 1 hook 没建、(j) 切分纪律没立 → Phase 1 迁移 = commit 无拦截 = 新规则继续漂移 = 回到本 session 起点，轮一圈。

**Phase 0 的 4 条完成硬指标（第 3 节末）必须全 ✓ 才能启动 Phase 1。**

---

## 10. 不升格的 fallback

若不走 action (a)：
- AGENTS.md / ADR / spec / skill 全不动
- 本 session 产出沉淀在 wiki/ops 作 archive
- 下次 session 加载时按 candidate 对待
- 下轮有动力再推进 Phase 0

**这也是合法选项。** candidate 不是必须升格。

---

## 11. 本 playbook 的定位

- **内容** —— 来自 distill + 本 session 务实对账，无框架层增量
- **地位** —— candidate
- **升格路径** —— Phase 0 action (a) 是唯一通道

本 playbook 不决策。

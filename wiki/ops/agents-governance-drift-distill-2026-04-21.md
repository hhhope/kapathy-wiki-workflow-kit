---
title: AGENTS.md 治理漂移二次蒸馏 2026-04-21
type: distill
canonical_object: agents-governance-drift
artifact_type: distill
language: zh-CN
audience: self
domain: personal-ops
status: active
updated_at: 2026-04-21
ai_generated: true
derived_from:
  - wiki/ops/agents-governance-drift-retro.md
  - wiki/ops/agents-governance-drift-explore.md
  - wiki/ops/agents-governance-remediation-explore-2026-04-21.md
  - wiki/ops/openspec-explore-trigger-drift-retro.md
related_objects:
  - agent-governance-gate-gap
  - wiki-readable-views
  - conversation-handoff
  - disagreement-management
  - agents-governance-drift-distill-calibration
notes_scope: 全过程复盘 + TDD 走完（47 framework case + 12 skill-gate case）+ v3.1 候选框架 + 候选 enforcement bundle + 工作流切分建议；**candidate distill，非 stable decision / canonical governance framework**；继续校准需与 calibration-retro + replay-validation 同读
---

# AGENTS.md 治理漂移二次蒸馏 2026-04-21

## 0. 本文件定位

对 2026-04-21 全 session（~14 轮对话）的二次蒸馏，包含：

1. 全程复盘 — 方法漂移 + trigger 漂移 + scope 漂移
2. 完整 TDD 过程 — 47 test case + v1 → v2 → v3 → v3.1 迭代
3. **v3.1 候选框架** — 6 层（含 S0–S2 / A1–A3 / B1–B3）+ 12 条规则（作者当前倾向，未达共识）
4. AGENTS.md 488 → ~35 行**候选迁移路径**（~35 是作者优化目标，非共识边界）
5. 剩余风险 + 工具依赖
6. 附带发现（ADR-0007 重号 bug）
7. Enforcement 策略（跨 agent 四 class + Codex no-hook 现实）
8. Skill-based gate TDD（12 case，3 处严重 FAIL）
9. **候选** enforcement bundle + 工作流切分建议

与 4 份 derived_from 关系：

| 源 | 作者 | 贡献 | 本文件吸收 |
|----|------|------|-----------|
| `agents-governance-drift-retro.md` | 我 | 14+8 项诊断 | 作为基础诊断集 |
| `agents-governance-drift-explore.md` | Codex | A/B 二分 | 补了更前置读法，指出矩阵抽象级问题 |
| `agents-governance-remediation-explore-2026-04-21.md` | 我 | 5D×4G 矩阵 | 主轴/排序存在问题；新 explore 补了更前置读法；非零价值，未正式废弃 |
| `openspec-explore-trigger-drift-retro.md` | Codex | trigger drift pattern | 指出方法漂移的结构性原因 |

本文件是 **candidate distill**，不作决定、不作为 stable decision 或 canonical governance framework。详见下一节。

---

## 0.1 Status 说明（candidate distill，非 stable decision）

本文件是 candidate distill。继续阅读前请注意：

**事实层**（可作 session 记录）：
- Part 1（session arc + 三层漂移回顾）
- Part 2（TDD 过程：v1 → v2 → v3 → v3.1 的迭代过程 + 每轮 case 列表 + 发现）
- Part 6（ADR-0007 重号发现）
- Part 9.2（skill TDD 的 12 个 case 本身）
- Part 12（session 元层结论）

**候选模型层**（作者当前倾向，未达共识）：
- Part 3（v3.1 候选框架 —— 6 层 + 12 规则）
- Part 4（488 → ~35 行候选迁移路径，含数字目标）
- Part 7（后续动作候选清单）
- Part 8（候选 enforcement 策略）
- Part 9.3–9.5（skill TDD 的结论性判断）
- Part 10（候选 enforcement bundle）
- Part 11（工作流切分建议）

**TDD 走过证明的是"校准证据齐全"，不是"框架已正确或已被接受"。**

继续校准时建议与下列一起读：
- `wiki/ops/agents-governance-drift-distill-calibration-retro.md`
- `wiki/ops/agents-governance-drift-distill-replay-validation-2026-04-21.md`

这两份文件记录本 distill 当前越过共识边界的 overclaim 点，以及 replay contract 校验通过的 bounded proof。

---

## 1. 全程复盘（session arc）

### 1.1 Arc 图

```
 T1 "检查 AGENTS.md 问题"
   ↓
 T1a 诊断 22 项 → retro 落盘（agents-governance-drift-retro.md）
   ↓
 T2-4 我迭代 5D × 4G 耦合矩阵 "整改方向"
   ↓
 T5  Codex 独立写 A/B explore → 补了更前置读法，指出矩阵抽象级问题
 T5a Codex 写 trigger-drift retro → 指出我一直在 routing 不在 exploring
   ↓
 T6-7 回拉 "Claude Code best practice 分工"
   分工表 v0 → v1（漏元规则）→ 用户纠偏
   ↓
 T8 "走过 TDD 么?" → 我承认空气推演
   现场跑 T1-5 → v1 挂 5 处 → v2
   ↓
 T9-11 继续测 T18-47 → v2 挂 10 处 → v3 → v3 挂 5 处 → v3.1
   ↓
 T12 "复盘 + 落 wiki" → 本文件
```

### 1.2 session 内部暴露的三层漂移

**方法漂移（我的，5 轮都在犯）：**
- Turn 1-4 用结构化输出（5D × 4G 矩阵）当答案本身，不是推理工具
- Turn 5 Codex A/B 二分指出这是抽象级偏高的问题
- Turn 8 被用户追问 "TDD" 才真正对框架做压力测试
- **教训：结构密度 ≠ 思考深度。矩阵装饰制造虚假精确。**

**Trigger 漂移（Codex A2 诊断 + 在本 session 反复命中）：**
- 用户显式 `/opsx:explore` 被我执行成 routing / 落盘判断
- 没进 explore 姿态，直接产 structured artifact
- skill 文本（"stance, not workflow / don't auto-capture"）与 AGENTS.md（"explore 先留 trace"）冲突，我每次都默认倒向 AGENTS.md 侧
- **教训：显式 skill trigger 时，交互姿态应先于内容路由**

**Scope 漂移（我多次拔高，用户多次拉回）：**
- 我几次把简单问题（分工 + metadata）拔到治理哲学（GC / Rust lifetime / Kubernetes reconcile / α/β/γ/δ 方案矩阵）
- 每次用户拉回："偏了先不搞这么大"
- Converge 到 "Claude Code best practice + 具体分工 + 元规则 + metadata" 这条主轴
- **教训：用户明确约束（"尽快落地"）需要在每 turn 重新确认，不是一次听到就够**

### 1.3 关键转折点（3 个）

1. **Codex 独立介入**（Turn 5）：不是我自己发现框架错，是 Codex 写了不同视角的 explore 后我才看清
2. **用户追问 "走过 TDD 么?"**（Turn 8）：强制从 "写框架" 切换到 "测试框架"；本次 TDD 能做完是此问的结果
3. **用户 "不要迎合我"**（Turn B/C/A 类比）：阻止我在不同意时说 "对"；让 Java GC 类比被修正为 Rust lifetime + K8s reconcile

---

## 2. 完整 TDD 过程

### 2.1 v1（初始框架，Turn 6-7 推出）

**Anchor：**
- 5 层分工清晰（CLAUDE.md × 2 / AGENTS.md / wiki/adr / skills）
- 一条规则只写一处
- 元规则 canonical 在 ADR

**v1 Test（5 case，现场跑于 Turn 8）：**

| # | Test | v1 结果 |
|---|------|--------|
| T1 | `openspec/specs/*/spec.md` 放哪 | **FAIL** — 5 层漏 openspec/specs/ |
| T2 | archive-review canonical 在哪 | **FAIL** — ADR-0007 + spec 双 canonical，优先关系未定 |
| T3 | Wiki 管道 11 ADR 的 summary | **PARTIAL FAIL** — 1 行规则需限定 "per referenced canonical" |
| T4 | skill 内部规则 vs AGENTS.md 冲突 | **FAIL** — 无 resolution |
| T5 | 新 meta-rule creation path | **FAIL** — 只定 placement，不定 creation |

**v1 挂 5 处中 4 FAIL + 1 PARTIAL。**

### 2.2 v1 → v2 迭代（5 修正）

1. 加 6 层 `openspec/specs/`
2. ADR vs spec 优先关系
3. 1 行 summary per referenced canonical（+ >3 canonicals 用 gateway）
4. R4 conflict resolution（repo > global, AGENTS.md > skill 内部）
5. R3 creation path（evidence-based vs proposal-based）

### 2.3 v2 Test（18 case）

| # | Test | v2 结果 |
|---|------|--------|
| T18 | team-lore 候选 promotion | **FAIL** — R3 无此路径 |
| T19 | "English-first" 风格约定 | ⚠️ v2 可处理但未显式 |
| T20 | skill 间依赖 | PASS |
| T21 | supersede 传播到 proxy | **FAIL** — R5 未强制 |
| T22 | 并发修改 | PASS（git 层）|
| T23 | frontmatter schema 漂移 | PASS |
| T24 | 隐形规则（未写下来的约定） | PASS（框架强制可见）|
| T25 | Claude session vs Codex session | ⚠️ L2/L5 实际是并行 agent-specific 配置，v2 混为一层 |
| T26 | scope 层叠 | **FAIL** — R4 "repo > 全局" 过粗 |
| T27 | 外部 canonical（Anthropic docs）| **FAIL** — R2 只管内部 |
| T28 | explainer 漂移 | **FAIL** — R9 缺失 |
| T29 | 框架自身放哪 | PASS（S1 ADR）|
| T30 | skill lifecycle | **FAIL** — R5 只覆盖 ADR |
| T31 | 紧急规则 | **FAIL** — R3 无紧急路径 |
| T32 | 保留策略 | PASS |
| T33 | draft skill → formal | **FAIL** — R3 无 skill 创建路径 |
| T34 | 删除 | PASS |
| T35 | 多 agent 适用性 | **FAIL** — 无 applicability 声明 |

**v2 挂 10 处（含 ⚠️）。**

### 2.4 v2 → v3 迭代（9 修正）

1. L2 与 L5 拆为 **agent-specific 并行**（Claude 侧 A 系列 / Codex 侧 B 系列）
2. 新增 **S 层概念**（跨 agent 共享 canonical）
3. R3 补 3 条创建路径（team-lore 晋升 / 紧急 / skill 创建）
4. R4 改 **scope stack**（窄 scope 赢：skill-execution > session > repo-shared > global）
5. R5 延伸至所有 rule 层 + **supersede 传播硬规则**
6. R2 外部 canonical citation
7. R8 agent applicability
8. R9 explainer-canonical 同步（必须 cite ID + `synced-against` 标注）
9. R1 scope 标注（`scope: personal | project`）

### 2.5 v3 Test（12 case，Turn 11 一次性跑完）

| # | Test | v3 结果 | 关键发现 |
|---|------|--------|---------|
| T36 | AGENTS.md 488 行逐段归层 | **PASS** | 可降至 ~35 行（比之前估 104 激进）|
| T37 | 25 份 ADR 分类 | **PASS with finding** | **sequencing 是第三类**（12 份，"X before Y" 型）|
| T38 | 29 份 spec 分类 | **PASS with finding** | **6 份 spec 是 meta-rule 语义**（Requirement form）|
| T39 | 迁移中间态 | **GAP** — 无 protocol |
| T40 | observability | **GAP** — 需 tooling |
| T41 | backward compat | **GAP** — 需 transition policy |
| T42 | 工具依赖 | **HARD DEPENDENCY** — v3 无 tooling 是 aspirational |
| T43 | 对抗性内容 | PASS |
| T44 | 依赖链 | **PARTIAL GAP** — transitive supersede 未覆盖 |
| T45 | 多语言漂移 | **GAP** — 无 translation policy |
| T46 | claude-mem / team-lore | **PARTIAL GAP** — 应标外部参考源 |
| T47 | v3 自身治理 | PASS |

**T37 + T38 联动最重要的发现：**
- S1 和 S2 **不是 "meta-rule vs capability" 的互斥分工**
- S1 = Decision form（决策 + rationale + consequences）
- S2 = Contract form（Requirement + Scenario）
- **同一 topic 可以两层都有**（ADR 记决策，spec 记行为），互补不重复
- v3 的 R4 "ADR > spec" **是错的**，冲突才是 bug

### 2.6 v3 → v3.1 迭代（2 refinement + 3 new rules + 2 hard dependency）

**Refinement：**
- R4 废除 "ADR > spec"：互补并存，冲突即 bug
- S1 分子类：decision + sequencing

**新规则：**
- R10 Migration protocol（canonical 先立 → verify → proxies 原子 → 旧删）
- R11 Transition policy（grandfather existing + opportunistic migrate）
- R12 Translation policy（canonical 单语言 + 译本为 explainer）

**硬依赖（v3.1 外但必须具备）：**
- Tooling（pre-commit + drift scanner）
- 人工依赖图纪律（或未来补 graph tool）

---

## 3. v3.1 候选框架

> **此节是 candidate governance model，非 stable decision。** 以下 6 层 + 12 规则是作者走完 TDD 后的 preferred model，尚未在本 session 形成共识。采用前需独立决定。

### 3.1 Layers

**Shared canonical（跨 agent）：**

| # | 路径 | 角色 | 加载 |
|---|------|------|------|
| S0 | `<repo>/PROJECT.md` | 项目身份 + 跨 agent 共享 context | 可选（若缺，A2/B2 用 @import 同步）|
| S1 | `<repo>/wiki/adr/` | 元规则（decision + sequencing 子类）| 按需引用 |
| S2 | `<repo>/openspec/specs/` | 行为契约（含 Requirement 形式的 meta-rule）| 按需引用 |

**Agent-specific（并行）：**

| Claude 侧 | Codex 侧 | 角色 | 加载 |
|----------|---------|------|------|
| A1 `~/.claude/CLAUDE.md` | B1 `~/.codex/AGENTS.md` | 全局用户偏好 | session auto |
| A2 `<repo>/CLAUDE.md` | B2 `<repo>/AGENTS.md` | 项目 agent-specific + runtime proxy | repo session auto |
| A3 `.claude/skills/*/SKILL.md` | B3 `.codex/skills/*/SKILL.md` | 任务性技能 | description 触发 |

**P 层（非 rule，不占 canonical 名额）：**

| # | 路径 | 内容 |
|---|------|------|
| P1 | `wiki/ops/` | retro / explore / intake / method explainer |
| P2 | `wiki/domains/` | 领域专题 |
| P3 | `wiki/templates/` | sample / 模板 |
| P4 | `wiki/reports/` | 输出产物 |
| P5 | `wiki/timeline/` | 时间视图 |
| P6 | `skills-drafts/` | 草稿 skill 评估材料 |

### 3.2 12 条 Rules

**R1 Canonical uniqueness**
- 每条规则唯一 canonical 源，按内容类型归层
- 可选 `scope: personal | project` 标签

**R2 Runtime proxy**
- 其他层最多 1 行 summary per referenced canonical，必带 ID
- topic > 3 canonicals → 1 行 gateway + 综述页链接
- 外部 canonical（Anthropic docs / upstream repo）以 citation 引用
- P-layer explainer 不受 1 行限制（受 R9 约束）
- Summary 超限 → 自动 trigger migration

**R3 Creation paths（6 条）**
- Evidence-based meta-rule: retro (P1) → OpenSpec change → ADR (S1) → proxies
- Proposal-based capability: OpenSpec change → spec (S2) → proxies
- Domain / user preference / config value: 直接写入 canonical 层，不 gated
- Skill 创建: skills-drafts (P6) → evaluation → formal (A3/B3)
- 紧急路径: 直接入 A2/B2 proxy + 强制后补正式化（deadline 标注）
- Team-lore 晋升: repo finding → `wiki/team-lore-candidates.md` → team-lore

**R4 Scope stack**（替换原 "ADR > spec"）
- 窄 scope 赢。scope 从窄到宽：skill-execution (A3/B3) > session (A2/B2) > repo-shared (S0/S1/S2) > global (A1/B1)
- 同 scope 内：**ADR 和 spec 互补不互斥**。Decision-form 在 S1，Contract-form 在 S2，同 topic 可两层都有。冲突即 bug。
- 上层沉默 → 下一层宽 scope 适用

**R5 Lifecycle**
- Status: proposed / accepted / superseded / deprecated，适用 ADR / spec / skill
- Superseded entity 保留 + supersedes 指针
- **Supersede 必须传播到所有 runtime proxies**（硬规则，pre-commit 或 OpenSpec change tasks.md 强制）
- OpenSpec change 完成 → archive

**R6 Breakthrough annotation**
- 跨类内容放置附 rationale
- 击穿点不是错，是有标注的 tactical 决策

**R7 Skill-internal meta-rule**
- 定义 skill 自身契约的 meta-rule 留 SKILL.md，不迁 S1
- 冲突走 R4

**R8 Agent applicability**
- agent-specific 层（A/B）规则只对该 agent 生效
- 跨 agent 规则必须在 S 层
- 若 A2 和 B2 需 share context，(a) 用 S0 作源，或 (b) 一个作源另一个 @import

**R9 Explainer-canonical 同步**
- P1 explainer 必须 cite canonical ID
- 可超 1 行，但标注 `synced-against: <canonical-id>@<version-or-date>`
- canonical 更新时触发 drift check

**R10 Migration protocol（新）**
- 顺序：canonical 先立 → verify 完整 → proxies 原子更新（一个 commit）→ 旧内容最后删
- 不允许 canonical 未立时先动 proxy

**R11 Transition policy（新）**
- Existing 内容 grandfather，可标 `scope: legacy`
- 新增必须按 v3.1 合规
- Touch 到旧段时 opportunistic migrate
- 不强制全量 retrofit

**R12 Translation policy（新）**
- canonical 一种权威语言（`.codex/skills/*` 英文 / wiki 中文，per AGENTS.md L35）
- 译本是 P-layer explainer，不是并列 canonical
- 译本漂移走 R9

### 3.3 v3.1 硬依赖（外部能力）

- **Pre-commit grep**：检查 proxy 层是否有 >1 行 summary 违规
- **Pre-commit check**：确认 proxy 引用的 ADR/spec ID 真实存在
- **周期性 drift scan**：explainer vs canonical 同步性
- **Transitive supersede 图**（长期）：B 被 supersede 后，引用 B 的其他 rule 是否要审

**作者判断：若要真正采用 v3.1，tooling 是基础前提；仅有候选框架无 tooling 支撑时，漂移风险高。**

---

## 4. AGENTS.md 488 → ~35 行候选迁移路径

> **~35 是作者优化目标，非本 session 已共识的必要值。** 本节是若采用 v3.1，可能的迁移路径；不是已定 phase plan。

### 4.1 逐段归层表（24 个 section）

| # | Section | 行数 | v3.1 去向 | 残留 |
|---|---------|------|----------|------|
| 1 | Preamble（repo identity）| 3 | S0 PROJECT.md 或 B2 留 | 3 |
| 2 | OpenSpec Trigger | 6 | S1 ADR-0001 已有 | 1 proxy |
| 3 | Decision Observability | 10 | S1 ADR-0002 已有 | 1 proxy |
| 4 | High-Frequency Principles | 9 | S2 spec（skill-evaluation-evidence）+ L6 skill description | 3 |
| 5 | Skill Authoring Contract | 9 | S1 ADR-0010 + S2 spec | 1 proxy |
| 6 | Archive Review Default | 11 | S1 ADR-0007 + S2 spec | 1 proxy |
| 7 | Explore Trace Default | 7 | S1 ADR-0009 + S2 spec | 1 proxy |
| 8 | Conversation Handoff Default | 24 | S2 spec（conversation-north-star-handoff）| 1 proxy |
| 9 | Example-Driven Capture | 21 | S2 spec | 1 proxy |
| 10 | Disagreement Management | 21 | S2 spec | 1 proxy |
| 11 | Live Re-Anchor Gate | 22 | S1 ADR-0024 + S2 spec | 1 proxy |
| 12 | Wiki Naming Model | 38 | S2 spec（wiki-naming-model）| 1 proxy |
| 13 | Wiki Frontmatter Model | 28 | S2 spec | 1 proxy |
| 14-22 | Wiki 管道下游 9 段 | 205 | S2 specs（9 份）+ P1 explainers | 1 gateway |
| 23 | Scope Of Policy | 4 | S1（可能新 ADR）| 1 proxy |
| 24 | Material Processing | 8 | B2 Codex-specific 保留 | 8 |
| 25 | Meeting Note Output | 10 | B2 保留 + L6 skill reference | 10 |
| -- | 结构（headers / blanks） | ~52 | 保留 | ~5 |

**作者优化目标：488 行 → ~35 行**（此数字仅为作者倾向，非共识边界）

残留分布：
- Codex-specific（Material Processing + Meeting Note）= 18 行
- Proxies（15 条 1 行 summary + 1 gateway）= 16 行
- 结构 / preamble = ~5 行

### 4.2 执行顺序（建议 4 phase）

**Phase 1（准备前提，不改 AGENTS.md）：**
1. Fix ADR-0007 重号（见第 6 节）
2. 为 v3.1 本身起 OpenSpec change + 新 ADR（作为 S1 canonical）
3. 建最小 tooling：pre-commit grep 检查 1 行 summary + ID 存在性

**Phase 2（AGENTS.md 迁移，按 R10 protocol）：**
4. Wiki 管道 240 行 → gateway + 综述页链接（最大块）
5. 5 个 meta-rule section → proxy 化（OpenSpec / Archive / Explore / Skill-Authoring / Re-Anchor）
6. 4 个 capability section → proxy 化（Handoff / Example-Driven / Disagreement / Principles）

**Phase 3（A2/B2 重整）：**
7. 保留 Codex-specific 段（Material Processing / Meeting Note）在 B2
8. 新建 `<repo>/CLAUDE.md`（A2，目前不存在）
9. 可选：建 `<repo>/PROJECT.md`（S0）

**Phase 4（跨全局文件）：**
10. 处理 team-lore 路径漂移（A1 vs B1）
11. OpenSpec boundary 三处重复合流
12. evaluation.md 三套字段合流（单独 OpenSpec change）

若采用此路径，建议遵守：
- R10（canonical 先立 → proxy 后动 → 旧删）
- R11（不强制 retrofit，新增必须合规）

---

## 5. 剩余未测风险

v3.1 通过 47 test 但未深测：

1. **跨 agent scope 合并语义** — Claude / Codex / 未来第三 agent 的 rule 合并未压测
2. **动态 skill invocation 临时 rule 作用域** — R4 是静态层级，动态 scope 未定义
3. **Tooling 本身的 governance** — 谁维护 pre-commit 脚本？
4. **大规模团队场景** — 当前是单人 + 2 agent，团队级未考虑
5. **隐式规则** — 靠"人的记忆"持有的约定，框架强制可见但现实中仍然存在
6. **代码注释里的 rule 引用** — 框架不管，有 drift 风险

---

## 6. 附带发现（repo 实际 bug）

**ADR 编号 0007 重复：**
- `wiki/adr/0007-archive-review-before-archive.md`
- `wiki/adr/0007-retire-draft-skills-as-runtime-surface.md`

两份都在 git 管理中。应当其中一份重编号（例如第二份改 0007b 或整体重号到 0026）。

**影响：**
- `wiki/adr/index.md` 两份都列，但引用 "ADR-0007" 无法单义
- R10 迁移时 proxy 无法单义 cite "ADR-0007"
- 与 v3.1 正交，但**影响 Phase 2 执行的可操作性**（若未先消歧，迁移步骤 proxy 写法不稳定）

---

## 7. 后续动作候选（不作决定，只列候选）

| 代号 | 动作 | 前置 | 优先 |
|------|------|------|------|
| (a) | 为 v3.1 起 OpenSpec change + 新 ADR（S1 canonical） | 无 | 高 |
| (b) | Fix ADR-0007 重号 | 无 | 高（影响 d 的可操作性）|
| (c) | 建最小 tooling（pre-commit）| 无 | 高 |
| (d) | AGENTS.md Phase 2 迁移 | a + b + c | 中 |
| (e) | 建 `<repo>/CLAUDE.md`（A2）| 无 | 中 |
| (f) | 合流 evaluation.md 三套字段 | a | 中 |
| (g) | 建 `<repo>/PROJECT.md`（S0）| 无 | 低 |
| (h) | 三份全局文件分工 ADR（A1/B1 漂移）| a | 低 |
| (i) | 建 `governance-change-gate` skill（prompt-level 提示）| 无 | 中（marginal，不可替代 c）|
| (j) | 落地工作流切分纪律（治理层编辑只在 Claude Code） | 无 | 中 |
| (k) | Claude 侧 PreToolUse hook（tool-level，Codex 无对应） | 无 | 中（Claude 独有 bonus）|
| (l) | 周期性 drift scan 脚本（Layer 4 兜底） | c | 低 |

**作者倾向的起步组合：若采用 v3.1，a + b + c + j 是作者认为比较自洽的开端**（前三项给 v3.1 canonical + 结构 enforcement 基础，j 补 Codex 侧弱点）。**这不是已达共识的前置条件，仅作参考顺序。** 详细 enforcement 机制见 Part 8-11。

---

## 8. Enforcement 策略（候选，跨 agent）

> **本节是 candidate enforcement 设计**，非已达共识的 enforcement mainline。以下分类和结论都属于作者当前倾向。

前面 1-7 节给出 v3.1 候选框架和候选迁移路径。框架本身不自动 enforce —— 若要落地，需配套机制防继续漂移。本节说明 enforcement 的候选层级结构、Codex 侧的硬限制、以及跨 agent 倾向可靠的候选基础设施。

### 8.1 四种 enforcement class

| Class | 依赖 | Claude 生效 | Codex 生效 | 强度 |
|-------|------|------------|------------|------|
| 1 · Git pre-commit hook | git | ✅ | ✅ | 强（commit 时机械阻断）|
| 2 · Claude Code PreToolUse hook | Claude Code | ✅ | ❌ | 强（tool 时机械阻断）|
| 3 · OpenSpec change + 人类 review | ADR-0001 + 0008 | ✅ | ✅ | 强（过程 + 语义）|
| 4 · 文件内 self-check / skill body | AGENTS.md / SKILL.md | ⚠️ agent 会跳 | ⚠️ agent 会跳 | 弱 |

**跨 agent 可靠的只有 1、3。Class 2 是 Claude 独有；Class 4 依赖 agent 自觉，本 session 多次证明会被跳过。**

### 8.2 Codex 无 hook 的实质问题

Codex CLI 没有 Claude Code `settings.json` hook 的等价物。意味着：

- **agent 自主编辑**（无 user prompt 触发）在 Codex 侧不可机械拦截
- AGENTS.md / wiki/adr/ / openspec/specs/ 的编辑在 Codex session 下只能靠 prompt-level 约束

三种填补尝试（均有限制）：
- **Skill-based gate**：description 匹配触发（详见 Part 9 TDD，挂 3 处严重）
- **Codex wrapper**：shell alias 包装 `codex`，调用前跑 pre-flight
- **File-system 级保护**：chmod 关键文件，强制走明确流程

**三者都无法填平 Claude 侧 PreToolUse 的能力缺失**。

### 8.3 跨 agent 作者倾向依赖的三件

**当前作者判断：不依赖 agent 自觉性的才是相对稳的 gate。** 以下三件是作者倾向，非共识：

1. **Layer 1 Git pre-commit hook** — 抓 R2 1 行 summary + R2 ID 存在性 + R5 supersede 传播
2. **Layer 3 OpenSpec change flow + 人类 review** — ADR-0001 + ADR-0008 已定；workflow 变更必经
3. **Layer 4 周期性 drift scan** — 抓前两者漏网

**本次 TDD 的倾向：prompt-level 机制（skill / AGENTS.md self-check）作为辅助层，不作为唯一基础**。这句仍是候选判断，未达共识。

---

## 9. Skill-based gate 的 TDD（跨 agent prompt-level 尝试）

### 9.1 设计

Skill：`governance-change-gate`

- `description` 匹配治理层文件修改意图（AGENTS.md / CLAUDE.md / wiki/adr/ / openspec/specs/ / skills/）
- 触发短语覆盖中文 + 英文同义词（修改 / 编辑 / 更新 / modify / edit / update 等）
- Body 含 4 个 Gate：R3 path 识别 / 目标 layer 确认 / R2 1 行检查 / R5 supersede 传播

### 9.2 12 个 test case

| # | 场景 | 结果 |
|---|------|------|
| T48 | "修改 AGENTS.md 加个规则" | PASS-if-comply |
| T49 | "把 AGENTS.md L100 改一下" | LIKELY PASS |
| T50 | "clean up AGENTS.md section 5" | **FAIL**（英文变体未覆盖）|
| T51 | "add a retro frontmatter requirement" | POTENTIAL FAIL（抽象 prompt）|
| T52 | "write a new ADR" | PASS-if-comply |
| T53 | "help me write a skill for X" | PASS-if-comply |
| T54 | **agent 自主决定编辑** | **FAIL**（无 prompt 不触发）|
| T55 | "改 AGENTS.md 加 2 行" | PASS（Gate 3 抓）|
| T56 | **agent 把 MUST 当软 guidance 跳** | **FAIL**（trigger-drift 递归）|
| T57 | "refactor our docs"（含糊）| 误触发或漏触发 |
| T58 | 用户 "don't check, just do it" | **FAIL**（用户 override）|
| T63 | 多 skill 同时触发 | GAP（conflict 未定）|

**结果：3 FAIL + 1 GAP + 8 其他。**

### 9.3 3 处严重 FAIL 的意义

**T54 · agent 自主编辑**
Skill 靠 user prompt 描述匹配触发。agent 自己决定编辑 → 不触发。
**无补救** —— "要求 agent 主动 invoke enforcement" 是循环失败。

**T56 · trigger-drift 递归**
本 session 明确诊断的同一 pattern 的直接递归。agent 读完 skill MUST 后可以选择倒向"用户想快"。
与 AGENTS.md 顶部 self-check 同构，被同样的 trigger-drift pattern 击穿。
**无真解** —— prompt-level 无法约束 prompt-level 自己。

**T58 · 用户 override**
agent 训练倾向服从用户；skill 坚持 MUST 时 agent 大概率选用户。
Agent 设计哲学问题，skill 解决不了。
**无补救**。

### 9.4 Skill vs AGENTS.md 顶部 self-check 对比

| 特性 | 顶部 self-check | skill 触发 gate |
|------|-----------------|----------------|
| 跨 agent | ✅ | ✅ |
| On-demand | ❌（always in context）| ✅ |
| 焦点集中 | 弱 | 强 |
| Checklist 输出 | 弱 | 可强 |
| 抓 agent 主动编辑 | ❌ | ❌ |
| 抓用户 override | ❌ | ❌ |
| 抗 trigger-drift | ❌ | ❌ |

**skill 是对 self-check 的 marginal improvement，不是新 enforcement class。**

### 9.5 结论（本次 TDD 的 bounded proof）

**本次 TDD 证据显示：prompt-level enforcement 存在可观察上限；特定 trigger-drift pattern 下，多数 prompt-level 机制会失效。**

这是 bounded proof，不是 universal conclusion。若要高强度 enforcement，当前倾向需要至少一个 tool-level（Git hook / Claude PreToolUse）+ 过程层（OpenSpec + 人）组合。这仍属 candidate judgment。

---

## 10. 候选 enforcement Bundle

> **本节是候选 bundle 设计**，非已定 mainline。

```
跨 agent 实质 enforcement（抓得住漂移）：
  Layer 1 · Git pre-commit         ← 结构违规，机械
  Layer 3 · OpenSpec + 人类 review  ← 语义 + 过程违规
  Layer 4 · drift scan             ← 兜底

跨 agent prompt-level 辅助（提示作用，不强制）：
  Layer 2a · governance-change-gate skill  ← on-demand
  Layer 2b · AGENTS.md 顶部 trigger        ← always-on
  （两者功能重叠，任选或共用；enforcement 上限相同）

Claude 侧 bonus：
  Layer 2c · PreToolUse hook       ← 唯一能抓 agent 主动编辑的 tool-level
                                     Codex 无等价物 —— T54 硬伤
```

### 10.1 每层的 enforcement 边界

- **Layer 1** 抓：R2 1 行、R2 ID 存在、R5 传播、新增未经 OpenSpec 的 workflow 变更
- **Layer 3** 抓：语义错层、R10 migration 违反、R11 transition 违反、R12 translation 违反
- **Layer 4** 抓：Layer 1+3 漏网（漂移积累 + 隐式违规）
- **Layer 2（a/b/c）**：提示作用，不 guarantee 抓到任何东西

### 10.2 最小可运行配置（候选）

**作者倾向：Layer 1 + Layer 3 + workflow 切分纪律 = 候选最小防漂移集。** 此组合仅为作者当前倾向，非共识边界。Layer 2 + Layer 4 是可叠加的强化层候选。

---

## 11. 工作流切分建议（Codex 侧 enforcement 弱的补偿）

Codex prompt-level 弱于 Claude tool-level 不可消除。**务实答案：按 agent 能力切分任务**。

| 任务类型 | 推荐 agent | 原因 |
|---------|-----------|------|
| AGENTS.md / wiki/adr/ / openspec/specs/ 编辑 | Claude Code | PreToolUse hook 抓 agent 主动编辑 |
| 实现代码、迁移动作、skill body 编写 | Codex 或 Claude | 实现层漂移风险小 |
| 大批量文件操作 | Codex | 批量编辑更快 |
| 架构决策讨论 | Claude Code | 需 anchor 约束，hook 帮补 |

**这不是 v3.1 正式规则（不进 S1），是务实配套纪律。**

### 11.1 落地方式

- A1 `~/.claude/CLAUDE.md` 加一节：Claude Code 优先用于治理层编辑
- B1 `~/.codex/AGENTS.md` 加一节：Codex 遇到治理层编辑需求时，建议切到 Claude Code
- 配套：Layer 1 Git pre-commit 保证即使在 Codex 下直接改也有 commit-time 拦截

---

## 12. session 元层结论

**做对的（值得保留）：**
- Codex 独立介入写不同视角 explore —— 没他就看不到矩阵是错的
- 用户追问 "走过 TDD 么?" —— 强制从推演到验证
- 用户多次纠偏 "不要搞这么大" —— 保护 anchor 不被 scope drift 稀释

**做错的（方法债务）：**
- 用结构密度当思考深度 —— 矩阵装饰制造虚假精确
- 显式 skill trigger 未先确认交互姿态 —— trigger-drift 一次没避开
- scope 拔高（GC / Rust / K8s / α/β/γ/δ）—— 每次都要用户拉回

**结构性原因（需后续治理）：**
- skill 文本（"stance, not workflow"）与 AGENTS.md（"先留 trace"）冲突未解决
- 软判断短语（"clearly continues" / "repeatedly converges"）仍留在 AGENTS.md 里

后续若真做 v3.1 落地，以上方法债务会反复出现。需配合 R8 / R9 在执行时主动识别。

---

**本 distill 不决策。** 候选动作见第 7 节。若后续要推进，建议：
- 先为 v3.1 起 OpenSpec change + 新 ADR（否则 candidate 框架本身无 canonical）
- 然后按 R10 protocol 执行

**再次提醒：本文件是 candidate distill。TDD 走过 ≠ 框架被接受。继续校准时与 `agents-governance-drift-distill-calibration-retro.md` + `agents-governance-drift-distill-replay-validation-2026-04-21.md` 同读。**

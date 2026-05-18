---
title: AGENTS.md 治理漂移复盘 2026-04-21
type: retro
canonical_object: agents-governance-drift
artifact_type: retro
language: zh-CN
audience: self
domain: wiki
layer: ops
ops_area: agent-governance
status: active
updated_at: 2026-04-21
ai_generated: true
derived_from:
  - wiki/ops/agent-governance-gate-gap-retro-2026-04-18.md
  - wiki/ops/karpathy-skills-learning-retro-2026-04-16.md
  - wiki/ops/scope-drift-retro.md
related_objects:
  - disagreement-management
  - conversation-handoff
notes_scope: 诊断轮产出；未决定治理动作，仅留痕供下一轮参照
---

# AGENTS.md 治理漂移复盘 2026-04-21

## 1. 复盘背景

本次对话由"帮我检查 AGENTS.md 的问题"起步。用户两次明确纠偏：

- 第 1 次：agent 过早锁定 plan 并打算直接创建诊断文档，用户要求"先不要去修改……我们要检查很多东西，先聊清楚"
- 第 2 次：诊断铺开后用户要求"先把规范聊清楚"，退回讨论模式，先看 AGENTS.md 本身问题再谈治理

这两次纠偏形成了 repeated north-star pull：北极星始终是"治理 AGENTS.md 与 skills 漂移"，非单次 Q&A。

按 repo `AGENTS.md` L81–86 的 Durable output 路由：

> drift, disagreement, or repeated process confusion → `wiki/ops` retro

本次完全命中该路由。讽刺的是：`wiki/ops/agent-governance-gate-gap-retro-2026-04-18.md` 本身就是为警示"规则存在、执行没触发"——而本对话到决定落盘为止仍未留痕，正是该复盘描述的漂移模式在本 session 的重演。

## 2. 三份规则源的漂移图

在本次对话前未被单独画过，本次首次浮出：

| 文件 | 归属 | 加载者 | 行数 | 角色 |
|---|---|---|---|---|
| `~/.codex/AGENTS.md` | 全局 | Codex CLI | 282 | 健康检查 / OpenSpec 边界 / git 纪律 / 路由表 |
| `~/.claude/CLAUDE.md` | 全局 | Claude Code | ~162 | 健康检查 / REQ 识别 / lore 三层匹配 |
| `./AGENTS.md`（repo） | 仓库 | Codex + AGENTS.md-aware agent | 488 | 仓库 workflow + Wiki 管道 + 方法默认 |

跨文件漂移条目：

| # | 漂移点 | 具体位置 |
|---|---|---|
| 1 | team-lore 路径不一致 | `~/.codex/AGENTS.md` L14 `/mnt/d/team-lore/wiki` vs `~/.claude/CLAUDE.md` `~/team-lore/LORE.md` |
| 2 | evaluation.md 字段三套规范 | 全局 Codex L274–278（散文） vs repo L27（Baseline–Before–After–Residual）vs repo L40（Pressure–RED–GREEN–Residual） |
| 3 | OpenSpec boundary 规则重复 | 全局 Codex L115–127 vs repo AGENTS.md L43–53 Archive Review Default |
| 4 | main 分支保护规则文件内重复 | 全局 Codex L170 与 L178 两处 |
| 5 | Skill 引用格式不一致 | 全局 Codex L264–266 用全路径 `~/.codex/skills/X/SKILL.md` vs repo AGENTS.md L28–31 只写纯名字 |

更根本的问题：**"谁负责定义什么"从未在任何一处明确**。全局 Codex L271 声明自己是"健康检查/REQ/lore/git 四件事的权威"，L280 说"仓库语义归仓库"，但没有一处声明"AGENTS.md 本身的内容 scope 是什么"。

## 3. repo `AGENTS.md` 14 项诊断

🔴 Load-bearing
- **1. evaluation.md 两套互斥字段**（L27 vs L40）——同一 artifact 两套必填字段清单
- **2. Disagreement Management L127–130 markdown 缩进 bug**——`wiki/ops retro` 一条未缩进到 `Default routing after the method layer:` 之下

🟠 结构性
- **3. Wiki 管道 11 段 288 行是规格不是行为规则**（L223–462）——488 行中 288 行是 spec 形态
- **4. AGENTS.md 自身 scope 未定义**——定义了"什么该走 OpenSpec / 进 ADR / 写 skill"，但没定义"什么该进 AGENTS.md 本身"，无上限增长
- **5. 缺"AGENTS.md / skill / ADR / wiki-ops 的层级归属"元规则**——ADR-0001/0006/0008 只定 promotion 方向，没定每层收什么
- **6. Section 命名后缀不统一**——24 段中 16 个 "X Default" + 8 个其他形态（Gate / Contract / Trigger / Observability / Principles / Scope Of Policy / Output）

🟡 规则歧义
- **7. 4 个 principle skill 被点名但无调用路径**（L28–31）
- **8. "English-first" 自相矛盾**——L35 规定 `.codex/skills/*` 英文为主，L486 AGENTS.md 自己插入中文 `待确认` / `需你澄清`
- **9. 软判断堆积**——L59 `clearly continues` / L65 `repeatedly converges` / L123 `redirection has occurred`，全靠 agent 自由心证
- **10. Conversation Handoff 无落地路径**（L63–86）——讲触发与字段，不讲保存路径（实际路径已存在于 `wiki/ops/conversation-handoff-mode.md` / `sample-codex-handoff.md` / `codex-handoff-rules.md`，只是 AGENTS.md 未引用）
- **11. Explore Trace 无 fail-safe**（L57–61）——要求 trace 写完才能继续，但未定写失败时的阻塞逻辑

🔵 小问题
- **12. 无 TOC**——488 行 30+ 段无目录
- **13. 术语碎片**——trace / intake / retro / ADR / OpenSpec change / archive-review.md / handoff mode 7+ 术语散落各段，无统一术语表
- **14. 无版本 / 废弃机制**——只 Wiki 管道段标 "Version 1"；其他段无版本；废弃流程未定

## 4. 全局 `~/.codex/AGENTS.md` 8 项诊断

🔴 跨文件漂移
- **G1. team-lore 路径与 `~/.claude/CLAUDE.md` 不一致**（L14）
- **G2. evaluation.md 字段构成第三套规范**（L274–278）——与 repo AGENTS.md 两套字段并不统一

🟠 内部重复
- **G3. main 分支保护规则 L170 与 L178 两处重复**
- **G4. OpenSpec boundary L115–127 与 repo AGENTS.md L43–53 高度重复**——改一处另一处落后

🟡 结构与清晰度
- **G5. Task start 一次需读 6–8 个文件**（L58–75）——落实成本高
- **G6. "global source of truth" 权威声明分散在 L186–189 / L271 / L280 三处**——无单一段落声明本文件 scope
- **G7. Skill 引用用全路径 vs repo AGENTS.md 用纯名字**（L264–266 vs repo L28–31）

🔵 小问题
- **G8. 无版本 / 修订日期 / 目录**——与 repo AGENTS.md 同样缺陷

## 5. 已有 wiki / ADR 覆盖映射

14 项 repo 诊断对账：

| # | 已有沉淀 | 覆盖状态 |
|---|---|---|
| 1 | `openspec/specs/skill-evaluation-evidence/spec.md`（Baseline 系列）+ `openspec/specs/local-skill-pressure-tests/spec.md`（Pressure 系列） | 部分：源于两份分层 spec，AGENTS.md L27/L40 把分层关系压平后表现为矛盾 |
| 2 | 无 | 空白：纯 markdown bug |
| 3 | ADR-0013 到 ADR-0023（11 份） + `wiki/ops/agent-readable-wiki-*.md`（10 份） | **完整**：AGENTS.md 288 行是这 21 份文件的复述 |
| 4 | `wiki/ops/scope-drift-retro.md` 谈的是 OpenSpec change 实施 scope，不是 AGENTS.md 内容 scope | 空白 |
| 5 | `wiki/ops/agent-governance-gate-gap-retro-2026-04-18.md` L103–108 已定四层归属 | 部分：缺 AGENTS.md 和 skill 两层 |
| 6 | 无 | 空白 |
| 7 | `karpathy-skills-learning-retro` 催生 principle-skills-layer OpenSpec，skill 本体存在 | 路径缺失只是 AGENTS.md 写作问题 |
| 8 | 无 | 空白 |
| 9 | 无 | 空白 |
| 10 | `wiki/ops/conversation-handoff-mode.md` / `sample-codex-handoff.md` / `codex-handoff-rules.md` | **不是缺路径，是 AGENTS.md 未引用现有路径** |
| 11 | ADR-0009 已定 explore-trace 规则；fail-safe 未定义 | 部分 |
| 12–14 | 无 | 空白 |

### 三个关键反转

**A. Wiki 管道 288 行原本不该在 AGENTS.md 里**
ADR-0013 到 ADR-0023（11 条）+ 10 份 `wiki/ops/agent-readable-wiki-*.md` 已完整沉淀。按 ADR-0002（稳定决策进 ADR），repo AGENTS.md 里那 288 行本该只留一条触发指引 + 链接，不应完整复述。

**B. `agent-governance-gate-gap-retro` 给出了漂移治理的半成品答案**
该复盘 L103–108 已定四层归属（ADR / OpenSpec / archive-review / retro），只差没把 AGENTS.md 和 skill 两层写进去。补完这张表就是治理动作的入口。

**C. `karpathy-skills-learning-retro` L183–194 是被违反的历史建议**
原文明确："对 AGENTS.md 可以继续加强的，**不是再加更多长条款**，而是补一层更短的高频原则。"
实际 AGENTS.md 从 374 行（2026-04-20 早）→ 487 行（2026-04-20 晚）一日内涨 113 行——反方向走。这条建议**已沉淀但未生效**。

## 6. Open questions 与候选下一步

本 retro 不作决定；下面只列选项供下一轮参考。

### Q1：三套 evaluation.md 字段
- (a) 合并成一套统一字段（放弃 skill-evaluation-evidence / local-skill-pressure-tests 分层语义）
- (b) 在 AGENTS.md 明确写出分层关系（base + 附加）而非并列两条规则
- (c) 废弃其中一个 OpenSpec spec，统一到另一个

### Q2：Wiki 管道 288 行
- (a) 迁到 `openspec/specs/`，AGENTS.md 只留触发指引 + 链接
- (b) 保留现状，但在 AGENTS.md 前加 TOC 降低阅读成本
- (c) 拆分为独立的 `wiki/agent-readable-runtime.md` 综述页，AGENTS.md 链接过去

### Q3：AGENTS.md / skill 层级归属
- (a) 新建 ADR，补完 `agent-governance-gate-gap-retro` L103–108 四层表，加入 AGENTS.md 和 skill
- (b) 保留现状，仅靠作者经验
- (c) 分散治理：AGENTS.md 里自己定义自己的 scope（元规则）

### Q4：跨三文件（global Codex / global Claude / repo）漂移
- (a) 全局 Codex AGENTS.md 与 Claude CLAUDE.md 合并或明确分工
- (b) 建立一份 ADR 声明三份文件的职责边界
- (c) 本轮不处理——全局文件是个人 dotfiles，已超出本仓库 scope

### Q5：本复盘自身的去向
- (a) 作为独立 retro 留着，不绑定任何 OpenSpec change
- (b) 后续若起治理 OpenSpec change，本 retro 作为 derived_from 来源

## 7. 后续关注点

- 若下一轮要动 AGENTS.md，按 AGENTS.md OpenSpec Trigger（L5–10）必须先起 OpenSpec change
- 若决定合并 evaluation.md 字段，需先读完 `enforce-skill-evaluation-evidence` 和 `require-local-skill-pressure-tests` 两份 archived change 的完整 proposal / design，确认分层初衷
- `conversation-handoff-mode.md` / `sample-codex-handoff.md` / `codex-handoff-rules.md` 三份现有 handoff 文档间的关系本身也可能存在漂移，本轮未展开
- 三份 AGENTS / CLAUDE 源的角色区分（Part 2）未在任何 ADR 中留痕，是当前最大的治理空白

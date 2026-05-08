---
canonical_object: account-knowledge-base
artifact_type: ops-overview
title: account-knowledge-base / team-knowledge-path
type: ops
language: zh-CN
status: active
created_at: 2026-05-07
updated_at: 2026-05-08
related_objects:
  - learning-capture-routing
  - behavior-replay-gate
  - wiki-runtime-auto-routing
  - team-lore-candidates
derived_from:
  - wiki/ops/account-knowledge-base-structure-explore.md
  - wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md
  - PROJECT.md
  - wiki/index.md
  - wiki/role-boundaries.md
  - wiki/team-lore-candidates.md
---

# 团队知识库构建路径

> 这页是 `account-meeting-lore` 的团队知识库入口说明，只负责三件事：解释为什么要从 `lore` 走到 `team-lore` 再走到结构化 `wiki`，说明三层怎么分工，告诉读者下一步该读哪一页。

## 一句话定位

团队知识库不是资料归档，而是把一次性经验逐步变成可复用、可检索、可验证的团队记忆。

一句话记忆：`Lore = 管现场记忆`，`Team Lore = 管跨项目复用`，`Wiki = 管结构化生产、导航和发布`。

## 插图 1：从现场经验到团队知识库

```text
Chat / inbox / Feishu / meeting
        |
        v
Lore: 现场记忆
  - logs
  - sources
  - ops trace
  - project context
        |
        v
Team Lore: 跨项目复用
  - principles
  - pitfalls
  - workflows
  - templates
        |
        v
Wiki: 结构化知识库
  - source / domain / timeline / report / ops
  - index / frontmatter / graph / runtime routing
  - reviewable markdown + git history
```

这条链路的重点不是“多建几个目录”，而是让知识每升一层都变得更稳定、更少依赖当时的聊天上下文。

## 这页适合谁看

| 如果你现在想解决 | 先用这页做什么 | 下一步去哪 |
|---|---|---|
| 经验为什么总丢 | 看 `lore -> team-lore -> wiki` 的演变路径 | 继续看本页 |
| 什么该进 team lore | 看晋升规则和去项目化边界 | `wiki/role-boundaries.md`、`wiki/team-lore-candidates.md` |
| wiki 为什么不是资料夹 | 看三层分工和五类页面 | `wiki/index.md` |
| agent 下次怎么自动读对上下文 | 看 runtime routing 和 behavior replay | `wiki/ops/agent-readable-*`、`wiki/ops/behavior-replay-gate.md` |

## 插图 2：你如何驾驭这套知识库

```text
你 / 决策者
  | 目标、边界、是否继续
  v
AGENTS.md / OpenSpec
  | 开工门禁、变更边界、完成条件
  v
Lore
  | 捕获现场事实、偏差、可疑经验
  v
Team Lore
  | 去项目化、提炼原则、模板、坑点
  v
Wiki
  | 结构化导航、证据链接、agent-readable runtime context
  v
Feishu / reports / H5
  | 对外阅读和发布形态
```

人负责目标和取舍；`AGENTS.md` 与 OpenSpec 负责约束；Lore 负责现场记忆；Team Lore 负责复用；Wiki 负责结构化、可读化和后续检索。

## 我们现在处于什么阶段

| 维度 | 当前状态 | 下一步 |
|---|---|---|
| Lore | 已有 `sources`、`ops trace`、学习捕获、漂移复盘 | 减少只停留在聊天里的经验 |
| Team Lore | 已有 `/mnt/d/team-lore/wiki`、principles、pitfalls、index | 把候选材料去项目化后再晋升 |
| Project Wiki | 已有 `Sources / Domains / Timeline / Reports / Ops` | 补足真实 account domain taxonomy |
| Agent-readable Wiki | 已有 naming、frontmatter、graph、routing、context injection 规范 | 防止结构产物被过度宣称为自动执行 |
| Evidence Gate | 已有 behavior replay、learning capture、OpenSpec archive review | 所有“下次会触发”的规则都保留回放证据 |

## 默认生命周期

| 阶段 | 默认主入口 | 产出 |
|---|---|---|
| `capture` | chat、`inbox/`、Feishu link、meeting notes | 原始输入被登记，避免直接写成结论 |
| `lore` | `wiki/sources`、`wiki/ops`、local logs | 现场事实、摘要、偏差、待确认项 |
| `project wiki` | `wiki/domains`、`wiki/timeline`、`wiki/reports` | 当前项目可复用的业务理解和交付表达 |
| `team-lore candidate` | `wiki/team-lore-candidates.md` | 可能跨项目复用的原则、模板、坑点 |
| `team-lore` | `/mnt/d/team-lore/wiki` | 去项目化后的 shared principle / pitfall / workflow |
| `agent-readable wiki` | naming、frontmatter、graph、runtime routing | 让 agent 能按结构读、按证据用、按边界停 |
| `publish` | Feishu、report、H5 | 面向人的阅读和传播形态 |

## 整体约束

| 约束 | 含义 | 在本 repo 里怎么生效 |
|---|---|---|
| 不从 chat 直接进 team lore | 聊天是现场，不是 durable knowledge | 先落 source / ops / log，再进入候选池 |
| 不把 source 当结论 | source 只是证据层 | report 和 domain 必须链接 source，不反向替代 source |
| 不把 report 当知识源 | report 是表达层 | 可复用模式沉淀到 examples 或 team-lore candidate |
| 不把 ops 当业务知识 | ops 管行为和治理 | 业务语义进入 domains，稳定决策进入 ADR |
| 不把规则当已生效 | 行为资产需要验证 | behavior replay gate 要求回放证据 |
| 不把结构当智能 | graph / routing 是结构辅助 | 不宣称自动检索等于语义理解或自主执行 |

## 这套结构解决什么问题

| 典型问题 | 对应答案 |
|---|---|
| 经验只在聊天里，下次上下文丢失 | Lore 捕获现场，wiki 固化可读结构 |
| 项目经验看起来有用，但不知道能不能复用 | 先进入 `team-lore-candidates`，去项目化后再晋升 |
| wiki 越写越像资料堆 | 用 source / domain / timeline / report / ops 分层 |
| agent 不知道先读什么 | 用 index、frontmatter、graph、runtime routing 建阅读路径 |
| 规则写了但下次不触发 | 用 behavior replay gate 验证未来行为声明 |
| Feishu 文档好看但 repo 不可追溯 | Feishu 作为发布面，markdown wiki 作为 durable truth |

## 三层分工

| 层 | 主要回答的问题 | 真相源 | 不负责什么 |
|---|---|---|---|
| `Lore` | 这次现场发生了什么、有什么可疑经验 | logs、source、ops trace、project context | 不负责任务进度和 archive 结论 |
| `Team Lore` | 去掉项目背景后，什么仍可复用 | git-backed shared wiki、principle、pitfall、workflow、template | 不收原始项目材料 |
| `Wiki` | 知识如何被组织、检索、发布和复用 | markdown repo、index、frontmatter、links、OpenSpec specs | 不替代 OpenSpec 的 change lifecycle |

## Wiki 内部五层分工

| 层 | 主要回答的问题 | 真相源 | 不负责什么 |
|---|---|---|---|
| `Sources` | 这件事的上游证据是什么 | Feishu link、会议纪要、附件、原始材料摘要 | 不直接输出管理结论 |
| `Domains` | 这个业务主题长期怎么理解 | 稳定业务页、source links | 不承接一次性周报草稿 |
| `Timeline` | 某个周期发生了什么变化 | 周/月/季度页、source/report links | 不替代 source 原文 |
| `Reports` | 给某类受众怎么表达 | 汇报草稿、H5、交接材料 | 不作为原始证据源 |
| `Ops` | agent 和个人操作怎么推进 | trace、retro、handoff、reminder、method | 不替代业务 domain 或正式 spec |

## 默认使用顺序

| 场景 | 先看什么 | 原因 |
|---|---|---|
| 新材料、会议纪要、Feishu 文档 | `wiki/sources` | 先保留证据，再做提炼 |
| 想知道这是不是可复用经验 | `wiki/role-boundaries.md` | 先判断服务当前交付还是未来复用 |
| 想晋升到 team lore | `wiki/team-lore-candidates.md` | 先候选、去项目化、再晋升 |
| 想写汇报或 H5 | `wiki/reports` + source / timeline | 汇报必须有上游支撑 |
| 想处理 agent 行为、学习、漂移、规则争议 | `wiki/ops` | 操作和治理先留痕 |
| 想改变默认行为或规则 | `openspec/changes` | workflow/default 行为变化必须 scoped |
| 想让 agent 下次读对上下文 | `wiki/ops/agent-readable-*` | 结构化阅读路径优先于语义猜测 |

## 运行态：从 Lore 到 Graph，再回到 Wiki

| 阶段 | 动作 | 目的 |
|---|---|---|
| `start` | 健康检查、读 `PROJECT.md`、读 active OpenSpec | 先确认能不能开工和边界 |
| `load lore` | 从 wiki index 进入 1-2 个相关页面 | 定场景、边界和历史坑点 |
| `narrow structure` | 必要时用 graph / relation / routing 结果缩范围 | 找结构证据，不靠全文乱搜 |
| `execute` | 按 skill / OpenSpec / git truth-source 执行 | 把目标转成可验证改动 |
| `absorb` | 新事实进 source / ops / candidate / team-lore | 防止经验再次丢回聊天 |

## 安装与迁移：新项目如何长出团队知识库

| 步骤 | 能力 | 要做什么 | 完成标志 |
|---|---|---|---|
| 1 | Governance baseline | 建 `AGENTS.md`、rules、skills、OpenSpec 入口 | agent 知道开工门禁和停止条件 |
| 2 | Project Lore | 建 `PROJECT.md`、`wiki/index.md`、sources / ops | 新输入能被登记和分类 |
| 3 | Team Lore Candidate | 建候选池和晋升规则 | 可复用经验不会直接污染 shared knowledge |
| 4 | Team Lore | 接入 git-backed shared wiki | index 能导航到 principle / pitfall / workflow |
| 5 | Agent-readable Wiki | 补 naming、frontmatter、graph、runtime routing | agent 能按结构读、按证据用 |
| 6 | 验证 | 至少走通一条 `输入 -> lore -> candidate -> wiki` 路径 | 不是空目录或漂亮说明页 |

## 证据页：哪些说法不能夸大

| 不能直接说什么 | 更准确的说法 |
|---|---|
| “有 wiki 就有团队知识库” | 只有可导航、可复用、可验证的 wiki 才是知识库 |
| “进了 team-lore 就是真理” | team-lore 是跨项目复用层，仍需要来源和边界 |
| “Graph / routing 能自动理解语义” | 它们是结构证据和阅读顺序，不是语义保证 |
| “Feishu 同步就是沉淀完成” | Feishu 是发布或来源面，durable truth 仍在 git-backed markdown |
| “规则写进 AGENTS 就会自动生效” | 未来行为声明需要 replay evidence |

## 路线图：从 L1 到 L4 的知识库成熟度

| Level | 核心目标 | 知识库状态 | 典型风险 |
|---|---|---|---|
| `L1` | 个人和项目能记住事实 | 有 source / notes / chat 摘要 | 经验散落，靠人记 |
| `L2` | agent 按约束完成单次任务 | 有 AGENTS、OpenSpec、Lore、wiki 分层 | 能做事，但阶段协作不稳 |
| `L3` | 可验证的阶段化协作 | 有 replay evidence、candidate 晋升、review 节奏 | 阶段契约不清会退回 L2 |
| `L4` | AI 驱动的工程协作面 | 有自动路由、lint、图谱、持续吸收 | 没有硬 gate 会变成自动化幻觉 |

## 阅读地图

| 你现在最关心什么 | 建议先读 | 重点收获 |
|---|---|---|
| 团队知识库为什么要分层 | `wiki/role-boundaries.md` | 当前交付和未来复用的判断标准 |
| 可复用经验如何晋升 | `wiki/team-lore-candidates.md` | 候选字段、晋升检查表 |
| 项目内材料如何流转 | `wiki/index.md`、`wiki/inbox-intake.md` | source / domain / timeline / report / ops |
| agent 如何读 wiki | `wiki/ops/agent-readable-wiki-runtime-auto-routing.md` | open first / open next / do not open first |
| 行为资产怎么验证 | `wiki/ops/behavior-replay-gate.md` | future behavior claim 的 replay evidence |
| team lore 的 shared 形态 | `/mnt/d/team-lore/wiki/index.md` | principle / pitfall / workflow 的入口 |

## 当前不做

- 不把本页升级成 `wiki/index.md` 的替代入口。
- 不同步到飞书 wiki。
- 不把本页内容直接提升为 repo 默认导航规则。
- 不把参考页里的 `OpenSpec / Lore / Graphify / lore-bootstrap` 结论原样搬进本 repo。

## Feishu 参考来源

- 四篇主文：
  - `Account Harness：总览（OpenSpec / Lore / Graphify / Lore Bootstrap，更新至 2026-04-13）`
  - `Account Harness：运行态（Lore + Graphify，更新至 2026-04-13）`
  - `Account Harness：安装与迁移（更新至 2026-04-13）`
  - `Account Harness：验证结果与案例（更新至 2026-04-13）`
- 阶段规划引用：`AICoding L1-L4 路线图（更新至 2026-04-13）`
- 本页借鉴的是其页面组织方式：入口说明、一句话定位、适合谁看、插图、分层表、阶段状态、默认生命周期、整体约束、解决问题、分工、使用顺序、阅读地图。
- 本页内容基于当前 repo 的 `PROJECT.md`、`wiki/index.md`、`wiki/role-boundaries.md`、`wiki/team-lore-candidates.md`、`AGENTS.md`、OpenSpec specs 和 team-lore shared wiki 结构。

---
canonical_object: account-knowledge-base
artifact_type: ops-overview
title: account-knowledge-base / workbench
type: ops
language: zh-CN
status: active
created_at: 2026-05-07
updated_at: 2026-05-07
related_objects:
  - learning-capture-routing
  - behavior-replay-gate
  - wiki-runtime-auto-routing
derived_from:
  - wiki/ops/account-knowledge-base-structure-explore.md
  - wiki/sources/feishu-wiki-FYDcwFGaOi6A1Bkg9rfcIp3DnCS.md
  - PROJECT.md
  - wiki/index.md
---

# Account 知识库工作台

> 这页是 `account-meeting-lore` 的操作入口说明，只负责三件事：解释这个知识库在管什么，说明各层分工，告诉读者下一步该去哪里。

## 一句话定位

`Account 知识库` 是账户组材料、会议、汇报和 agent 协作治理的可复用工作台，不是单个文档库。

一句话记忆：`Sources = 管证据`，`Domains = 管业务理解`，`Timeline = 管时间演进`，`Reports = 管交付表达`，`Ops = 管操作与治理`。

## 这页适合谁看

| 如果你现在想解决 | 先用这页做什么 | 下一步去哪 |
|---|---|---|
| 搞清这个 repo 到底管什么 | 先看五层分工和默认流转 | 继续看本页 |
| 判断新材料应该放哪里 | 看 `Sources / Domains / Timeline / Reports / Ops` 的边界 | `wiki/index.md`、`wiki/templates/` |
| 判断 agent 行为、学习、漂移该怎么落地 | 看 Ops 与 OpenSpec / ADR 的边界 | `wiki/ops/index.md` |
| 找已经验证过的输出形态 | 看 examples 与 reports 的区别 | `wiki/examples/index.md`、`wiki/reports/index.md` |

## 你如何驾驭这套知识库

| 层 | 先看什么 | 负责什么 |
|---|---|---|
| 你 / 决策者 | 目标、边界、是否继续 | 决定材料要解决的问题、受众是谁、是否需要变成规则 |
| `AGENTS.md` | health check、OpenSpec gate、runtime routing | 约束 agent 能不能开工、先读什么、何时停止 |
| `wiki/` | sources、domains、timeline、reports、ops | 承载长期知识、操作记录、交付物和导航 |
| `openspec/` | proposal、design、tasks、spec | 管 scoped change 的过程、约束和完成状态 |
| `.codex/skills/` | learning、meeting、material、OpenSpec skills | 给高频任务提供运行时方法卡 |
| `lark-cli` / Feishu | source fetch、发布、同步 | 读取外部证据或发布结果，不作为长期知识真相源 |

一句话记忆：你给目标和许可；`AGENTS.md` 和 skills 约束 agent；`wiki` 承接知识；`OpenSpec` 管变更；Feishu 是来源或发布面，不是 repo 的 durable truth。

## 我们现在处于什么阶段

| 维度 | 当前状态 | 下一步 |
|---|---|---|
| 知识库结构 | 已有 `Sources / Domains / Timeline / Reports / Ops` 主结构 | 补足真实 account domain taxonomy |
| 材料入口 | 已有 source 模板、inbox intake、会议纪要放置规则 | 把更多真实 Feishu / 会议材料转成 source 页 |
| 汇报产出 | 已有管理周报、涅槃项目汇报、H5 one-pager | 抽出稳定 report pattern，沉淀到 examples |
| Agent 治理 | 已有 OpenSpec、ADR、learning capture、behavior replay gate | 继续用 evidence gate 防止规则写了但不触发 |
| Feishu 集成 | 已可通过授权读取 wiki / docs | 只在需要参考或发布时读取，不把 Feishu 当主库 |

## 默认生命周期

| 阶段 | 默认主入口 | 产出 |
|---|---|---|
| `intake` | `inbox/`、Feishu link、会议材料 | 原始输入被登记，避免直接写成结论 |
| `source` | `wiki/sources/` | 上游证据、链接、摘要、可追溯来源 |
| `structure` | `wiki/domains/`、`wiki/timeline/` | 稳定业务理解和周期演进 |
| `compose` | `wiki/reports/` | 面向受众的汇报、交接、H5 或管理材料 |
| `operate` | `wiki/ops/` | 行为、主线、提醒、学习、漂移、handoff |
| `decide` | `wiki/adr/`、`openspec/specs/` | 跨 change 仍成立的稳定决策或正式约束 |
| `publish` | Feishu / external share | 对外同步说明、结果或可读版本 |

## 整体约束

| 约束 | 我们怎么借鉴参考页 | 在本 repo 里怎么生效 |
|---|---|---|
| 入口页只做总览 | 不在总览页展开所有正文 | 本页只解释分工、流转、下一步，不替代各目录 index |
| 分层必须清楚 | 参考页用四层解释 Account Harness | 本页用五层解释 account knowledge base |
| 完成要可验证 | 参考页强调 evidence / readback | 本 repo 用 OpenSpec validate、behavior replay、source links |
| Feishu 是协作面 | 参考页是可读发布形态 | repo 仍以 markdown wiki 为长期真相源 |
| 学习不能直接变规则 | 有用信息要过证据边界 | learning capture 先候选，promotion 再走 OpenSpec / evidence gate |

## 这套结构解决什么问题

| 典型问题 | 对应答案 |
|---|---|
| 新材料到底放哪里 | 先进入 `wiki/sources`，再链接到 domain / timeline / report |
| 业务理解和汇报草稿混在一起 | `Domains` 管稳定业务理解，`Reports` 管面向受众表达 |
| 周报材料过期后找不到脉络 | `Timeline` 按周期承接变化和回顾 |
| agent 学习、漂移、分歧只留在聊天里 | `Ops` 留 trace / retro / handoff |
| 规则写了但下次没触发 | `Behavior Replay Gate` 要求未来行为声明有回放证据 |
| 稳定决策散落在 design 或聊天里 | `ADR` 只记录跨 change 仍成立的决策 |

## 五层分工

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
| 新 Feishu 文档、会议纪要、附件 | `wiki/sources` | 先保留证据，再做提炼 |
| 要写管理汇报或项目汇报 | `wiki/reports` + 相关 source / timeline | 汇报必须有上游支撑 |
| 要沉淀账户业务理解 | `wiki/domains` | domain 是可复用业务语义层 |
| 要追一段时间的进展 | `wiki/timeline` | 时间视角能保留演进脉络 |
| 要处理 agent 行为、学习、漂移、规则争议 | `wiki/ops` | 这是操作和治理层 |
| 要改变默认行为或规则 | `openspec/changes` | workflow/default 行为变化必须 scoped |
| 要记录稳定跨 change 决策 | `wiki/adr` | ADR 是稳定决策层，不是事件日志 |

## 阅读地图

| 你现在最关心什么 | 建议先读 | 重点收获 |
|---|---|---|
| 知识库整体入口 | `wiki/index.md` | 主结构和推荐流转 |
| 原始材料怎么放 | `wiki/sources/index.md`、`wiki/inbox-intake.md` | source metadata、会议纪要、inbox 分类 |
| 汇报怎么组装 | `wiki/reports/index.md`、`wiki/templates/report-template.md` | 面向受众的输出结构 |
| agent 行为怎么治理 | `AGENTS.md`、`wiki/ops/index.md` | hard stops、skills、output routing |
| 学习材料怎么处理 | `wiki/ops/learning-capture-routing.md` | link trigger、score、promotion boundary |
| 规则如何变成可验证行为 | `wiki/ops/behavior-replay-gate.md` | future behavior claim 的 replay evidence |
| 稳定决策在哪里 | `wiki/adr/index.md` | 跨 change 决策边界 |

## 当前不做

- 不把本页升级成 `wiki/index.md` 的替代入口。
- 不同步到飞书 wiki。
- 不把本页内容直接提升为 repo 默认导航规则。
- 不基于飞书参考页新增 OpenSpec `SHALL`。

## Feishu 参考来源

- 参考页：`Account Harness：总览（OpenSpec / Lore / Graphify / Lore Bootstrap，更新至 2026-04-13）`
- 节点：`FYDcwFGaOi6A1Bkg9rfcIp3DnCS`
- 本页借鉴的是其页面组织方式：入口说明、一句话定位、适合谁看、分层表、阶段状态、默认生命周期、整体约束、解决问题、分工、使用顺序、阅读地图。
- 本页没有复用其具体结论；内容基于当前 repo 的 `PROJECT.md`、`wiki/index.md`、`AGENTS.md`、OpenSpec specs 和现有 wiki 结构。

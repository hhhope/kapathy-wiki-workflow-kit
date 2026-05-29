---
title: account-group-onboarding-h5 / report gate review
layer: ops
domain: account-clearing
ops_area: report-quality
canonical_object: account-group-onboarding-h5
artifact_type: gate-review
language: zh-CN
audience: internal
knowledge_level: working
period: 2026-05-29
source_links:
  - ../reports/account-group-onboarding-h5.html
  - ../sources/split-account-core-rd-investment-source-2026-05-26.md
status: draft
updated_at: 2026-05-29
ai_generated: true
---

# account-group-onboarding-h5 / report gate review

## Article Intent Contract

- Reader: 账户组新入职应届生。
- Reader job: 快速理解账户组做什么、核心链路怎么串、正在做哪些项目、自己能从哪里上手，以及 AI 协作体系如何进入日常工程。
- Main line: 先建立账户领域地图，再落到真实项目入口，最后给出新人 3 天、第一周、30/60/90 天成长路径。
- Non-goals: 不复刻 PPT；不做管理述职；不暴露账号、密码、内网地址、联系人、测试环境细节；不把 AI 体系讲成泛化工具宣传。
- User-owned judgments: H5 优先；复用历史技术 H5 风格；必须包含规划、正在做的项目、新人能做什么和能获得什么；新增 AI 体系建设。

## Reference Output Shape

- Selected shape: 技术架构海报式 + 培训路线式长页 H5。
- Retained patterns: 粗线条技术海报、能力地图、深色/暖纸对比、信息卡片、路线图、任务池。
- Modified patterns: 管理驾驶舱的高密度数据只用于项目入口，不作为主视觉；新人路径用更清晰的 3 天 / 第一周 / 30-60-90 结构承接。
- Rejected patterns: 纯 PPT 搬运、长表格堆叠、个人名单/联系人曝光、单纯 AI 工具清单。

## Evidence Map

| H5 Section | Source | Use | Boundary |
| --- | --- | --- | --- |
| 你加入的是什么小组 | `账户组技术规划与述职 _v6.pptx` | 职责边界、系统规模、治理方向 | 只保留职责和规模级别，不放负责人姓名 |
| 账户体系能力地图 | `账户组技术规划与述职 _v6.pptx`, `4.0清结算账户体系概述.pdf` | 开户、账户、账务、余额、结算、对账、渠道、风险能力 | 以新人认知地图表达，不复刻源图 |
| 核心业务链路 | `账户组技术现状分享.pptx`, `4.0清结算账户体系概述.pdf` | 开户、收单/付款、分账/提现、记账、对账主链路 | 不展开敏感系统地址或客户细节 |
| 典型业务对象 | `账户组技术现状分享.pptx` | 多渠道收款、宝财通、宝户通、银企云/银企通 | 只讲对象和关系，不讲内部访问方式 |
| 常见问题 | `账户组技术现状分享.pptx` | 无法提现、开户失败、入金失败、入账慢、热点更新、压测调优 | 改写为训练场景，不做事故复盘 |
| 正在做的项目 | `wiki/sources/split-account-core-rd-investment-source-2026-05-26.md` | 宝财通/二级商户、结算/出款/清算、报表联调、余额账本验证 | 不使用个人投入排名 |
| 技术规划 | `账户组技术规划与述职 _v6.pptx` | 统一账户、余额中心、账务标准化、结算对账收敛、可观测、风险地图 | 只保留方向和新人可理解的价值 |
| AI 协作体系 | Feishu `Account Harness：总览` | OpenSpec / Lore / Graphify / lore-bootstrap 四层模型 | 讲工程协作边界，不讲仓库内部治理细节 |
| AI Coding 成熟度 | Feishu `AICoding L1-L4 路线图` | 当前 L2，下一步 L2 -> L3 阶段协作固定化 | 不承诺已经达到 L3/L4 |
| 新人上手路径 | Feishu `账户组技术小组新人入职指引`, `IT技术小组新人入职指引` | Day 1/2/3、第一周任务、规范、环境、第一项任务 | 去除账号、密码、内网 URL、联系人 |

## Sensitive Information Boundary

The H5 must not contain:

- account names, passwords, SSH setup details, VPN setup details, test-system URLs, internal IP addresses, personal owner names, personal emails, or group QR codes;
- exact production incident timelines unless rewritten as generic training scenarios;
- raw person-day tables or personal contribution ranking;
- Feishu document tokens or internal source URLs in the reader-facing body.

Allowed in the H5:

- business object names such as 宝财通、宝户通、多渠道收款、银企云/银企通;
- capability names such as 开户、账务、余额、结算、对账、报表、风险地图;
- AI collaboration names such as OpenSpec、Lore、Graphify、lore-bootstrap;
- aggregate onboarding rhythm: Day 1 / Day 2 / Day 3 / 第一周 / 30-60-90.

## Section Drift Review

| Section | Objective | Status |
| --- | --- | --- |
| Cover | Establish the training promise | Task 3 passed |
| Group and capability map | Build first mental model | Task 3 passed |
| Business chain and objects | Explain domain flow | Task 3 passed |
| Problems and active projects | Show real work entry | Task 3 passed |
| Technical planning | Connect work to future direction | Task 3 passed |
| AI collaboration and maturity | Explain AI体系建设 as engineering gates | Planned |
| Newcomer path and task pool | Tell newcomer what to do and gain | Planned |
| Closing | Reframe newcomer role from requirement receiver to accountable engineer | Planned |

## Verification Log

- Feishu sync: not performed; local H5 review only until explicit user approval.
- Account-domain content check: passed after sections 0-7 included capability map, business chain, business objects, typical problems, active projects, and technical planning.
- AI and onboarding content check: passed after sections 8-13 included four-layer AI collaboration, L1-L4 maturity, 3-day onboarding, first-week task, 30/60/90 growth path, and task pool.
- Pending: HTML parser check.
- Pending: source-to-screen mapping check.
- Pending: sensitive-info grep.
- Pending: desktop screenshot.
- Pending: mobile screenshot.
- Pending: final index link check.

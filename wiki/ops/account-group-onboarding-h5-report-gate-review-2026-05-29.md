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
| AI collaboration and maturity | Explain AI体系建设 as engineering gates | Task 4 passed |
| Newcomer path and task pool | Tell newcomer what to do and gain | Task 4 passed |
| Closing | Reframe newcomer role from requirement receiver to accountable engineer | Task 4 passed |

## Rewrite Diagnosis

- User feedback: the chapter order is acceptable, but the content is too thin.
- Failure mode: the first draft collapsed the account capability map into generic cards and omitted the real system architecture.
- Missing domain depth: account model, bank-account / channel connection, accounting, balance, clearing/settlement, reconciliation, reports, parent-child account, multi-account model, and difference handling were not explained as an engineering structure.
- Corrected boundary: `授信能力` and `垫资能力` must not be presented as account-group capability groups; reconciliation and parent-child account capability must be present.
- Rewrite standard: each section must explain real domain objects, module boundaries, chain dependencies, and newcomer task entry.

## Revised Source-To-Section Map

| H5 Section | Required Source Anchor | Rewrite Use |
| --- | --- | --- |
| Capability map | `账户体系能力地图` slide | Rebuild as multi-cluster capability graph; include account basic, unified accounting, clearing/settlement, unified balance, data/report/service, revenue, reconciliation, parent-child and multi-account model; exclude 授信/垫资 groups. |
| System architecture | 宝财通 architecture slide, 多渠道收款 architecture slide | Rebuild layered architecture: entrance/gateway, product, service, data, payment channels, partner banks, operation/back-office. |
| Core chain | 账户技术现状 + 规划 slides | Explain entry/opening, account model, bank-account relation, transaction, split/withdraw/refund, accounting/voucher/balance, clearing/settlement, reconciliation/report/difference, monitoring/risk. |
| Business objects | 多渠道收款、宝户通、宝财通、银企通/债转 slides | Show product objects by architecture position, not as isolated product names. |
| Problems | Typical problem slide | Map withdrawal failure, opening failure, deposit failure, slow posting, reconciliation difference, settlement difference, account/balance inconsistency to chain checkpoints. |
| Projects | Split-account source and 2026 planning slides | Map project entries to account model, parent-child account, balance-ledger verification, settlement/clearing, reconciliation/reporting, bank-account/channel access. |
| AI collaboration | Account Harness and AICoding roadmap | Explain how AI supports account-domain design, review, verification, structure lookup, and knowledge reuse. |
| Newcomer path | Account and IT onboarding docs | Keep Day 1/2/3 and first-week rhythm while removing credentials, URLs, personal contacts, and QR-code instructions. |

## Verification Log

- Feishu sync: not performed; local H5 review only until explicit user approval.
- Account-domain content check: passed after sections 0-7 included capability map, business chain, business objects, typical problems, active projects, and technical planning.
- AI and onboarding content check: passed after sections 8-13 included four-layer AI collaboration, L1-L4 maturity, 3-day onboarding, first-week task, 30/60/90 growth path, and task pool.
- HTML parser check: passed with `python3 -m html.parser wiki/reports/account-group-onboarding-h5.html`.
- Source-to-screen mapping check: passed in two steps. Source coverage was checked with `rg -n "账户组技术规划与述职|账户组技术现状分享|4.0清结算账户体系概述|分账核心改造|账户组技术小组新人入职指引|IT技术小组新人入职指引|Account Harness|AICoding L1-L4" wiki/ops/account-group-onboarding-h5-report-gate-review-2026-05-29.md`; H5 landing coverage was checked with `rg -n "开户|账务|余额|结算|对账|报表|风险治理|多渠道收款|宝财通|宝户通|银企云|无法提现|开户失败|入金失败|入账慢|热点更新|压测调优|OpenSpec|Lore|Graphify|lore-bootstrap|当前更接近 L2|L2 -> L3|Day 1|Day 2|Day 3|30 天|60 天|90 天" wiki/reports/account-group-onboarding-h5.html`.
- Sensitive-info grep: passed with exit code 1 and no reader-facing matches from `rg -n "密码|账号已开通|Ethan|@baofu|10\\.254|http://10\\.|https://test-|云枢|VPN|扫码|二维码|GitLab|Jira|王竹|彬彬|杨锋将|token=|feishu.cn/wiki|feishu.cn/docx" wiki/reports/account-group-onboarding-h5.html`; domain vocabulary such as `账户` or generic `账号` is allowed when it does not expose credentials or account names.
- Desktop screenshot: passed with `playwright screenshot --full-page --viewport-size=1440,1800 file:///mnt/d/cloud/account-meeting-lore/wiki/reports/account-group-onboarding-h5.html /tmp/account-group-onboarding-desktop-full.png`; cover, capability map, business chain, AI maturity, 30/60/90 path, and task pool are readable without overlap.
- Mobile screenshot: passed with `playwright screenshot --full-page --viewport-size=390,1200 file:///mnt/d/cloud/account-meeting-lore/wiki/reports/account-group-onboarding-h5.html /tmp/account-group-onboarding-mobile-full.png`; cards stack cleanly and no horizontal overflow is visible.
- Font boundary: H5 uses a local Windows CJK font-face for WSL/Playwright readability; this is a local QA dependency, not a credential or publication claim.
- Final index link check: passed after adding `wiki/reports/index.md` entry for `account-group-onboarding-h5.html`.
- Rewrite account-domain content check: passed after cover, engineering boundary, capability map, system architecture, core chain, business objects, problem handling, active project entries, and technical planning were rewritten with domain-dense content.
- Rewrite excluded capability check: passed after `授信能力` and `垫资能力` were absent from the reader-facing H5.

## Decision

- Local H5 draft is ready for user review.
- Feishu sync is not approved by default and remains a separate follow-up.
- Extracted image assets were not required because primary visuals were rebuilt in HTML/CSS.

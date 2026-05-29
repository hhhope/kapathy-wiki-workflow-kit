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

## Visual Gate Failure Override

- Current status: previous Visual Gate pass claim is invalid.
- User rejection: the H5 reduced source architecture diagrams, capability maps,
  Nirvana diagrams, and latest project-report evidence into generic CSS boxes.
- Failure mode: the page looked like a generic card-based explanation rather
  than account-group technical training material. It did not preserve or redraw
  the source diagrams that carry architecture, domain structure, project scope,
  and onboarding entry points.
- Gate consequence: the earlier local-review decision is superseded. The H5 is
  not review-ready until it has standalone source-backed visual assets, embeds
  them in the key sections, and passes fresh desktop/mobile visual inspection.
- Repair change: `openspec/changes/redraw-account-onboarding-h5-source-visuals`.

## Repair Visual Plan

| Visual | Source Anchor | H5 Job | Repair Standard |
| --- | --- | --- | --- |
| Account capability map | `账户体系能力地图` slide | Teach the account capability landscape | Redraw as a map/graph; exclude `授信能力` and `垫资能力`; do not use six isolated cards as the primary visual. |
| Account system architecture | 多渠道收款 architecture + 宝财通 architecture slides | Show entrance, product, service, data, channel, and bank layers | Redraw as a layered architecture diagram with account, clearing, transaction, channel, and bank positions visible. |
| Account core chain | account technical status + clearing/account materials | Show how funds and account evidence flow | Redraw as a lane diagram from onboarding/opening to accounting, balance, clearing, reconciliation, and observability. |
| Nirvana / latest project map | `现状.png`, `最终方案.png`, `优化后图示.png`, `清算的内容.png`, split-account/core report | Show what the team is really doing now | Redraw current pressure, target architecture, clearing/account-service relation, and newcomer task entry points in one source-backed section. |

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
- Rewrite AI/newcomer content check: passed after AI collaboration was tied to account-domain design, module lookup, verification evidence, and knowledge reuse, and after Day 1/2/3, first-week, and 30/60/90 paths were rewritten.
- Rewrite HTML parser check: passed with `python3 -m html.parser wiki/reports/account-group-onboarding-h5.html`.
- Rewrite required content check: passed for capability map, system architecture, core chain, account-domain AI collaboration, and newcomer path.
- Rewrite sensitive-info grep: passed with no reader-facing matches for credentials, personal names, internal URLs, Feishu URLs, token strings, QR-code, GitLab, Jira, VPN, docs, or Apifox project links.
- Rewrite desktop screenshot: passed with `/tmp/account-group-onboarding-rewrite-desktop-full.png`.
- Rewrite mobile screenshot: passed with `/tmp/account-group-onboarding-rewrite-mobile-full.png`.

## Decision

- Local H5 draft is ready for user review.
- Feishu sync is not approved by default and remains a separate follow-up.
- Extracted image assets were not required because primary visuals were rebuilt in HTML/CSS.

## Rewrite Decision

- Superseded by Visual Gate Failure Override above. The rewrite added domain
  depth but still failed because it reduced the source visuals to box/card
  layouts.
- Feishu sync is not approved by default and remains a separate follow-up.
- Sensitive onboarding access details from Feishu source documents were intentionally excluded.

## Source-Visual Repair Evidence

| Asset | Editable Source | H5 Embed | Verification Role |
| --- | --- | --- | --- |
| Account capability map | `wiki/reports/assets/account-group-onboarding-h5/account-capability-map.svg` | `wiki/reports/assets/account-group-onboarding-h5/account-capability-map.png` | Replaces card-based capability blocks with a source-backed map. |
| Account system architecture | `wiki/reports/assets/account-group-onboarding-h5/account-system-architecture.svg` | `wiki/reports/assets/account-group-onboarding-h5/account-system-architecture.png` | Replaces layered CSS boxes with a diagram based on source architecture slides. |
| Account core chain | `wiki/reports/assets/account-group-onboarding-h5/account-core-chain.svg` | `wiki/reports/assets/account-group-onboarding-h5/account-core-chain.png` | Replaces wrapped flow cards with a lane-based funds-result responsibility chain. |
| Nirvana / latest project entry map | `wiki/reports/assets/account-group-onboarding-h5/nirvana-project-entry-map.svg` | `wiki/reports/assets/account-group-onboarding-h5/nirvana-project-entry-map.png` | Adds Nirvana current-state, target architecture, clearing/account relation, and latest project entry points. |

## Source-Visual Repair Verification Log

- SVG parser check: passed for all four SVG assets with `python3 -m xml.etree.ElementTree`.
- PNG export check: passed after exporting all four SVG assets with `playwright screenshot`.
- H5 embed check: switched from SVG-as-`img`, then `iframe`, then `object` after screenshots showed font or loading failures; final H5 embeds PNG assets generated from the SVG source visuals.
- HTML parser check: passed with `python3 -m html.parser wiki/reports/account-group-onboarding-h5.html`.
- Asset-reference grep: passed with `rg -n "account-capability-map\\.png|account-system-architecture\\.png|account-core-chain\\.png|nirvana-project-entry-map\\.png|这版先看重绘图|涅槃与最新项目" wiki/reports/account-group-onboarding-h5.html`.
- Excluded capability grep: passed with no matches for `授信能力|垫资能力` across H5 and visual assets.
- Sensitive-info grep: passed with no matches for credentials, internal URLs, Feishu URLs, token strings, QR-code instructions, personal emails, or access instructions across H5 and visual assets.
- Desktop screenshot: passed after visual inspection with `/tmp/account-group-onboarding-source-visuals-desktop.png`; all four PNG visuals render with readable Chinese text and no blank frames.
- Mobile screenshot: passed after visual inspection with `/tmp/account-group-onboarding-source-visuals-mobile.png`; visuals render as complete scaled images without horizontal clipping.
- Diff hygiene: passed with `git diff --check`.

## Source-Visual Repair Decision

- Local H5 draft is repaired for user review as a source-visual-driven version.
- Prior Visual Gate pass is invalid and remains recorded as a failure.
- Feishu sync is not approved by default and remains a separate follow-up.

## Heading And Roadmap Repair

- User feedback: the source-visual repair still carried a process-oriented
  section title, changed several chapter titles into informal wording, and left
  `技术规划` as card fragments instead of a planning route.
- Repair boundary: preserve the user's requested chapter structure, remove the
  process-oriented visual-index section, and treat `技术规划路线` as a first-class
  visual section.
- Removed reader-facing title: `这版先看重绘图，再看说明`.
- Restored / repaired section titles: `你加入的是什么小组`, `账户体系能力地图`,
  `核心业务链路`, `我们支撑的对象`, `正在做的项目`, `技术规划路线`,
  `AI 如何与我们协作`, `AI Coding 成熟度：当前站在哪一层`.
- Group-section rewrite: `你加入的是什么小组` now introduces the account
  technical group as the technical base for account relationships, accounting,
  balance, clearing/settlement, reconciliation/reporting, bank-account
  relations, channels, and observable funds results.

## Heading And Roadmap Visual Evidence

| Asset | Editable Source | H5 Embed | Verification Role |
| --- | --- | --- | --- |
| Technical planning fishbone roadmap | `wiki/reports/assets/account-group-onboarding-h5/account-technical-roadmap-fishbone.svg` | `wiki/reports/assets/account-group-onboarding-h5/account-technical-roadmap-fishbone.png` | Replaces technical-planning cards with a route from current multi-model / silo state to trustworthy funds results. |

## Heading And Roadmap Verification Log

- SVG parser check: passed for `account-technical-roadmap-fishbone.svg` with
  `python3 -m xml.etree.ElementTree`.
- PNG export check: passed after exporting the fishbone SVG with
  `playwright screenshot`; visual inspection used
  `/tmp/account-technical-roadmap-fishbone.png`.
- HTML parser check: passed with
  `python3 -m html.parser wiki/reports/account-group-onboarding-h5.html`.
- Required-heading grep: passed for the user-requested section titles and the
  repaired `我们支撑的对象` title.
- Removed-title grep: passed with no reader-facing matches for the rejected or
  informal titles.
- Sensitive-info grep: passed with no matches for credentials, internal URLs,
  Feishu URLs, token strings, QR-code instructions, personal emails, or access
  instructions across the H5 and the fishbone SVG.
- Desktop screenshot: passed after visual inspection with
  `/tmp/account-h5-heading-roadmap-desktop.png`; section order, source visuals,
  and the technical planning fishbone are visible.
- Mobile screenshot: passed after visual inspection with
  `/tmp/account-h5-heading-roadmap-mobile.png`; sections stack without visible
  horizontal clipping and the fishbone remains embedded as a complete image.
- Diff hygiene: passed with `git diff --check`.
- OpenSpec validation: passed with
  `openspec validate repair-account-h5-headings-roadmap --strict`; PostHog
  network flush errors were emitted after the local validation success and do
  not change the validation result.

## Heading And Roadmap Decision

- Local H5 draft now follows the requested chapter titles and adds a fishbone
  roadmap for `技术规划路线`.
- Feishu sync is not approved by default and remains a separate follow-up.

## AI Offering And Visual Style Repair

- User feedback: `AI 如何与我们协作` should explain what the account group can
  provide, including Account Harness, and the overall H5 style still looked
  rough and visually poor.
- Repair change: `openspec/changes/refine-account-h5-ai-offering-style`.
- AI section repair: the section now starts from account-group offerings:
  account-domain maps, Account Harness constraints, source material,
  verification evidence, and human judgment boundaries.
- Tool framing repair: OpenSpec, Lore, Graphify, and lore-bootstrap are now
  presented as supporting mechanisms rather than the lead message.
- Visual repair: the H5 removed the graph-paper background, thick black section
  borders, heavy block shadows, and repeated heavy card outlines. The page now
  uses a calmer internal technical-training style with lighter containers,
  disciplined card hierarchy, restrained shadows, and source-backed diagrams as
  the primary visual evidence.

## AI Offering And Visual Style Verification Log

- HTML parser check: passed with
  `python3 -m html.parser wiki/reports/account-group-onboarding-h5.html`.
- Required AI-offering grep: passed for `账户组能提供什么`,
  `Account Harness 约束`, `账户域输入`, `人工判断边界`, `OpenSpec`, `Lore`,
  `Graphify`, and `lore-bootstrap`.
- Undesired phrase grep: passed with no reader-facing matches for the old
  tool-first or rejected-process phrasing.
- Sensitive-info grep: passed with no matches for credentials, internal URLs,
  Feishu URLs, token strings, QR-code instructions, personal emails, or access
  instructions.
- Desktop screenshot: passed after visual inspection with
  `/tmp/account-h5-ai-style-desktop.png`; the page is calmer and source-backed
  diagrams remain primary.
- Mobile screenshot: passed after visual inspection with
  `/tmp/account-h5-ai-style-mobile.png`; sections stack without visible
  horizontal clipping.
- Diff hygiene: passed with `git diff --check`.
- OpenSpec validation: passed with
  `openspec validate refine-account-h5-ai-offering-style --strict`; PostHog
  network flush errors were emitted after the local validation success and do
  not change the validation result.

## AI Offering And Visual Style Decision

- Local H5 draft is repaired for user review on AI offering and visual style.
- Feishu sync is not approved by default and remains a separate follow-up.

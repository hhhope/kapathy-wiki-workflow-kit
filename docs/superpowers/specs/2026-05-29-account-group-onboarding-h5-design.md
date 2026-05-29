# Account Group Onboarding H5 Design

Date: 2026-05-29
Status: revision-written-review-pending
Route: brainstorm -> superpowers spec; OpenSpec read-only until spec review.

## Revision Note

The first H5 draft failed the reader job. Its sections were acceptable, but the
content inside them was too thin: the account capability map collapsed into a
few generic cards, the system architecture was absent, and core account-group
domains such as account model, bank-account / channel connection, accounting,
settlement, reconciliation, reporting, balance, and parent-child account
structure were not explained with enough engineering substance.

This revision keeps the screen order but changes the content standard: each
section must expose the real account-domain structure, not motivational
onboarding prose.

## Goal

Create an H5-first onboarding/training material for account-group fresh graduates. The material should help a newcomer understand:

- what the account group owns;
- how account, accounting, settlement, reconciliation, channel, and risk capabilities connect;
- which active projects they may join;
- how the team's AI engineering collaboration system changes daily work;
- what they can do and gain in the first days, first week, and first 30/60/90 days.

The output is a reader-facing internal H5 draft, not a final published Feishu page and not an OpenSpec implementation artifact.

## Reader Intent Contract

Reader: new graduates joining the account technical group.

Reader job-to-be-done: quickly build a mental model of the account domain, know how to start work, and understand which engineering capabilities they will grow.

Main line: first build the account-domain architecture and capability map, then
walk the fund/account chain through real modules, then land on project entry and
AI-assisted engineering collaboration.

Non-goals:

- do not reproduce every slide from the source PPT/PDF, but do preserve the
  load-bearing domain structure from the source visuals;
- do not expose unnecessary personal names, sensitive customer details, or overly granular production data;
- do not make the page a management performance report;
- do not turn AI体系建设 into a generic AI tool advertisement.

User-owned judgment:

- the selected delivery form is H5-first;
- the visual direction should reuse historical styles;
- the H5 should include account planning, active projects, and what newcomers can do and gain.

Agent-allowed work:

- extract and reorganize the source materials;
- propose H5 structure, evidence mapping, and visual components;
- later implement the HTML draft after explicit approval and planning.

## Source Materials

Primary local materials:

- `inbox/账户组技术规划与述职 _v6.pptx`
- `inbox/账户组技术现状分享.pptx`
- `inbox/4.0清结算账户体系概述.pdf`
- `wiki/sources/split-account-core-rd-investment-source-2026-05-26.md`

Feishu wiki materials read during brainstorming:

- `账户组技术小组新人入职指引`
- `IT技术小组新人入职指引`
- `Account Harness：总览（OpenSpec / Lore / Graphify / Lore Bootstrap，更新至 2026-04-13）`
- `AICoding L1-L4 路线图（更新至 2026-04-13）`

Source roles:

- 技术规划与述职: responsibilities, scale, risk exposure, governance, 2026 planning.
- 技术现状分享: business objects, typical modules, typical problems and handling mechanisms.
- 4.0清结算账户体系概述: foundational account/clearing/settlement concepts and boundaries.
- 分账核心改造 source: active project evidence and realistic task pool.
- 新人入职指引: Day 1/2/3, first-week tasks, development flow, monitoring, incident and duty practices.
- Account Harness and AICoding roadmap: AI collaboration model, maturity path, and engineering gates.

New extraction emphasis after user feedback:

- `账户体系能力地图` slide: treat the map as a capability graph, not a
  three-card summary. It includes account basic capability, unified accounting
  capability, clearing/settlement capability, unified balance capability,
  revenue capability, data/service capability, reporting capability, and
  reconciliation-related capability. Do not add 授信能力 or 垫资能力 as H5
  capability groups; the user explicitly rejected them.
- `宝财通` architecture slide: use the layered structure as the system
  architecture baseline: gateway layer, product layer, service layer, data
  layer, payment channels, partner banks, operation/back-office sides, and
  modules such as member system, transaction system, clearing system, risk
  control system, refund center, agent system, channel system, and account
  posting.
- `多渠道收款` architecture slide: use the upstream/middle/downstream structure:
  upstream product entrances, middle product implementations such as 银户通 /
  债转 / 宝财通 / 宝户通, and downstream direct banks plus self-owned channels.

## Output Shape

Build a long-scroll internal H5 page with roughly 15 screens. It should feel like a hybrid of:

- technical architecture poster: bold visual map, strong section hierarchy, reusable historical account/wiki H5 language;
- training journey: explicit newcomer path, task pool, and capability growth.

Do not make it a traditional PPT clone. Each screen should answer one question and contain one primary visual or card group plus short explanatory text.

## Visual Direction

Use the historical repo H5 style family, especially:

- thick-line technical poster treatment from `team-knowledge-architecture-h5.html` and `account-wiki-visuals.html`;
- dense but readable management cards from `split-account-core-rd-investment-analysis-2026-05-26.html`;
- restrained internal briefing layout from `nirvana-phase1-direct-sales-brief.html`.

Recommended palette:

- warm paper background for poster sections;
- dark navy/black outlines for hierarchy;
- blue/green/orange/purple accents to distinguish account domain, project work, risk/governance, and AI collaboration.

Avoid a one-note single-hue page, decorative gradients as the main visual, and text-heavy slide screenshots.

## Screen Plan

0. Cover: `账户组体系：从资金账户链路到 AI 协作成长`.
1. Account-group engineering boundary: explain that the group owns trustworthy
   fund/account results, not a single backend system. This section must answer
   three concrete questions: what money/account outcomes the group controls,
   what domain capabilities the team has, and what hard engineering abilities a
   newcomer can learn from these capabilities.
2. Account capability map: a real capability graph, not three buckets. It must
   include account basic capability, parent-child / multi-account model,
   unified accounting capability, clearing/settlement capability, unified
   balance capability, reconciliation/reporting/data-service capability, and
   revenue capability. Exclude 授信能力 and 垫资能力 as capability groups.
3. System architecture: layered architecture from entrances to services and
   data: API/H5/BM entrances; product layer; service layer; data layer; payment
   channels and partner banks; operation management and back-office sides.
4. Core business chain: entry / onboarding / account opening -> account model
   and bank-account relation -> transaction / collection / payment -> split
   account / withdrawal / refund -> accounting / voucher / balance -> clearing
   and settlement -> reconciliation / reports / difference handling -> risk,
   monitoring, and observability.
5. Typical business objects: multi-channel collection, 宝财通, 宝户通, 银企云 /
   银企通, bank-account access, and where each object sits in the architecture.
6. Typical problems and handling: withdrawal failure, account-opening failure,
   deposit failure, slow posting, hot updates, pressure testing, reconciliation
   differences, settlement differences, and account/balance inconsistency.
7. Active project entries: 宝财通 / 二级商户关系, settlement / withdrawal /
   clearing, reports / integration, balance-ledger verification, account merge,
   parent-child account or mother-real-child-virtual account direction.
8. Technical planning: unified account model, balance service, accounting
   standardization, settlement/reconciliation platform convergence,
   observability, risk map, technical debt governance, and JDK / Spring Boot
   upgrade where relevant.
9. AI collaboration system: OpenSpec manages change, Lore manages durable
   memory, Graphify manages structure, lore-bootstrap manages adoption. This
   section must be connected to account-domain work, not isolated tooling.
10. AI Coding maturity: L1-L4 model, current L2 baseline, next target L2 -> L3
    stage collaboration, and what this means for account-domain design,
    implementation, review, verification, and knowledge capture.
11. Newcomer 3 days / first week: Day 1 accounts/tools, Day 2 environment/code
    run, Day 3 norms/small task, first-week target: run one core account flow,
    read one module, and produce one evidence-backed note.
12. Newcomer 30/60/90: 30 days understand account-domain objects and chain, 60
    days participate in one module, 90 days independently troubleshoot and ship
    a small verifiable task with design, test, review, and evidence.
13. Task pool and gained capabilities: development, integration, accounting /
    settlement / reconciliation / reporting, production incident handling,
    monitoring/duty, knowledge-base writing, and AI collaboration materials.
14. Closing: newcomers are not only "receiving requirements"; they learn to
    control a fund/account chain and turn complex engineering into verifiable
    results.

## Content Components

Capability map:

- one large poster-like map with account-domain capabilities grouped by
  ownership area and maturity status.
- must show more than three groups. Minimum groups:
  - account basic capability: account lifecycle, account type management,
    personal wallet account, parent-child account relation, multi-account
    model, mother-real-child-virtual account direction;
  - unified accounting capability: accounting query, daily cut, reverse /
    adjustment, entry-rule engine, standard posting model, voucher center where
    applicable;
  - clearing/settlement capability: clearing/settlement rules, settlement /
    withdrawal / clearing result handling, unified reconciliation platform,
    basic reconciliation, difference handling;
  - unified balance capability: available balance, real-time balance,
    frozen balance, balance engine or balance-service convergence;
  - data/report/service capability: data and service, balance query, report
    capability, data external service;
  - revenue capability: revenue account, split profit / split account, revenue
    calculation and account handling where source-backed.
- do not introduce 授信能力 or 垫资能力 as capability groups.

Business chain diagram:

- flow diagram showing where account, bank-account relation, transaction,
  accounting, balance, clearing/settlement, reconciliation, reports, and risk
  observability happen.
- it should make dependencies visible: upstream product entrance creates
  identity and account relation; transaction creates fund movement; accounting
  and balance make the result internally trustworthy; clearing/settlement and
  reconciliation verify it against external or downstream results.

System architecture diagram:

- use the 宝财通 / 多渠道 architecture slides as the baseline.
- show layers rather than slogans:
  - entrance / gateway: API, H5, BM and upstream product entrances;
  - product: payment split-account product and account product;
  - service: base service, member system, transaction system, clearing system,
    risk system, refund center, agent system, channel system;
  - data: merchant, user, payment, channel, finance, and risk data;
  - external connections: bank union / network union / self-owned payment
    channels and partner banks such as bank-enterprise channel connections;
  - operation / back-office sides: operation management platform, AD, BM.

Project entry cards:

- each active project card includes "domain position", "what it changes",
  "what a newcomer can do", and "what capability it trains".
- cards should be concrete enough for onboarding:
  - account model / account merge;
  - parent-child account / mother-real-child-virtual account direction;
  - balance and ledger verification;
  - settlement / withdrawal / clearing;
  - reconciliation / reports / data validation;
  - 宝财通 / 二级商户关系;
  - bank-account / channel access.

AI collaboration panel:

- four-layer model: OpenSpec, Lore, Graphify, lore-bootstrap.
- maturity ladder: L1, L2, L3, L4.
- plain-language explanation of why the next step is stage collaboration, not blind automation.
- must show how AI helps with account-domain work: reading historical designs,
  checking whether a new requirement duplicates existing account capability,
  comparing module boundaries, producing design / review / verification
  evidence, and preserving reusable knowledge.

Newcomer path:

- Day 1/2/3 and first-week checklist from onboarding docs.
- 30/60/90 path as the H5's practical landing section.
- Do not use generic onboarding labels as the content. The reader-facing wording should be closer to:
  "账户组管的是资金结果", "我们手里有哪些能力", and "新人能练到哪些硬能力".

Task pool:

- map task categories to gained capabilities.
- examples: API/test environment setup -> engineering hygiene; reconciliation/reporting -> data accuracy; incident/duty -> risk awareness; AI collaboration -> specification, verification, and knowledge reuse.

## Evidence Handling

Use source facts as anchors, but rewrite for newcomers.

Allowed:

- business object names;
- technical direction names;
- aggregate scale and project categories when useful;
- Day 1/2/3 onboarding rhythm;
- AI collaboration layer names and maturity levels.

De-noise or abstract:

- personal names unless required by the user's final content decision;
- credentials, internal account instructions, exact test URLs, and sensitive operational links;
- overly granular production incident details;
- raw spreadsheet/person-day tables unless converted to training meaning.

## Verification Plan

Before claiming the H5 draft is review-ready:

- verify source-to-screen mapping for all 15 screens;
- verify the revised capability map contains the required account-domain groups
  and does not include 授信能力 or 垫资能力 as groups;
- verify system architecture includes layered entrance/product/service/data/
  channel/bank/back-office structure;
- verify the core chain includes account model, bank-account relation,
  accounting, balance, clearing/settlement, reconciliation, reports, and
  difference handling;
- check that every screen has one clear reader question;
- check no sensitive account, credential, or internal URL residue leaks into reader-facing text;
- run a visual QA pass at desktop and mobile widths if an HTML draft is implemented;
- confirm AI体系建设 appears as engineering collaboration with gates and evidence, not as generic tooling.

## Implementation Defaults

- Rebuild the primary visuals directly in HTML/CSS by default. Use extracted images only if a source visual carries information that would be lossy to redraw.
- Produce a standalone local H5 review draft under `wiki/reports/` by default. Supporting assets may be added only when the H5 needs reusable images or thumbnails.
- Do not sync to Feishu or publish by default. Treat Feishu sync as a separate explicit approval step after local H5 review.

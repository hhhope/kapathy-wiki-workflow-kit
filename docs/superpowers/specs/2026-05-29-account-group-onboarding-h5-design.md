# Account Group Onboarding H5 Design

Date: 2026-05-29
Status: written-spec-review-pending
Route: brainstorm -> superpowers spec; OpenSpec read-only until spec review.

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

Main line: from account-domain cognition to real project entry, then to AI-assisted engineering collaboration and growth path.

Non-goals:

- do not reproduce every slide from the source PPT/PDF;
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

## Output Shape

Build a long-scroll internal H5 page with roughly 14 screens. It should feel like a hybrid of:

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
1. What group am I joining: account-group responsibility boundary, business objects, system scale, and why it matters.
2. Account capability map: account opening, account model, accounting, balance, settlement, reconciliation, channel, reporting, and risk.
3. Core business chain: account opening -> acquiring/payment -> split account/withdrawal -> posting/accounting -> reconciliation.
4. Typical business objects: multi-channel collection, 宝财通, 宝户通, 银企云/银企通, and where they sit in the map.
5. Typical problems and handling: withdrawal failure, account-opening failure, deposit failure, slow posting, hot updates, pressure testing.
6. Active project entries: 宝财通/二级商户关系, settlement/withdrawal/clearing, report/integration, balance and ledger verification.
7. Technical planning: unified account model, balance center, accounting standardization, settlement/reconciliation convergence, observability, risk map.
8. AI collaboration system: OpenSpec manages change, Lore manages durable memory, Graphify manages structure, lore-bootstrap manages adoption.
9. AI Coding maturity: L1-L4 model, current L2 baseline, next target L2 -> L3 stage collaboration.
10. Newcomer 3 days / first week: Day 1 accounts/tools, Day 2 environment/code/project run, Day 3 norms/small task, first-week core flow.
11. Newcomer 30/60/90: understand chain, join modules, independently troubleshoot and deliver small work, use AI collaboration safely.
12. Task pool and gained capabilities: development, integration, reconciliation/reporting, production incident handling, monitoring/duty, knowledge-base writing, AI collaboration materials.
13. Closing: newcomers are not only "receiving requirements"; they learn to control a fund-account chain and turn complex engineering into verifiable results.

## Content Components

Capability map:

- one large poster-like map with account-domain capabilities grouped by lifecycle.
- should be the first durable visual anchor.

Business chain diagram:

- flow diagram showing where account, clearing, settlement, reconciliation, and reporting happen.
- should explain direction and dependency, not every system detail.

Project entry cards:

- each active project card includes "what it is", "what a newcomer can do", and "what capability it trains".

AI collaboration panel:

- four-layer model: OpenSpec, Lore, Graphify, lore-bootstrap.
- maturity ladder: L1, L2, L3, L4.
- plain-language explanation of why the next step is stage collaboration, not blind automation.

Newcomer path:

- Day 1/2/3 and first-week checklist from onboarding docs.
- 30/60/90 path as the H5's practical landing section.

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

- verify source-to-screen mapping for all 14 screens;
- check that every screen has one clear reader question;
- check no sensitive account, credential, or internal URL residue leaks into reader-facing text;
- run a visual QA pass at desktop and mobile widths if an HTML draft is implemented;
- confirm AI体系建设 appears as engineering collaboration with gates and evidence, not as generic tooling.

## Implementation Defaults

- Rebuild the primary visuals directly in HTML/CSS by default. Use extracted images only if a source visual carries information that would be lossy to redraw.
- Produce a standalone local H5 review draft under `wiki/reports/` by default. Supporting assets may be added only when the H5 needs reusable images or thumbnails.
- Do not sync to Feishu or publish by default. Treat Feishu sync as a separate explicit approval step after local H5 review.

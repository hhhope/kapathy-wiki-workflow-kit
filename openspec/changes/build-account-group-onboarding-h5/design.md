# Design: Account Group Onboarding H5

## Source And Audience

- Audience: account-group new graduates.
- Primary local sources:
  - `inbox/账户组技术规划与述职 _v6.pptx`
  - `inbox/账户组技术现状分享.pptx`
  - `inbox/4.0清结算账户体系概述.pdf`
  - `wiki/sources/split-account-core-rd-investment-source-2026-05-26.md`
- Feishu wiki sources read during design:
  - `账户组技术小组新人入职指引`
  - `IT技术小组新人入职指引`
  - `Account Harness：总览（OpenSpec / Lore / Graphify / Lore Bootstrap，更新至 2026-04-13）`
  - `AICoding L1-L4 路线图（更新至 2026-04-13）`

The H5 should help a newcomer answer four questions:

1. What does the account group own?
2. How do account, accounting, settlement, reconciliation, channel, and risk
   capabilities connect?
3. Which active project areas can I join, and what will I learn?
4. How does the team's AI collaboration system shape daily engineering work?

## Artifact

Create a standalone HTML file:

- `wiki/reports/account-group-onboarding-h5.html`

The page must open directly in a browser and use inline CSS only unless a small
interaction is explicitly justified later. No external dependency, backend,
build pipeline, live API call, Feishu sync, or asset extraction is required by
default.

## Sections

The H5 uses a long-scroll format with about fourteen reader-visible sections:

1. Cover: `账户组体系：从资金账户链路到 AI 协作成长`.
2. What group am I joining: responsibilities, business objects, scale, and why
   the group matters.
3. Account capability map: account opening, account model, accounting,
   balance, settlement, reconciliation, channel, reporting, and risk.
4. Core business chain: account opening -> acquiring/payment -> split
   account/withdrawal -> posting/accounting -> reconciliation.
5. Typical business objects: multi-channel collection, 宝财通, 宝户通,
   银企云/银企通.
6. Typical problems and handling: withdrawal failure, account-opening failure,
   deposit failure, slow posting, hot updates, and pressure testing.
7. Active project entries: 宝财通/二级商户关系, settlement/withdrawal/clearing,
   report/integration, balance and ledger verification.
8. Technical planning: unified account model, balance center, accounting
   standardization, settlement/reconciliation convergence, observability, risk
   map.
9. AI collaboration system: OpenSpec manages change, Lore manages durable
   memory, Graphify manages structure, lore-bootstrap manages adoption.
10. AI Coding maturity: L1-L4 model, current L2 baseline, next target L2 -> L3
    stage collaboration.
11. Newcomer 3 days / first week: Day 1 accounts/tools, Day 2
    environment/code/project run, Day 3 norms/small task, first-week core flow.
12. Newcomer 30/60/90: understand chain, join modules, independently
    troubleshoot and deliver small work, use AI collaboration safely.
13. Task pool and gained capabilities: development, integration,
    reconciliation/reporting, production incident handling, monitoring/duty,
    knowledge-base writing, AI collaboration materials.
14. Closing: newcomers are not only receiving requirements; they learn to
    control a fund-account chain and turn complex engineering into verifiable
    results.

## Visual Direction

Use the repo's existing H5 language:

- thick-line technical poster treatment from `team-knowledge-architecture-h5.html`
  and `account-wiki-visuals.html`;
- dense but readable management cards from
  `split-account-core-rd-investment-analysis-2026-05-26.html`;
- restrained internal briefing layout from
  `nirvana-phase1-direct-sales-brief.html`.

The page should rebuild primary visuals in HTML/CSS. Extracted images are
optional only when a source visual carries information that would be lossy to
redraw.

## Public Output Boundary

The H5 is an internal review draft. It may use business-object and capability
names, but it must not expose credentials, internal test URLs, personal contact
details, personal rankings, Feishu tokens, or sensitive production details in
the reader-facing body.

The gate review record must preserve the source-to-screen mapping,
sensitive-information boundary, verification results, and explicit statement
that Feishu sync was not performed.

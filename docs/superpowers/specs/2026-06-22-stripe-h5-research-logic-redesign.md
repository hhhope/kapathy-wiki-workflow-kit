# Stripe H5 Research Logic Redesign

## Selected Direction

Use direction A from the visual companion:

> BVP-style trend report + three-dimensional timeline.

The user selected this because it is easier to understand than a flat chapter
list. The H5 should learn from `State of the Cloud 2024`: start with a strong
theme, split the argument into trend cards, and give every trend a compact set
of notable data points and implications.

Reference used for shape:

- `https://www.bvp.com/atlas/state-of-the-cloud-2024`

The design should not copy BVP's visual identity. It should copy the reporting
logic:

- one top theme
- several trend areas
- each trend has a takeaway
- each trend has notable data points
- each trend has an implication
- charts support trends rather than becoming raw source dumps

## Problem Being Fixed

The current H5 drifted because it kept adding visible material blocks without
first fixing the research argument. The user rejected three sections in
particular:

- `市场位置计算面板`
- `公司运营、市场位置、并购与技术事件线`
- `AI 交易链路时间线：从商品发现到机器支付`

The shared failure is that each section looks like a source bucket. None of the
three clearly says what it proves. Market metrics, acquisitions, technology
events, and AI transaction changes are mixed into charts without a visual
grammar.

## Core Reader Question

The H5 should answer:

> Stripe 如何理解 AI 时代的交易变化，它如何重新定位自己，我们能从它的路径中学到什么？

The answer:

> Stripe's AI-era bet is not "payments plus AI." It is that AI changes the
> transaction system itself: who buys, where demand appears, how products are
> represented, how usage is priced, how payment is authorized, how settlement
> happens, and where risk appears. Stripe is using its payment, billing, risk,
> wallet, stablecoin, and developer-interface capabilities to position itself
> as infrastructure for that new transaction system.

## Page-Level Structure

The H5 should use this reader-facing sequence:

1. `AI 时代，Stripe 要争夺的不是支付按钮，而是交易系统入口`
2. `五个趋势定义 Stripe 的 AI 交易基础设施路径`
3. `三维时间轴：时间 x 证据维度 x 证明任务`
4. `趋势 1：交易入口从网站迁移到 Agent surface`
5. `趋势 2：商品表达从网页转向机器可读 catalog / API`
6. `趋势 3：计费从订阅转向 usage / token / event`
7. `趋势 4：结算从 card rails 扩到 wallet / stablecoin / machine payment`
8. `趋势 5：风险从盗卡扩到 token theft / tool misuse / resource abuse`
9. `Stripe 的定位：从支付 API 到 AI 交易基础设施`
10. `我们能学什么`
11. `来源与证据边界`

Do not use internal chapter names such as `核心判断`, `原有能力底座`,
`市场位置计算面板`, or `公司运营、市场位置、并购与技术事件线` as visible
reader-facing headings.

## BVP-Style Trend Card Model

Each trend should follow the same visual grammar:

| Field | Meaning |
|---|---|
| Trend area | What is changing in the market or transaction system |
| Key takeaway | One sentence the reader should remember |
| Notable data points | 3-5 metrics / events / launches / acquisitions |
| Stripe implication | What this means for Stripe's positioning |
| Evidence trail | Promoted sources that support the claim |

Example trend card:

| Field | Draft content |
|---|---|
| Trend area | Agent commerce |
| Key takeaway | Demand generation and checkout are moving into AI surfaces. |
| Notable data points | Copilot Checkout; Agentic Commerce Suite; ProductCatalogImport; Shared Payment Token |
| Stripe implication | Stripe must make product catalogs, payment authorization, and merchant controls machine-readable. |
| Evidence trail | Stripe Copilot release; agentic commerce docs; seller docs |

## Three-Dimensional Timeline

The timeline is the central visual. It should not be a flat list of events.

Dimensions:

1. `time`: 2010, 2015, 2020, 2023, 2024, 2025, 2026.
2. `evidence lane`: company scale, market position, acquisition / capability
   gap, product / technical event, AI transaction shift, organization signal.
3. `proof tag`: what the event proves.

Example layout:

| Time | Company scale | Market position | Acquisition / gap | Product / tech | AI transaction shift | Proof tag |
|---|---|---|---|---|---|---|
| 2010-2014 | developer adoption | no scale claim | none | API / SDK / docs | none | interface foundation |
| 2015-2019 | platforms / SaaS | merchant expansion | none | Connect / Billing / Radar / Terminal | none | merchant operating layer |
| 2020-2022 | pandemic growth / valuation cycle | funding context | Paystack / TaxJar / BBPOS | Treasury / Tax / Identity / Issuing | early AI not central | financial operations layer |
| 2023 | $1T processed volume | 1% GDP equivalent | none | Revenue suite pressure | AI customers pressure billing / risk | system-scale signal |
| 2024 | ~$1.4T secondary volume | peer/share-gain signals | Bridge announced | agent docs begin mattering | AI distribution pressure | market-position expansion |
| 2025 | $1.9T / 5M+ businesses | 1.6% GDP equivalent | Bridge / Privy / Metronome | stablecoin / wallet / usage stack | agent commerce becomes productized | capability gap closing |
| 2026 | Sessions 288 launches | AI infra narrative | Tempo / ecosystem moves | Link wallets / MPP / x402 / Radar token theft | machine payment and agent wallets | AI transaction infrastructure |

Visual requirements:

- Use horizontal time.
- Use lanes for evidence categories.
- Use colors consistently:
  - scale / market: green
  - acquisition / capability gap: red
  - product / technical event: gold
  - AI transaction shift: blue
  - organization / risk: slate
- Each node has one proof tag.
- Clicking or tapping a node opens evidence details.

The timeline should answer: "When did Stripe's positioning change, and which
evidence supports that change?"

## Market Position Visual

Market position should become one sub-view inside the three-dimensional
timeline, not a standalone calculation panel.

Reader-facing title:

> Stripe 是否已经接近系统级入口？

Visual design:

- first show Stripe processed-volume growth: `$1T -> ~$1.4T -> $1.9T`
- then show GDP-equivalent movement: `1.0% -> 1.6%`
- then show peer reference bands: PayPal, Adyen, Worldpay / Global Payments
  where comparable
- formulas and take-rate notes go in an expandable evidence drawer

Do not show:

- `两公司 TPV 参照`
- unexplained sensitivity ranges like `$2.8B-$35.9B`
- formulas as the main story

The claim should be:

> Stripe's visible processing surface is large enough to treat it as a serious
> candidate for AI-era transaction infrastructure, but the page must not claim a
> precise audited global market share.

## Acquisition / Capability Gap Visual

Acquisitions should be shown as capability gap closures, not as a flat M&A list.

| Gap | Stripe move | What it enables in the AI-era transaction system |
|---|---|---|
| local payment network | Paystack | regional payment coverage |
| tax and reconciliation | TaxJar / Recko | global merchant operations |
| offline / hardware | BBPOS / Terminal | omnichannel payment surface |
| merchant-of-record | Lemon Squeezy | software and digital goods selling |
| stablecoin orchestration | Bridge | stablecoin settlement and orchestration |
| wallet abstraction | Privy | agent / app wallet infrastructure |
| usage and event rating | Metronome | token / event / outcome billing |

This visual answers:

> What gaps did Stripe have to close before it could credibly move from
> payments into AI transaction infrastructure?

## AI Transaction Visual

AI transaction change should be a chain, not a timeline.

Chain:

1. demand appears: website / app -> Copilot / Gemini / ChatGPT / agent surface
2. product is represented: page -> catalog / API / inventory / price feed
3. price is calculated: subscription -> usage / token / event / outcome
4. buyer is authorized: card entry -> wallet / one-time token / approval
5. payment settles: card rails -> stablecoin / MPP / x402 / machine payment
6. risk moves: card fraud -> token theft / fake signup / tool misuse /
   resource abuse

Each step should show:

- old state
- AI-era state
- Stripe evidence
- open proof boundary

This visual answers:

> Which parts of the transaction does AI rewrite, and where does Stripe place
> itself?

## Source Use Model

The 1000-source queue should not appear as a content brag. It should power the
evidence trails.

States:

1. `queued`: concrete URL collected but not read.
2. `read`: source opened, dated, and summarized.
3. `classified`: assigned to a trend, lane, and proof tag.
4. `promoted`: allowed to support visible H5 claims.

Evidence roles:

- `scale`: TPV, customers, valuation, liquidity.
- `market`: peer TPV, take-rate mechanics, share-gain commentary.
- `product`: Billing, Radar, Connect, Tax, Treasury, Link.
- `acquisition`: capability-gap closure.
- `technical`: API, docs, MCP, preview headers, GitHub.
- `ai_transaction`: agent checkout, catalog, wallet, stablecoin, MPP / x402.
- `organization`: JD, audit, compliance, stablecoin, AI platform roles.

The page should show promoted evidence only. The source appendix can explain
queue size and unresolved evidence gaps.

## What We Learn

The final section should not praise Stripe. It should extract reusable lessons:

- Infrastructure strategy means turning messy financial operations into
  programmable interfaces.
- AI changes more than the payment step; it changes demand generation, product
  representation, pricing, authorization, settlement, and risk.
- Docs, APIs, SDKs, sandboxes, and agent-readable files become distribution
  channels.
- Acquisitions should be read as capability-gap closure.
- To evaluate an AI-finance infrastructure company, look across scale, market
  position, capability gaps, transaction-chain coverage, technical interfaces,
  organization signals, and evidence strength.

## Acceptance Criteria

- The first screen states the AI-era transaction infrastructure thesis.
- The page uses BVP-style trend cards: trend area, key takeaway, notable data
  points, implication, evidence trail.
- The central timeline is three-dimensional: time, evidence lane, proof tag.
- Market position is a trend-supporting visual, not a calculation panel.
- Acquisitions are organized by capability gap.
- AI transaction change is shown as a chain, not a time-only timeline.
- Every visual has one job.
- Every load-bearing claim links to promoted evidence.
- The page does not imply all 1000 sources have been read.
- The result stays an internal draft until source promotion and report review
  gates pass.

## Out Of Scope For Next Implementation

- Feishu sync.
- public-ready investment conclusion.
- exact audited global market-share percentage.
- full reading of all 1000 queued sources.
- new external dashboard or database UI.
- unrelated style overhaul outside the Stripe H5.

## Implementation Boundary

Implementation may begin only after this selected direction is reviewed and the
next implementation plan is approved. The next implementation should update the
H5 structure and supporting source/gate notes, not add another independent
visual module.

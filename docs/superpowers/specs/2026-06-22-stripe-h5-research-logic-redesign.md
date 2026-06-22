# Stripe H5 Research Logic Redesign

## Context

The current Stripe H5 drifted because it kept adding visible material blocks
without first fixing the research argument. The user rejected three chapters in
particular:

- `市场位置计算面板`
- `公司运营、市场位置、并购与技术事件线`
- `AI 交易链路时间线：从商品发现到机器支付`

The shared failure is not a missing data point. The failure is that each chapter
looks like a source bucket, while no chapter clearly says what it proves.
Charts, timelines, acquisitions, market metrics, and AI transaction evidence
compete for the same explanatory role.

No more H5 implementation should happen until this redesign is reviewed.

## Reader Question

The H5 should answer one question:

> How does Stripe understand the AI-era change in economic activity, how is it
> positioning itself, and what can we learn from that positioning?

The answer should not be "Stripe is strong" or "Stripe has many AI products."
The answer should be:

> Stripe appears to believe that AI changes who initiates transactions, how
> products are represented, how usage is priced, how payment is authorized, how
> settlement happens, and where risk appears. Stripe's strategy is to turn its
> existing payment, billing, risk, wallet, and settlement capabilities into
> infrastructure for that new transaction shape.

## Use Of The 1000 Sources

The 1000-source queue is not a page-content target. It is the evidence supply
chain.

Sources must be promoted through four states:

1. `queued`: concrete URL collected but not read.
2. `read`: source opened, dated, and summarized.
3. `classified`: assigned to one or more evidence roles.
4. `promoted`: allowed to support a visible H5 claim.

Evidence roles:

- `company_scale`: TPV, customers, valuation, liquidity events, profitability
  signals.
- `market_position`: peer TPV, processed volume, revenue / TPV, take-rate
  mechanics, analyst share-gain commentary.
- `capability_base`: API, docs, SDK, Billing, Radar, Connect, Tax, Treasury,
  Issuing, Link.
- `capability_gap`: acquisitions and product launches that fill a missing
  ability.
- `ai_transaction_shift`: agent checkout, catalog feed, usage billing, wallet
  authorization, stablecoin, machine payment, AI risk.
- `organization_signal`: JD, team, audit, compliance, AI platform, risk and
  stablecoin roles.

The H5 should show only promoted evidence. The source pack and queue can show
the rest.

## Approaches Considered

### A. Keep Current Structure And Improve Charts

This keeps the existing three chapters and makes each chart prettier.

Trade-off: lowest effort, but it preserves the core problem. The reader still
has to assemble the argument from scattered modules.

Decision: reject.

### B. Rebuild Around A Research Argument

This reorganizes the H5 into a sequence of proof jobs:

1. state the thesis
2. show Stripe's existing capability base
3. prove market position and scale
4. show how acquisitions fill capability gaps
5. show how AI changes the transaction chain
6. infer Stripe's AI-era worldview
7. extract lessons

Trade-off: higher rewrite cost, but it gives every chart a job and makes the
page readable as research rather than a dashboard.

Decision: recommended.

### C. Turn It Into A Research Dashboard

This treats the H5 as an analyst console with filters for source type, year,
product, acquisition, market metric, and AI transaction component.

Trade-off: strong for internal exploration, weak as a reader-facing argument.
It would also invite more source dumping.

Decision: reject for the current H5, keep as possible future internal tool.

## Recommended Chapter Design

### 01 Core Thesis

Job: tell the reader what the H5 is trying to prove.

Content:

- one paragraph thesis
- four proof anchors: 2025 TPV, AI customer pressure, Bridge / Privy /
  Metronome, agentic commerce / machine payments

Visual:

- one horizontal "from payments to AI economic infrastructure" path

Not allowed:

- source queue explanation
- market-share caveats
- general AI rhetoric

### 02 Original Capability Base

Job: explain why Stripe can plausibly move into AI economic infrastructure.

Argument:

Stripe did not start as an AI company. It built a reusable interface layer for
payments, then expanded into merchant operations and financial operations.

Structure:

- API / SDK / docs / testing
- Connect / Billing / Radar / Tax
- Treasury / Capital / Issuing / Link
- Stablecoin / wallet / agent-facing interfaces

Visual:

- capability ladder, not a year-by-year timeline

Evidence:

- official annual letters
- docs and API references
- product pages

### 03 Market Position And Scale

Job: answer whether Stripe has enough scale and relative market position for
the AI-infrastructure claim to matter.

This chapter should not be named `市场位置计算面板`. It should be named:

> Stripe 是否已经接近系统级入口

Reader-facing claims:

- Stripe's processed volume grew from $1T in 2023 to $1.9T in 2025.
- Stripe's own GDP-equivalent framing moved from 1.0% to 1.6%.
- Peer comparison should show relative position, not pretend to produce global
  audited market share.
- Take-rate formulas belong in a footnote or expandable detail, not the main
  visual.

Visual:

- primary chart: Stripe TPV growth line / bars
- secondary chart: peer TPV reference band for PayPal, Adyen, Worldpay /
  Global Payments where comparable
- small note: revenue / TPV is a method, not Stripe revenue

Not allowed:

- "two-company TPV share" as a headline number
- unexplained sensitivity range such as `$2.8B-$35.9B`
- leading with caveats before the reader sees the trend

### 04 Capability Gaps And Acquisitions

Job: prove that acquisitions are not trivia; they map to missing capabilities.

Structure:

| Gap | Acquisition / event | Why it matters |
|---|---|---|
| local payment network | Paystack | Africa and local payment coverage |
| tax and finance ops | TaxJar / Recko | sales tax, reconciliation |
| physical / offline | BBPOS / Terminal | hardware and offline payment |
| merchant-of-record | Lemon Squeezy | software and digital goods selling |
| stablecoin orchestration | Bridge | stablecoin payment and settlement |
| wallet abstraction | Privy | agent / app wallet infrastructure |
| usage rating | Metronome | token / event / outcome billing |

Visual:

- capability-gap matrix
- optional timeline only as a secondary axis

Not allowed:

- a flat acquisition list
- mixing valuation, product release, and acquisition in the same card without a
  clear "gap" label

### 05 AI Transaction Chain

Job: explain exactly what AI changes in the transaction.

This chapter should not be another timeline. It should be a chain:

1. discovery: human search / website -> AI app / Copilot / Gemini / ChatGPT
2. product representation: webpage -> catalog / API / inventory / price feed
3. pricing: subscription -> usage / token / event / outcome
4. authorization: card entry -> wallet / one-time token / approval
5. settlement: cards -> stablecoin / machine payment / MPP / x402
6. risk: card fraud -> token theft / fake signup / tool misuse / prompt
   injection / resource abuse

Visual:

- transaction-chain diagram with before / after rows
- evidence chips attached to each step

Evidence:

- agentic commerce docs
- Copilot Checkout
- Sessions 2026
- machine payment docs
- AI security / Radar / relevant JDs

Not allowed:

- time-only timeline cards
- abstract section titles like `AI changes financial objects`
- evidence labels that do not point to a transaction-chain step

### 06 Stripe's AI-Era Worldview

Job: infer Stripe's strategy from the evidence.

Claims:

- AI increases company creation and product launch speed.
- AI moves commerce entry points away from merchant websites and toward agent
  surfaces.
- AI products need more granular billing and faster feedback between cost and
  revenue.
- Agent commerce needs wallet, authorization, approval, and risk infrastructure.
- Content, APIs, and data sources become monetizable resources through machine
  payment protocols.

Visual:

- five "Stripe believes..." cards, each with one evidence trail

Not allowed:

- claiming Stripe has already won the AI infrastructure layer
- claiming protocol adoption without customer / partner / community evidence

### 07 What We Learn

Job: turn Stripe's path into reusable lessons.

Lessons:

- In infrastructure markets, the winning move is often to turn messy operations
  into programmable interfaces.
- AI changes distribution, billing, authorization, settlement, and risk at the
  same time.
- Documentation, SDKs, sandboxes, and agent-readable interfaces become
  distribution channels.
- M&A should be read as capability-gap filling, not only revenue expansion.
- A finance AI infrastructure company should be evaluated across scale,
  customer structure, technical interfaces, protocol participation, M&A, and
  hiring.

Visual:

- final synthesis map

## Visual Grammar

Each visual type must have one job:

- `path`: explain strategic evolution.
- `bar / line chart`: show growth and relative scale.
- `matrix`: map capability gaps to acquisitions or products.
- `chain`: show how AI changes transaction steps.
- `evidence trail`: connect a claim to sources.

One visual must not mix all jobs. If a chart contains timeline, acquisition,
market, and AI evidence at once, it should be split.

## Information Architecture

The reader-facing H5 should hide source-management mechanics until the end.

Recommended order:

1. thesis
2. capability base
3. scale and market position
4. capability gaps and acquisitions
5. AI transaction chain
6. Stripe's AI-era worldview
7. lessons
8. source appendix

The source appendix should explain the 1000-source queue, promoted evidence, and
remaining evidence gaps.

## Acceptance Criteria

- A reader can explain the H5 thesis in one sentence after the first screen.
- Every chapter has a visible "this chapter proves..." role.
- No chapter title is a raw source bucket such as `company operations, market
  position, acquisitions, and technical events`.
- Market-position visuals show growth and relative position before formulas.
- Acquisition visuals are organized by capability gap.
- AI visuals are organized by transaction-chain step, not by time alone.
- Source references are visible on load-bearing claims.
- The page does not imply all 1000 sources have been read.
- The H5 remains an internal draft unless source promotion and review gates pass.

## Out Of Scope For The Next Implementation

- Feishu sync
- public-ready investment conclusion
- exact audited global market-share percentage
- full reading of all 1000 queued sources
- new external dashboard or database UI

## Open Questions For User Review

1. Should the H5 thesis emphasize "AI transaction infrastructure" or broader
   "AI economic infrastructure"?
2. Should peer comparison include only payment companies, or also commerce /
   cloud / stablecoin infrastructure comparables?
3. Should the final lesson section target internal product strategy, investment
   research, or AI-finance architecture learning?

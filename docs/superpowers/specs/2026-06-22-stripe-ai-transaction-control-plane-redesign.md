# Stripe AI Transaction Control Plane H5 Redesign

## Route

Route: brainstorm -> superpowers spec; OpenSpec remains read-only until this
written design is reviewed.

This spec replaces the failed `证据坐标` repair direction. It does not authorize
HTML implementation yet.

## What We Are Doing

We are not making a Stripe source warehouse. We are building a reader-facing H5
that answers one research question:

> In the AI era, what does Stripe think the transaction system is becoming, how
> is Stripe positioning itself inside that system, and what can we learn from
> the path?

The answer we will test in the H5:

> AI moves commerce from a human checkout flow into a machine-readable
> transaction control plane. The control points are demand entrance, product
> representation, pricing and metering, buyer authorization, settlement rail,
> and risk control. Stripe's products, acquisitions, developer surfaces, market
> scale, and hiring signals should be read by how they attach to those control
> points.

## Why The Current Draft Failed

The current draft has useful material but the design is wrong:

- It makes `evidence` the reader-facing frame. That turns the page into an
  audit warehouse instead of a strategy report.
- The market panel, timeline, AI chain, capability map, signal cloud, and source
  inventory are adjacent modules. They do not clearly answer one shared
  question.
- The BVP reference was applied as trend-card vocabulary, not as a visual
  argument system.
- The 1000-source queue is shown as quantity, but the reader cannot see how
  sources change the judgment.
- The signal cloud is clickable but not useful. It does not filter the system,
  show density over time, or connect source categories to control points.
- Acquisitions appear as capability cards, but they are not visually attached to
  the transaction step they repair.

The next H5 must solve relationship first, then prose.

## BVP Reference: What To Copy And What Not To Copy

Reference: `https://www.bvp.com/atlas/state-of-the-cloud-2024`.

Use from BVP:

- one clear thesis before detailed material
- a small set of named trend areas
- strong visual blocks that carry the argument
- notable data points under each trend
- implications after facts, not before facts
- jumpable sections and scan-friendly rhythm

Do not copy from BVP:

- visual brand, palette, illustrations, or typography
- VC prediction tone
- broad market hype as proof
- trend labels that are not native to Stripe

Stripe adaptation:

- BVP's subject is `AI Cloud`.
- Our subject is `AI transaction control plane`.
- BVP's trend areas become six transaction control points.
- BVP's notable data points become Stripe metrics, acquisitions, API/docs,
  partner launches, JD signals, and source density.

## Reader-Facing Thesis

Working title:

> Stripe: 从支付 API 到 AI 交易控制面

First-screen thesis:

> AI 不只是让支付更智能，而是把交易拆成机器可以发现、读取、计量、授权、结算和风控的系统。Stripe 的路径，是把支付、账单、风控、钱包、稳定币、协议和开发者工具接到这些控制点上。

Avoid on the page:

- `证据坐标`
- `核心判断`
- `原有能力底座`
- `市场位置计算面板`
- `能力迁移地图`
- `不是...而是...` as a repeated paragraph pattern
- meta labels such as `proof tag`, `evidence lane`, `source queue` as primary
  reader headings

Evidence still exists, but it sits in drawers, labels, source chips, and the
appendix layer.

## Page Structure

### 1. Hero: The Control Plane Claim

Job: Tell the reader what the H5 is trying to prove.

Visible content:

- title: `Stripe: 从支付 API 到 AI 交易控制面`
- subtitle: AI changes the whole transaction system, not only checkout.
- four top metrics:
  - `$1.9T` processed volume in 2025
  - `1.6%` GDP-equivalent framing from Stripe
  - `288` Sessions 2026 launches
  - `1000` concrete source rows, marked as a triage queue

Visual:

- full-width system diagram preview, not a text card grid
- six control points visible above the fold
- Stripe product/acquisition/API markers placed on the diagram

### 2. Master Visual: AI Transaction Control Plane

Job: Carry the whole article.

Horizontal flow:

1. Demand entrance
2. Product representation
3. Pricing and metering
4. Buyer authorization
5. Settlement rail
6. Risk control

For each control point, show:

- old transaction object
- AI-era transaction object
- Stripe capability
- key source types
- unresolved proof boundary

Initial mapping:

| Control point | Old object | AI-era object | Stripe signals |
|---|---|---|---|
| Demand entrance | website / app traffic | Copilot, Gemini, ChatGPT, agent surface | Copilot Checkout, Agentic Commerce Suite |
| Product representation | product page and checkout SKU | catalog feed, inventory feed, pricing feed, order approval | ProductCatalogImport, 15-minute inventory/pricing refresh, Checkout Session fulfillment |
| Pricing and metering | subscription / invoice | token, event, usage, outcome | Billing, Revenue suite, Metronome, streaming payments |
| Buyer authorization | card entry / saved credential | wallet, one-time token, approval hook, Shared Payment Token | Link wallets for agents, SPT, Privy |
| Settlement rail | card rails / bank payout | stablecoin, MPP, x402, machine payment | Bridge, Tempo, machine payments docs |
| Risk control | card fraud / dispute | token theft, fake signup, prompt/tool misuse, resource abuse | Radar token theft, AI Security JD, seller approval hook |

Interaction:

- clicking a control point filters all lower sections
- hover/click reveals source chips and source strength
- color means control point, not arbitrary evidence category

### 3. Trend Blocks: Six Control Points, BVP-Style

Job: Explain each control point in a consistent report grammar.

Each trend block uses:

- `Change`: what changed in the transaction system
- `Stripe move`: what Stripe placed there
- `Data / event`: 3-5 hard markers
- `Implication`: what this means for Stripe's position
- `Source drawer`: promoted sources and boundary

Example:

`Demand entrance`

- Change: commerce surfaces move from merchant-owned sites into AI surfaces.
- Stripe move: Copilot Checkout and Agentic Commerce Suite place Stripe inside
  agent-driven discovery and purchase flows.
- Data / event: Microsoft Copilot Checkout, Agentic Commerce Protocol, Shared
  Payment Token, Google/Gemini relation from Sessions 2026.
- Implication: Stripe is not only processing checkout; it is trying to become
  the commerce interface between agents, merchants, and buyer credentials.

### 4. Three-Dimensional Timeline

Job: Show how the control plane formed over time.

This timeline is not the primary thesis. It is the historical proof layer under
the master visual.

Dimensions:

- x-axis: time from 2010 to 2026
- y-axis: signal lane
- z/semantic layer: which control point the node strengthens

Signal lanes:

- company scale and operating path
- market position and valuation/liquidity
- acquisition / capability gap
- product and API surface
- AI protocol / partner launch
- organization / JD / risk signal

Required behavior:

- draggable year control
- color by control point
- lane icons or labels for scale, acquisition, API, protocol, organization
- each node opens a concise detail drawer
- drawer states: what happened, why it matters, source strength

Key time anchors:

- 2010-2014: API, SDK, docs, test environment form the programmable payment
  entry.
- 2015-2019: Connect, Billing, Radar, Terminal and platform/SaaS customers
  expand Stripe into merchant operations.
- 2020-2022: Treasury, Capital, Identity, Tax, Issuing plus Paystack, TaxJar,
  Recko, OpenChannel, BBPOS deepen financial operations.
- 2023: $1T processed volume and AI customer pressure make billing, tax, and
  risk more central.
- 2024: usage billing, stablecoin, agent tooling, and Bridge move into the
  story.
- 2025: $1.9T volume, 1.6% GDP-equivalent framing, 5M+ businesses,
  Bridge/Privy/Metronome, claimable sandboxes.
- 2026: Copilot Checkout, Sessions 2026, Link wallets for agents, streaming
  payments, Radar token theft, HTTP 402, MPP, x402.

### 5. Market Position Dashboard

Job: Answer whether Stripe is large enough to discuss as a system-level
transaction candidate.

Reader-facing claim:

> Stripe's disclosed processing surface is large enough to analyze it as a
> serious AI transaction infrastructure candidate. The page should show growth
> and relative scale, not pretend to have an audited global market share.

Visuals:

- processed-volume line or stepped area: `$1T -> ~$1.4T -> $1.9T`
- GDP-equivalent movement: `1.0% -> 1.6%`
- peer reference bars: PayPal, Adyen, Worldpay/Global Payments where comparable
- take-rate sensitivity as an expandable drawer, not the headline

Rules:

- do not show unexplained labels like `两公司 TPV 参照`
- do not show huge sensitivity ranges as the main takeaway
- source boundary must say which figures are official self-report and which are
  secondary/peer mechanics

### 6. Acquisition Overlay

Job: Show what gaps Stripe bought or integrated to cover the control plane.

This is an overlay on the master visual, not a standalone M&A list.

Mapping:

| Move | Control point | Gap repaired |
|---|---|---|
| Paystack | settlement / local acceptance | regional payment coverage |
| TaxJar / Recko | merchant operations | tax, finance automation, reconciliation |
| BBPOS / Terminal | demand and payment surface | offline / omnichannel payment |
| Lemon Squeezy | product and merchant operations | merchant-of-record / digital goods selling |
| Bridge | settlement rail | stablecoin orchestration |
| Privy | buyer authorization | wallet abstraction |
| Metronome | pricing and metering | usage, event, token, outcome rating |

Interaction:

- toggle `Acquisitions`
- acquired capabilities light up on their control point
- detail drawer shows date/source confidence and why it matters

### 7. Source Heatmap, Not Word Cloud

Job: Make the 1000-source work visible without pretending all 1000 rows are
read conclusions.

Replace the word cloud with a matrix:

- rows: source type
  - official annual/newsroom
  - docs/API/changelog
  - jobs/JD
  - GitHub/code/community
  - partner/media/protocol
  - research/risk
- columns: the six transaction control points
- optional time filter: 2010-2022, 2023, 2024, 2025, 2026

Each cell shows:

- queued count
- read/classified count
- promoted count
- representative sources
- skip or boundary reason

Known inventory to surface:

- 1000 concrete URL rows
- 487 docs/API/changelog rows
- 292 jobs/JD rows, including 260 job detail pages
- 160 GitHub/code/community routes
- promoted source count shown separately from queue count

This section answers:

> How did the source base shape the article?

It does not answer:

> How many URLs did we collect?

### 8. What We Learn

Job: Convert Stripe analysis into a reusable framework.

Do not praise Stripe. Extract a method:

- In AI finance, look for changes in transaction objects, not only product
  names.
- Infrastructure advantage appears when one company can connect multiple
  control points.
- Acquisitions matter when they close control-plane gaps.
- Docs, APIs, sandboxes, SDKs, MCP, llms.txt, and sample repos are distribution
  surfaces in an AI-agent world.
- Market scale matters because a control-plane claim is weak without sufficient
  transaction volume.
- JD signals matter only when tied to a concrete control point and dated source.

## Visual Style

The page should feel like a strategy atlas, not a dashboard dump.

Rules:

- one dominant master diagram
- fewer standalone cards
- charts must have jobs
- color maps to control points consistently across the page
- source details live in drawers or expandable chips
- no decorative word cloud
- no nested cards
- no meta-process prose in reader-facing sections
- mobile layout keeps the master flow as a horizontally scrollable or stacked
  control-plane diagram

Suggested palette by control point:

- demand entrance: blue
- product representation: teal
- pricing and metering: amber
- authorization: violet
- settlement rail: green
- risk control: red

## Source And Boundary Model

The H5 can use source strength, but not as the main public frame.

Source states:

- queued: concrete URL collected
- read: opened and summarized
- classified: assigned to control point and signal lane
- promoted: allowed to support visible claims

Reader-visible source labels:

- official self-report
- direct docs/API
- partner release
- job signal
- secondary report
- community/code route
- research/risk lens

Boundary examples:

- Stripe annual figures are official self-report, not independent audit.
- GDP-equivalent share is not global payments market share.
- 2024 processed volume is secondary/proxy unless promoted from a stronger
  source.
- acquisition chronology from secondary compiled sources must not be treated as
  public-ready diligence.
- x402/MPP security research is a risk lens, not a Stripe-specific failure
  claim.

## Acceptance Criteria

- First screen states the AI transaction control-plane thesis.
- The master visual explains the relationship between transaction change and
  Stripe capabilities before any source inventory appears.
- BVP influence is visible in structure: thesis, trend areas, data points,
  implications, jumpable sections.
- Timeline is a historical support layer and uses time x signal lane x control
  point, not a flat event list.
- Market position appears as understandable growth and relative-scale charts,
  with formulas in drawers.
- Acquisitions are shown on the control points they repair.
- The word cloud is replaced by a source heatmap or signal matrix.
- 1000 sources are represented as a triage and promotion system, not as 1000
  conclusions.
- Reader-facing headings do not use `证据坐标`, `能力迁移地图`, `核心判断`, or
  similar internal labels.
- Every visual has one job and can be described in one sentence.
- The H5 remains an internal draft until screenshot QA, interaction QA, source
  integrity checks, and report gate review pass.

## Out Of Scope

- reading all 1000 queued sources
- Feishu sync
- public investment conclusion
- claiming audited global market share
- unrelated report-style overhaul outside this Stripe H5
- adding new data not already in source pack unless a later implementation plan
  explicitly includes source promotion

## Self-Review

Placeholder scan: no TBD/TODO placeholders.

Internal consistency: the master object is consistently the AI transaction
control plane. Evidence is support infrastructure, not the reader-facing frame.

Scope check: this is one H5 redesign. It is large but bounded to the Stripe H5,
gate review notes, and necessary visual assets.

Ambiguity check: implementation must not start from current `证据坐标` modules.
It must rebuild around the master control-plane visual, then attach timeline,
market, acquisition, and source heatmap as supporting lenses.

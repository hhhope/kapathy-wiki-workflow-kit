# Design: Stripe AI Company Evolution H5 Rewrite

## Source Of Design

Implementation follows:

- `docs/superpowers/specs/2026-06-22-stripe-h5-research-logic-redesign.md`
- user-selected visual direction A: BVP-style trend report plus
  three-dimensional timeline
- reference shape: `https://www.bvp.com/atlas/state-of-the-cloud-2024`

The H5 should learn the reference's report logic, not copy its brand identity.

## Reader Intent

Audience: internal readers evaluating Stripe's AI-era positioning, not users
debugging a source database.

Reader job:

1. Understand why AI changes Stripe's strategic surface.
2. See Stripe's company scale, market position, acquisitions, technical events,
   and AI transaction evidence in one coherent structure.
3. Extract reusable lessons for AI-era financial infrastructure strategy.

## Core Thesis

Stripe's AI-era bet is not "payments plus AI." AI changes the transaction
system itself: who initiates transactions, where demand appears, how products
are represented, how usage is priced, how payment is authorized, how settlement
happens, and where risk appears.

Stripe is positioning payment, billing, risk, wallet, stablecoin, and developer
interfaces as infrastructure for that new transaction system.

## Information Architecture

Use this reader-facing sequence:

1. Cover thesis: AI-era Stripe is competing for the transaction system entrance.
2. Five trends defining Stripe's AI transaction infrastructure path.
3. Three-dimensional timeline: time x evidence lane x proof tag.
4. Trend 1: transaction entrance moves from websites to agent surfaces.
5. Trend 2: product expression moves from pages to machine-readable catalog /
   API.
6. Trend 3: billing moves from subscription to usage / token / event.
7. Trend 4: settlement expands from card rails to wallet / stablecoin /
   machine payment.
8. Trend 5: risk expands from card fraud to token theft / tool misuse /
   resource abuse.
9. Positioning synthesis: from payment API to AI transaction infrastructure.
10. Lessons and evidence boundary.

Avoid visible headings rejected by the user, including `核心判断`, `原有能力底座`,
`市场位置计算面板`, and `公司运营、市场位置、并购与技术事件线`.

## Visual Model

### Trend Cards

Each trend uses the same fields:

- trend area
- key takeaway
- notable data points
- Stripe implication
- evidence trail

### Three-Dimensional Timeline

The timeline dimensions are:

- time: 2010, 2015, 2020, 2023, 2024, 2025, 2026
- evidence lane: company scale, market position, acquisition / capability gap,
  product / technical event, AI transaction shift, organization signal
- proof tag: the specific strategic point the event supports

Use consistent lane colors:

- scale / market: green
- acquisition / capability gap: red
- product / technical event: gold
- AI transaction shift: blue
- organization / risk: slate

### Market Position

Market position is a supporting view, not the page's main panel. It should show:

- Stripe processed-volume growth: `$1T -> ~$1.4T -> $1.9T`
- GDP-equivalent movement: `1.0% -> 1.6%`
- peer reference bands where comparable

Keep formulas, take-rate mechanics, and uncertainty notes in an evidence detail
or footnote. Do not headline unexplained sensitivity ranges.

### Acquisition Gap Map

Show acquisitions as capability gap closures:

- Paystack: local payment coverage
- TaxJar / Recko: tax and reconciliation
- BBPOS / Terminal: offline / hardware surface
- Lemon Squeezy: merchant-of-record / digital goods
- Bridge: stablecoin orchestration
- Privy: wallet abstraction
- Metronome: usage / event rating

### AI Transaction Chain

The AI transaction visual is a chain, not a timeline:

1. demand appears
2. product is represented
3. price is calculated
4. buyer is authorized
5. payment settles
6. risk moves

Each step shows old state, AI-era state, Stripe evidence, and proof boundary.

## Public Output Boundary

The H5 is an internal review draft. It must expose reader-visible citation or
source handles on load-bearing claims and must not claim to have fully read or
audited all queued sources.

The gate review artifact must record:

- reader intent and selected reference shape
- source-use model
- evidence boundary
- section drift review
- visual verification
- explicit no-Feishu-sync / no-publication status

## Verification

Before completion:

- run static grep checks for rejected headings and source-management residue
- run HTML parse or structural checks
- run `git diff --check`
- produce or refresh desktop and mobile screenshots when local browser tooling
  is available
- update gate review with verification evidence

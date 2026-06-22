# Design: Stripe Evolution Atlas H5 Refinement

## Reader Intent

The reader should leave with one answer:

> Stripe's AI-era position is best understood through its long migration from
> payment API to embedded financial infrastructure. AI raises the value of
> object models, authorization boundaries, billing design, credit/risk design,
> and ecosystem integration because coding and integration costs fall while
> design, evaluation, compliance, and accountability become more important.

## Page Architecture

1. Cover atlas: title, time spine, processed-volume line, peer reference,
   source status, and two financial relationship tracks.
2. Company evolution timeline: strategy, market, acquisition, technical product,
   AI / Agent, credit / risk, evidence.
3. Embedded-finance position: how Stripe moves from API entry to operating layer
   to accounts, cards, financing, wallets, stablecoins, and Agent workflows.
4. AI-era payment restructuring: five-layer diagram covering entrance,
   credential / entitlement, tool / API, protocol / responsibility, and the two
   base relationship lines.
5. Credit relationship line: transaction data, underwriting, limit / term /
   pricing, use case, repayment source, delinquency / dispute / risk, and
   re-evaluation.
6. Strategy validation: strategic choice -> capability accumulation -> metric /
   event evidence -> AI-era reuse.
7. Evidence boundary: promoted evidence vs classified source queue.

## Visual Rules

- Use a report-like Atlas style, not a dark technology dashboard.
- Use one restrained color system:
  - strategy: deep ink
  - market / scale: teal
  - acquisition / capability gap: amber
  - product / technical model: green
  - AI / Agent: muted violet
  - credit / risk: red
  - evidence: grayscale with solid / outline / dashed strength cues
- Every major section must have a real visual object: timeline, lane matrix,
  stack diagram, flow diagram, comparison table, or evidence drawer.
- Do not use word clouds as the main signal surface.
- Avoid headings such as `核心判断`, `原有能力底座`, `市场位置计算面板`,
  `证据坐标`, and `能力迁移地图`.

## Evidence Contract

Visible load-bearing claims need a source handle. Evidence drawer rows use:

- source_id
- source_type
- original_quote
- supports
- boundary

Required quotes:

- S172: `embedding financial services into your platform, including accounts,
  cards and financing`
- S008: `a one-time-use card is issued per task`
- S008: `you approve each payment`
- S167: `eligibility is based on factors like your payment volume and history on
  Stripe`
- S167: `Stripe deducts a fixed percentage of your sales`

## Implementation Approach

The current H5 is oversized. Do not rewrite the entire file in one step.

1. Patch the title, hero, visual CSS, and first-screen atlas.
2. Patch timeline and data arrays.
3. Patch AI system diagram, credit relationship flow, strategy validation, and
   evidence drawer.
4. Run static checks and visual smoke verification where tooling is available.

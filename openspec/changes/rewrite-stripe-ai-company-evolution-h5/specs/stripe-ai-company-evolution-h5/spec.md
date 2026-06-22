## ADDED Requirements

### Requirement: BVP-style Stripe AI H5 structure

The Stripe AI company evolution H5 SHALL present the selected BVP-style
reader-facing structure instead of a flat source-bucket report.

#### Scenario: Reader opens the rewritten H5

- **WHEN** a reader opens `wiki/reports/stripe-ai-company-evolution-h5.html`
- **THEN** the first screen states the thesis that Stripe is positioning for
  AI-era transaction infrastructure
- **AND** the page presents trend-card sections with trend area, key takeaway,
  notable data points, Stripe implication, and evidence trail
- **AND** rejected internal headings such as `核心判断`, `原有能力底座`,
  `市场位置计算面板`, and `公司运营、市场位置、并购与技术事件线` are not used as
  reader-facing section titles

### Requirement: Three-dimensional evidence timeline

The Stripe AI company evolution H5 SHALL use a timeline organized by time,
evidence lane, and proof tag.

#### Scenario: Reader reviews company and technology evolution

- **WHEN** a reader reaches the timeline section
- **THEN** events are grouped by time
- **AND** each event belongs to a visible evidence lane such as company scale,
  market position, acquisition / capability gap, product / technical event, AI
  transaction shift, or organization signal
- **AND** each event has a proof tag explaining what the event supports

### Requirement: AI transaction chain and evidence boundary

The Stripe AI company evolution H5 SHALL explain AI-era transaction change as a
transaction chain and preserve source-use boundaries.

#### Scenario: Reader reviews AI-era changes

- **WHEN** a reader reaches the AI transaction section
- **THEN** the page shows the chain from demand discovery through product
  representation, pricing, authorization, settlement, and risk movement
- **AND** each step distinguishes old state, AI-era state, Stripe evidence, and
  proof boundary
- **AND** the page does not claim that all 1000 queued sources have been fully
  read or audited
- **AND** load-bearing claims expose reader-visible source or evidence handles

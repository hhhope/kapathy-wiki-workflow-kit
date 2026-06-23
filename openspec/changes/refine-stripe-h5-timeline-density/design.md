# Design: Strategy Topology And Timeline Integrated Acquisition Nodes

## Reader Change

The reader should not encounter acquisitions as a separate list. They should see
each acquisition as a commercial action inside the timeline:

- what gap it closed
- which technical object or operating capability it added
- which later AI-era transaction or credit problem reused it

The reader should also stop seeing strategy as seven parallel product rows.
The chapter must show three relationships:

- main trunk: developer entry -> platform merchants -> revenue / financial
  operations -> agent transaction infrastructure
- horizontal capabilities: risk, global/local expansion, tax/reconciliation,
  offline hardware, issuing/wallet/credential, stablecoin/new rails
- AI cross-reuse: usage billing, wallet abstraction, restricted credentials,
  stablecoin settlement, protocol payment, and risk evidence recombine on the
  earlier trunk

## H5 Changes

1. Company timeline keeps its main heading.
2. The acquisition cards are replaced with a compact timeline / scatter visual:
   x-axis year, y-axis capability layer, color by missing capability type.
3. The strategy chapter is replaced by a strategy topology visual, not a
   four-column causal card grid.
4. The previous standalone acquisition section is removed.
5. The comprehensive view intro states the node count and coverage dimensions.
6. The `chapters` data set expands to 36 nodes:
   - company / market nodes
   - product / technical object nodes
   - acquisition / commercial-action nodes
   - credit / embedded-finance nodes
   - agent / protocol nodes
   - risk / organization nodes

## Verification

- H5 visible grep should not show the old standalone acquisition heading.
- H5 visible grep should not show `并购 / 能力补位 lane`.
- H5 visible grep should show `战略拓扑时间图`.
- H5 visible grep should show `主干递进`, `横向补位`, and `AI 复用`.
- H5 should parse.
- `git diff --check` should pass.
- Desktop and mobile screenshots should show the strategy topology and
  acquisition timeline / scatter without obvious overlap.

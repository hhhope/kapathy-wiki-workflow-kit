# Refine Stripe H5 Visual Atlas

## Why

The current Stripe H5 still exposes internal working labels, scattered evidence
blocks, and a weak visual hierarchy. The user has rejected this shape because it
does not explain Stripe's company evolution, embedded-finance path, AI-era
payment transformation, credit relationship line, entitlement/card line, MCP /
protocol line, and market/acquisition evidence as one coherent analysis.

The previous rewrite change is already complete, so this follow-up change
creates a narrow implementation boundary for the next visible H5 iteration.

## What Changes

- Rework `wiki/reports/stripe-ai-company-evolution-h5.html` into a Stripe
  Evolution Atlas:
  - company evolution from payment API to embedded payments, embedded finance,
    and Agent-workflow transaction / credit execution
  - visual first screen with time spine, processed-volume line, peer reference,
    relationship tracks, and source status
  - main timeline with lanes for strategy, market, acquisition, technical
    product, AI / Agent, credit / risk, and evidence
  - AI-era payment restructuring as a five-layer system diagram
  - standalone credit relationship flow
  - evidence drawers with source id, original quote, supported claim, and
    boundary
- Remove reader-visible working labels that sound like internal tools or
  conversational placeholders.
- Preserve internal-draft status and source-boundary wording.

## Non-Goals

- No new crawler, source collection, backend, or build system.
- No claim that all 1000 queued source rows have become 1000 read conclusions.
- No exact audited global payment-market-share claim.
- No Feishu sync or publication claim.
- No edits to unrelated visual-agent or skill-governance work.

## Impact

This changes one internal review H5 and, if needed, the related gate review
artifact. It does not alter the source queue.

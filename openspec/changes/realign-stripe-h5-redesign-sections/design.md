# Design: Stripe H5 Redesign Section Realignment

## Source Of Design

Use `docs/superpowers/specs/2026-06-22-stripe-ai-transaction-control-plane-redesign.md`
as the execution overlay for the H5 structure. OpenSpec owns this repair's
scope and task ledger.

## Drift Cause

The implementation failed at the boundary between design and OpenSpec:

1. The redesign document stated that implementation should remain stopped until
   the corrected thesis was translated into H5 design.
2. The subsequent implementation used `refine-stripe-h5-visual-atlas`, whose
   scope was visual atlas and evidence density, not chapter 4-6 realignment.
3. Verification checked keyword coverage, visual density, source references,
   and screenshot smoke, but did not check the chapter acceptance structure.

This produced a page where relevant terms appeared but the strategic argument
was compressed into cards and matrices.

## Repair Structure

Patch the current H5 in place rather than rewriting the oversized file.

1. Add a visible chapter for `哪些战略造就了 Stripe`.
   - Use a causality visual where each row reads:
     strategic choice -> capability accumulation -> later product / acquisition
     -> AI-era reuse.
   - Include developer entry, platform merchants, revenue operations, risk
     infrastructure, global/local gap fill, issuing / wallet / entitlement
     entry, and new financial rails.

2. Add a visible chapter for `Stripe 为什么坚持做难事：API、规范和领域模型`.
   - Explain that standardization is commercial strategy, not engineering
     cleanliness.
   - Show the hard work and commercial meaning: domain model, API/docs/test
     mode, merchant operation abstraction, embedded risk/compliance, issuing
     / entitlement entry, and new rails.

3. Rebuild the AI-era payment chapter around the redesign's subsections:
   - infrastructure pressure
   - transaction relationship and credit relationship
   - entitlement / card / tokenized credential entry
   - MCP / skills / sandbox / API tooling
   - AP2 / ACP / MPP / x402 protocol accountability
   - return to Stripe's company path

4. Keep evidence boundaries visible.
   - The H5 remains an internal draft.
   - Product and partner releases prove direction and mechanism, not market
     maturity.
   - The source queue remains triage, not fully read proof.

## Verification

- Static grep must find the required chapter headings and subsection labels.
- Static grep must confirm rejected visual labels do not reappear.
- HTML parser must accept the H5.
- `git diff --check` must pass for scoped files.
- Report gate review must record this repair and any limitations.
- Frontmatter precheck should be run for the new retro; legacy global blockers
  may remain as explicit residual risk.

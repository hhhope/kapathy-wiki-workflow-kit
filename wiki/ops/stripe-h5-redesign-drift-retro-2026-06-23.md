---
layer: ops
domain: ai-workflow
ops_area: report-quality
canonical_object: stripe-h5-redesign-drift
artifact_type: retro
title: "Stripe H5 redesign drift retro"
status: draft
created: 2026-06-23
---

# Stripe H5 Redesign Drift Retro

## What Happened

The Stripe H5 had a clear redesign document:
`docs/superpowers/specs/2026-06-22-stripe-ai-transaction-control-plane-redesign.md`.
That document said the visible H5 should explain Stripe as a company evolution
case, then specifically restore:

1. strategic causality: strategic choice -> capability accumulation -> later
   product / acquisition -> AI-era reuse
2. why Stripe keeps doing hard work: APIs, domain objects, docs, tests,
   protocols, risk, tax, and compliance
3. AI-era payment restructuring: infrastructure pressure, transaction and
   credit relationship lines, entitlement / credential entry, MCP / skills,
   protocol accountability, and return to Stripe's company path

The later implementation instead followed `refine-stripe-h5-visual-atlas`,
which was narrower. It improved the atlas surface, first-screen composition,
source handles, timeline density, and visual smoke evidence, but it did not
make the redesign document the acceptance structure for chapters 4-6.

## Direct Cause

The implementation boundary was wrong.

- The Superpowers redesign was treated as supporting material.
- The OpenSpec change in force was about visual atlas refinement, not section
  realignment.
- Verification checked that many keywords existed, but did not verify that the
  required chapter sequence existed as reader-facing structure.
- The page therefore contained `交易关系`, `信用关系`, `Issuing`, `MCP`, `x402`,
  `Bridge`, `Privy`, and related terms, while still compressing the argument
  into cards, matrices, and generic atlas blocks.

## Contributing Factors

- Multiple Stripe OpenSpec changes were active or recent, and their boundaries
  looked adjacent.
- The existing re-anchor page already said implementation should remain
  stopped, but that stop condition was not replayed before editing.
- The H5 file is oversized, which encouraged patching visible modules instead
  of first checking the reader path.
- The report gate review recorded visual and source-reference checks, but not a
  specific chapter-structure acceptance check for the latest redesign.

## Corrective Action

Create a dedicated OpenSpec repair:
`openspec/changes/realign-stripe-h5-redesign-sections/`.

This repair must only:

- record the drift cause and boundary
- add the missing strategic causality chapter
- add the missing hard-work / domain-model chapter
- rebuild the AI-era payment chapter around the redesign's subsections
- update the gate review and verification evidence

It must not claim Feishu sync, public release, completed 1000-source reading, or
archive readiness.

## Replay Check

Future agent situation:

> A Superpowers redesign exists, but an OpenSpec change with a narrower visual
> or density scope is also present.

Expected behavior:

1. Open the redesign and the active OpenSpec change.
2. Compare acceptance structures before editing.
3. If the active change does not own the redesign acceptance, create or select
   a new OpenSpec repair.
4. Verify chapter structure directly, not only keyword presence or screenshots.

This replay should stop the exact failure mode from recurring: keyword
coverage must not be accepted as structure coverage.

## Current Proof Boundary

This retro records the local drift and the repair path for this Stripe H5. It
does not change repo-wide behavior rules, skills, or global instructions.

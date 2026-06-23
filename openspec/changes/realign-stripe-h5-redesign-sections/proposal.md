# Realign Stripe H5 Redesign Sections

## Why

The Stripe H5 drifted after a clear Superpowers redesign was written. The
current page contains many relevant keywords, but it does not preserve the
approved reader path for chapters 4-6:

- strategic causality: strategic choice -> capability accumulation -> later
  product / acquisition -> AI-era reuse
- the hard-work explanation: APIs, domain objects, docs, test mode, risk,
  tax, compliance, and protocols as business strategy
- AI-era payment restructuring: infrastructure pressure, transaction and
  credit relationship lines, entitlement / credential entry, MCP / skills,
  protocol accountability, and return to Stripe's company path

The drift happened because a narrow visual-atlas OpenSpec change was used as
the implementation boundary while the redesign spec was treated as supporting
material instead of acceptance structure.

## What Changes

- Record the cause analysis and replay in a repo-visible `wiki/ops` retro.
- Realign `wiki/reports/stripe-ai-company-evolution-h5.html` with the
  redesign's chapter 4-6 structure.
- Update the report gate review with drift cause, repair boundary, and
  verification notes.
- Keep the repair scoped to the Stripe H5 and its quality evidence.

## Non-Goals

- No Feishu sync, publication, or review-ready claim.
- No new source collection or claim that the 1000-source queue is fully read.
- No broad rewrite of the whole H5 beyond the drifted chapter structure.
- No edits to repo workflow rules, skills, AGENTS.md, or unrelated reports.
- No archive of earlier Stripe changes.

## Impact

This repair changes one internal H5 draft, one report gate review, one drift
retro, and this OpenSpec change ledger. It does not change the source queue or
repo-level behavior assets.

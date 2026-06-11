---
name: product-discovery-wiki-capture
description: Use when PM or product-discovery analysis has explicit wiki, durable-memory, reuse, follow-up, or missing-capture repair intent.
---

# Product Discovery Wiki Capture

## Purpose

Bridge PM/product-discovery work into repo-visible wiki memory when the user
expects durable capture. This skill does not replace PM plugins; it governs the
repo-local output boundary after or alongside those plugins.

## When To Use

Use this skill when PM/product-discovery analysis has one of these signals:

- explicit wiki recording intent
- durable memory or "record this" intent
- reuse in a later PRD, report, OpenSpec change, product strategy, or product
  discovery thread
- the user corrects a prior PM/product-discovery answer as missing wiki capture

## Output Target

Default durable output is `wiki/ops/` because the record usually preserves
working assumptions, opportunity framing, validation plans, and next actions.

Use the repo wiki frontmatter taxonomy gate before creating or editing wiki
frontmatter.

## Minimum Capture Fields

- source prompt or situation
- PM/product-discovery route used
- target segment or ICP
- opportunity framing
- assumptions and risks
- validation experiments
- what was not formalized
- next step

## Parent Gates

- External articles, repos, papers, READMEs, or examples still route through
  `learning-capture` for source learning and grounding.
- Reader-facing reports, Feishu drafts, H5/share pages, README, docs, examples,
  or published templates still route through `public-report-quality-gate`.
- Wiki frontmatter creation or edits still route through
  `wiki-frontmatter-taxonomy`.
- OpenSpec-governed workflow repairs still require OpenSpec before semantic
  skill or routing edits.

## Non-Triggers

- one-off PM/product-discovery answers with no wiki, durable-memory, reuse, or
  follow-up intent.
- Latest-news lookup or raw market fact lookup with no local reuse intent.
- Source learning where the only durable artifact should be a source-learning
  note.

Do not create durable wiki output by default for those cases.

## Common Mistakes

- Editing a third-party plugin cache instead of adding repo-local routing.
- Treating every PM analysis as wiki-worthy.
- Letting product-discovery capture replace source grounding, public-output
  gates, frontmatter taxonomy, or OpenSpec lifecycle gates.

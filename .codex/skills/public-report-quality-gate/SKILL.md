---
name: public-report-quality-gate
description: Use when the user asks to write, polish, review, sync, or prepare reader-facing reports, Feishu review drafts, H5/share drafts, public materials, or reference-shaped outputs for an audience outside the current chat or worklog.
---

# Public Report Quality Gate

## Overview

Gate reader-facing output before it becomes a Feishu draft, report, H5, or
shareable material. Internal wiki notes are not public-ready by default.

## When To Use

Use this skill when the request involves:

- public reports, executive summaries, share drafts, H5 pages, or Feishu review
  drafts
- rewriting internal wiki/ops material for readers
- using an article, Feishu page, visual example, or prior report as an output
  reference
- claiming a draft is ready for review, sync, publish, or external reading

Do not use this skill for raw source capture, private scratch notes, or code
implementation reports unless the user asks for a reader-facing deliverable.

## Hard Rules

- Do not publish, sync to Feishu, or claim review-ready when any hard gate fails.
- Before Feishu sync or a review-ready claim, create or update a repo-visible
  `wiki/ops/*-report-gate-review.md` artifact.
- When a reference artifact is provided, write or state the reference structure
  map before drafting.
- When content spans multiple reader jobs, choose a split strategy before
  writing a single long draft.
- Treat voice quality as a hard gate, not a small style score.
- Preserve the core narrative. If the stated story changes, stop and re-anchor.
- State what each diagram or visual carries; do not add decorative diagrams.
- Keep source reading, learning capture, visual generation, Feishu operations,
  and final verification under their own skills.

## Load

- Scorecard and hard gates: `references/scorecard.md`
- Gate review artifact contract: `references/gate-review-artifact.md`
- Report group templates and split routing: `references/report-group-templates.md`
- Validation scenarios: `references/pressure-scenarios.md`

## Common Mistakes

- Turning a wiki ops note into a Feishu draft without rewriting for readers
- Copying a reference page's section labels without mapping its structure
- Packing overview, runtime, migration, validation, and roadmap into one page
- Using slogans such as "X = manages Y" instead of explaining the evolution
- Letting repo paths, OpenSpec details, or agent workflow leak into public text

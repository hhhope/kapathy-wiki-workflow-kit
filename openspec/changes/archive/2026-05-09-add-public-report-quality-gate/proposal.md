## Why

Reader-facing materials are now a recurring output path: the user asks for
Feishu review drafts, public reports, H5 pages, and reference-shaped documents
based on internal wiki material and external examples.

The current repository has material-processing and learning-capture skills, but
it does not have a gate that stops an internal wiki note from being published as
a reader-facing report. The latest account knowledge-base review draft exposed
the gap:

- the Feishu reference group was not mapped before writing
- one article carried overview, runtime, migration, validation, and roadmap
  content instead of being split
- chat-like wording and internal operational phrasing leaked into the draft
- the core story `lore -> team-lore -> wiki` drifted from an evolution path into
  a static responsibility table

## What Changes

- Add a repo-local `public-report-quality-gate` skill for reader-facing reports,
  Feishu review drafts, H5/share drafts, and reference-driven public materials.
- Add scorecard, template routing, and pressure-scenario references for the
  skill.
- Add the skill to repo `AGENTS.md` high-frequency routing.
- Require hard gates for reference mapping, split strategy, voice quality,
  narrative consistency, visual intent, and publish readiness.
- Record RED/GREEN evidence in `evaluation.md`.

## Impact

- Updates repo `AGENTS.md`.
- Adds `.codex/skills/public-report-quality-gate/`.
- Adds a spec for `public-report-quality-gate`.
- Does not rewrite `wiki/ops/account-knowledge-base-workbench.md`.
- Does not create or update a Feishu document.
- Does not replace `material-collaboration-defaults`, `learning-capture`,
  visual/H5 skills, or Lark document skills; it gates their reader-facing
  output path.

# Design

## Entry Boundary

`AGENTS.md` owns the compact entry rule:

Before acting, classify the user intent. If the request writes, rewrites,
polishes, prepares, or updates an artifact that will be read outside the current
chat or worklog, route through the applicable parent gate before editing.

## Parent Gate Boundary

Agent Intent Routing only chooses the parent gate. It does not replace
specialized gates.

Minimum map:

- repo-public artifact -> `public-report-quality-gate` lightweight path
- reader-facing report / Feishu draft / H5 / share page ->
  `public-report-quality-gate` full path
- external article / repo / README used for learning -> `learning-capture`
- semantic skill edit -> skill authoring contract
- wiki frontmatter edit -> wiki frontmatter taxonomy gate

## Public Gate Lightweight Path

`public-report-quality-gate` continues to own reader-facing and public material
quality. A repo-public artifact enters a lightweight path that requires:

- reader and job-to-be-done identification
- artifact-specific constraint scan before drafting
- no accidental internal residue
- fresh verification before completion, review-ready, publish, or sync claims

The lightweight path does not require a `wiki/ops/*-report-gate-review.md`
artifact by default for small repo-public documentation edits.

## README Constraint Scan

For README work, the artifact-specific scan checks README-related constraints in:

- `AGENTS.md`
- `PROJECT.md`
- `openspec/specs`
- `.codex/skills`
- `wiki/adr`
- `wiki/ops`

The scan is relevance-filtered. It does not require opening every unrelated
README mention.

## Proof Boundary

Tests and evaluation evidence prove repo-visible routing text and pressure
scenario coverage. They do not prove every future AI client will load the
correct skill unless that client honors repo `AGENTS.md` and skill routing.

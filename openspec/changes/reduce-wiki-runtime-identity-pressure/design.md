# Design: Reduce Wiki Runtime Identity Pressure

## Goal

Move stable, explicitly named runtime evidence from `warnings` into graph nodes
so downstream runtime surfaces can reason over structure instead of treating
the same pages as unresolved noise.

## Resolver Policy

Use only explicit structural signals:

- `openspec/specs/<canonical-object>/spec.md` maps to
  `<canonical-object> / spec`.
- Known LLM Wiki runtime ADR filenames map to their named runtime object and
  artifact type `adr`.
- Existing frontmatter remains the highest-priority source of identity.

This avoids adding frontmatter to OpenSpec specs, which are owned by OpenSpec
format expectations, and avoids deriving identities from arbitrary prose.

## Targeted Wiki Metadata

Add frontmatter to `wiki/ops/agent-readable-wiki-graph-extraction.md` because it
is a core runtime method page and is already listed as a governance entry in
`wiki/index.md`.

## Boundaries

- Do not batch-migrate unrelated intake, report, source, or example pages.
- Do not infer identities for arbitrary ADRs or ops pages from prose.
- Do not alter scoring formulas.
- Do not change command behavior beyond better graph inputs.

## Verification

- Unit tests cover spec-path identity and runtime ADR identity resolution.
- Live graph extraction must show warning count below the current 91 baseline.
- Existing graph/scorecard/queue tests must still pass.

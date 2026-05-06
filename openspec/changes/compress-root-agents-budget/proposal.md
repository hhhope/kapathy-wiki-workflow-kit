## Why

The archived `compress-codex-agents-md` change proved that
`~/.codex/AGENTS.md` now matches the Root AGENTS Pattern Catalog, but it also
recorded a budget failure: the file ended at 283 lines, above the 150-200
instruction budget target.

That archive explicitly deferred line-count compression to a successor change
and named two safe compression vectors:

- consolidate `Execution discipline` and `Git discipline`
- extract the `Global Rule Routing` table into a separate root reference file

This change is that successor. It is budget governance for the already-adopted
root model, not a new behavior-asset model.

## What Changes

- Refactor only personal root Codex guidance under `~/.codex/`.
- Keep `~/.codex/AGENTS.md` as the global entrance card and safety floor.
- Move the detailed Global Rule Routing table out of `AGENTS.md` into a
  root-local reference file such as `~/.codex/rule-routing.md`.
- Consolidate duplicated execution/git discipline wording while preserving the
  hard stops, dirty-tree handling, commit discipline, branch boundary, and git
  truth-source checks.
- Record before/after line counts, section mapping, and self-check evidence in
  `evaluation.md`.

## Capabilities

### Modified Capabilities

- `root-governance-alignment`: extend the existing root compression scenario
  from Pattern Catalog compliance to instruction-budget compression.

## Impact

- Edits `~/.codex/AGENTS.md`.
- May add or edit one root-local support file under `~/.codex/` for extracted
  routing detail.
- Does not edit repo `AGENTS.md`, repo `.codex/skills/`, repo `wiki/`, repo
  `rules/`, or `~/.claude/CLAUDE.md`.
- Does not reopen `compress-codex-agents-md` or add new Pattern Catalog fields.

## Out of Scope

- Solving deferred rows from the archived routing table such as S1, S5, A5,
  Q1, Q2, or Q4.
- Adding read-only or UI operation types to the root self-check checklist.
- Creating or changing skills.
- Creating new repo workflow policy, ADRs, wiki method pages, or Pattern
  Catalog entries.

## Why

The archived `compress-codex-agents-md` change proved that
`~/.codex/AGENTS.md` now matches the Root AGENTS Pattern Catalog, but it did not
prove that the root context reduces agent drift.

The first successor plan drifted toward single-file line-count compression:
move `Global Rule Routing` into `~/.codex/rule-routing.md` and then ask root
`AGENTS.md` to load that file for non-trivial work. That would reduce
`AGENTS.md` line count without proving a reduction in loaded context.

This change corrects the successor scope. It governs root context as an
agent-legible map: short enough to avoid drift, structured enough to route the
agent to the right source of record, and testable enough to prove that moved
content is not hidden default context.

## What Changes

- Refactor only personal root Codex guidance under `~/.codex/`, after the
  evidence gate is corrected.
- Keep `~/.codex/AGENTS.md` as the global entrance card and safety floor.
- Treat line count as supporting evidence only.
- Add loaded-context evidence: default loaded context, triggered loaded
  context, and whether a moved reference still sits on the default path.
- Add a RED/GREEN harness scenario that fails file-moving without progressive
  loading.
- Add agent-legibility evidence: the next agent can identify where to read,
  how to verify, and what artifact preserves recovery after interruption.
- Require every adopted best practice to cite a verifiable evidence shape:
  external documentation excerpt, local demo/fixture, or git-like project
  comparison.
- Consolidate duplicated execution/git discipline wording only if it preserves
  hard stops, dirty-tree handling, commit discipline, branch boundary, and git
  truth-source checks.

## Capabilities

### Modified Capabilities

- `root-governance-alignment`: extend the existing root compression scenario
  from Pattern Catalog compliance to agent-legible progressive context
  governance.

## Impact

- May edit `~/.codex/AGENTS.md` after evidence is updated.
- May add or edit one root-local support file under `~/.codex/` only if it is
  trigger-gated and does not remain on the default loaded path.
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
- Treating a file move as success when the moved file is still loaded by
  default.
- Building a new harness, checker, skill, or workflow system in this change.
- Promoting article-derived advice into root behavior without quantifiable or
  reproducible evidence.

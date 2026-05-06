## Why

`~/.codex/AGENTS.md` has grown from 223 to 281 lines (+26%) between 2026-04-01 and 2026-04-25 and has stayed at 281 lines since. It is the personal global Codex entrance card shared across every repository on this machine; per the now-adopted Principle 4 (instruction budget is finite), every line in it taxes every repository.

The `decide-root-governance-alignment` change (archived 2026-05-06) adopted the Pattern Catalog, the six-step minimum process, and the Issue Routing Table that classifies 18 concrete findings (C1–C3 / S1–S5 / A1–A5 / M1–M5) against the file. Eleven of those rows are labeled `candidate-root-edit` — they are the mechanical compression work this change performs. The remaining rows are `defer-change`, `accept-as-divergence`, or `reject-claim` and stay out of scope.

This is the "use the rules" change that the adopted model was meant to enable. It does not propose new governance; it applies the existing governance to one file.

## What Changes

- Apply the 11 `candidate-root-edit` rows from the adopted Issue Routing Table to `~/.codex/AGENTS.md`:
  C1 (team-lore path), C2 (OpenSpec archive-review detail inlined), C3 (WSL hard-coded path), S2 (wording), S4 (precedence coverage), A2 (technical checkpoints consolidation), M1 (backup residue), M2 (`task-related` vs `local junk` definition), M3 (large-file guardrail language list), M4 (single-entry `Paths` section), M5 (self-check read-only / UI types).
- Record before/after line count and a layer-breakdown of the compressed file (how many lines are Root-layer content vs Repo-ish residue vs Rule-ish residue).
- Produce `evaluation.md` with before/after evidence and residual risks.
- Validate the compressed file against the Pattern Catalog Root AGENTS entry (Purpose / Owns / Must Not Own / Anti-patterns).

## Capabilities

### Modified Capabilities

- `root-governance-alignment`: apply the adopted model to the personal global Codex entrance card.

## Impact

- Edits `~/.codex/AGENTS.md` (personal global dotfile). This is the first change in the governance thread that touches the file.
- Does not edit repo `AGENTS.md`, `rules/`, `skills/`, or wiki method pages.
- Does not touch `decide-no-repo-local-commit-hook` or `phase1-repo-agents-compression` scope.
- Expected outcome: line count drops from 281 to a reviewed target; every remaining line is justified under the Root AGENTS pattern.

## Out of Scope

- `~/.claude/CLAUDE.md` edits (claude-side symmetry — deferred per task 2.7 of the archived change).
- Repo `AGENTS.md` compression (parked in `phase1-repo-agents-compression`).
- Creating new Pattern Catalog patterns or adding checklist items (§13 anti-drift rule continues to bind).
- `defer-change` rows from the routing table (S1, S5, A5, Q1, Q2, Q4) — each opens its own change when prioritized.

# Archive Review

Decision: closed without implementation.

## Evidence

- Source trace `wiki/ops/wiki-status-slash-command-reanchor.md` asked whether
  `/wiki:status` should replace `/report-wiki-portfolio:wiki-status`.
- Later runtime direction superseded slash-style wiki commands:
  - `README.md` says the current wiki runtime is the repo-local skill surface.
  - `tests/test_wiki_status_command.py` rejects `/wiki:status` in the
    `wiki-status` skill.
  - `tests/test_wiki_runtime_skills.py` rejects slash command references in
    active runtime docs and wiki skills.
  - `openspec/specs/wiki-status-skill/spec.md` defines the active status
    entrypoint as `.codex/skills/wiki-status/SKILL.md`.
- User approved closing this follow-up directly on 2026-05-18.

## Decision

Do not implement `/wiki:status` from this change.

The active runtime remains the repo-local `$wiki-status` skill surface. This
change is archived as a rejected/superseded follow-up so it no longer appears as
active implementation work.

## Boundary

- No command, skill, runtime script, README, ADR, or spec behavior is changed by
  this close-out.
- No OpenSpec spec delta from this change is promoted into `openspec/specs/`.
- Existing status-only boundaries remain owned by `wiki-status-surface`,
  `wiki-status-skill`, and the repo-local `wiki-status` skill.

## Residual Risk

Historical archive records still mention earlier slash-command experiments.
Those records are history, not the current active runtime surface.

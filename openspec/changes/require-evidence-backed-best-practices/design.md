## Design Boundary

Target layer: repo `AGENTS.md` plus the existing
`example-driven-wiki-capture` OpenSpec capability.

This change adds a promotion gate for reusable learning. It does not create a
new skill, wiki method page, root dotfile rule, replay harness, or automation.

## Decision

Example-driven learning may be captured as candidate knowledge, but it must not
be promoted into behavior assets unless one accepted evidence shape is recorded:

- external-document excerpt with URL and exact section or line reference
- local demo or fixture with RED/GREEN, input/output, and command or manual
  replay record
- git-like project comparison with repository, commit or path, and observable
  structure or behavior difference

The landing layer is repo `AGENTS.md` because the rule must apply before a
trigger-specific skill is selected. The spec delta updates
`example-driven-wiki-capture` because that capability already owns capture and
adaptation-boundary behavior.

## Non-Goals

- No root `~/.codex/AGENTS.md` edits.
- No repo-local or global skill edits.
- No new wiki method page.
- No new evidence checker, replay harness, or automation.
- No broad rewrite of example-driven capture behavior beyond promotion gating.

## Evidence Plan

`evaluation.md` records baseline behavior, after behavior, self-check result,
and residual risk. `tasks.md` records that the repo `AGENTS.md` gate exists,
the accepted evidence shapes are exact, and OpenSpec validation passed.

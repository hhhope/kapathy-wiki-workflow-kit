# Archive Review: add-wiki-status-slash-command

Review date: 2026-05-09

## Decision

Archive-ready only as part of the ordered wiki status command chain, after this
note and normal spec sync.

This change is not archive-ready as a standalone final contract because its
delta spec captured the first, rejected command surface: a Claude-only
`/wiki:status` command. Later changes replaced that with a repo-local Codex
plugin command, renamed the user-facing namespace back to `/wiki:status`, and
added marketplace install metadata.

## Evidence

- `tasks.md` is fully complete.
- `evaluation.md` records RED/GREEN evidence for the original command
  implementation.
- `openspec validate add-wiki-status-slash-command --strict` passed during the
  original implementation and again during archive readiness review.
- Git history shows this change was superseded by:
  - `replace-claude-wiki-status-with-codex-plugin-command`
  - `rename-wiki-status-command-namespace`
  - `add-repo-plugin-marketplace-install-path`

## Proof Boundary

The implementation evidence is real, but the final product contract must not
preserve the obsolete Claude-only command surface as the accepted mainline
state. The accepted contract should come from the later ordered chain:

1. repo-local Codex plugin packaging
2. `/wiki:status` as the user-facing command
3. repo marketplace install path

## Next Action

When archiving, process the wiki status command changes in chronological order
and let the later deltas settle the final canonical spec. Do not archive this
change alone as the final command contract.

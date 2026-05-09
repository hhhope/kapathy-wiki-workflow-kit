# Rename Wiki Status Command Namespace

## Why

The repo-level Codex command was corrected into plugin packaging, but its
documented invocation overfit the repository/plugin identifier:
`/report-wiki-portfolio:wiki-status`. The product-facing command should use the
short wiki capability namespace that matches the existing command style:
`/wiki:status`.

## What Changes

- Rename the wiki status command contract to `/wiki:status`.
- Preserve the repo-published Codex plugin packaging:
  - `.codex-plugin/plugin.json`
  - `commands/wiki-status.md`
- Update tests and spec evidence so the old long command name is rejected.

## Impact

- Users see and discuss the command as `/wiki:status`.
- The command remains a thin wrapper around `scripts/build_wiki_status.py`.
- Query, scorecard, graph UI, and change queue remain out of scope.

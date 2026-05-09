# Replace Claude Wiki Status With Codex Plugin Command

## Why

The previous wiki status slash-command implementation created a Claude command
at `.claude/commands/wiki/status.md`. That does not satisfy the product need:
the command should be a repo-level Codex capability that can ship with this
repository and be reused by other users.

## What Changes

- Add a repo-root Codex plugin manifest at `.codex-plugin/plugin.json`.
- Add a Codex plugin command at `commands/wiki-status.md`.
- Remove the Claude-only wiki status command.
- Keep the command focused on refreshing and summarizing generated wiki status
  artifacts.

## Impact

- Users should invoke the repo-level command as
  `/report-wiki-portfolio:wiki-status` after the repo plugin is available to
  their Codex environment.
- The command remains a thin wrapper around `scripts/build_wiki_status.py`.
- Query, scorecard, graph UI, and change queue remain out of scope.

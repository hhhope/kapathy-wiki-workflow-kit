## Why

The repository now has a repeatable wiki status generator, but using it still
requires remembering the exact script path. The user asked to expose it as a
slash command so an agent can refresh and read the status surface directly.

## What Changes

- Add a Claude slash command for wiki status refresh.
- Keep the command as a thin wrapper around `python3 scripts/build_wiki_status.py`.
- Add tests that verify the command points to the generator and generated
  artifacts.
- Do not add query, scorecard, graph, or change queue behavior.

## Impact

- Adds `.claude/commands/wiki/status.md`.
- Adds `tests/test_wiki_status_command.py`.
- Adds OpenSpec coverage for the command.
- Does not stage or alter existing untracked `.claude/commands/opsx/*` files.

# Design

## Decision

Keep the repo-local Codex plugin packaging, but use the product capability
namespace as the user-facing command name:

```text
/wiki:status
```

This mirrors existing local command naming such as `/opsx:apply`, where the
namespace is the capability/product surface, not the repository directory name.

## Files

- `commands/wiki-status.md`: document `/wiki:status`.
- `tests/test_wiki_status_command.py`: require `/wiki:status` and reject the
  previous long command spelling.
- `openspec/changes/rename-wiki-status-command-namespace/specs/wiki-status-slash-command/spec.md`:
  update the command contract.

## Boundary

This is a naming correction only. It does not change the generated wiki status
artifacts, the status generator, or the backlog items for query, scorecard,
graph UI, and change queue.

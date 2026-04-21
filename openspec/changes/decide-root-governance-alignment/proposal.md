## Why

Even after repo-local cleanup, `agents-governance-drift` cannot be treated as
fully closed while the relationship between:

- repo `AGENTS.md`
- root `~/.codex/AGENTS.md`
- root `~/.claude/CLAUDE.md`

remains undefined.

The repository needs an explicit decision about whether those root-level files
should align with the repo mainline, intentionally diverge, or partially sync.

## What Changes

- Define the accepted relationship between repo governance and root dotfiles.
- Record which parts must align and which parts may intentionally diverge.
- If needed, make the minimum root-level wording updates to match the accepted
  relationship.

## Capabilities

### New Capabilities

- `root-governance-alignment`: The repository SHALL explicitly decide the
  relationship between repo-level governance and root dotfile governance before
  treating `agents-governance-drift` as fully closed.

### Modified Capabilities

- `repo-agents-governance-phase0`

## Impact

- Adds OpenSpec artifacts under
  `openspec/changes/decide-root-governance-alignment/`.
- Creates the decision boundary for repo-vs-root governance drift.

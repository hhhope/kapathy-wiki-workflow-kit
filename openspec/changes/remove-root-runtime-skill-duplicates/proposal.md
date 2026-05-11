# Remove Root Runtime Skill Duplicates

## Why

The supported runtime skill source for this repository is `.codex/skills`.
Root/user-scope copies of the same `wiki-*` and `openspec-*` skills create two
visible entries. The old repo plugin marketplace metadata and plugin skill
copies also reintroduce the obsolete `report-wiki-portfolio:*` namespace.

## What Changes

- Remove root/user-scope duplicates for this repo's `wiki-*` and `openspec-*`
  skills.
- Remove repo plugin marketplace metadata and plugin skill copies for this
  runtime surface.
- Keep repo-local `.codex/skills/wiki-*` and `.codex/skills/openspec-*` as the
  only supported source.
- Update README, specs, and tests to block reintroducing root/user-scope
  duplicates.

## Impact

- Affects local user-scope skill state, obsolete plugin metadata/source copies,
  and repo guidance/tests.
- Does not remove or alter repo-local skill bodies.

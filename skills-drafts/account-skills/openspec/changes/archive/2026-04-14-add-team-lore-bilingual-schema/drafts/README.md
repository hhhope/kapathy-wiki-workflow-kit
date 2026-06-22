# Draft Migrations — team-lore first rollout slice

These files are draft rewrites for the first rollout slice of the `team-lore` agent-memory contract.

They are intentionally stored in the current repository instead of being written directly to `/mnt/d/team-lore/wiki`, because team lore should not be edited directly from this workflow without explicit approval.

## Scope of this draft set

- `wiki/index.md`
- `projects/account-skills/overview.md`
- `projects/account-team-efficiency/overview.md`
- `pitfalls/admin-scope-ui-backend-drift.md`
- `principles/explicit-team-selection-for-platform-admin.md`

## What changed in the drafts

Each draft applies the retrieval-first contract:

- `Scope`
- `Aliases`
- `Applies When`
- `Not For`
- `Top Facts` or `Top Checks`
- `Watchpoints`
- `Load Next` where applicable
- longer explanation pushed into `Notes`

## Review intent

These drafts should be reviewed for:

1. whether the first screen is cheap enough for an arbitrary agent to load
2. whether page boundaries are clearer than the current pages
3. whether the next-hop guidance is explicit enough
4. whether the current minimal mixed-language routing support is enough for the first rollout slice

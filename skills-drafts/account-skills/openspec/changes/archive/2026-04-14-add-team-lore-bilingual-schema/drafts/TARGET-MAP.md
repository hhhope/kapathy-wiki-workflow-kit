# Target Map — first rollout slice

Date: 2026-04-13
Change: `add-team-lore-bilingual-schema`

This file maps each draft and patch artifact to the corresponding target page in `/mnt/d/team-lore/wiki`.

## Draft to target mapping

| Draft artifact | Target page in team lore | Patch artifact |
|---|---|---|
| `drafts/wiki/index.md` | `/mnt/d/team-lore/wiki/index.md` | `patches/wiki-index.patch` |
| `drafts/projects/account-skills/overview.md` | `/mnt/d/team-lore/wiki/projects/account-skills/overview.md` | `patches/project-account-skills-overview.patch` |
| `drafts/projects/account-team-efficiency/overview.md` | `/mnt/d/team-lore/wiki/projects/account-team-efficiency/overview.md` | `patches/project-account-team-efficiency-overview.patch` |
| `drafts/pitfalls/admin-scope-ui-backend-drift.md` | `/mnt/d/team-lore/wiki/pitfalls/admin-scope-ui-backend-drift.md` | `patches/pitfall-admin-scope-ui-backend-drift.patch` |
| `drafts/principles/explicit-team-selection-for-platform-admin.md` | `/mnt/d/team-lore/wiki/principles/explicit-team-selection-for-platform-admin.md` | `patches/principle-explicit-team-selection-for-platform-admin.patch` |

## Why these five pages

- `index.md` is the shared entry surface.
- The two project overview pages are the most likely first-hop startup pages.
- The selected pitfall and principle are high-frequency pages for the platform-admin scope problem that repeatedly showed up in the RED scenarios.

## Sync rule

This package is intentionally migration-ready but not self-applying. The source repository should not write directly to `/mnt/d/team-lore/wiki` from this workflow.

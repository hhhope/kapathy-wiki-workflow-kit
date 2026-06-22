# Sync Checklist — first rollout slice

Date: 2026-04-13
Change: `add-team-lore-bilingual-schema`

Use this checklist when applying the first rollout slice into `/mnt/d/team-lore/wiki`.

## Before sync

- Confirm the target repository is the intended team lore repo.
- Confirm the target pages still exist at the paths listed in `TARGET-MAP.md`.
- Review the corresponding patch file for each page before applying it.
- Do not batch unrelated wiki cleanup into the same sync.

## Apply

- Apply `patches/wiki-index.patch` to `wiki/index.md`.
- Apply `patches/project-account-skills-overview.patch` to `projects/account-skills/overview.md`.
- Apply `patches/project-account-team-efficiency-overview.patch` to `projects/account-team-efficiency/overview.md`.
- Apply `patches/pitfall-admin-scope-ui-backend-drift.patch` to `pitfalls/admin-scope-ui-backend-drift.md`.
- Apply `patches/principle-explicit-team-selection-for-platform-admin.patch` to `principles/explicit-team-selection-for-platform-admin.md`.

## Verify after sync

- Each synced page exposes a retrieval-first first screen:
  - `Scope`
  - `Aliases`
  - `Applies When`
  - `Not For`
  - `Top Facts` or `Top Checks`
  - `Watchpoints`
  - `Load Next` when navigation is needed
- `index.md` remains thin and still points to the correct project/pitfall/principle pages.
- The two project overview pages can still route a fresh agent to the next likely page in `1-2` hops.
- The pitfall page still exposes the first diagnostic checks without requiring narrative mining.
- The principle page remains stable and does not absorb project-specific implementation detail.

## Re-run evidence

- Re-run the section-shape check or equivalent structure validation on the synced pages.
- Re-run the fresh-context scenarios against the synced pages, not only against the drafts.
- Keep the mixed-language judgment honest: alias support may move routing to `Pass`, but first-load interpretation can still remain `Partial`.

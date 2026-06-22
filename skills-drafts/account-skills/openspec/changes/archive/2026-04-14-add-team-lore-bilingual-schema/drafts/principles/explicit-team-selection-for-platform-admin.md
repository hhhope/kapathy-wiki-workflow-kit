---
tags: [lore/principle]
principle: explicit-team-selection-for-platform-admin
---

# Principle — explicit-team-selection-for-platform-admin

## Rule
Platform admin is a real authenticated role, but not an implicit business-team member. Authenticate first, then require explicit team selection whenever a business read or write targets team-owned data.

## Aliases
- 平台管理员显式选团队
- 平台管理显式 team 选择
- admin 显式 team selection
- explicit team selection for admin

## Applies When
- defining login or `/api/auth/me` shapes for platform admin
- deciding how frontend pages restore or switch management-team scope
- deciding whether backend business routes may omit `team_id`
- translating legacy `tenant_*` compatibility semantics into current `team_*` runtime behavior

## Not For
- ordinary user membership rules where a team must exist as part of authentication
- generic RBAC guidance that is not about platform-admin versus team-owned business scope

## Top Facts
- Teamless platform-admin authentication is valid for management entry.
- Business reads and writes that target team-owned data still require explicit team selection.
- Treating platform admin as if it always has a default workspace hides permission boundaries and creates scope drift across UI, auth, and repository layers.

## Why
The product model says platform admin manages teams first and only enters a business team when needed. Treating admin as if it always had a default workspace hides permission boundaries and creates scope drift between UI, auth, and repository layers.

## Watchpoints
- Frontend pages often regress by restoring an implicit team even when backend auth correctly returns `team=null`.
- Backend convenience shortcuts that allow missing `team_id` can turn a management flow into a hidden business-team assumption.

## Load Next
- If the stable rule is being violated in runtime behavior, load [[pitfalls/admin-scope-ui-backend-drift]].
- If the task is about auth/session mechanics, load [[projects/account-team-efficiency/domains/platform-admin-auth-and-team-scope]].

## Anti-patterns
- [[pitfalls/admin-scope-ui-backend-drift]]

## Evidence
- [[projects/account-team-efficiency/overview]]
- [[projects/account-team-efficiency/domains/platform-admin-auth-and-team-scope]]

## Notes
This principle should stay short and stable. Project-specific implementation detail belongs in the domain and pitfall pages, not in the rule itself.

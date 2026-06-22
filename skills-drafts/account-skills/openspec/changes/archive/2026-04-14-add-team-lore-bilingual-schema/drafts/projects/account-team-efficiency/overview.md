---
tags: [lore/project-overview]
project: account-team-efficiency
---

# Project Overview — account-team-efficiency

## Scope
Startup context for the FastAPI + Vue operations platform with team-scoped runtime behavior, platform-admin management flows, and MySQL-backed execution state.

## Aliases
- 团队后台项目概览
- 平台管理项目概览
- account-team-efficiency 项目概览
- platform admin product overview
- team-scoped operations overview

## Applies When
- starting work in `account-team-efficiency`
- deciding whether a task is primarily about auth/team scope, shared-object UX, or team-scoped runtime behavior
- checking whether a platform-admin problem is product-model drift or implementation drift

## Not For
- governance-kit or shared skill authoring work in `account-skills`
- deep implementation detail once a specific domain page already matches the task scene
- treating this page as a substitute for the active OpenSpec change or local runtime logs

## Top Facts
- The current product shape is a MySQL-only runtime with team registration, platform-admin management, and read-only shared task/dictionary semantics.
- Platform-admin is a management role and must not silently gain an implicit business team during login or session recovery.
- Team-scoped wrappers and compatibility layers are critical because legacy `tenant_*` semantics can still drift from current `team_*` behavior.
- Shared-object visibility and platform-admin UX regressions often come from scope disagreement across UI state, route helpers, and backend wrappers rather than from missing rows alone.

## Boundaries
- Owns: team registration and membership, team-scoped config/runtime data, dashboard/batch operations, platform-admin management flows, and MySQL-backed execution state.
- Calls: Jira-like HTTP data sources, local scheduler/runtime services, MySQL persistence, and shared Lore Wiki pages.
- Must not: silently fabricate a team for platform-admin login, blur platform scope with team scope in UI or APIs, or let legacy `tenant_*` naming leak into new team-facing product semantics.

## Watchpoints
- Platform-admin flows are brittle whenever login, selected team scope, and API routing disagree about whether an active business team exists.
- Legacy compatibility layers can drift from new team semantics if route/service code skips shared wrappers.
- Shared-object visibility breaks quickly when ownership metadata is missing or stale.
- Frontend shared-object UX regresses when oversized pages keep page-local state and browser-default confirmation flows instead of the team-first product surface.

## Load Next
- If the issue is login, session recovery, or explicit `team_id` rules for platform admin, load [[projects/account-team-efficiency/domains/platform-admin-auth-and-team-scope]].
- If the issue is page-level team management UX, shared lists, or shared dictionary surfaces, load [[projects/account-team-efficiency/domains/team-admin-and-shared-ui]].
- If the issue is cross-page team scope drift, load [[pitfalls/admin-scope-ui-backend-drift]].
- If the issue is the stable product rule for platform-admin team selection, load [[principles/explicit-team-selection-for-platform-admin]].

## Notes
This page is for startup orientation. Once the task scene is clear, agents should move to the matching domain or pitfall page instead of continuing to mine this overview for detail.

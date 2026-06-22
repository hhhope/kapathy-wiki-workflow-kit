---
tags: [lore/pitfall]
pitfall: admin-scope-ui-backend-drift
---

# Pitfall — admin-scope-ui-backend-drift

## Scope
Failure pattern where platform-admin login, selected team scope, route helpers, and ownership metadata disagree about which team a request is actually operating on.

## Aliases
- 平台管理员范围漂移
- 平台管理 scope 漂移
- 团队选择漂移
- admin scope drift
- wrong-team platform admin state

## Trigger signals
- Platform admin sees one team in the UI while API calls actually query another team.
- Login or session bootstrap assumes every authenticated user has an active team and redirects into a fake workspace.
- Shared lists suddenly look empty even though the backing rows still exist.
- Team-edit or member-management UI appears to succeed while runtime still behaves like a different team or stale route table.

## Top Checks
- Confirm whether the current session is a valid platform-admin session with `team=null` rather than a fabricated business-team session.
- Confirm whether the frontend is reading one global management-team scope or hiding page-local shadow state.
- Confirm whether reads and writes are going through team-scoped wrappers that backfill ownership metadata on compatibility rows.

## Failure mode
The platform-admin path appears authenticated, but UI state, route helpers, and repository ownership metadata disagree about the active team. The result is empty data, wrong-team reads, partial admin flows, or brittle workarounds that hide the real contract.

## Avoidance
- Keep platform-admin login explicit: authenticated admin with `team=null` is valid; do not fabricate a team.
- Reuse one global management-team scope in the frontend instead of per-page shadow state.
- Route team-bound reads and writes through team-scoped wrappers that backfill `team_id/tenant_id/owner_team_id` on compatibility rows.
- Force explicit `team_id` for admin override flows that target business data.
- Preserve stable team ids on edit, expose member add/remove in the same admin surface, and restart/revalidate runtime routes before treating the flow as closed.
- Resolve shared placeholders through the current-team-visible shared dictionary path, not owner-only lookup.

## Not For
This pitfall is specific to platform-admin and cross-team management flows. It does not mean every user-facing page should support teamless access.

## Watchpoints
- UI-only fixes can hide backend scope drift for a while and then fail again on another page.
- Compatibility rows that still only retain legacy owner semantics can make a correct query look like a missing-data problem.
- Runtime drift can persist after source changes if services are not restarted and revalidated.

## Load Next
- If the issue starts with login/session rules, load [[projects/account-team-efficiency/domains/platform-admin-auth-and-team-scope]].
- If the issue starts with page UX or shared-object surfaces, load [[projects/account-team-efficiency/domains/team-admin-and-shared-ui]].
- If the issue is the stable rule behind this pitfall, load [[principles/explicit-team-selection-for-platform-admin]].

## Seen in
- [[projects/account-team-efficiency/domains/platform-admin-auth-and-team-scope]]
- [[projects/account-team-efficiency/domains/team-admin-and-shared-ui]]

## Related principles
- [[principles/explicit-team-selection-for-platform-admin]]

## Notes
This pitfall is diagnostic-first. If a future revision makes the first three checks harder to see than the narrative, the page has drifted away from the agent-memory contract.

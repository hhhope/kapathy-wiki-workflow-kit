---
tags: [lore/index]
---

# Lore Wiki Index

## Scope
Shared navigation entrypoint for durable Lore knowledge across projects, pitfalls, and principles.

## Aliases
- Lore 索引
- 团队知识入口
- 知识库入口
- lore index
- team lore entry

## Applies When
- starting task context recovery from the shared wiki
- looking for the first likely page to load for a project or shared failure pattern
- deciding whether to read a project overview, pitfall, or principle next

## Not For
- detailed task progress or execution status
- raw event history from local project `logs/`
- project-specific debugging when the relevant project overview or domain page is already known

## Top Facts
- `index.md` is the shared navigation layer, not the durable fact layer itself.
- Project overviews are the default first hop for project startup context.
- Pitfalls are the default first hop for repeated failure patterns that cut across tasks or layers.
- Principles are the default first hop for stable reusable rules that should survive project-specific detail changes.

## Watchpoints
- If index entries only describe pages but do not hint at the next hop, agents will over-read neighboring pages.
- If a project overview becomes a catch-all page, index navigation loses precision even when links remain correct.
- If shared failures are left inside project prose instead of promoted to pitfall/principle pages, the index under-represents reusable knowledge.

## Load Next
- If you are starting work in this repo, load [[projects/account-skills/overview]].
- If you are starting work in the operations product, load [[projects/account-team-efficiency/overview]].
- If your problem is platform-admin scope drift, load [[pitfalls/admin-scope-ui-backend-drift]].
- If your problem is platform-admin team selection rules, load [[principles/explicit-team-selection-for-platform-admin]].

## Projects

- [[projects/account-skills/overview]] — Skill library and Codex governance kit for reusable agent workflows.
- [[projects/account-team-efficiency/overview]] — Team-scoped sync, dashboard, and platform-admin operations product on a MySQL runtime.
- [[projects/account-asl/overview]] — Closed DDD anti-corruption service whose module-boundary knowledge remains reusable.

## Pitfalls

- [[pitfalls/admin-scope-ui-backend-drift]] — Platform-admin login, scope state, and owner-team metadata drift can make correct data appear empty or target the wrong team.
- [[pitfalls/behavior-assets-without-evidence]] — Editing AGENTS, rules, or skills without RED/GREEN evidence causes silent workflow drift.
- [[pitfalls/bootstrap-entry]] — A wiki bootstrap that leaves placeholders behind is not a usable memory layer.
- [[pitfalls/cross-layer-dependency-creep]] — Layered Java/DDD repos decay when common/domain modules absorb framework or adapter concerns.

## Principles

- [[principles/evidence-before-rollout]] — Behavior assets should not ship without testable before/after evidence.
- [[principles/explicit-team-selection-for-platform-admin]] — Platform admin should authenticate without an implicit team and supply explicit team scope for business operations.
- [[principles/wiki-in-git]] — Durable Lore knowledge should live in a git-backed wiki repository.
- [[principles/keep-anti-corruption-boundaries-explicit]] — Anti-corruption repos must keep module dependency and ownership boundaries explicit.

## Notes
This page should stay thin. If a future agent needs durable operational detail, that detail belongs in the linked page rather than in the index.

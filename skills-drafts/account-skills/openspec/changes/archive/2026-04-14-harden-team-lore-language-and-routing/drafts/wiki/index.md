---
tags: [lore/index]
---

# Lore Wiki Index

## Scope
Shared navigation entrypoint for durable Lore knowledge across projects, pitfalls, and principles.

## Summary
- 共享知识入口页：先决定下一跳，再进入具体项目页、pitfall 或 principle。Shared wiki entrypoint: decide the next hop before loading project, pitfall, or principle detail.

## Aliases
- Lore 索引
- 团队知识入口
- 知识库入口
- lore index
- team lore entry

## Applies When
- 从零启动任务上下文时，先用这页决定默认读取路径。Use this page first when recovering task context from scratch.
- 你还不知道该先看 project overview、pitfall 还是 principle。Use it when the next lore page is still undecided.

## Not For
- 这页不提供任务进度、执行状态或 archive 结论。This page does not answer task progress, execution status, or archive readiness.
- 已经知道具体目标页时，不要停在 index 重复读。Do not stay on the index once the target page is already known.

## Top Facts
- 默认读取路径是 `index -> overview -> domain / pitfall / principle`。The default startup path is `index -> overview -> domain / pitfall / principle`.
- `index.md` 只负责导航，不承载长期细节事实。`index.md` is a navigation layer, not the long-term fact layer.
- `overview` 是项目启动第一跳，`pitfall` 处理复发故障，`principle` 处理稳定规则。`overview` is the first project hop, `pitfall` handles repeated failure patterns, and `principle` handles stable rules.

## Watchpoints
- 如果 index 只列链接、不提示下一跳，agent 会过读相邻页面。If index only lists links without next-hop intent, agents will over-read neighboring pages.
- 如果 project overview 变成大杂烩，index 的精确导航会退化。If a project overview becomes a catch-all page, index precision degrades.

## Load Next
- 规范包 / governance kit 启动：[[projects/account-skills/overview]]。For governance-kit startup: [[projects/account-skills/overview]].
- 复发的行为资产验证问题：[[pitfalls/behavior-assets-without-evidence]]。For repeated behavior-asset validation failures: [[pitfalls/behavior-assets-without-evidence]].
- 业务系统 team-scope 规则：[[projects/account-team-efficiency/overview]]。For operations-product team-scope work: [[projects/account-team-efficiency/overview]].

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
Keep this page thin. If a detail starts helping only one project or one repeated failure shape, move it into the linked page instead of expanding the index.

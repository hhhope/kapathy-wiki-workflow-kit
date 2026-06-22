---
tags: [lore/project-overview]
project: account-skills
---

# Project Overview — account-skills

## Scope
Shared project-startup context for the reusable skill library and Codex governance kit in this repository.

## Summary
- 这是 `account-skills` 的启动页：先装项目边界，再决定去 domain、pitfall 还是 principle。This is the `account-skills` startup page: load project boundaries first, then branch to domain, pitfall, or principle.

## Aliases
- 规范包项目概览
- 治理安装项目概览
- account-skills 项目概览
- governance kit overview
- codex governance overview

## Applies When
- 你在修改 skills、rules、templates、安装流或治理说明。Use this page when changing skills, rules, templates, install flows, or governance guidance.
- 你要判断一条变更属于 repo 本地资产、shared lore，还是 Feishu-facing share material。Use it when deciding whether a change belongs in repo assets, shared lore, or Feishu-facing share material.

## Not For
- 这页不回答具体业务功能路径的运行时调试。This page is not for product-specific runtime debugging.
- 这页不替代 OpenSpec 的任务进度真相。This page does not replace OpenSpec as the task-progress truth source.

## Top Facts
- `account-skills` 管可复用 agent workflow 资产：skills、治理模板、eval fixtures、安装说明。`account-skills` owns reusable agent workflow assets: skills, governance templates, eval fixtures, and install guidance.
- 行为资产改动必须带可追溯的 before/after evidence。Behavior-asset changes require traceable before/after evidence.
- 这类治理变更完成前，还要同步 Feishu-facing source markdown。Material governance changes also require the Feishu-facing source markdown to be updated in the same work cycle.

## Boundaries
- Owns: reusable skills, governance templates, eval fixtures, install flows, and shareable agent workflow guidance.
- Calls: local git tooling, Codex home configuration, Feishu-facing source docs, and shared lore wiki pages.
- Must not: rely on repo-private assumptions inside reusable kit content, ship behavior-asset changes without traceable evidence, or mix project-local logs into the shared wiki repo.

## Watchpoints
- 如果全局 AGENTS、repo 模板和本地 skills 分别改动但没有统一 contract，治理内容会快速漂移。Governance content drifts quickly when AGENTS, templates, and local skills are edited independently.
- 如果安装说明只有 prose 没有命令面和验证面，agent 很容易高估完成度。Install guidance becomes hollow when it has prose but no command surface or verification path.

## Load Next
- 治理安装 / Lore bootstrap 边界：[[projects/account-skills/domains/codex-governance-installation]]。For governance installation or Lore bootstrap boundaries: [[projects/account-skills/domains/codex-governance-installation]].
- 行为资产没证据的失败模式：[[pitfalls/behavior-assets-without-evidence]]。For behavior-asset changes without proof: [[pitfalls/behavior-assets-without-evidence]].
- 稳定规则层：[[principles/evidence-before-rollout]]。For the stable rule behind this repo: [[principles/evidence-before-rollout]].

## Notes
This page should stay startup-friendly. Long-form repo history, Feishu share detail, or implementation notes belong in the linked pages once they stop helping first-load context.

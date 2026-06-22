---
tags: [lore/project-overview]
project: account-skills
---

# Project Overview — account-skills

## Scope
Shared project-startup context for the reusable skill library and Codex governance kit in this repository.

## Aliases
- 规范包项目概览
- 治理安装项目概览
- account-skills 项目概览
- governance kit overview
- codex governance overview

## Applies When
- starting work in `account-skills`
- updating reusable skills, templates, rules, or governance installation behavior
- checking whether a change belongs in project-local assets, shared lore, or Feishu-facing share material

## Not For
- implementing product-specific runtime behavior for `account-team-efficiency`
- debugging a single feature path once the relevant domain page is already known
- treating this page as task-progress truth instead of using the active OpenSpec change

## Top Facts
- `account-skills` owns reusable agent workflow assets: skills, governance templates, eval fixtures, and install guidance.
- Behavior-asset changes in this repo require traceable before/after evidence rather than prose-only confidence.
- Shared lore and governance content can drift when global AGENTS, repo templates, and local skills are edited independently.
- Feishu-facing share material is part of the working surface for this repo and should be refreshed in the same work cycle when governance content changes materially.

## Boundaries
- Owns: reusable skills, governance templates, eval fixtures, install flows, and shareable agent workflow guidance.
- Calls: local git tooling, Codex home configuration, Feishu-facing source docs, and shared lore wiki pages.
- Must not: rely on repo-private assumptions inside reusable kit content, ship behavior-asset changes without traceable evidence, or mix project-local logs into the shared wiki repo.

## Watchpoints
- Governance content drifts quickly when AGENTS, rules, templates, and skills are edited without a shared contract.
- Skill quality drops quickly when semantic skill edits skip RED/GREEN evidence.
- Installation guidance becomes hollow when it stops at prose and lacks command surface or verification path.

## Load Next
- If the issue is governance installation or Lore bootstrap boundaries, load [[projects/account-skills/domains/codex-governance-installation]].
- If the issue is behavior-asset validation discipline, load [[pitfalls/behavior-assets-without-evidence]].
- If the issue is when durable knowledge belongs in git-backed wiki instead of chat or logs, load [[principles/evidence-before-rollout]].

## Notes
This page should stay startup-friendly. Long-form repository history or Feishu share detail should live elsewhere once it stops helping a first task-start read.

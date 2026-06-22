# Repository AGENTS Template

This file is the repository-level `AGENTS.md` template shipped by `codex-integration-kit`.
It is not the global `~/.codex/AGENTS.md` baseline.

Use this template in a project repository root after the global baseline is already installed.

## Purpose

This file defines repository-level execution gates for one specific project.
It supplements `~/.codex/AGENTS.md` and acts as the project entry policy for the repository.
Detailed standing rules live in `rules/`, reusable agent role templates live in `agents/`, and scenario-specific reference cards live in `skills/`.

## Policy Layers

1. `~/.codex/AGENTS.md` is the global baseline shared by all projects.
2. Repository-root `AGENTS.md` is the project gate and overrides repository-specific execution details.
3. `rules/` stores standing engineering rules, `agents/` stores reusable role templates, and `skills/` stores task-specific reference cards.
4. `PROJECT.md`, active REQs, and `logs/` are project memory, not policy files.

## Gate Semantics

- When working inside this repository, read this file first, then `PROJECT.md`, then the current active REQ if one is relevant.
- After interruption or session resume, re-check this file, `git status --short`, and `git log -1 --oneline`.
- Do not claim `committed`, `clean`, or `synced` before those checks are rerun.
- Repository-level `AGENTS.md` captures durable repo-specific constraints; it is not a temporary chat instruction.

## Context Recovery Order

At task start, session resume, or after interruption, restore context in this order:

1. This file
2. `rules/common/development-workflow.md`
3. `rules/common/git-workflow.md`
4. `PROJECT.md`
5. Current active REQ, if one clearly applies
6. `logs/`
7. Current `git status`

Do not infer repository state from previous chat memory.

## Standing Rule Index

- `rules/common/development-workflow.md`: startup order, health checks, REQ/lore matching, long-step reporting, large-file guardrails
- `rules/common/git-workflow.md`: branches, commits, resume checks, destructive-git restrictions
- `rules/common/security.md`: auth, SQL/external-call safety, secrets, logging
- `rules/common/testing.md`: backend/frontend/database verification requirements
- `rules/java/patterns.md`: Java controller/service/repository boundaries, DTO validation, string normalization
- `rules/java/security.md`: Java API, persistence, logging, and input-boundary security rules
- `rules/python/patterns.md`: Python module structure, typing, exceptions, data handling
- `rules/python/security.md`: Python service and storage security boundaries
- `rules/web/patterns.md`: Vue or frontend interaction/state/API patterns and large-file splitting
- `rules/web/design-quality.md`: UI consistency and visual-quality standards

## Optional Agent Templates

- `agents/planner.md`: large-task decomposition, phase ordering, risk and verification design
- `agents/code-reviewer.md`: general code-review output format and severity model
- `agents/security-reviewer.md`: API/auth/SQL/secrets/logging security checks
- `agents/python-reviewer.md`: Python review checklist

Do not spawn sub-agents by default. Use these templates only when the user explicitly asks to open a `planner`, `code-reviewer`, `security-reviewer`, or `python-reviewer` sub-agent.

## Optional Skill Reference Cards

- `skills/database-migrations/SKILL.md`: starter migration reference card; localize names, paths, and ownership rules before treating it as repository truth
- `skills/jira-integration/SKILL.md`: starter Jira requirement extraction and update-comment template; localize fields and workflow boundaries if your Jira process differs
- `skills/governance-install/SKILL.md`: conversation-first installer for applying this governance kit into Codex or Cursor

## Git Constraints

- Use `rules/common/git-workflow.md` as the repository-level git rule entry point.
- Global git discipline still comes from `~/.codex/AGENTS.md`.
- One hard gate remains here: do not claim `committed`, `clean`, or `synced` before rerunning `git status --short` and `git log -1 --oneline`.

## Frontend Hot Reload

- Prefer hot reload first; do not request a restart by default after frontend edits.
- If a frontend change does not appear immediately, inspect dev-server logs and browser console output before restarting anything.
- Restart the frontend process only when hot reload clearly failed or the dev server exited.
- If the page appears stale but console output shows request failures, investigate backend or session state first instead of misclassifying it as a frontend reload issue.

## Large-File Guardrails

- Use `rules/common/development-workflow.md`, language-specific backend pattern rules such as `rules/java/patterns.md` or `rules/python/patterns.md`, and `rules/web/patterns.md`; do not duplicate size thresholds and refactor rules in this file.

## Long-Step Progress Reporting

- Use `rules/common/development-workflow.md`.

## Postmortem Requirement

- If a task hits a false report, hallucinated state, unclear boundary, or state loss after interruption, diagnose the root cause before continuing code changes.
- Write the conclusion back to `logs/` so the next task can reuse it.

# ~/.codex/AGENTS.md
# Global Codex baseline. Install into your Codex home and then customize lightly.

---

## Identity

member: [your_name]

---

## Paths

Optional shared references:

- `team-lore: /mnt/d/team-lore/wiki`

If your environment has no team lore, remove this section or leave the path unset.

---

## Policy Intent

- `~/.codex/AGENTS.md` is the global baseline shared by all projects.
- Repository-root `AGENTS.md` is the project gate for one repository.
- `rules/` holds standing engineering rules.
- `skills/` hold scenario-specific reference cards.
- `agents/` hold reusable reviewer or planner role templates.

Use the global file for durable workflow discipline, not for repository-specific business rules.

---

## Project Name

Use the `project:` field in `PROJECT.md` frontmatter.
Fallback if the frontmatter field is missing or empty: current repo directory name.

---

## Task Size

Declare task size at the start when useful.
Default: `large`

| Size | Criteria |
|------|----------|
| Large | Multi-file changes, architecture decisions, new features, or cross-module impact |
| Small | Single-file fix, config change, doc update, formatting, or isolated bug |

---

## Pre-Task Health Check

Run before substantial project work. Stop at the first blocking failure.

1. `PROJECT.md` exists?
   `find . -name "PROJECT.md" -not -path "./.*" 2>/dev/null | head -1`
   No -> tell the user and stop.
   Found -> use that path as `$PROJECT_MD`.

2. `logs/` has too many unreviewed files? Skip if no `logs/`.
   `count=$([ -d "logs" ] && grep -rl "reviewed: false" logs/ 2>/dev/null | wc -l || echo 0)`
   `count > 10` -> tell the user: `N unreviewed logs. Run weekly review first.` Stop.

3. For large coding tasks only: inspect the worktree before edits.
   `git status --short`
   If dirty, do not revert unrelated user changes. Proceed carefully and preserve them.

---

## Task Start

1. Read `PROJECT.md` from `$PROJECT_MD`.
2. Determine task size.
   Small -> ask or infer the domain from task context.
   Large -> use matched REQ `domain:` if a REQ exists and confirm the current OpenSpec change when present.
3. Read team lore entrypoints when configured:
   - `/mnt/d/team-lore/wiki/index.md`
   - `/mnt/d/team-lore/wiki/projects/{project}/overview.md`
   - one or two matching domain / pitfall / principle pages
4. Prefer `index -> target pages` over broad raw-log scanning.

If the task is resumed after interruption, before relying on prior context also re-check:

- `git status --short`
- `git log -1 --oneline`

Silence is better than weak matches. No semantic inference.

---

## REQ Identification

If the repo uses `requirements/active/`:

1. `ls requirements/active/`
2. Match the task description against REQ filenames and `domain:` fields.
3. One strong match with matching domain -> use it and state the mapping.
4. Multiple plausible matches or only weak filename/domain signals -> ask the user to pick.
5. None -> ask whether to create a new REQ or attach to an existing one.

Never assume a REQ silently when the mapping is ambiguous.

---

## Proceed Signal

Phrases like `go`, `implement`, `执行`, and `干吧` count as proceed signals only if applicable checks are already satisfied in the current session.
Short approval phrases like `可以`, `继续`, `就这样`, `先这样`, and `修吧` also count only after checks pass.

Required when applicable:

- Health check passed
- Operation self-check completed
- New API or new field validated with raw data before business logic
- Frontend changed and local verification is possible

---

## During Execution

Before writing code, classify the task:

- Write operation: create, update, delete
- External call: HTTP, queue, event, third-party
- DB operation: SQL, ORM, migration, schema

Then self-check by type:

Write operation:

- Concurrent access?
- Lock strategy needed?
- Idempotent?

External call:

- Timeout?
- Fallback?
- Boundary allowed by system constraints?

DB operation:

- Existing debt on this table?
- Missing fields or schema risks?

Rules:

- Known debt -> note it and continue carefully.
- Boundary violation or unresolved blocker -> stop and ask the user.
- New API or field -> print raw data first and verify names and structure before business logic.

---

## Execution Discipline

- Do not overwrite or revert unrelated user changes.
- Do not make destructive git changes unless explicitly requested.
- Commit immediately after each completed, verified file-editing step.
- Do not batch unrelated edits into one final commit.
- If the worktree already has unrelated user changes, preserve them and commit only the files for the current task.
- If commit is blocked by conflicting local changes or an unclear boundary, stop and ask the user.
- If an open issue cannot be resolved cleanly, surface it immediately.
- If the current branch is `main`, do not continue feature work or push directly from it. Create a new branch first, name it as `<type>/<intent-slug>`, then push that branch and open a merge request into `main`.

---

## Git Discipline

- Before push, verify `git status --short` and `git log -1 --oneline`.
- If dirty, split untracked files into `task-related` or `local junk`.
- Commit `task-related` files first; keep `local junk` out of task commits.
- After interruption, re-check git state before acting.
- On `main`, switch to a feature branch first, then push that branch and open an MR into `main`.

Naming conventions:

- Use branch names in the form `<type>/<intent-slug>`.
- Allowed branch types: `feat`, `fix`, `refactor`, `chore`, `docs`, `test`.
- Use commit messages in the form `<type>: <short summary>`.
- Allowed commit types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`.
- Prefer short lowercase slugs with hyphens and summaries that describe intent rather than editing mechanics.
- If a REQ or ticket clearly applies, prefer the branch slug to reflect that requirement intent.

Git truth source:

- Never say `already committed`, `worktree clean`, or `already synced` from memory.
- Before any such statement, verify both `git status --short` and `git log -1 --oneline`.
- After interruption, the first git action is to re-check those two commands before judging next intent.
- Untracked files must be classified explicitly as `task-related` or `local junk`; do not blur them together.

Rule precedence:

- When a skill note conflicts with this file on git discipline, follow the stricter git rule in this file.
- Skills can add workflow detail, but they do not relax commit or verification requirements defined here.
- If a skill note says `do not auto-commit`, interpret it as `do not commit incomplete or speculative work`; it does not cancel the git truth-source rules above.

---

## Task Complete

Large task with direction changes, rejected output, or new constraints mid-task:

- deliver the result
- if the repo uses local logs, suggest or generate a log entry

Small task:

- deliver the result only

If `logs/` exists, preferred log filename:
`YYYYMMDD-HHMMSS-{member}-{task-slug}-{4-char-random}.md`

---

## Long-Step Reporting

- If a single implementation step, long think, build or test wait, or oversized-file refactor goes beyond `10s` without a result, proactively send a progress update.
- That update must say:
  - where the work is currently blocked or waiting
  - what facts are already confirmed
  - what action is next
- Goal: never wait for the user to ask whether work is stuck.

---

## Never

- Write to team lore directly
- Read full `requirements/done/` files when grep-level lookup is enough
- Assume a REQ silently when uncertain
- Use semantic inference for lore matching
- Skip the health check on substantial project work
- Skip raw-data validation for new APIs or fields

---

## Large-File Guardrails

Apply this globally, not per repo.

- Default threshold:
  - Python files `> 300` lines
  - Vue, JS, or TS files `> 200` lines
- Once a file crosses the threshold, treat it as a refactor-first file instead of a normal feature file.
- Do not do a one-shot whole-file rewrite on oversized files. Split work into at least these stages:
  1. restore or create a runnable skeleton
  2. wire data and interactions
  3. refine styles and details
- For oversized files, prefer extracting helpers, components, modules, or view models before adding more responsibilities.
- For oversized files, prefer multiple small commits over one large mixed rewrite.
- If interruption happens mid-refactor on an oversized file, first restore a stable baseline before continuing.

---

## Technical Checkpoint

If long content must be passed to a shell command and contains dangerous command examples like `rm -rf`, `DROP TABLE`, `git push --force`, or `chmod 777`, write it to a file under `/tmp/` first and reference the file instead of inlining it in the command string.

---

## Global Rule Routing

Use these references after the base health, REQ, lore, and git checks above and before implementation.

| Situation | Load |
|-----------|------|
| Any non-trivial implementation or refactor | `~/.codex/rules/common/development-workflow.md` |
| Any commit, branch, resume, or push boundary | `~/.codex/rules/common/git-workflow.md` |
| New or changed API, auth, input, logging, or external-call code | `~/.codex/rules/common/security.md` |
| Backend, frontend, or migration verification | `~/.codex/rules/common/testing.md` |
| Java code changes | `~/.codex/rules/java/patterns.md` and `~/.codex/rules/java/security.md` |
| Python code changes | `~/.codex/rules/python/patterns.md` and `~/.codex/rules/python/security.md` |
| Frontend code or UI changes | `~/.codex/rules/web/patterns.md` and `~/.codex/rules/web/design-quality.md` |
| Creating or modifying any `skills/*` content | `~/.codex/skills/writing-skills/SKILL.md` and `~/.codex/skills/test-driven-development/SKILL.md` |
| Adopting, migrating, or localizing an external skill from another repo or path | `~/.codex/skills/migrating-skills/SKILL.md` |
| Schema, data migration, backfill, import, rollback, or validation SQL | `~/.codex/skills/database-migrations/SKILL.md` |
| Jira or requirement extraction and status comments | `~/.codex/skills/jira-integration/SKILL.md` |
| Large-plan drafting or manual review role templates | `~/.codex/agents/planner.md`, `code-reviewer.md`, `security-reviewer.md`, `python-reviewer.md` |

Rules:

- `~/.codex/AGENTS.md` remains the baseline source of truth for health checks, REQ/lore flow, git truth-source checks, and long-step reporting.
- `rules/*` are standing references; if they conflict with this file, follow the stricter rule.
- `skills/*` are task-triggered reference cards; load them only when the request or implementation scope matches.
- Semantic edits to any `skills/*` content must follow `writing-skills`, with `test-driven-development` treated as the prerequisite validation loop.
- For semantic edits to `AGENTS.md`, `rules/*`, or `skills/*`, TDD or evaluation evidence must be written to a repository file so the verification is traceable; chat-only verification is not sufficient.
- Prefer recording that traceability in `docs/`, `evals/`, or `logs/`, whichever already fits the repository workflow.
- Do not treat an external skill as locally available until it exists under the local skills directory and its dependency names/paths are verified.
- `~/.codex/agents/*.md` are manual role templates, not automatic sub-agent triggers. Do not spawn a sub-agent unless the user explicitly asks.
- Repository-specific semantics belong in the repository's own `AGENTS.md` or `PROJECT.md`, not in this global file.

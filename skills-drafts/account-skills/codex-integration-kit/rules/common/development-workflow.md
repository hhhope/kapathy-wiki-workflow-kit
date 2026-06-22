# Development Workflow

## Startup Order

At task start, session resume, or after interruption, restore context in this order:

1. `AGENTS.md`
2. `PROJECT.md`
3. Current active REQ, if one clearly applies
4. `logs/`
5. Current `git status --short`

Do not infer repository state from previous chat memory.

## Task Size

Default to `large`.

| Size | Criteria |
|------|----------|
| Large | Multi-file changes, architecture decisions, new features, cross-module impact |
| Small | Single-file fixes, config updates, docs edits, formatting, isolated bugs |

## Pre-task Health Check

Run this before substantial project work. Stop at the first blocking failure.

1. Check whether `PROJECT.md` exists
   - `find . -name "PROJECT.md" -not -path "./.*" 2>/dev/null | head -1`
   - If no result is returned, tell the user and stop
2. If `logs/` exists, count unreviewed logs
   - `count=$([ -d "logs" ] && grep -rl "reviewed: false" logs/ 2>/dev/null | wc -l || echo 0)`
   - If `count > 10`, ask the user to run weekly review first
3. For large code changes, inspect the worktree before edits
   - `git status --short`
   - Do not revert unrelated user changes

## REQ and Lore

- If `requirements/active/` exists, match the task against REQ filenames and frontmatter `domain:`.
- If exactly one strong REQ match exists, state that mapping explicitly before proceeding.
- If there are multiple weak matches or the mapping is uncertain, do not assume; ask the user.
- For lore lookup, use strict text matching only. Do not use semantic inference. Silence is better than weak matches.

## Pre-Implementation Self-Check

Before writing code, classify the operation type and run the matching checks:

- Write operation: concurrent access, lock strategy, idempotency
- External call: timeout, fallback, system-boundary constraints
- DB operation: known table debt, missing fields, schema risks

Known debt can be noted and handled carefully. If a boundary is unclear or a blocker is unresolved, stop and ask the user.

## Behavior Asset Change Gate

- Treat `AGENTS.md`, `rules/*`, and `skills/*` as behavior assets, not ordinary prose.
- Any semantic behavior-asset change must include verification evidence that is traceable in the repository; chat-only evidence is insufficient.
- Minimum traceability record:
  - expected behavior change
  - RED baseline scenario or command
  - observed failure before the change
  - GREEN verification using the same scenario or command after the change
  - file path where the evidence is recorded
- Preferred traceability locations:
  - `docs/` for governance or workflow verification notes
  - `evals/` when the repo already uses evaluation fixtures
  - `logs/` when the repo uses task logs as durable project memory

## Skill Change Gate

- Semantic edits under `skills/*` must follow `writing-skills`.
- `writing-skills` requires `test-driven-development` as the validation prerequisite; do not skip the RED -> GREEN -> REFACTOR loop.
- For semantic skill edits, the RED/GREEN evidence must be written to a repository file before the change is considered complete.

## Large-File Guardrails

Default thresholds:

- Python files `> 300` lines
- Vue / JS files `> 200` lines

Once a file crosses the threshold, do a split/refactor decision first. Do not do a one-shot whole-file rewrite. Prefer extracting helpers, components, modules, or config models before adding more responsibilities.

Default stage order:

1. Restore or create a runnable skeleton
2. Wire data and interactions
3. Refine styles and details

## Long-Step Progress Reporting

If one implementation step, long think, build/test wait, or large-file refactor takes more than `10s` without a result, proactively send a progress update that states:

- where the work is blocked or waiting
- what facts are already confirmed
- what action is next

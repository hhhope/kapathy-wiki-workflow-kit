# ~/.claude/CLAUDE.md
# Global config. Each member maintains their own. Never commit.

---

## Identity

member: []

---

## Paths

team-lore: /mnt/d/team-lore/wiki

---

## Project name

From `project:` field in PROJECT.md frontmatter.
Fallback: current repo directory name.

---

## Health check

Run before every substantial project task:

1. PROJECT.md exists?
   `find . -name "PROJECT.md" -not -path "./.*" 2>/dev/null | head -1`
   No -> stop

2. Local logs backlog too large?
   `count=$([ -d "logs" ] && grep -rl "reviewed: false" logs/ 2>/dev/null | wc -l || echo 0)`
   `count > 10` -> stop and run weekly review

3. Large task?
   - small -> continue
   - large -> confirm active OpenSpec change with `proposal.md`, `design.md`, `tasks.md`
   Missing -> stop and route to propose

4. Progress truth source?
   `tasks.md` must be the only execution-progress source

---

## Task start

1. Read `PROJECT.md`
2. Read current OpenSpec change docs
3. Read `/mnt/d/team-lore/wiki/index.md`
4. Read `/mnt/d/team-lore/wiki/projects/{project}/overview.md`
5. Read one or two matching domain pages
6. Read one or two matching pitfall / principle pages

Prefer:
- `index -> target pages`

Avoid:
- broad grep across raw logs as the primary retrieval path

Startup budget target:
- P50: 3-4 pages
- P90: <= 6 pages

---

## During execution

Classify the work:
- Write operation
- External call
- DB operation

Self-check:

Write operation:
- concurrent access?
- lock strategy?
- idempotent?

External call:
- timeout?
- fallback?
- boundary allowed?

DB operation:
- known debt?
- schema risk?

New facts:
- unresolved -> `UNKNOWNS`
- deviation -> `logs/`
- stable reusable lesson -> absorb during weekly review

---

## Task complete

Large task with corrections / follow-ups / direction changes:
- deliver result
- create a log

Small task:
- deliver result only

Logs are local event records. Durable memory lives in the wiki.

---

## Never

- Treat Lore as the task-progress truth source
- Execute large work without an active OpenSpec change
- Promote team-wide knowledge from one project only
- Replace wiki page retrieval with raw log scanning
- Skip health check

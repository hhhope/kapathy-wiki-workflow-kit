# ~/.codex/AGENTS.personal.example.md
# Personal strong-opinion overlay example. Merge selected parts into ~/.codex/AGENTS.md only if they fit your workflow.

This file is intentionally stricter than the global baseline.
It is an example overlay, not the recommended default for every team.

---

## Identity

member: [your_name]

---

## Recommended Overlays

Adopt these only if you want stronger execution discipline:

- Treat most coding tasks as `large` by default.
- Always run the health check before any non-trivial repository work.
- After interruption, always re-check `git status --short` and `git log -1 --oneline` before acting.
- Commit immediately after each completed, verified editing step.
- If a task changes frontend behavior, prefer local verification before declaring completion.
- If a new API or field is involved, inspect raw data or the actual wire shape before adding business logic.
- If the current branch is `main`, branch off before feature work.
- Use branch names as `<type>/<intent-slug>` and commit messages as `<type>: <short summary>`.
- Allowed branch types: `feat`, `fix`, `refactor`, `chore`, `docs`, `test`.
- Allowed commit types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`.
- If a task runs long, proactively report what is blocked, what is confirmed, and what is next.

---

## Strong Git Truth-Source Rule

- Never rely on memory for repository state.
- Before saying `clean`, `committed`, `already pushed`, or `already synced`, rerun:
  - `git status --short`
  - `git log -1 --oneline`
- If untracked files exist, classify them explicitly as `task-related` or `local junk`.

---

## Strong Ask-User Boundaries

Stop and ask instead of guessing when:

- REQ mapping is ambiguous
- repo boundary is unclear
- new dependency, destructive action, or production-facing risk appears
- a blocker cannot be resolved without changing the agreed direction

---

## Suggested Personal Notes

If you keep a personal setup, add only your own durable items here:

- member name
- team lore path
- preferred progress-reporting threshold
- preferred branch naming convention

Avoid hardcoding repository-specific business rules into the personal overlay.

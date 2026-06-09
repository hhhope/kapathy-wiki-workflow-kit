# Tasks

- [x] 1. Add OpenSpec proposal, design, spec, tasks, and evaluation evidence for
      `req-human-review`.
- [x] 2. Add `.codex/skills/req-human-review/SKILL.md` as a bounded worker.
- [x] 3. Update `.codex/skills/req-agent/SKILL.md` to route through
      `req-human-review` before handoff.
- [x] 4. Update `.codex/skills/req-handoff/SKILL.md` to block handoff when
      Human Review demand facts are unsynchronized.
- [x] 5. Add `wiki/templates/requirements-human-review-template.md`.
- [x] 6. Run focused behavior evidence checks:
      `rg` coverage for the new phase/template, requirements checker on the
      Baofu case, behavior asset checker, and OpenSpec validation.
- [x] 7. Commit only scoped files and stop at the OpenSpec hard stop when tasks
      are complete.

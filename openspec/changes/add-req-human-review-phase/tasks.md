# Tasks

- [x] 1. Add OpenSpec proposal, design, spec, tasks, and evaluation evidence for
      `req-human-review`.
- [ ] 2. Add `.codex/skills/req-human-review/SKILL.md` as a bounded worker.
- [ ] 3. Update `.codex/skills/req-agent/SKILL.md` to route through
      `req-human-review` before handoff.
- [ ] 4. Update `.codex/skills/req-handoff/SKILL.md` to block handoff when
      Human Review demand facts are unsynchronized.
- [ ] 5. Add `wiki/templates/requirements-human-review-template.md`.
- [ ] 6. Run focused behavior evidence checks:
      `rg` coverage for the new phase/template, requirements checker on the
      Baofu case, behavior asset checker, and OpenSpec validation.
- [ ] 7. Commit only scoped files and stop at the OpenSpec hard stop when tasks
      are complete.

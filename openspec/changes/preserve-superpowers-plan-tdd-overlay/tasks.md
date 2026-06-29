# Tasks

- [x] 1. Create OpenSpec change artifacts for Superpowers plan/TDD overlay preservation.
- [ ] 2. Add repo-local rule coverage to the appropriate workflow skill or guidance.
  - Candidate target: `.codex/skills/openspec-apply-change/SKILL.md`.
  - Keep `tasks.md` as the progress ledger.
  - Require overlay mapping and conformance evidence when a Superpowers plan exists.
- [ ] 3. Add behavior replay evidence.
  - Positive case: Superpowers brainstorming plus writing-plan details feed an
    OpenSpec change without losing TDD strategy.
  - Negative case: ordinary OpenSpec change with no Superpowers artifact does
    not require an overlay.
  - Drift case: Stripe H5-style keyword/screenshot verification fails because
    it ignores the mapped acceptance structure.
- [ ] 4. Run validation.
  - `openspec validate preserve-superpowers-plan-tdd-overlay --strict`
  - behavior asset checker if behavior guidance is edited
- [ ] 5. Stop at completion boundary and perform archive review separately.

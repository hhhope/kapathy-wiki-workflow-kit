# Tasks

- [x] Add OpenSpec proposal, design, spec deltas, and evaluation evidence for the visual-agent entry hardening.
- [x] Update `visual-agent` with an observable entry marker, direct-worker bypass rule, and explicit child-route map.
- [x] Update `public-report-quality-gate` delegation references and pressure scenarios so reader-facing visual work routes through `visual-agent` before worker skills.
- [x] Run scoped baseline/GREEN text checks, behavior asset checks, and OpenSpec validation.
- [x] Commit only scoped task-related files and stop at the OpenSpec completion boundary.

Verification note: `openspec validate harden-visual-agent-entry-route --strict`
passed. `git diff --check` passed for scoped files. Scoped `rg` checks confirmed
the required `Using visual-agent` / `public-report-quality-gate ->
visual-agent` route strings and removed old direct public-gate child mappings.
`python3 scripts/check_behavior_assets.py` still fails only on pre-existing
`openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md` evaluation gaps.

# Tasks

- [x] Add OpenSpec proposal, design, spec delta, and evaluation evidence.
- [x] Update `.codex/skills/visual-agent/SKILL.md` with source-role and delivery
      capability runtime boundaries.
- [x] Update `.codex/skills/visual-agent/evaluation.md` with pressure scenarios,
      RED baseline, GREEN result, and residual risks.
- [x] Run scoped text checks, OpenSpec validation, behavior-asset check, and
      `git diff --check`.
- [x] Commit only task-related files.

Verification note: `openspec validate enforce-visual-image-delivery-boundary
--strict` passed. Scoped `rg` found the new source-role and delivery-capability
runtime terms in `visual-agent`, its evaluation, and the change artifacts.
Scoped `git diff --check -- .codex/skills/visual-agent
openspec/changes/enforce-visual-image-delivery-boundary` passed.
`python3 scripts/check_behavior_assets.py` still returns non-zero for
pre-existing `initialize-llm-wiki-seed-repo/evaluation.md` evidence gaps and
the parallel `realign-stripe-h5-redesign-sections` missing evaluation; it no
longer reports this change after the evaluation format repair.

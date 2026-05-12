# Archive Review

Review date: 2026-05-12

## Decision

Archive-ready after this review note is committed.

## Reason

This change modifies repo-local skill behavior and future OpenSpec/Superpowers
runtime routing. That makes the archive decision governance-heavy enough to
require change-local reasoning before archival.

The implementation evidence is complete:

- `tasks.md` is fully checked.
- `proposal.md`, `design.md`, and delta spec describe the execution-overlay
  authority boundary.
- `evaluation.md` records pressure scenarios, RED baseline, GREEN result, and
  residual risks.
- `.codex/skills/openspec-apply-change/SKILL.md` now states that detailed
  Superpowers planning inside an OpenSpec change is an execution overlay, not a
  second task list.
- `.codex/skills/openspec-apply-change/references/execution-overlay.md` gives
  the real bad/good example.

## Validation

- `openspec validate clarify-openspec-superpowers-overlay --strict` passed.
- `openspec validate --all` passed: 48 items, 0 failed.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_wiki_graph_extraction_identity.WikiGraphExtractionIdentityTest.test_live_extraction_resolves_target_runtime_pages` passed.
- Text replay checks confirmed the old `add-product-status-contract`
  implementation plan matches drift patterns, while the Good Shape overlay
  section has no independent task headings or progress checkboxes.

PostHog DNS flush errors were telemetry noise after local validation results.

## Proof Boundary

This is bounded behavior replay evidence, not multi-session rollout telemetry.
Future agents still need to load the repo-local `openspec-apply-change` skill
for the rule to influence execution.

## Next Action

Archive normally so the delta spec updates the main `openspec-apply-change`
spec and the review note travels with the archived change.

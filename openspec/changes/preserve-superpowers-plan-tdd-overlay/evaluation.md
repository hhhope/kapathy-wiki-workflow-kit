# Evaluation

## Pressure Scenarios

| Case | Input or situation shape | Trigger condition | Expected route | Repo-visible artifact | Expected output | Promotion or non-promotion boundary | Proof boundary |
|---|---|---|---|---|---|---|---|
| positive trigger: Superpowers plan approved for multi-file work | User has approved Superpowers spec and plan | Work needs check/archive | implement from Superpowers plan, use OpenSpec only for check/archive | Superpowers plan, this OpenSpec change | plan blocks drive execution | OpenSpec does not replace plan | local replay only |
| negative should-not-trigger: small one-session edit | Simple one-file fix | No lifecycle/archive need | no OpenSpec wrapper required | none | direct small-task flow | no durable wrapper | local replay only |
| drift case: Stripe H5 drift | Superpowers design used as supporting context | Verification checks keywords/screenshots only | fail plan-check/check evidence | Stripe drift records | missing acceptance path is reported | no archive-ready claim | local replay only |
| scope change | Implementation discovers new scope | plan no longer matches scope | stop and update/create OpenSpec | active change | no silent merge | user confirms scope | local replay only |

## Replay Evidence

- input or situation shape: Superpowers-native work with possible OpenSpec lifecycle.
- trigger condition: approved Superpowers plan plus multi-file or long-lived check/archive need.
- expected route: execute from Superpowers plan; use OpenSpec for check/archive or scope-change stops.
- repo-visible artifact: `.codex/skills/openspec-apply-change/SKILL.md`, this change, Superpowers spec/plan.
- expected output: no second implementation plan in `tasks.md`.
- promotion or non-promotion boundary: repo-local workflow guidance only.
- proof boundary: local unit tests and manual replay, not multi-session telemetry.

## RED Baseline

Observed current failure: existing guidance permits OpenSpec to preserve or
rewrite an overlay instead of clearly stating that Superpowers plan remains the
implementation plan and OpenSpec tasks are check/archive only.

RED command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_native_superpowers_openspec_workflow -v
```

Observed RED result:

- Missing workflow wording in `.codex/skills/openspec-apply-change/SKILL.md`.
- Missing plan-check boundary in this change's `design.md`.
- Missing check/archive boundary in this change's `tasks.md`.
- Missing `evaluation.md` before this file was added.

## GREEN Result

Commands run on 2026-06-29:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_native_superpowers_openspec_workflow -v
openspec validate preserve-superpowers-plan-tdd-overlay --strict
python3 scripts/check_behavior_assets.py
```

Observed GREEN result:

- `tests.test_native_superpowers_openspec_workflow`: 4 tests passed.
- `openspec validate preserve-superpowers-plan-tdd-overlay --strict`: valid.
- `scripts/check_behavior_assets.py`: non-zero due existing unrelated active
  changes; this change was not reported in the checker output.

Behavior proof:

- The apply skill now states that the Superpowers plan is the implementation
  plan.
- The apply skill now states that OpenSpec tasks are the check/archive ledger.
- The active change defines plan-check as Superpowers plan review, not an
  OpenSpec progress step or second plan.
- The active change keeps `tasks.md` out of block-level implementation progress.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`
- `.codex/skills/openspec-router/SKILL.md`
- `.codex/skills/openspec-apply-change/SKILL.md`
- `openspec/specs/openspec-apply-change/spec.md`
- `wiki/ops/stripe-ai-company-evolution-h5-structure-explore-2026-06-23.md`

Owns:

- Repo-local Superpowers/OpenSpec check/archive boundary.

References:

- Existing OpenSpec source-of-truth and archive rules.
- Superpowers native brainstorming and writing-plans rules.

Rejects:

- Editing upstream Superpowers plugins.
- Turning OpenSpec tasks into a second implementation plan.

## Residual Risks

- `scripts/check_behavior_assets.py` remains non-zero because
  `openspec/changes/initialize-llm-wiki-seed-repo/evaluation.md` lacks the
  required behavior-evaluation sections and
  `openspec/changes/realign-stripe-h5-redesign-sections` lacks
  `evaluation.md`. Those are pre-existing or unrelated active-change issues and
  were not modified here.
- Future agents must load repo guidance.

# Evaluation: add wiki medical loop skills

## Behavior Replay

- Situation shape: user asks how to use the newly implemented LLM-WIKI medical
  loop and expects skill-level routing rather than raw Python commands.
- Trigger condition: prompts mention doctor output, 确诊, treatment, surgery,
  recovery, 复查, or "how do I use this".
- Expected route: use user-facing skills in this order:
  `wiki-doctor -> wiki-confirm -> wiki-treatment -> wiki-surgery -> wiki-recovery`.
- Repo-visible artifact: `.codex/skills/wiki-*/SKILL.md` files and generated
  records under the existing `wiki/ops/wiki-*-runs/` directories.
- Expected non-output: stage skills do not directly create OpenSpec changes,
  mutate taxonomy, write MOC pages, or treat records as approval.
- Proof boundary: marker tests prove the behavior contract is present in the
  skill surface; they do not prove future natural-language routing in every
  model session.

## RED Baseline

Command:

```bash
python3 -m unittest tests/test_wiki_medical_loop_skills.py
```

Result: failed as expected before skill changes.

Key failures:

- `.codex/skills/wiki-confirm/SKILL.md` did not exist.
- `.codex/skills/wiki-treatment/SKILL.md` did not exist.
- `.codex/skills/wiki-surgery/SKILL.md` did not exist.
- `.codex/skills/wiki-recovery/SKILL.md` did not exist.
- `wiki-doctor` did not expose the next-stage sequence.
- `wiki-review-decisions` did not identify itself as a legacy compatibility
  alias for `wiki-confirm`.

This confirms the drift: executable Python layers existed, but the user-facing
skill surface did not.

## GREEN Result

Commands:

```bash
python3 -m unittest tests/test_wiki_medical_loop_skills.py tests/test_wiki_review_decisions_skill.py tests/test_wiki_runtime_skills.py
python3 scripts/check_behavior_assets.py
openspec validate add-wiki-medical-loop-skills --strict
```

Results:

- Skill tests: `Ran 9 tests ... OK`
- Behavior asset checker: exit 0
- OpenSpec strict validation: valid
- OpenSpec CLI printed PostHog DNS telemetry warnings only; validation exited 0.

## Prior-Art / Common-Rule Dedupe

- Owns: repo-local medical-loop skill names, stage routing labels, and
  compatibility boundary for `wiki-review-decisions`.
- References: existing Python executors and archived OpenSpec changes for
  doctor, confirm/review, treatment, surgery, and recovery behavior.
- Rejects: turning `wiki-doctor` into a full automatic router in this change;
  that remains a later phase after stage skill names stabilize.

## Residual Risks

- The current session's available-skill list may not include newly added skills
  until the next skill discovery refresh.
- `wiki-review-decisions` still exists for compatibility; future docs should
  prefer `wiki-confirm`.
- Full `wiki-doctor` triage behavior is intentionally deferred to a later
  phase.

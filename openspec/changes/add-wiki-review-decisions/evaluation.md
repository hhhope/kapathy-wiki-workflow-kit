# Evaluation: add wiki review decisions

## Pressure Scenarios

### Positive: doctor diagnosis needs confirmation

- Input or situation shape: user asks to turn `wiki-doctor` findings into a
  confirmation sheet.
- Trigger condition: the request mentions confirm, review decision, 确诊,
  route, treatment candidate, or surgery candidate for doctor output.
- Expected route: use `wiki-review-decisions` and generate a draft decision
  record under `wiki/ops/wiki-review-decisions/` only when explicitly asked.
- Repo-visible artifact: `.codex/skills/wiki-review-decisions/SKILL.md` and
  `wiki/ops/wiki-review-decisions/*-review-decisions.md`.
- Expected output: draft buckets with detail refs and proof boundary.
- Promotion or non-promotion boundary: the record does not promote candidates
  into writes; treatment and surgery remain later workflows.
- Proof boundary: the record is routing evidence, not human approval.

### Negative should-not-trigger: user asks to repair frontmatter directly

- Input or situation shape: user asks to write frontmatter, taxonomy config,
  relation fields, MOC, ADR, AGENTS, or OpenSpec lifecycle state.
- Trigger condition: the request is write-capable repair rather than diagnosis
  confirmation.
- Expected route: do not use `wiki-review-decisions` as the repair executor;
  route to the appropriate later approved workflow or OpenSpec change.
- Repo-visible artifact: no review-decision record is required unless the user
  first asks to triage doctor findings.
- Expected output: boundary explanation or later workflow selection.
- Promotion or non-promotion boundary: `wiki-review-decisions` cannot promote
  diagnosis into writes.
- Proof boundary: repair proof must come from later treatment, surgery, or
  recovery workflows.

## RED Baseline

- Before this change, no `.codex/skills/wiki-review-decisions/SKILL.md` exists.
- Before this change, no `scripts/build_wiki_review_decisions.py` CLI exists.
- Before this change, no repo-visible review-decision record writer exists.
- RED command:
  `python3 -m unittest tests/test_wiki_review_decisions_skill.py`
- RED result: failed as expected because the repo-local skill file was absent:
  `AssertionError: False is not true : wiki-review-decisions skill must exist`.

## GREEN Result

- Added `.codex/skills/wiki-review-decisions/SKILL.md` as a compact
  English-first tool-wrapper module for confirming, triaging, or routing
  `wiki-doctor` findings into review decisions.
- The skill references `scripts/build_wiki_review_decisions.py` and
  `python3 scripts/build_wiki_review_decisions.py`, while requiring
  `--write-decision-record` for explicit decision-record writes under the
  default `wiki/ops/wiki-review-decisions/` directory.
- The skill preserves the required buckets:
  `accepted_candidates`, `rejected_candidates`, `deferred_items`,
  `treatment_candidates`, `surgery_candidates`, and `openspec_required`.
- The skill states the proof boundary: outputs are draft review routing, not
  approval, and draft review decisions are not human approval.
- The skill preserves hard boundaries against OpenSpec lifecycle mutation,
  task completion, queued work execution, frontmatter writes, taxonomy config
  mutation, relation-field writes, and `wiki/moc` writes.
- GREEN command:
  `python3 -m unittest tests/test_wiki_review_decisions_skill.py`
- GREEN result: passed, `Ran 1 test in 0.016s`, `OK`.
- Script existence note: at this slice boundary,
  `scripts/build_wiki_review_decisions.py` was still absent
  (`test -e scripts/build_wiki_review_decisions.py; echo script:$?` returned
  `script:1`); the skill intentionally references the separately owned code
  worker output.
- Behavior-asset check command:
  `python3 scripts/check_behavior_assets.py`
- Behavior-asset check result: exit code 0 with no output.

## Prior-Art / Common-Rule Dedupe

Scanned:

- Repo `AGENTS.md`
- `openspec/specs/skill-authoring-contract/spec.md`
- `openspec/specs/skill-evaluation-evidence/spec.md`
- `openspec/specs/local-skill-pressure-tests/spec.md`
- `openspec/changes/formalize-llm-wiki-medical-loop`
- `.codex/skills/wiki-doctor/SKILL.md`

Owns:

- `wiki-review-decisions` owns only the review/confirmation routing stage that
  converts doctor output into draft decision records.

References:

- `wiki-doctor` remains the diagnosis surface.
- The medical-loop OpenSpec remains the lifecycle vocabulary owner.
- Repo OpenSpec and AGENTS gates remain the lifecycle and workflow-change owner.

Rejects:

- This change rejects adding treatment, surgery, recovery, or direct wiki repair
  behavior to the review-decision skill.

## Residual Risks

- Local pressure evidence is the minimum gate; broader multi-session rollout
  proof remains future evidence.
- Review-decision records are draft routing artifacts until a human confirms
  them.
- Treatment and surgery execution still require separate changes.

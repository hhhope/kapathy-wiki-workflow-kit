# Evaluation: wiki-doctor review records

## Evidence

- `python3 -m unittest tests/test_wiki_content_adjudication.py`
  - RED baseline: failed before implementation because
    `scripts.wiki_doctor_review_records` did not exist and the CLI lacked
    `--write-review-record`.
  - GREEN result from Worker B: passed, 7 tests.
- `python3 -m unittest tests/test_wiki_runtime_skills.py`
  - RED baseline: failed after adding markers because `wiki-doctor` did not
    mention explicit review-record generation.
  - GREEN result from Worker C: passed, 5 tests.
- `python3 -m unittest tests/test_wiki_content_adjudication.py tests/test_wiki_runtime_skills.py`
  - Result: passed, 12 tests.
- `python3 scripts/build_wiki_content_adjudication.py --limit 0`
  - Result: completed without `review_record_path`, preserving default
    stdout-only behavior.
- `python3 scripts/build_wiki_content_adjudication.py --limit 5 --write-review-record`
  - Result: wrote
    `wiki/ops/wiki-doctor-runs/2026-05-14-130526-review.md`.
  - Summary: 153 candidates, 153 full details, 144 review focus entries,
    3 taxonomy candidates, 71 drift traces, 112 eval warnings.
  - The generated record includes proof boundary and next review actions.
- `python3 scripts/check_behavior_assets.py`
  - Result: passed.
- OpenSpec validation: `openspec validate add-wiki-doctor-review-records --strict`
  reported `Change 'add-wiki-doctor-review-records' is valid` and exited `0`.
  PostHog network flush warnings appeared after validation because
  `edge.openspec.dev` DNS resolution failed; the validation result itself
  passed.

## Pressure Scenarios

| Scenario | Expected route | Result |
| --- | --- | --- |
| Positive: explicit review-record request | Build adjudication package and write Markdown diagnosis under `wiki/ops/wiki-doctor-runs/` | Passed |
| Negative: ordinary doctor diagnosis | Preserve stdout-only behavior and create no review-record file | Passed |
| Negative: taxonomy candidates appear | Record candidates without mutating taxonomy YAML | Passed |
| Negative: accepted judgments appear | Record diagnosis without frontmatter, MOC, or OpenSpec task writes | Passed |

## RED Baseline

Input or situation shape: the adjudication package exists and `wiki-doctor`
can summarize it.

Trigger condition: user asks for a durable diagnosis record or doctor run
record.

Observed failure before this change: `scripts/build_wiki_content_adjudication.py`
only prints JSON and has no explicit review-record write path.

## GREEN Result

Expected route:

```text
wiki-doctor -> build adjudication package -> explicit review record ->
human review -> later explicit fix or OpenSpec
```

Repo-visible artifact: `scripts/wiki_doctor_review_records.py`,
`scripts/build_wiki_content_adjudication.py`, `.codex/skills/wiki-doctor/SKILL.md`,
targeted tests, and
`wiki/ops/wiki-doctor-runs/2026-05-14-130526-review.md`.

Expected output: a Markdown diagnosis record with scan scope, summary, taxonomy
candidates, drift traces, eval result, proof boundary, and next review actions.

Promotion or non-promotion boundary: the review record does not become approved
frontmatter, taxonomy config, MOC pages, or OpenSpec task completion.

Proof boundary: this proves deterministic record generation and boundary text,
not semantic correctness of every candidate or multi-session enforcement.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`
- `PROJECT.md`
- `openspec/specs/behavior-replay-gate/spec.md`
- `wiki/ops/behavior-replay-gate.md`
- `openspec/changes/add-wiki-content-adjudication-eval/design.md`
- `openspec/changes/add-wiki-content-adjudication-eval/evaluation.md`
- `openspec/changes/rename-wiki-content-adjudication-skill-to-doctor/design.md`
- `.codex/skills/wiki-doctor/SKILL.md`

Owns:

- Explicit `wiki-doctor` diagnosis record generation.

References:

- Existing content adjudication package and eval.
- Existing behavior replay and skill evaluation gates.
- Existing review-only doctor boundary.

Rejects:

- Default file writes during ordinary diagnosis.
- Direct frontmatter writes from doctor output.
- Silent taxonomy mutation.
- Treating a diagnosis record as repair approval.

## Parent Gate Preservation

Parent gate: `wiki-doctor` remains a review-only diagnostic wrapper around the
content adjudication package. The new record is a persisted diagnosis, not an
apply or repair command.

## Residual Risks

- Human review remains required for taxonomy expansion and structure writes.
- A Markdown record can become stale after wiki content changes.
- This evidence does not prove future agents will always choose record
  generation unless the trigger is explicit.

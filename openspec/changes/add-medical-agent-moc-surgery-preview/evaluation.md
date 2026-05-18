# Evaluation: medical-agent MOC surgery preview

## RED / GREEN Evidence

- RED tests were added before implementation in commit `f531154`, with follow-up test fix `1db6a74`.
- GREEN implementation landed in commit `916d3c2`, with classifier tightening in `2c079a4`.
- Classifier coverage in `tests/test_wiki_medical_agent.py` includes:
  - `MOC review` -> `moc_surgery_preview`
  - `knowledge-map review` -> `moc_surgery_preview`
  - negative case `mock preview apply confirmed treatments` -> `treatment_preview`

## Verification

Command:

```bash
python3 -m unittest tests.test_wiki_medical_agent tests.test_wiki_surgery tests.test_wiki_moc_projection
```

Result: passed, `Ran 35 tests in 7.877s`, `OK`.

Command:

```bash
python3 scripts/build_wiki_medical_agent.py --intent-text "moc preview surgery"
```

Result: exited 0 and returned the current active case preview with:

- `intent: moc_surgery_preview`
- `allowed_action: preview_moc_surgery_plan`
- `moc_projection.candidate_count: 185`
- `surgery_preview.moc_projection_count: 185`
- `next_action: review_moc_surgery_preview`

Command:

```bash
test -d wiki/moc
```

Result: exited 1, expected. No `wiki/moc` directory exists after preview verification.

Command:

```bash
openspec validate add-medical-agent-moc-surgery-preview --strict
```

Result: exited 0, `Change 'add-medical-agent-moc-surgery-preview' is valid`.
PostHog DNS flush warnings were observed after validation output; they are telemetry-only and did not change the command exit status.

## Review Evidence

- Spec compliance re-review approved after fix commit `2c079a4`.
- Code-quality re-review approved after fix commit `2c079a4`.

## Residual Boundary

This change only previews MOC surgery items through the medical-agent route. It does not apply MOC writes, write `wiki/moc`, update runtime wiki files, or archive the OpenSpec change.

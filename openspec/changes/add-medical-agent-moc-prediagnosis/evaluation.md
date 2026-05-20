# Evaluation: medical-agent MOC prediagnosis

## RED Baseline

- `tests.test_wiki_medical_agent` failed before implementation because
  `prediagnosis` did not exist on allowed `moc_surgery_preview` payloads.
- MOC temperature clue language did not all route to `moc_surgery_preview`.

## GREEN Result

- `python3 -m unittest tests.test_wiki_medical_agent tests.test_wiki_moc_temperature tests.test_wiki_moc_projection tests.test_wiki_surgery`
  passed: 65 tests ran in 12.687s.
- `openspec validate add-medical-agent-moc-prediagnosis --strict` passed and
  reported `Change 'add-medical-agent-moc-prediagnosis' is valid`.
- The OpenSpec validation emitted a non-blocking PostHog telemetry warning:
  `getaddrinfo EAI_AGAIN edge.openspec.dev`.
- `python3 scripts/build_wiki_medical_agent.py --intent-text "MOC 温度线索 先不要写"`
  returned `intent: moc_surgery_preview`, `allowed_action:
  preview_moc_surgery_plan`, `prediagnosis.kind: moc_temperature`, and
  `prediagnosis.write_boundary: read_only_no_files_written`.

## Boundary Proof

- The `prediagnosis` section does not include raw `clue_windows`.
- The dry-run summarized 5 review-needed clues and 4 orphan relation MOC pages
  without writing files.
- `git status --short wiki/moc wiki/ops/wiki-medical-cases wiki/ops/wiki-surgery-runs wiki/ops/wiki-treatment-runs`
  produced no output after the dry-run.
- The dry-run did not write `wiki/moc`.
- The dry-run did not write treatment or surgery records.
- Mechanical relations remain blocked by default: `derived_from` and
  `related_objects` were reported as blocked relations and are not admitted.

## Residual Risk

- The prediagnosis is a bounded summary over existing worker evidence. It does
  not replace human confirmation or case-file authority.

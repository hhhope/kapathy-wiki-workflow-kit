# Evaluation: add MOC temperature reading board

Date: 2026-05-19
Baseline HEAD before evidence: `3ce8881 fix: isolate medical MOC admission payload`

## Evidence Table

| Check | Command | Result | Evidence |
|---|---|---|---|
| MOC temperature, projection, and medical-agent tests | `python3 -m unittest tests.test_wiki_moc_temperature tests.test_wiki_moc_projection tests.test_wiki_medical_agent` | PASS | Ran 51 tests in 8.428s. Output ended with `OK`. |
| Wiki status and surgery regression tests | `python3 -m unittest tests.test_wiki_status tests.test_wiki_surgery` | PASS | Ran 29 tests in 1.606s. Output ended with `OK`. |
| OpenSpec strict validation | `openspec validate add-moc-temperature-reading-board --strict` | PASS with non-blocking telemetry warning | Printed `Change 'add-moc-temperature-reading-board' is valid` and exited 0. After validation, OpenSpec printed PostHog flush warnings caused by `getaddrinfo EAI_AGAIN edge.openspec.dev`; this was telemetry/network flushing only and did not fail validation. |
| MOC projection dry-run | `python3 scripts/build_wiki_moc_projection.py` | PASS | JSON output had `"mode": "dry-run"` and included `temperature_admission`. Summary: `candidate_count=184`, `create_count=0`, `update_count=0`, `noop_count=184`, `orphan_count=4`. Temperature counts: `admitted=0`, `blocked=425`, `needs_review=38`, `total=463`. |
| Compact JSON confirmation | `python3 -c '...'` running `scripts/build_wiki_moc_projection.py` and parsing stdout as JSON | PASS | Parsed `mode=dry-run`, `has_temperature_admission=True`, `admitted_relations=[]`, `generated_relation_entries=0`, and summary `create_count=0`, `update_count=0`. |
| No file writes from dry-run | `git status --short -- wiki/moc openspec/changes/add-moc-temperature-reading-board` before editing evaluation/tasks | PASS | No output before evaluation/task edits, confirming the projection dry-run did not write `wiki/moc` or change-local files. |

## Behavior Replay

| Situation | Trigger | Expected behavior | Observed behavior |
|---|---|---|---|
| Raw relation graph edges exist without admitted review evidence | Build MOC projection without a relation admission plan admitting relation types | Relation MOC pages are not generated from raw relation groups; relation state remains in admission summary only | Dry-run parsed `admitted_relations=[]` and `generated_relation_entries=0`. |
| Mechanical relation types are present | Projection encounters relation evidence such as `derived_from` and `related_objects` without explicit high-temperature admission | Mechanical relation types remain blocked or review-needed, not generated as relation MOC candidates | Dry-run `temperature_admission` counts were `blocked=425`, `needs_review=38`, `admitted=0`; generated relation entries were absent. |
| Medical-agent MOC preview path is exercised | Medical-agent unit tests run with MOC temperature admission preview coverage | Preview surfaces admission state while remaining read-only | Combined medical-agent/MOC test suite passed with 51 tests. |
| OpenSpec lifecycle validation runs after implementation | Strict validation for `add-moc-temperature-reading-board` | Change artifacts validate under strict OpenSpec rules | OpenSpec printed the valid-change line and exited 0. |

## Proof Boundary

- Evidence proves the implemented repository behavior for unit-covered MOC temperature, projection, status, surgery, and medical-agent preview paths at baseline HEAD `3ce8881`.
- Evidence proves the default projection command is a dry-run, emits `temperature_admission`, produces no create/update operations, and does not write files in this verification run.
- Evidence does not prove a human-reviewed admission JSON rollout with admitted relation pages in production content; it only proves admitted relation generation through the existing unit coverage and no-admission default behavior in the current wiki state.
- The PostHog warning is a telemetry network flush failure after successful OpenSpec validation, not a validation failure.

## Residual Risks

- Current repository content has no admitted relation reviews in the default projection run, so live dry-run evidence covers the blocked/review-needed path more strongly than the admitted relation path.
- The projection output includes existing orphan relation MOC files as orphan state in the full dry-run JSON, but the compact parse confirmed no generated relation entries and no create/update writes.
- Network-restricted environments may continue to print non-blocking PostHog telemetry warnings after OpenSpec commands.

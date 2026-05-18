# Evaluation: object lifecycle MOC preview

## Evidence

| Check | Result | Notes |
| --- | --- | --- |
| `python3 -m unittest tests.test_wiki_moc_projection.WikiMocProjectionTest.test_object_preview_groups_pages_by_lifecycle_not_ops_area` before implementation | RED | Failed because object preview had a flat list and no `## Sources / Learning` heading. |
| `python3 -m unittest tests.test_wiki_moc_projection.WikiMocProjectionTest.test_object_preview_groups_pages_by_lifecycle_not_ops_area` after implementation | PASS | Object preview now includes lifecycle sections and does not use `learning-capture` or `workflow-trace` as section headings. |
| `python3 -m unittest tests.test_wiki_moc_projection` | PASS | 6 tests passed. |
| `python3 -m unittest tests.test_wiki_moc_projection tests.test_wiki_graph_summary tests.test_wiki_status tests.test_wiki_decision_trace_eval` | PASS | 33 tests passed. |
| `python3 scripts/build_wiki_moc_projection.py` | PASS | Dry-run produced 184 create actions, 0 update, 0 noop, 0 orphan; no files written. |
| `python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10` | PASS with warnings | 0 blocking errors; existing 5 producer warnings remain. |
| `openspec validate add-object-lifecycle-moc-preview --strict` | PASS | Change validated; PostHog telemetry flush printed DNS warnings after local validation. |
| `test -d wiki/moc` | PASS boundary | Command exited non-zero, confirming `wiki/moc` was not created. |

## RED Baseline

Input shape: an object MOC with pages across reading notes, OpenSpec spec, ADR,
method, and replay evidence.

Expected route: render object preview as lifecycle sections rather than a flat
list.

Observed failure before implementation:

```text
AssertionError: '## Sources / Learning' not found in ...
<!-- BEGIN GENERATED MOC: object=llm-wiki -->
- [[spec]] (openspec/specs / spec)
- [[0019-agent-readable-wiki-runtime-context-after-utilization]] (wiki/adr / adr)
- [[karpathy-llm-wiki-reading-notes]] (wiki/ops / reading-notes)
- [[wiki-readable-views-validation-harness]] (wiki/ops / replay-harness)
- [[wiki-runtime-layer-contract]] (wiki/ops / method)
<!-- END GENERATED MOC -->
```

## GREEN Result

Object MOC preview now groups explicit graph nodes by lifecycle stage:

```text
## Sources / Learning
- [[agent-governance-gate-gap-explore-2026-04-18]] (wiki/ops / explore)

## Evidence / Replay
- [[agent-governance-gate-gap-retro-2026-04-18]] (wiki/ops / retro)
```

Another current-repo example:

```text
## Specification
- [[spec]] (openspec/specs / spec)

## Evidence / Replay
- [[moc-apply-review-2026-05-18]] (wiki/ops / review)
```

The preview still uses explicit `source_layer` and `artifact_type` metadata.
It does not use `ops_area` values such as `learning-capture` or
`workflow-trace` as primary section headings.

## Residual Risks

- Some repo-specific artifact types still fall into `Other`, including several
  product/report production types. This is acceptable for the first version and
  should be tuned from actual preview review rather than guessed upfront.
- This change proves local preview behavior only. It does not prove Obsidian UI
  graph layout quality.
- No generated MOC pages were applied in this change.

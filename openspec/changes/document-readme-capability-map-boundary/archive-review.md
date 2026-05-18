# Archive Review

Decision: archive-ready.

## Evidence

- `tasks.md` is complete: 5/5 checked.
- `openspec validate document-readme-capability-map-boundary --strict` passed.
- README runtime-surface tests passed as part of the 52-test suite:
  `python3 -m unittest tests.test_wiki_content_enrichment
  tests.test_wiki_content_adjudication tests.test_wiki_moc_projection
  tests.test_wiki_graph_summary tests.test_wiki_status
  tests.test_wiki_decision_trace_eval tests.test_wiki_runtime_skills
  tests.test_codex_plugin_marketplace -v`.
- `wiki/adr/0034-readme-capability-map-is-project-description.md` has explicit
  frontmatter and records the stable README boundary decision.
- `wiki/ops/readme-capability-map-boundary-drift-retro-2026-05-14.md` records
  the drift trigger and corrected framing.

## Boundary

- README is project orientation, not runtime authority.
- Runtime behavior remains owned by OpenSpec, ADRs, skills, command docs, and
  implementation evidence.

## Residual Risk

Future README edits can still drift into runtime claims; this change records
the boundary but does not make README a gate.

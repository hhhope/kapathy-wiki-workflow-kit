# Evaluation

## Pressure Scenarios

1. A user asks "wiki 现在健康吗" and should not have to pick between status,
   graph, scorecard, query, or apply.
2. A page has `derived_from:` or `related_objects:` in frontmatter, but graph
   relation coverage is unexpectedly low.
3. Taxonomy drift exists in legacy pages, and the normal status surface should
   show the drift without duplicating taxonomy vocabulary.
4. A graph summary includes both wiki pages and `openspec/specs` nodes for the
   same object, and the readable summary should not bury the user in spec paths.
5. Diagnostics suggest a repair, but the command surface must not silently edit
   runtime behavior outside OpenSpec.

## RED Baseline

Before this change:

- `commands/wiki-status.md` described status as a generated manifest summary
  but did not name it as the default health entry or mention domain taxonomy /
  graph parse health.
- `scripts/build_wiki_status.py` returned no `domain_taxonomy_health` or
  `graph_parse_health` fields.
- `scripts/extract_wiki_graph.py::parse_frontmatter` only parsed list items
  that started at column zero, so normal indented YAML relation lists parsed as
  empty.
- `scripts/summarize_wiki_graph.py` selected representative pages by sorted
  path, so `openspec/specs/.../spec.md` could dominate readable summaries.
- `commands/wiki-apply.md` summarized self-directed execution but did not name
  repair routes or the OpenSpec boundary for runtime repairs.

## GREEN Result

After this change:

- `/wiki:status` command docs identify it as the default health entry and name
  inbox, OpenSpec, identity, relation, domain taxonomy, and graph parse health.
- `build_manifest()` includes `domain_taxonomy_health` and
  `graph_parse_health`.
- Status Markdown renders `## Domain Taxonomy Health` and
  `## Graph Parse Health`.
- Indented YAML relation lists are parsed as relation values and no longer
  trigger graph parse health drift.
- Graph summaries retain spec counts, source layers, and artifact types while
  preferring non-spec representative pages and exposing
  `collapsed_spec_page_count`.
- `/wiki:apply` command docs list the repair routes and preserve the no-direct-
  mutation boundary.

## Verification

- `python3 -m unittest tests/test_wiki_status.py tests/test_wiki_graph_summary.py tests/test_wiki_frontmatter_taxonomy.py tests/test_wiki_runtime_commands.py`
  - Result: pass, 23 tests.
- `python3 scripts/build_wiki_status.py`
  - Result: pass; generated `wiki/status/manifest.json` and
    `wiki/status/wiki-status.md` during live verification.
  - Note: generated files were restored before commit because the current dirty
    worktree contains unrelated inbox and wiki material that would pollute the
    generated snapshot.
- `python3 scripts/extract_wiki_graph.py`
  - Result: pass; raw graph still includes covered layer `openspec/specs` and
    emitted 200 nodes, 385 edges, 0 warnings in this worktree.
- `openspec validate improve-wiki-routing-diagnostics --strict`
  - Result: pass; OpenSpec reported the change as valid.
  - Note: PostHog telemetry flush reported DNS/network errors after validation;
    the validation result itself was successful.
- `python3 scripts/check_behavior_assets.py`
  - Result: pass, exit code 0.

## Residual Risks

- Domain taxonomy health intentionally surfaces existing legacy drift; this
  change does not migrate those pages.
- Graph parse health only detects raw relation fields that parse as empty. It
  does not validate whether relation targets are semantically correct.
- The parser remains a bounded frontmatter helper, not a full YAML replacement
  for arbitrary markdown metadata.

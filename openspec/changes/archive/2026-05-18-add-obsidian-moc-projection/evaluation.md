# Evaluation: Obsidian MOC projection

## Evidence

| Check | Result | Notes |
| --- | --- | --- |
| `python3 -m unittest tests/test_wiki_moc_projection.py tests/test_wiki_graph_summary.py tests/test_wiki_status.py tests/test_wiki_decision_trace_eval.py` | PASS | 30 tests passed. |
| `python3 -m unittest tests/test_wiki_moc_projection.py tests/test_wiki_graph_summary.py tests/test_wiki_status.py tests/test_wiki_decision_trace_eval.py tests/test_wiki_graph_extraction_identity.py` | PASS | 40 tests passed. |
| `python3 -m unittest tests/test_wiki_runtime_skills.py` | PASS | Skill docs now expose MOC projection inspect/preview boundaries. |
| `python3 scripts/summarize_wiki_graph.py --limit 3` | PASS | Output includes `moc_candidates`; no files written. |
| `python3 scripts/build_wiki_moc_projection.py` | PASS | Dry-run reports 153 create actions in current repo; no files written. |
| `python3 scripts/build_wiki_status.py --output-dir /tmp/wiki-status-moc-check` | PASS | Status output written outside repo and includes MOC projection health. |
| `openspec validate add-obsidian-moc-projection --strict` | PASS | Change validated; telemetry flush later printed network warnings. |
| `python3 scripts/check_behavior_assets.py` | PASS | Required after repo-local skill docs changed. |

## Pressure Scenarios

| Scenario | Expected route | Result |
| --- | --- | --- |
| Positive: Obsidian graph only shows index links and user asks for graph-visible relations | Route as `obsidian_graph_projection`; read graph/status; preview MOC projection; require explicit generator for writes | PASS |
| Negative: agent tries to make status, graph, apply, react, or eval write MOC files directly | Eval replay rejects forbidden action; skill docs preserve inspect/preview boundary | PASS |

## RED Baseline

Input or situation shape: user wanted Obsidian graph visibility from existing
frontmatter/domain/object/relation structure.

Trigger condition: Obsidian sees Markdown `[[wikilinks]]`, while existing repo
graph structure lives in frontmatter and script outputs.

Observed failure before this change: graph/status/apply/react had no MOC
candidate, health, preview, generator, or eval route for
`obsidian_graph_projection`.

## GREEN Result

Expected route:

```text
wiki-react -> graph MOC candidates -> status MOC health -> apply preview
-> explicit build_wiki_moc_projection.py --apply
```

Repo-visible artifacts:

- `scripts/wiki_moc_projection.py`
- `scripts/build_wiki_moc_projection.py`
- `scripts/summarize_wiki_graph.py`
- `scripts/build_wiki_status.py`
- `scripts/wiki_status_render.py`
- `scripts/derive_self_directed_execution.py`
- `wiki/evals/wiki-react-trace-cases.json`
- `.codex/skills/wiki-graph/SKILL.md`
- `.codex/skills/wiki-status/SKILL.md`
- `.codex/skills/wiki-apply/SKILL.md`
- `.codex/skills/wiki-react/SKILL.md`

Expected output:

- Graph summary includes MOC candidates.
- Status includes MOC projection health.
- Apply output includes MOC projection preview.
- Generator dry-run is default; `--apply` is explicit.

Promotion or non-promotion boundary: MOC projection is implemented as a runtime
capability, but current repo MOC files are not generated unless the explicit
generator write mode is invoked.

Proof boundary: tests prove local script behavior and boundary checks. They do
not prove Obsidian UI rendering or graph layout quality.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`
- `PROJECT.md`
- `wiki/adr/0033-wiki-react-eval-apply-openspec-boundary.md`
- `wiki/adr/0034-readme-capability-map-is-project-description.md`
- `openspec/specs/wiki-graph-extraction/spec.md`
- `openspec/specs/wiki-status-surface/spec.md`
- `.codex/skills/wiki-graph/SKILL.md`
- `.codex/skills/wiki-status/SKILL.md`
- `.codex/skills/wiki-apply/SKILL.md`
- `.codex/skills/wiki-react/SKILL.md`

Owns:

- The repo-specific frontmatter-to-MOC projection runtime capability.

References:

- Existing graph extraction and status surfaces.
- Existing wiki runtime layer boundary.
- Existing skill authoring and behavior replay gates.

Rejects:

- Replacing frontmatter as source of truth with body links.
- Making status, graph, apply, react, or eval write MOC files implicitly.
- Adding a graph UI or per-page relation blocks in this change.

## Residual Risks

- Current repository dry-run reports 153 MOC files would be created; applying
  that directly may be noisy until the user approves the generated surface.
- Some OpenSpec spec pages share the stem `spec`, so Obsidian link targets for
  spec pages may need a later alias/path policy.
- Obsidian UI rendering has not been manually checked.

## Expected Checks

- `openspec validate add-obsidian-moc-projection --strict`
- `python3 -m unittest tests/test_wiki_moc_projection.py tests/test_wiki_graph_summary.py tests/test_wiki_status.py tests/test_wiki_decision_trace_eval.py`
- `python3 scripts/build_wiki_moc_projection.py --root /tmp/...` dry-run does not write
- `python3 scripts/build_wiki_moc_projection.py --root /tmp/... --apply` writes generated blocks

## Boundary

This change proves controlled MOC projection mechanics. It does not prove
Obsidian UI rendering, graph layout quality, or per-page relation block support.

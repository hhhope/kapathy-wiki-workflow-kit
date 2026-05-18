# Evaluation: wiki content enrichment preview

## Evidence

- `python3 -m unittest tests/test_wiki_content_enrichment.py tests/test_wiki_status.py tests/test_wiki_decision_trace_eval.py tests/test_wiki_runtime_skills.py tests/test_wiki_moc_projection.py tests/test_wiki_graph_summary.py tests/test_wiki_graph_extraction_identity.py`
  - Result: passed, 49 tests.
- `python3 scripts/build_wiki_content_enrichment.py --limit 5`
  - Result: preview completed without page writes.
  - Summary: 152 entries, 136 review-needed, 16 high-confidence, 136
    medium-confidence, 0 low-confidence.
- `python3 scripts/build_wiki_status.py --output-dir /tmp/wiki-status-enrichment-check`
  - Result: wrote status preview artifacts under `/tmp`, not the repo wiki.
- `python3 -m unittest tests/test_wiki_status_command.py tests/test_wiki_runtime_skills.py`
  - Result: passed, 7 tests.
- `python3 scripts/check_behavior_assets.py`
  - Result: passed.
- `openspec validate add-wiki-content-enrichment-preview --strict`
  - Result: passed.
  - Concern: OpenSpec printed PostHog network flush warnings for
    `edge.openspec.dev`, but the validation command exited successfully.

Requested-but-unavailable check:

- `python3 -m unittest tests/test_wiki_runtime_commands.py`
  - Result: not runnable because `tests/test_wiki_runtime_commands.py` does
    not exist in this checkout.

## Pressure Scenarios

| Scenario | Expected route | Result |
| --- | --- | --- |
| Positive: ops page lacks required frontmatter | Enrichment preview suggests candidates with evidence and marks review need | Passed by `tests/test_wiki_content_enrichment.py` |
| Negative: agent tries to write frontmatter directly from enrichment preview | Eval rejects direct write action | Passed by `tests/test_wiki_decision_trace_eval.py` |

## RED Baseline

Input or situation shape: MOC projection needs clean frontmatter, but covered
pages may have missing or stale classification.

Trigger condition: page content has enough bounded evidence for a candidate,
but no reviewed frontmatter yet.

Observed failure before this change: graph and MOC could only project existing
frontmatter; there was no content-to-frontmatter preview layer.

## GREEN Result

Expected route:

```text
wiki-react -> enrichment preview -> status/apply preview -> explicit reviewed frontmatter edit -> graph -> MOC
```

Repo-visible artifact: `scripts/wiki_content_enrichment.py`,
`scripts/build_wiki_content_enrichment.py`, status/apply/react surfaces, and
`wiki/evals/wiki-react-trace-cases.json`.

Expected output: candidate frontmatter/relation preview with confidence,
evidence, and `needs_review`.

Promotion or non-promotion boundary: candidates do not become page frontmatter
until an explicit reviewed write happens.

Proof boundary: deterministic preview does not prove semantic truth or LLM
understanding.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`
- `PROJECT.md`
- `wiki/config/frontmatter-taxonomy.yaml`
- `wiki/ops/agent-readable-wiki-frontmatter.md`
- `wiki/adr/0033-wiki-react-eval-apply-openspec-boundary.md`
- `openspec/changes/add-obsidian-moc-projection/design.md`

Owns:

- Deterministic content-to-frontmatter enrichment preview for `wiki/ops` and
  `wiki/adr`.

References:

- Existing taxonomy gate and graph extraction contracts.
- Existing runtime layer boundaries.

Rejects:

- LLM-only hidden semantic inference.
- Direct page writes from status/apply/enrichment preview.

## Parent Gate Preservation

Parent gate: the enrichment preview preserves the wiki runtime layer boundary.
It feeds graph and MOC only after reviewed frontmatter exists.

## Residual Risks

- Deterministic heuristics can miss valid relationships.
- Candidates may still need human review for domain and relation accuracy.

# Evaluation: wiki content adjudication eval

## Evidence

- `python3 -m unittest tests/test_wiki_content_adjudication.py`
  - RED baseline result before implementation: failed with
    `ModuleNotFoundError: No module named 'scripts.wiki_content_adjudication'`.
  - GREEN result after implementation: passed, 4 tests.
- `python3 -m unittest tests/test_wiki_status.py tests/test_wiki_decision_trace_eval.py tests/test_wiki_runtime_skills.py tests/test_wiki_content_adjudication.py`
  - RED integration result before wiring: failed because status lacked
    `content_adjudication_health`, eval cases lacked
    `wiki-content-adjudication`, and runtime skills lacked adjudication
    markers.
  - GREEN result after wiring: passed, 33 tests.
- `python3 -m unittest tests/test_wiki_content_adjudication.py tests/test_wiki_content_enrichment.py tests/test_wiki_status.py tests/test_wiki_decision_trace_eval.py tests/test_wiki_runtime_skills.py tests/test_wiki_moc_projection.py tests/test_wiki_graph_summary.py tests/test_wiki_graph_extraction_identity.py`
  - Result: passed, 54 tests.
- `python3 scripts/build_wiki_content_adjudication.py --limit 5`
  - Result: completed without page writes.
  - Summary: 152 candidates, 152 full details, 143 review focus entries,
    3 taxonomy candidates, 71 drift traces.
- `python3 scripts/build_wiki_status.py --output-dir /tmp/wiki-status-adjudication-check`
  - Result: wrote status preview artifacts under `/tmp`, not the repo wiki.
- `python3 scripts/derive_self_directed_execution.py`
  - Result: completed and included `content_adjudication_review_package` with
    `execution_boundary: review_only`.
- `python3 scripts/check_behavior_assets.py`
  - Result: passed.
- `openspec validate add-wiki-content-adjudication-eval --strict`
  - Result: passed.
  - Concern: OpenSpec printed PostHog network flush warnings for
    `edge.openspec.dev`, but the validation command exited successfully.

## Pressure Scenarios

| Scenario | Expected route | Result |
| --- | --- | --- |
| Positive: enrichment candidates exist | Package includes full detail and review focus sets with refs | Passed |
| Positive: unknown taxonomy value appears | Taxonomy candidate set surfaces value without YAML mutation | Passed |
| Negative: risky judgment has no evidence | Eval fails with missing evidence error | Passed |
| Negative: unsafe write is marked safe with unresolved risks | Eval fails and blocks safe-to-apply claim | Passed |

## RED Baseline

Input or situation shape: content enrichment produces candidate entries for
`wiki/ops` and `wiki/adr`.

Trigger condition: user asks the agent to judge whether candidates are true and
which risks require review.

Observed failure before this change: the repository only has flat preview
entries and decision-trace shape eval. It does not produce full detail review
sets, agent judgments, taxonomy candidates, or drift trace diagnostics.

## GREEN Result

Expected route:

```text
wiki-react -> content enrichment preview -> adjudication package ->
adjudication eval -> review package -> explicit reviewed write later
```

Repo-visible artifact: `scripts/wiki_content_adjudication.py`,
`scripts/build_wiki_content_adjudication.py`, status/apply/react surfaces,
`wiki/evals/wiki-react-trace-cases.json`, and targeted tests.

Expected output: review package with full detail and focused review sets,
taxonomy candidates, drift trace diagnostics, and eval errors/warnings.

Promotion or non-promotion boundary: adjudication output does not become page
frontmatter or taxonomy config until a separate explicit reviewed write occurs.

Proof boundary: deterministic adjudication checks evidence and risk flags, but
does not prove hidden semantic truth.

## Prior-Art / Common-Rule Dedupe

Scanned:

- `AGENTS.md`
- `PROJECT.md`
- `wiki/ops/agent-readable-wiki-frontmatter.md`
- `wiki/ops/agent-readable-wiki-runtime-auto-routing.md`
- `wiki/adr/0033-wiki-react-eval-apply-openspec-boundary.md`
- `openspec/changes/add-wiki-content-enrichment-preview/design.md`
- `openspec/changes/add-wiki-content-enrichment-preview/specs/wiki-content-enrichment-preview/spec.md`

Owns:

- Content adjudication package and adjudication eval output.

References:

- Existing content enrichment preview.
- Existing taxonomy and frontmatter gates.
- Existing runtime layer boundary ADR.

Rejects:

- Direct frontmatter writes from adjudication.
- Silent taxonomy mutation.
- Treating apply as semantic truth judgment.

## Parent Gate Preservation

Parent gate: adjudication remains a review/eval layer between preview and
explicit approved structure writes.

## Residual Risks

- Deterministic adjudication can still miss nuanced semantic relationships.
- User review remains required for taxonomy expansion and governance decisions.

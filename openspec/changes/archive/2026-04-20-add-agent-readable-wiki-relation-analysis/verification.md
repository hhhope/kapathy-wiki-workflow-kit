# Verification: Agent-Readable Wiki Relation Analysis

## Implemented Artifacts

- workflow page:
  - `wiki/ops/agent-readable-wiki-relation-analysis.md`
- analysis script:
  - `scripts/analyze_wiki_relations.py`
- sample artifact:
  - `scripts/examples/agent_readable_wiki_relation_analysis_sample.json`

## Input / Output Contract

- default input:
  - live output from `scripts/extract_wiki_graph.py`
- optional input:
  - explicit extracted graph JSON path
- output sections:
  - `summary`
  - `object_coverage`
  - `artifact_type_distribution`
  - `relation_type_distribution`
  - `unresolved_warning_summary`
  - `analysis_notes`

## Current-State Verification

Command sequence:

```bash
python3 scripts/extract_wiki_graph.py > /tmp/current_wiki_graph.json
python3 scripts/analyze_wiki_relations.py /tmp/current_wiki_graph.json
```

Observed summary:

- `canonical_object_count: 6`
- `cross_layer_object_count: 5`
- `analyzed_node_count: 19`
- `analyzed_edge_count: 4`
- `unresolved_warning_count: 57`

Observed structure signals:

- `conversation-handoff` shows cross-layer coverage with:
  - `method`
  - `sample`
  - `spec`
- `wiki-relation-analysis` is visible as a single-layer object in `wiki/ops`
- relation usage currently reflects:
  - `derived_from: 1`
  - `formalizes: 2`
  - `validates: 1`
- unresolved structure is still concentrated in:
  - `wiki/ops: 27`
  - `wiki/adr: 13`
  - `openspec/specs: 12`
  - `wiki/examples: 5`

## Sample Artifact Check

Command run:

```bash
python3 scripts/analyze_wiki_relations.py > scripts/examples/agent_readable_wiki_relation_analysis_sample.json
```

Result:

- sample artifact was generated from the current repository state
- sample summary matched the live analysis run

## OpenSpec Validation

Command run:

```bash
openspec validate add-agent-readable-wiki-relation-analysis
```

Result:

- change is valid
- PostHog telemetry emitted network errors to `edge.openspec.dev`
- telemetry failure did not block validation

## Proof Boundary

This change proves:

- the repository can analyze extracted graph structure deterministically
- the analysis can surface cross-layer object coverage and unresolved structural areas
- the analysis stays explicit about structural limits

This change does not prove:

- semantic graph understanding
- retrieval quality
- runtime routing quality
- rollout proof for the whole repository

## Residual Risks

- unresolved warnings remain high, especially in `wiki/ops`
- relation analysis still depends on structural identity only
- first version is descriptive, not a semantic or scored quality model

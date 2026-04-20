# Verification: Agent-Readable Wiki Semantic Scoring

## Implemented Artifacts

- workflow page:
  - `wiki/ops/agent-readable-wiki-semantic-scoring.md`
- scoring script:
  - `scripts/score_wiki_semantics.py`
- sample artifact:
  - `scripts/examples/agent_readable_wiki_semantic_scoring_sample.json`

## Factor Model

Version 1 uses explicit rule-based factors with a maximum score of `10`:

- `cross_layer_presence`: `0-3`
- `artifact_type_variety`: `0-2`
- `relation_presence`: `0-2`
- `formalization_depth`: `0-3`

Banding:

- `strong`: `7-10`
- `moderate`: `4-6`
- `weak`: `0-3`

## Current-State Verification

Command sequence:

```bash
python3 scripts/analyze_wiki_relations.py > /tmp/current_relation_analysis.json
python3 scripts/score_wiki_semantics.py /tmp/current_relation_analysis.json
```

Observed summary:

- `scored_object_count: 7`
- `score_range.min: 2`
- `score_range.max: 8`
- `strong: 5`
- `moderate: 0`
- `weak: 2`
- `unresolved_warning_total: 59`
- `unresolved_warning_pressure: high`

Observed differentiation:

- strongest object in current state:
  - `disagreement-management: 8`
- strong but slightly narrower objects:
  - `conversation-handoff: 7`
  - `example-driven-capture: 7`
  - `wiki-frontmatter-model: 7`
  - `wiki-naming-model: 7`
- weak single-layer objects:
  - `wiki-relation-analysis: 2`
  - `wiki-semantic-scoring: 2`

This confirms the sample artifact distinguishes stronger object families from thinner ones using explicit bounded factors.

## Sample Artifact Check

Command run:

```bash
python3 scripts/score_wiki_semantics.py > scripts/examples/agent_readable_wiki_semantic_scoring_sample.json
```

Result:

- sample artifact was generated from current repository state
- sample output matched the live semantic-scoring run

## OpenSpec Validation

Command run:

```bash
openspec validate add-agent-readable-wiki-semantic-scoring
```

Result:

- change is valid
- PostHog telemetry emitted network errors to `edge.openspec.dev`
- telemetry failure did not block validation

## Proof Boundary

This change proves:

- the repository can generate deterministic semantic scores from explicit repository evidence
- factor breakdown is visible and audit-friendly
- stronger and weaker object families can be distinguished without embeddings or hidden models

This change does not prove:

- retrieval quality
- runtime routing quality
- semantic understanding of unresolved pages
- semantic completeness of the repository

## Residual Risks

- unresolved warnings remain high, so scores still sit under heavy unresolved structural pressure
- current factors reward formalized object families more than raw topic richness
- version 1 uses bounded rule-based scoring only; it does not yet test whether scores correlate with retrieval usefulness

## Verification Note

When validating with a file input path, the relation-analysis file must be written before the scoring command reads it.

Parallel read/write on the same temp file can produce an empty-file JSON decode failure even when the scoring logic itself is correct.

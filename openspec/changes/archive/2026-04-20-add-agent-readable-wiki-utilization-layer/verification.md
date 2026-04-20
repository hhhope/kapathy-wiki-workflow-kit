# Verification: Agent-Readable Wiki Utilization Layer

## Implemented Artifacts

- workflow page:
  - `wiki/ops/agent-readable-wiki-utilization-layer.md`
- utilization script:
  - `scripts/derive_wiki_utilization.py`
- sample artifact:
  - `scripts/examples/agent_readable_wiki_utilization_sample.json`

## Banding Model

Version 1 uses explicit rule-based bands:

- `preferred`
  - requires strongest current bounded evidence
- `cautious`
  - object is usable but repository conditions still limit trust
- `blocked`
  - object remains too thin for stronger agent use

## Current-State Verification

Command sequence:

```bash
python3 scripts/score_wiki_semantics.py > /tmp/current_semantic_scoring.json
python3 scripts/derive_wiki_utilization.py /tmp/current_semantic_scoring.json
```

Observed summary:

- `object_count: 8`
- `preferred: 1`
- `cautious: 4`
- `blocked: 3`
- `unresolved_warning_pressure: high`
- `caution_active: true`

Observed differentiation:

- preferred:
  - `disagreement-management`
- cautious:
  - `conversation-handoff`
  - `example-driven-capture`
  - `wiki-frontmatter-model`
  - `wiki-naming-model`
- blocked:
  - `wiki-relation-analysis`
  - `wiki-semantic-scoring`
  - `wiki-utilization-layer`

This confirms the artifact distinguishes stronger candidates from cautionary and blocked ones instead of flattening them into a single usage state.

## Sample Artifact Check

Command run:

```bash
python3 scripts/derive_wiki_utilization.py > scripts/examples/agent_readable_wiki_utilization_sample.json
```

Result:

- sample artifact was generated from current repository state
- sample output matched the live utilization run

## OpenSpec Validation

Command run:

```bash
openspec validate add-agent-readable-wiki-utilization-layer
```

Result:

- change is valid
- PostHog telemetry emitted network errors to `edge.openspec.dev`
- telemetry failure did not block validation

## Proof Boundary

This change proves:

- the repository can generate deterministic agent-usage guidance from semantic-scoring output
- preferred, cautious, and blocked object candidates can be separated explicitly
- repository-wide caution remains visible instead of being flattened away

This change does not prove:

- retrieval readiness
- runtime automation readiness
- semantic understanding of unresolved pages
- that utilization guidance can replace direct source inspection

## Residual Risks

- repository-wide unresolved pressure remains high
- utilization is object-level only; it does not yet rank specific pages
- current banding is still rule-based and may not yet correlate with actual retrieval usefulness

## Verification Note

When validating with a file input path, the semantic-scoring file must be written before the utilization command reads it.

Parallel read/write on the same temp file can produce an empty-file JSON decode failure even when utilization logic itself is correct.

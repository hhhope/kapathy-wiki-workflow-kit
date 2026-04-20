# Verification: Agent-Readable Wiki Runtime Context

## Implemented Artifacts

- workflow page:
  - `wiki/ops/agent-readable-wiki-runtime-context.md`
- runtime-context script:
  - `scripts/build_wiki_runtime_context.py`
- sample artifact:
  - `scripts/examples/agent_readable_wiki_runtime_context_sample.json`

## Runtime Bundle Model

Version 1 bundle sections:

- `preferred_context`
- `supporting_context`
- `blocked_context`
- `runtime_caution`

## Current-State Verification

Command sequence:

```bash
python3 scripts/derive_wiki_utilization.py > /tmp/current_wiki_utilization.json
python3 scripts/build_wiki_runtime_context.py /tmp/current_wiki_utilization.json
```

Observed summary:

- `preferred_count: 1`
- `supporting_count: 4`
- `blocked_count: 4`
- `caution_active: true`

Observed differentiation:

- preferred context:
  - `disagreement-management`
- supporting context:
  - `conversation-handoff`
  - `example-driven-capture`
  - `wiki-frontmatter-model`
  - `wiki-naming-model`
- blocked context:
  - `wiki-relation-analysis`
  - `wiki-runtime-context`
  - `wiki-semantic-scoring`
  - `wiki-utilization-layer`

This confirms the runtime bundle preserves preferred, supporting, and blocked context separately instead of flattening them into a single retrieval set.

## Sample Artifact Check

Command run:

```bash
python3 scripts/build_wiki_runtime_context.py > scripts/examples/agent_readable_wiki_runtime_context_sample.json
```

Result:

- sample artifact was generated from current repository state
- sample output matched the live runtime-context run

## OpenSpec Validation

Command run:

```bash
openspec validate add-agent-readable-wiki-runtime-context
```

Result:

- change is valid
- PostHog telemetry emitted network errors to `edge.openspec.dev`
- telemetry failure did not block validation

## Proof Boundary

This change proves:

- the repository can generate a bounded runtime-ready context bundle from utilization output
- preferred, supporting, and blocked items remain separated
- caution is preserved in the runtime bundle

This change does not prove:

- retrieval readiness
- runtime autonomy
- unresolved page understanding
- that the bundle can replace direct source inspection

## Residual Risks

- repository-wide unresolved pressure remains high
- bundle entries are canonical-object level only; they do not yet rank specific pages within each object
- current runtime bundle is still explicit guidance, not integrated live retrieval

## Verification Note

When validating with a file input path, the utilization file must be written before the runtime-context command reads it.

Parallel read/write on the same temp file can produce an empty-file JSON decode failure even when runtime-context logic itself is correct.

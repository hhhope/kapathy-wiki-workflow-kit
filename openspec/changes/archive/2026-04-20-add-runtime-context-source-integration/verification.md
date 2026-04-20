# Verification: Runtime Context Source Integration

## Commands

```bash
python3 scripts/resolve_runtime_context_sources.py > scripts/examples/agent_readable_wiki_runtime_context_source_integration_sample.json
python3 scripts/resolve_runtime_context_sources.py scripts/examples/agent_readable_wiki_runtime_context_sample.json
openspec validate add-runtime-context-source-integration
```

## Before Result

- runtime context could identify preferred, supporting, and blocked canonical objects
- but it did not resolve those objects into concrete repo-visible source paths

## After Result

- live source-integrated runtime artifact resolves:
  - `disagreement-management` into `method -> adr -> spec -> replay evidence`
  - `conversation-handoff` into `method -> spec -> sample`
  - `example-driven-capture` into `method -> spec -> example -> runtime-validation`
  - `wiki-frontmatter-model` and `wiki-naming-model` into `method -> adr -> spec`
- blocked objects remain isolated from first-pass source selection
- `openspec validate add-runtime-context-source-integration` passes

## Proof Boundary

- this is bounded repository-local source guidance
- this is not external source retrieval proof
- this is not autonomous runtime loading proof
- this is not unresolved-page understanding proof

## Residual Risks

- source resolution remains limited to already formalized repo-visible pages
- live repository output can differ from replay output when the current change adds a new canonical object during the same run
- artifact ordering is deterministic but still policy-based rather than empirically optimized

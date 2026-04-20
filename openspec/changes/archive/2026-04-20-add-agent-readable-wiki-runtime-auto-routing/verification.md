# Verification: Runtime Auto Routing

## Commands

```bash
python3 scripts/derive_runtime_auto_routing.py > scripts/examples/agent_readable_wiki_runtime_auto_routing_sample.json
python3 scripts/derive_runtime_auto_routing.py scripts/examples/agent_readable_wiki_runtime_context_source_integration_sample.json
openspec validate add-agent-readable-wiki-runtime-auto-routing
```

## Before Result

- source-integrated runtime could resolve canonical objects into concrete repo-local sources
- but it still did not stage those sources into an explicit first-pass versus second-pass reading order

## After Result

- live runtime auto-routing artifact separates:
  - `open_first`
  - `open_next`
  - `do_not_open_first`
- replay against the archived source-integration sample preserves:
  - `disagreement-management` in `open_first`
  - supporting objects in `open_next`
  - blocked objects outside first-pass routing
- `openspec validate add-agent-readable-wiki-runtime-auto-routing` passes

## Proof Boundary

- this is bounded repository-local runtime routing guidance
- this is not external retrieval proof
- this is not automatic context injection proof
- this is not runtime autonomy proof

## Residual Risks

- live repository output can promote newly formalized objects into `open_first` or `open_next` during the same session
- version 1 preserves source-integration ordering and does not re-rank route sources by empirical usefulness
- route generation still depends on already formalized repo-visible pages only

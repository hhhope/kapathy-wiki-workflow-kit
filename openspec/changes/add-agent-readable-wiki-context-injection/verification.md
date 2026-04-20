# Verification: Automatic Context Injection

## Commands

```bash
python3 scripts/build_runtime_context_injection.py > scripts/examples/agent_readable_wiki_context_injection_sample.json
python3 scripts/build_runtime_context_injection.py scripts/examples/agent_readable_wiki_runtime_auto_routing_sample.json
openspec validate add-agent-readable-wiki-context-injection
```

## Before Result

- runtime auto routing could separate `open_first`, `open_next`, and blocked objects
- but it still did not load page content into a bounded injected-context bundle

## After Result

- live automatic context-injection artifact separates:
  - `injected_first_pass`
  - `secondary_context`
  - `excluded_objects`
- injected sources now include:
  - `page_path`
  - `artifact_type`
  - `source_layer`
  - `title`
  - bounded `excerpt`
- replay against the archived runtime auto-routing sample preserves:
  - first-pass routes in `injected_first_pass`
  - second-pass routes in `secondary_context`
  - excluded objects outside injected first-pass context
- `openspec validate add-agent-readable-wiki-context-injection` passes

## Proof Boundary

- this is bounded repository-local injected-context guidance
- this is not external retrieval proof
- this is not runtime autonomy proof
- this is not agent self-directed execution proof

## Residual Risks

- live repository output can inject newly formalized objects that were not present in earlier replay artifacts
- version 1 uses bounded excerpts rather than full-page semantic selection
- injected context still depends on already formalized repo-visible pages only

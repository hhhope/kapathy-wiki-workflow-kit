# Verification: Bounded Self-Directed Execution

## Commands

```bash
python3 scripts/derive_self_directed_execution.py > scripts/examples/agent_readable_wiki_self_directed_execution_sample.json
python3 scripts/derive_self_directed_execution.py scripts/examples/agent_readable_wiki_context_injection_sample.json
openspec validate add-agent-readable-wiki-self-directed-execution
```

## Before Result

- automatic context injection could separate `injected_first_pass`, `secondary_context`, and `excluded_objects`
- but it still did not express a bounded execution plan the agent could follow next

## After Result

- live bounded self-directed execution artifact separates:
  - `execute_now`
  - `defer_for_followup`
  - `do_not_execute`
- action sources now include only:
  - `page_path`
  - `artifact_type`
  - `source_layer`
  - `title`
- replay against the archived context-injection sample preserves:
  - first-pass injected context in `execute_now`
  - secondary context in `defer_for_followup`
  - excluded objects outside first-pass execution
- `openspec validate add-agent-readable-wiki-self-directed-execution` passes

## Proof Boundary

- this is bounded repository-local execution guidance
- this is not unrestricted agent autonomy proof
- this is not external retrieval proof
- this is not self-directed execution without guardrails

## Residual Risks

- live repository output can promote newly formalized objects into `execute_now` during the same session
- version 1 only derives bounded action bundles; it does not execute side effects
- execution plans still depend on already formalized repo-visible pages only

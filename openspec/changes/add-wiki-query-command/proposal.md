# Change: Add wiki query command

## Why

The repo now exposes the existing wiki runtime layers through `/wiki:*`
commands, but the user still has to choose which layer to invoke.

The LLM Wiki north star is durable compiled context for agents and humans. The
next product step is a task-shaped query entrypoint: given a current task or
question, the agent should produce a bounded set of wiki pages and runtime
artifacts to read first, read next, and avoid using as anchors.

## What Changes

- Add `/wiki:query` as a repo-local Codex command.
- Keep v1 query bounded and auditable:
  - refresh the manifest
  - use existing status/runtime route/context artifacts
  - use explicit text search over wiki pages when a focus term is provided
  - summarize a candidate reading packet with source paths and caution notes
- Add contract tests for the command.
- Document the command in README.

## Out Of Scope

- No vector search.
- No embeddings.
- No hidden semantic ranking.
- No graph UI.
- No automatic OpenSpec change creation.
- No automatic execution of returned context.

## Expected Outcome

Users can ask `/wiki:query <task or focus>` and get a bounded context packet:

- `open_first`
- `open_next`
- `do_not_anchor`
- matching wiki paths from explicit text search
- proof boundary notes

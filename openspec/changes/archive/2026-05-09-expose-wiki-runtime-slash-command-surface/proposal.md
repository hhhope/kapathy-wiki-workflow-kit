# Change: Expose wiki runtime slash command surface

## Why

The wiki already contains many runtime capabilities: manifest/status,
frontmatter, graph extraction, relation analysis, semantic scoring,
utilization, runtime context, source integration, auto routing, context
injection, and self-directed execution.

Only `/wiki:status` is currently exposed as a repo-local Codex slash command.
That makes the product surface feel much smaller than the actual LLM Wiki
runtime stack and forces users to remember scripts and wiki page names.

## What Changes

- Add a repo-local `/wiki:*` command surface for the existing runtime layers.
- Keep each command as a thin wrapper around existing scripts, generated
  artifacts, and wiki/spec records.
- Document the command list in README.
- Add contract tests that ensure the command files exist, use the `/wiki:`
  namespace, and preserve scope boundaries.

## Out Of Scope

- No new graph UI.
- No new score formulas.
- No natural-language query engine.
- No change queue or parallel OpenSpec orchestration.
- No modification to the runtime scripts beyond command-surface wiring.

## Expected Outcome

Users can discover and invoke the existing LLM Wiki runtime as a coherent
repo-level command surface:

- `/wiki:status`
- `/wiki:manifest`
- `/wiki:inbox`
- `/wiki:graph`
- `/wiki:scorecard`
- `/wiki:route`
- `/wiki:context`
- `/wiki:apply`

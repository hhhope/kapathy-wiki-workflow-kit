# Design: Wiki runtime slash command surface

## Current State

The repo has a Codex plugin with one command file:

```text
commands/wiki-status.md
```

The wiki runtime stack already exists in scripts and specs, including:

- `scripts/build_wiki_status.py`
- `scripts/extract_wiki_graph.py`
- `scripts/analyze_wiki_relations.py`
- `scripts/score_wiki_semantics.py`
- `scripts/derive_wiki_utilization.py`
- `scripts/build_wiki_runtime_context.py`
- `scripts/resolve_runtime_context_sources.py`
- `scripts/derive_runtime_auto_routing.py`
- `scripts/build_runtime_context_injection.py`
- `scripts/derive_self_directed_execution.py`

## Command Shape

Use one markdown file per repo-local command under `commands/`.

Each file must:

- show the intended `/wiki:*` invocation in the title
- name the scripts or generated artifacts it uses
- summarize what the command should report back
- state scope boundaries so commands do not silently create, modify, archive,
  or queue OpenSpec changes

## Command Mapping

| Command | Core Loop | Runtime Layer |
|---|---|---|
| `/wiki:status` | Retrieve / Apply | status surface |
| `/wiki:manifest` | Capture / Retrieve | manifest inspection |
| `/wiki:inbox` | Capture | pending inbox triage |
| `/wiki:graph` | Compile | graph extraction and relation analysis |
| `/wiki:scorecard` | Compile / Retrieve | semantic scoring and utilization |
| `/wiki:route` | Retrieve | source-integrated auto routing |
| `/wiki:context` | Retrieve | runtime context bundle |
| `/wiki:apply` | Apply | injected context to bounded execution plan |

## Boundary

These commands expose existing runtime capability; they do not promote
enhancements into core product scope.

`/wiki:apply` is intentionally bounded: it may summarize
`execute_now`, `defer_for_followup`, and `do_not_execute` guidance from the
self-directed execution artifact, but it must not execute those actions or
mark tasks complete by itself.

## Verification

- Add a command-surface test for the expected command files and boundaries.
- Update the existing status command test if needed.
- Run targeted unittest coverage.
- Run `openspec validate expose-wiki-runtime-slash-command-surface --strict`.

# Archive Review: add-wiki-query-command

## Decision

Archive-ready.

## Scope Check

This change added `/wiki:query` as a bounded retrieval command for task-shaped
wiki context. It did not add embeddings, vector search, hidden semantic ranking,
graph UI, change queue automation, or automatic execution.

Implemented surface:

- `commands/wiki-query.md`
- README command list entry for `/wiki:query`
- command contract tests covering `/wiki:query`

## Evidence

| Check | Result |
|---|---|
| Artifacts complete | PASS — proposal, design, spec delta, and tasks are present |
| Tasks complete | PASS — `tasks.md` has 9/9 complete |
| RED baseline | PASS — `tests.test_wiki_runtime_commands` failed before `commands/wiki-query.md` existed |
| Command file present | PASS — `commands/wiki-query.md` documents `/wiki:query` |
| README updated | PASS — README lists `/wiki:query` |
| Contract tests | PASS — `python3 -m unittest tests.test_wiki_runtime_commands tests.test_wiki_status_command tests.test_codex_plugin_marketplace` passed |
| OpenSpec validation | PASS — `openspec validate add-wiki-query-command --strict` passed |
| Diff hygiene | PASS — `git diff --check` passed |

## Boundary Review

`/wiki:query` preserves the intended proof boundary:

- it is bounded retrieval guidance, not semantic search
- it uses explicit text search and existing runtime artifacts
- it forbids embeddings and hidden semantic ranking
- it does not create, modify, archive, or queue OpenSpec changes
- it does not mark OpenSpec tasks complete
- it does not execute `/wiki:apply` or `execute_now` actions

## Residual Risk

The command is still documentation-driven and has not been exercised through
the interactive Codex slash picker in this archive review. The validated proof
is repo-local command shape, command contract tests, README discoverability, and
OpenSpec spec coverage.

## Next Action

Archive this change and sync its spec delta into main specs.

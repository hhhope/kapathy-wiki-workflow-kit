# Design: Wiki query command

## Product Role

`/wiki:query` is the first retrieval-shaped product command. It connects the
existing runtime stack to a user task without pretending the repo has a full
semantic search engine.

## Command Contract

Add:

```text
commands/wiki-query.md
```

The command title is:

```text
/wiki:query
```

## Workflow

1. Refresh status:

   ```bash
   python3 scripts/build_wiki_status.py
   ```

2. Build or inspect route/context artifacts:

   ```bash
   python3 scripts/derive_runtime_auto_routing.py > /tmp/wiki-runtime-auto-routing.json
   python3 scripts/build_runtime_context_injection.py > /tmp/wiki-context-injection.json
   ```

3. If the user provided focus text, run explicit repository text search:

   ```bash
   rg -n "<focus text>" wiki openspec/specs commands README.md
   ```

4. Return a bounded context packet:

   - `open_first`
   - `open_next`
   - `do_not_anchor`
   - explicit text matches
   - caution and proof boundary notes

## Boundaries

The command must state that v1 query is not semantic search. It cannot:

- use embeddings
- invent hidden rankings
- create, modify, archive, or queue OpenSpec changes
- mark OpenSpec tasks complete
- execute `/wiki:apply` results

## Verification

- Add/update command-surface tests.
- Run targeted unittest coverage.
- Run OpenSpec strict validation.
- Run `git diff --check`.

## Context

`add-source-manifest-and-wiki-status` added:

- `scripts/build_wiki_status.py`
- `wiki/status/manifest.json`
- `wiki/status/wiki-status.md`

The missing surface is a short command entrypoint.

## Decision

Add a Claude slash command:

```text
.claude/commands/wiki/status.md
```

Expected invocation:

```text
/wiki:status
```

The command should:

1. Run `python3 scripts/build_wiki_status.py`.
2. Report that it refreshed:
   - `wiki/status/manifest.json`
   - `wiki/status/wiki-status.md`
3. Read or summarize `wiki/status/wiki-status.md`.
4. Preserve scope boundaries: no query, scorecard, graph UI, or change queue.

## Boundaries

- This is a command wrapper only.
- Existing untracked `.claude/commands/opsx/*` files are not part of this
  change.
- The command does not change the generator behavior.

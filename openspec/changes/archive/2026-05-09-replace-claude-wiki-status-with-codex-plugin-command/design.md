# Design

## Decision

Use Codex's plugin command shape instead of Claude's command directory:

```text
.codex-plugin/plugin.json
commands/wiki-status.md
```

Examples in the local Codex plugin cache expose commands from a plugin root's
`commands/*.md` files. Their invocation shape is plugin-name plus command name,
for example `/vercel:status`; therefore this repo command is documented as:

```text
/report-wiki-portfolio:wiki-status
```

## Command Behavior

The command instructs Codex to:

1. Run `python3 scripts/build_wiki_status.py`.
2. Read `wiki/status/wiki-status.md`.
3. Summarize the generated status.
4. Point to `wiki/status/manifest.json` and `wiki/status/wiki-status.md`.

## Boundary

This change fixes the command surface only. It does not expand the LLM Wiki
runtime into query, scorecard, graph UI, or change queue.

## Residual Risk

Codex's global custom prompt support uses `~/.codex/prompts`, and upstream has
not planned root `.codex/prompts` lookup. This implementation therefore uses
the repo plugin form, which is the available repo-distributable command shape.

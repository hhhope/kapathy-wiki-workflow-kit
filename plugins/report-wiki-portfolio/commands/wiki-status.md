---
description: Refresh the repo-local LLM Wiki manifest and summarize the default health report.
argument-hint: optional focus text
---

# /wiki:status

Refresh and summarize the repository's default LLM Wiki health surface. Use
this command as the first health entry when the user asks whether the wiki is
healthy or what needs attention.

## Workflow

1. Run:

```bash
python3 scripts/build_wiki_status.py
```

2. Read `wiki/status/wiki-status.md`.
3. Summarize the status in the conversation, including:
   - wiki page count
   - source record count
   - pending inbox count
   - active and complete OpenSpec change counts
   - identity coverage
   - relation coverage
   - domain taxonomy health from the existing frontmatter checker
   - graph parse health for relation frontmatter that parsed as empty
   - the pending inbox list when present
4. Point the user to:
   - `wiki/status/manifest.json`
   - `wiki/status/wiki-status.md`

## Default Health Surface

Treat `/wiki:status` as the default health entry point for inbox, OpenSpec,
identity, relation, domain taxonomy, and graph parse diagnostics. It should
surface domain taxonomy drift from `scripts/check_wiki_frontmatter.py` without
duplicating the allowed domain or `ops_area` vocabulary from
`wiki/config/frontmatter-taxonomy.yaml`.

Graph parse health should call out pages where raw relation fields such as
`derived_from` or `related_objects` exist but parsed relation values are empty.
Route repairs through `/wiki:apply` or OpenSpec as appropriate; this command is
diagnostic only.

## Boundaries

- This command is a repo-local Codex plugin command, not a global prompt and not a Claude command.
- Do not implement scorecard, graph UI, natural-language query engine, or change queue.
- Do not create, modify, archive, open, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not treat generated status as product judgment; it is only a source manifest and routing surface.

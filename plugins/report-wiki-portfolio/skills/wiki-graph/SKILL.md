---
name: wiki-graph
description: Inspect the report wiki structural graph and relation-analysis runtime layers.
---

Use the wiki graph runtime surface for the report wiki repository.

Command contract: `plugins/report-wiki-portfolio/commands/wiki-graph.md`

When triggered:

1. Confirm the current repository has `scripts/extract_wiki_graph.py`.
2. Follow the command contract when present.
3. Run or reference `python3 scripts/extract_wiki_graph.py`,
   `python3 scripts/analyze_wiki_relations.py`, and
   `python3 scripts/summarize_wiki_graph.py`.
4. Read generated graph, relation-analysis, and summary JSON when available.
5. Summarize canonical objects, source layers, relation counts, warnings, and
   representative pages as structural evidence only.

Boundaries:

- Do not create, modify, archive, or queue OpenSpec changes.
- Do not mark OpenSpec tasks complete.
- Do not execute queued work.
- Do not claim semantic understanding from graph structure alone.

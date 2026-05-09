---
description: Run the existing wiki graph extraction and relation-analysis scripts, then summarize structural graph output.
argument-hint: optional canonical object or artifact focus
---

# /wiki:graph

Extract and summarize the repository's agent-readable wiki graph structure.

## Workflow

1. Run the live graph extractor:

```bash
python3 scripts/extract_wiki_graph.py > /tmp/wiki-graph.json
```

2. Run relation analysis from the extracted graph:

```bash
python3 scripts/analyze_wiki_relations.py /tmp/wiki-graph.json > /tmp/wiki-relation-analysis.json
```

3. Read `/tmp/wiki-graph.json`, `/tmp/wiki-relation-analysis.json`, and, when useful, the sample artifacts:
   - `scripts/examples/agent_readable_wiki_graph_sample.json`
   - `scripts/examples/agent_readable_wiki_relation_analysis_sample.json`
4. Summarize the structural graph output, including:
   - node count
   - edge count
   - warning count
   - cross-layer object count
   - artifact type and relation type highlights
   - unresolved warning concentration when present
5. Point the user to the governing wiki pages:
   - `wiki/ops/agent-readable-wiki-graph-extraction.md`
   - `wiki/ops/agent-readable-wiki-relation-analysis.md`

## Boundaries

- This command is a thin wrapper over `scripts/extract_wiki_graph.py`, `scripts/analyze_wiki_relations.py`, and their JSON artifacts.
- Do not create, modify, archive, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not implement graph UI, natural-language query engine, or change queue.
- Do not treat structural extraction as semantic understanding, retrieval quality, or rollout proof.
- Do not infer identities for unresolved pages beyond what the scripts output.

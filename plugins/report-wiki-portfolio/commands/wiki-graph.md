---
description: Run the existing wiki graph extraction and relation-analysis scripts, then summarize structural graph output.
argument-hint: optional canonical object or artifact focus
---

# /wiki:graph

Extract and summarize the repository's agent-readable wiki graph structure as
an explainable object view. Use this command as the structural drilldown when a
page, object, layer, artifact, or relation looks disconnected after the default
health view.

## Workflow

1. Run the live graph extractor:

```bash
python3 scripts/extract_wiki_graph.py > /tmp/wiki-graph.json
```

2. Run relation analysis from the extracted graph:

```bash
python3 scripts/analyze_wiki_relations.py /tmp/wiki-graph.json > /tmp/wiki-relation-analysis.json
```

3. Build the bounded object-view summary:

```bash
python3 scripts/summarize_wiki_graph.py --graph /tmp/wiki-graph.json --relation-analysis /tmp/wiki-relation-analysis.json > /tmp/wiki-graph-summary.json
```

4. Read `/tmp/wiki-graph-summary.json`, `/tmp/wiki-graph.json`, `/tmp/wiki-relation-analysis.json`, and, when useful, the sample artifacts:
   - `scripts/examples/agent_readable_wiki_graph_sample.json`
   - `scripts/examples/agent_readable_wiki_relation_analysis_sample.json`
5. Summarize the structural graph output, including:
   - node count
   - edge count
   - warning count
   - cross-layer object count
   - object-level source layers and artifact types
   - representative pages
   - whether raw `openspec/specs` nodes are present in the graph
   - readable object summaries with spec details collapsed by default
   - artifact type and relation type highlights
   - unresolved warning concentration when present
6. Point the user to the governing wiki pages:
   - `wiki/ops/agent-readable-wiki-graph-extraction.md`
   - `wiki/ops/agent-readable-wiki-relation-analysis.md`

## Structural Drilldown

Keep `/wiki:graph` focused on structure. Raw graph extraction includes
`wiki/ops`, `wiki/adr`, `openspec/specs`, and `wiki/examples`; do not remove
raw `openspec/specs` graph nodes because they prove formalization depth.

Readable summaries should favor object-level evidence and collapse spec details
by default. Expand spec details only when the user is checking archive review,
formalization proof, or another spec-specific question.

## Boundaries

- This command is a thin wrapper over `scripts/extract_wiki_graph.py`, `scripts/analyze_wiki_relations.py`, `scripts/summarize_wiki_graph.py`, and their JSON artifacts.
- Do not create, modify, archive, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not implement graph UI, natural-language query engine, or change queue.
- Do not treat structural extraction as semantic understanding, retrieval quality, or rollout proof.
- Do not infer identities for unresolved pages beyond what the scripts output.

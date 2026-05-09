---
description: Run the existing wiki semantic scoring and utilization scripts, then summarize object strength bands.
argument-hint: optional canonical object focus
---

# /wiki:scorecard

Build and summarize the repository's wiki semantic scorecard.

## Workflow

1. Run semantic scoring:

```bash
python3 scripts/score_wiki_semantics.py > /tmp/wiki-semantic-scoring.json
```

2. Run utilization banding from the score output:

```bash
python3 scripts/derive_wiki_utilization.py /tmp/wiki-semantic-scoring.json > /tmp/wiki-utilization.json
```

3. Read `/tmp/wiki-semantic-scoring.json`, `/tmp/wiki-utilization.json`, and, when useful, the sample artifacts:
   - `scripts/examples/agent_readable_wiki_semantic_scoring_sample.json`
   - `scripts/examples/agent_readable_wiki_utilization_sample.json`
4. Summarize the scorecard, including:
   - scored object count
   - score range
   - strong, moderate, and weak object counts
   - preferred, cautious, and blocked utilization counts
   - repository-wide caution or unresolved warning pressure
5. Point the user to the governing wiki pages:
   - `wiki/ops/agent-readable-wiki-semantic-scoring.md`
   - `wiki/ops/agent-readable-wiki-utilization-layer.md`

## Boundaries

- This command is a thin wrapper over `scripts/score_wiki_semantics.py`, `scripts/derive_wiki_utilization.py`, and their JSON artifacts.
- Do not create, modify, archive, or queue OpenSpec changes from this command.
- Do not mark OpenSpec tasks complete from this command.
- Do not implement graph UI, natural-language query engine, or change queue.
- Do not add or change score formulas from this command.
- Do not treat score bands as semantic truth, retrieval readiness, or permission to skip direct source inspection.

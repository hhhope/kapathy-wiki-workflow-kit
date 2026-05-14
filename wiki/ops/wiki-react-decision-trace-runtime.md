---
canonical_object: wiki-react-decision-trace
artifact_type: method
related_objects:
  - wiki-runtime-skill-surface
  - wiki-frontmatter-taxonomy-gate
  - wiki-semantic-scoring
  - wiki-relation-analysis
derived_from:
  - openspec/changes/introduce-wiki-react-decision-trace-eval/design.md
validated_by:
  - tests/test_wiki_decision_trace_eval.py
---

# wiki-react-decision-trace / method

This page defines the first bounded ReAct layer for repo-local wiki runtime
skills. It is a decision contract, not a new autonomous runtime.

## Loop

Use this compact loop for high-risk wiki work:

1. Intent: classify the request shape.
2. Action: choose bounded wiki observations to read or run.
3. Observation: separate static facts from exploratory judgments.
4. Decision: state the route and next step.
5. Boundary: state what is allowed and what must not happen.

## Decision Trace

Emit a compact `decision_trace` when the request involves `wiki-apply`,
frontmatter repair, article learning, exploratory scoring, relation
exploration, queued execution, or promotion into ADR/spec/skill behavior.

Minimum fields:

```json
{
  "intent": "frontmatter_repair",
  "evidence_object": "wiki/ops/example.md",
  "risk_level": "medium",
  "actions": ["classify_intent", "run_static_precheck"],
  "observations": {
    "static_facts": ["target.repair_hints available"],
    "exploratory_judgments": []
  },
  "decision": "suggest_page_frontmatter_fix",
  "boundary": "bounded_page_frontmatter_fix",
  "forbidden_actions_checked": ["taxonomy_mutation", "mark_openspec_done"]
}
```

## Static Facts

Static facts come from deterministic repo-local tools or artifacts:

- `scripts/wiki_gate_precheck.py`
- `scripts/check_wiki_frontmatter.py`
- `wiki/status/manifest.json`
- `wiki/status/wiki-status.md`
- graph, relation, scorecard, context, queue, and apply JSON artifacts

Static facts can support a hard gate only when the underlying checker owns that
gate.

## Exploratory Judgments

Article weight, temperature, source confidence, relation strength, and
promotion readiness are exploratory judgments in this version. They can guide a
candidate route, but they must not become hard gates or automatic promotions.

## Eval

Replay cases live in `wiki/evals/wiki-react-trace-cases.json`. The eval runner
validates agent-produced traces:

```bash
python3 scripts/eval_wiki_decision_trace.py --traces /tmp/wiki-decision-traces.json
```

The runner checks trace structure, allowed intents, required actions, forbidden
actions, and boundaries. It does not infer natural-language intent.

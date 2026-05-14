# Design: wiki ReAct decision trace eval

## Architecture

The first version has three parts:

1. Shared decision-trace reference
   - Defines the bounded ReAct loop: intent, action, observation, decision,
     boundary.
   - Requires a compact, auditable `decision_trace`.
   - Separates `static_facts` from `exploratory_judgments`.

2. Wiki skill integration
   - High-risk wiki skills reference the decision-trace contract before acting:
     `wiki-query`, `wiki-apply`, `wiki-explore`, and `wiki-scorecard`.
   - Existing status, manifest, graph, scorecard, context, and apply scripts
     remain the observation sources.

3. Deterministic eval harness
   - Case files live under `wiki/evals/`.
   - Agent or manual replay produces trace JSON.
   - Python validates trace structure and boundaries. It does not infer intent
     from the user input.

## Trace Contract

Each trace includes:

- `case_id`
- `input`
- `intent`
- `evidence_object`
- `risk_level`
- `actions`
- `observations.static_facts`
- `observations.exploratory_judgments`
- `decision`
- `boundary`
- `forbidden_actions_checked`

## Eval Contract

Each case can specify:

- `allowed_intents`
- `required_actions_all`
- `required_actions_any`
- `required_boundary`
- `forbidden_actions`
- `requires_static_facts`
- `requires_exploratory_judgments`

The harness passes only when the trace satisfies the case. If a case allows
multiple intents, any listed intent may pass. This keeps agent judgment flexible
while making boundaries strict.

## Boundary

Static facts can support hard gates only when they come from deterministic wiki
tools, such as frontmatter precheck, manifest, or status.

Exploratory judgments, including article weight, temperature, source
confidence, and relation strength, remain candidate judgments unless a later
OpenSpec change stabilizes their semantics.

## Verification

- RED/GREEN unit tests for `eval_wiki_decision_trace.py`.
- Runtime skill tests require high-risk wiki skills to reference the shared
  decision-trace contract.
- Behavior asset evaluation records replay evidence and parent-gate
  preservation.

---
layer: adr
domain: none
canonical_object: wiki-runtime-layer-boundary
artifact_type: adr
formalizes:
  - wiki-runtime-layer-boundary
derived_from:
  - wiki-runtime-layer-contract
  - wiki-react-decision-trace
  - brainstorming-drift-wiki-trace
---

# ADR-0033 Wiki React Eval Apply OpenSpec Boundary

## Status

Accepted

## Context

The wiki runtime now has several adjacent surfaces:

- `$wiki-react` for explicit route and boundary decisions
- `eval_wiki_decision_trace.py` for validating agent-produced traces
- `/wiki:apply` for bounded self-directed execution preview
- repair-route labels for diagnostic classes
- OpenSpec for runtime and workflow lifecycle

During the 2026-05-14 wiki runtime discussion, these layers were repeatedly
substituted for each other. The agent treated eval as a repair path, treated
`/wiki:apply` as a repair executor, and treated repair-route labels from design
documents as if executable repair infrastructure already existed.

The repository needs a stable decision that prevents these layers from being
used as substitutes for each other.

## Decision

Wiki runtime layers must not substitute for each other.

- `$wiki-react` owns explicit routing and `decision_trace` production for
  ambiguous or high-risk wiki requests.
- `eval_wiki_decision_trace.py` validates agent-produced traces against replay
  cases. It does not classify natural-language intent, execute repairs, or
  approve OpenSpec lifecycle steps.
- `/wiki:apply` previews bounded self-directed execution or context
  suggestions. It does not directly mutate runtime files, scripts, skills,
  AGENTS, command behavior, or OpenSpec state.
- Repair-route labels name diagnostic classes. They do not prove executable
  repair infrastructure exists.
- OpenSpec owns runtime, workflow, skill, AGENTS, command behavior, and repair
  capability changes.

## Consequences

- Passing trace eval proves only that trace shape and boundary checks passed.
- `/wiki:apply` output remains preview or suggestion unless a separate approved
  implementation path authorizes action.
- Naming a repair route such as `runtime-parser-fix` or `readable-graph-fix`
  does not imply implementation exists.
- Runtime or workflow behavior changes must not be hidden inside status, graph,
  apply, scorecard, or eval surfaces.
- Future wiki runtime explanations must identify which layer owns routing,
  validation, preview, route labeling, and lifecycle approval.

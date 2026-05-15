---
layer: ops
domain: wiki
ops_area: wiki-runtime
canonical_object: wiki-runtime-layer-contract
artifact_type: method
created_at: 2026-05-14
derived_from:
  - openspec/changes/stabilize-wiki-runtime-layer-contract/design.md
formalizes:
  - wiki-runtime-layer-contract
language: en
status: accepted
title: wiki-runtime-layer-contract / method
type: method
updated_at: 2026-05-14
---

# wiki-runtime-layer-contract / method

This page defines the stable layer contract for the repo-local wiki runtime.
It exists to keep the skill entrypoints, deterministic tools, decision traces,
and lifecycle gates from being treated as interchangeable.

## Architecture

```text
Core loop
  Capture -> Compile -> Retrieve -> Apply
    |
    v
Skill entrypoints
  wiki-react as explicit router and decision-trace entrypoint
  wiki-status / wiki-query / wiki-apply / wiki-scorecard as direct domain skills
    |
    v
Decision contract
  high-risk or ambiguous routes emit decision_trace before acting
    |
    v
Observation tools
  status, manifest, frontmatter precheck, graph, relation, scorecard,
  context, apply preview, queue preview
    |
    v
Boundaries
  inspect-only | candidate judgment | bounded page fix |
  requires user confirmation | requires OpenSpec
    |
    v
Eval and lifecycle gates
  trace eval validates agent-produced decision traces
  behavior asset checker validates behavior-change evidence
  OpenSpec owns workflow/runtime change lifecycle
```

## Layer Responsibilities

| Layer | Owns | Does not own |
|---|---|---|
| Core loop | The stable wiki work pattern: capture, compile, retrieve, apply. | Concrete routing decisions for every task. |
| Skill entrypoints | Human- and agent-facing entrypoints for wiki work. | Replacing domain-specific skills with one universal command. |
| Decision contract | The `decision_trace` shape for high-risk or ambiguous routes. | Deterministic scoring, linting, or lifecycle approval. |
| Observation tools | Script output and generated artifacts that describe current state. | Natural-language intent classification. |
| Boundaries | The action class allowed after observations are read. | Silent escalation into workflow changes. |
| Eval and lifecycle gates | Trace validation, behavior-asset validation, and OpenSpec lifecycle. | Substituting one gate for another. |

## Capability And Ownership Rules

`wiki-react` is the explicit router. It is not a replacement for domain skills.
Use it when the request is ambiguous, high-risk, or likely to cross from
inspection into repair, queueing, governance, or OpenSpec lifecycle decisions.
Its output should make the route visible through `decision_trace`.

Domain skills can still be called directly. `wiki-status`, `wiki-query`,
`wiki-apply`, and `wiki-scorecard` remain first-class entrypoints when the user
already knows the desired surface. Direct use does not bypass the decision
contract: high-risk routes still emit `decision_trace` before action.

Python tools are observations or actions. They can build status, precheck
frontmatter, derive graph/runtime artifacts, preview apply suggestions, and run
evals. They are not natural-language intent classifiers and must not decide
whether a user meant status, query, repair, or lifecycle work.

The scorecard is an observation layer. It describes semantic coverage,
utilization, blockers, and caution signals. It does not judge agent behavior,
approve wiki repairs, or replace OpenSpec review.

The eval harness validates traces. `scripts/eval_wiki_decision_trace.py`
checks whether agent-produced traces satisfy the decision contract for replay
cases. In short: trace eval validates agent-produced decision traces. It does
not replace the behavior-asset checker or OpenSpec task review.

The behavior asset checker validates behavior-change evidence. It checks
whether behavior changes carry the required evidence shape. It does not approve
runtime lifecycle changes by itself.

OpenSpec owns workflow/runtime change lifecycle. New or changed runtime
capabilities, workflow defaults, skill semantics, and governance behavior go
through scoped OpenSpec changes. Observation tools and scorecards can surface
evidence, but they do not own proposal, implementation, completion, or archive
decisions.

## Choosing An Entry Point

| Need | Use | Reason |
|---|---|---|
| Unsure which wiki route applies, or action risk is unclear | `wiki-react` | Produces a visible `decision_trace` before routing onward. |
| Current wiki health, manifest counts, blockers, and next inspection routes | `wiki-status` | Reads generated status and summarizes drift without repairing it. |
| Bounded retrieval for a task or topic | `wiki-query` | Builds context from route, context, and explicit text-search evidence. |
| Inspect bounded self-directed execution suggestions | `wiki-apply` | Previews candidate actions without silently applying workflow changes. |
| Semantic scoring and utilization diagnostics | `wiki-scorecard` | Observes coverage and caution bands without owning behavior judgment. |

## Proof Boundary

This contract documents the current architecture and ownership boundaries. It
does not add new runtime capability, change scorecard algorithms, or change
eval case semantics.

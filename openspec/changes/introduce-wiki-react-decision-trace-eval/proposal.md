# Proposal: introduce wiki ReAct decision trace eval

## Summary

Add a first-version bounded ReAct decision-trace contract for wiki runtime
skills, plus a deterministic eval harness that validates agent-produced traces
without replacing agent intent judgment.

## Motivation

The wiki skill runtime surface is now closed around repo-local skills, but the
runtime decision loop is not closed. Agents can still blur status lookup,
frontmatter repair, article learning, exploratory scoring, relation exploration,
and execution requests unless each wiki operation records a compact route and
boundary decision.

This change introduces a small, auditable layer:

- Agents classify intent and produce a decision trace.
- Existing wiki scripts remain the observation sources.
- Python eval validates trace shape, required actions, forbidden actions, and
  static-vs-exploratory boundaries.
- Scorecard remains an observation source, not the behavior judge.

## Scope

- Add a shared wiki ReAct decision-trace reference for repo-local wiki skills.
- Add sample eval cases under `wiki/evals/`.
- Add `scripts/eval_wiki_decision_trace.py`.
- Add tests for trace validation and runtime skill references.
- Update a bounded set of high-risk wiki skills to reference the decision trace
  contract.

## Non-Goals

- Do not restore plugin or slash command runtime.
- Do not make Python perform LLM intent classification.
- Do not change scorecard weights, article temperature semantics, or relation
  strength semantics.
- Do not allow autonomous writes, taxonomy changes, OpenSpec completion, or
  archive from the ReAct layer.

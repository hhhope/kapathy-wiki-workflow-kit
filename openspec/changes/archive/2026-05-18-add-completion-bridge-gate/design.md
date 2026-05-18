# Design: add completion bridge gate

## Problem

The current workflow has strong stop and verification rules, but completion
answers can still collapse into an engineering delivery checklist. That is
insufficient when the user's original request was partly evaluative, such as:

- "Does this process work?"
- "What did the dual-track experiment show?"
- "Why did this require me to point it out?"
- "What should we change next because of this run?"

The bridge must preserve two different truths:

1. Delivery evidence: what changed, what was verified, what remains blocked.
2. Original question: what the completed work tells us about the user's
   north-star, method experiment, or decision.

## Proposed Model

Add a completion bridge gate with three slots:

- `delivery_result`: concise implementation or archive outcome.
- `original_question`: the user-facing north-star, experiment, or evaluation
  question if one was explicit in the conversation or active trace.
- `bridge_answer`: the answer, partial answer, or reason it cannot yet be
  answered.

If there is no explicit original question, the gate should remain lightweight:
ordinary delivery summary is enough.

## Trigger Points

The gate should be evaluated when the assistant is about to report that scoped
work is complete, verified, archive-ready, or archived.

It is especially important when:

- the user framed the work as an experiment or process test;
- the session repeatedly returned to the same north-star;
- a trace or medical-case item identifies completion bridge drift;
- the final answer would otherwise only list files, tests, commits, or
  OpenSpec status.

## Boundaries

- The bridge does not authorize further implementation after OpenSpec tasks are
  complete.
- The bridge can recommend archive review, a new OpenSpec proposal, a retro, or
  a no-op.
- The bridge must say when the original question remains unanswered rather than
  overclaiming.
- The bridge should be concise and should not force long retrospectives for
  small tasks without an explicit broader question.

## Implementation Notes

A later implementation should choose the narrowest behavior surface. Likely
targets are:

- repo workflow guidance for completion reporting;
- a focused checker or replay fixture for completion-bridge cases;
- minimal medical-case evidence update if this candidate is closed.

The implementation should not edit skills or AGENTS without the required
behavior-asset gates and replay evidence.

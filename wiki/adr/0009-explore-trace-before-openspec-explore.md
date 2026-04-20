# ADR-0009 Explore Trace Before OpenSpec Explore

## Status

Accepted

## Context

`openspec-explore` discussions can produce assumptions, risks, and topic-opening context before any formal OpenSpec change exists. In this repository, that context was often left only in chat history, which made it hard to recover why an exploration started or whether a later discussion was continuing the same topic.

The repository already uses `wiki/ops/` as the operating-layer entry point for new inputs and evolving work threads. It needs a stable default for exploration traces without forcing early-stage thinking into full OpenSpec artifacts.

## Decision

- Every `openspec-explore` run must leave a repo-visible trace in `wiki/ops/` before the exploration continues.
- The trace reuses the existing `intake` page type and marks the page as an explore trace rather than introducing a new page type.
- Same-topic exploration updates the existing trace instead of creating duplicate pages.
- The trace records topic-opening context only. Formal scope, design, and progress still belong to OpenSpec artifacts when the exploration becomes an active change.

## Consequences

- Exploration history becomes recoverable from the repository without depending on chat history alone.
- `wiki/ops/` remains the single operating-layer intake surface for both material inputs and exploration traces.
- The repository avoids forcing every explore thread into a proposal or handoff too early.

## Context

The current `learning-capture` router already says that external articles,
repos, READMEs, and examples used as learning/reference/adaptation material
should trigger learning capture. It also says a bare source inside an active
learning, governance, reusable-method, or method-calibration thread is learning
material.

The remaining gap is operational observability: after a live replay, the user
asked whether the next link would actually route correctly. The answer existed
in chat, but chat is not a durable governance asset.

## Strategy

Use the replay matrix as the smallest governance anchor.

The runtime strategy is:

1. Detect whether the current thread supplies learning/governance context.
2. Classify the source shape before reading deeply.
3. Use a source-specific reader when needed, such as `weixin-reader`.
4. Run admission and score gates before deep read.
5. Route the result to the lowest durable layer:
   - `wiki/ops` for workflow, governance, or operating learning
   - `wiki/examples` for reusable output-shape examples
   - weekly-review candidate when topic fit is weak
6. Block promotion into `AGENTS.md`, skill hard rules, spec `SHALL`, or
   archive-ready claims unless evidence-backed promotion gates pass.

## Boundary

This change does not make every link a wiki page. The replay must preserve
negative paths:

- latest-news or fact lookup -> ordinary answer path
- raw body fetch only -> source-specific reader without learning capture
- bare link outside learning context -> ask/clarify or ordinary lookup
- low-scoring source -> skip reason or brief candidate
- secondary interpretation -> candidate evidence unless supported by primary
  source or local proof

## Evidence Plan

Use documentation-level behavior replay:

| Input shape | Expected route |
|---|---|
| Bare article link inside current learning/governance thread | `learning-capture` -> article module -> score -> wiki if >=75 |
| WeChat article link inside current learning/governance thread | `weixin-reader` -> article module -> score -> wiki if >=75 |
| GitHub repo/README link asking what to learn | repo/README module -> score -> wiki if >=75 |
| Raw fetch request | no learning capture; use source-specific reader only |
| Bare link with no local reuse context | clarify or ordinary lookup; no durable wiki by default |

## Risk

- This remains static replay evidence, not multi-session telemetry.
- The strategy can still fail if future agents skip the skill router despite the
  trigger.
- A future root/global change may need to move the generic part of
  `learning-capture` out of repo-local ownership.

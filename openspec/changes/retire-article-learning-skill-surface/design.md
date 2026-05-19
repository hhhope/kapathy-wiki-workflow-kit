# Design

## Runtime Routing

`learning-capture` is the only active runtime skill for learning requests. It
classifies whether the input is learning material, then routes by evidence
object to article, repo/README, example/reference, or mixed-source references.

`article-learning-capture` is retired as a skill surface. Article workflow
content may survive only as `learning-capture` reference material or historical
archive context.

## Article Rule Migration

The implementation classifies old article-skill content before migration:

- Keep article-only source metadata, source class, source grounding,
  score-first triage, copyright boundary, structured translation notes,
  transferable learning, rejected moves, and promotion boundaries.
- Deduplicate general learning routing and promotion rules already owned by
  `learning-capture` and repo governance.
- Delete old skill description wording, compatibility-entry wording, and
  trigger-oriented `When To Use` text.

## Chinese-First Durable Learning Output

Durable internal learning artifacts in `wiki/sources` and `wiki/ops` default to
Chinese. English remains valid when the user asks for English, the target
artifact is English-first, or the audience requires English.

## Evidence

The change records RED baseline, prior-art/common-rule dedupe, GREEN result,
pressure scenarios, behavior replay, OpenSpec validation, and behavior-asset
checker output in `evaluation.md`.

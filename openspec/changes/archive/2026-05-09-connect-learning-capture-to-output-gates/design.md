## Context

The repository now has two adjacent workflows:

- `learning-capture`: decides whether external material should become local
  learning, then scores, grounds, and routes it.
- `public-report-quality-gate`: checks reader-facing output before sync,
  publication, or review-ready claims.

The missing handoff is explicit reuse. A learning artifact can exist, but the
output gate does not require the agent to show how that artifact shaped the
output.

## Decision

Add a lightweight learning-output reuse gate. The gate does not replace
learning capture or report quality review. It adds one handoff contract:

> If a reader-facing output is based on learned references, the output process
> must show which learning artifacts were considered, which learning points
> were used, where they appear in the output, and why any relevant point was
> skipped.

## Field Model

Learning records should preserve two separate concepts:

- `domain`: the topic or domain of the source, such as `agent harness`,
  `skill authoring`, `wiki governance`, or `public report writing`.
- `reusable capability type`: the kind of output capability learned from the
  source.

Initial reusable capability types:

- `content`: concepts, arguments, facts, or claims
- `structure`: article order, section rhythm, reading map, split strategy
- `visual`: diagram role, visual density, lifecycle map, comparison graphic
- `evidence`: metrics, cases, observable scenes, proof style
- `boundary`: adoption boundary, future/current separation, non-claims

These are not business domains. They are the ways a source can change a future
output.

## Output Use Map

Before drafting or claiming review-ready status for a reference-shaped
reader-facing output, create or update the gate-review artifact with:

- learning artifact path or source reference
- domain/topic
- reusable capability type
- learning point
- intended output use: section, visual, metric, boundary, or skip
- skip reason when not used

The output use map is process evidence. The final article does not need to
publicly cite internal wiki paths unless the user asks for citations.

## Boundaries

- This change does not require every source link to become learning.
- This change does not force every learned point into the next output.
- This change does not treat source learning as proof of local implementation.
- Promotion into `AGENTS.md`, specs, hard skill rules, or root skills still
  requires the existing evidence-backed promotion path.

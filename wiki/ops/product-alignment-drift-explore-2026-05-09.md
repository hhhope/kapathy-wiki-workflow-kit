---
canonical_object: product-alignment-drift
artifact_type: explore-trace
related_objects:
- report-wiki-product-plan
- scorecard-calibration-gap
- learning-source-routing-gap
- product-capability-and-graph-gap
- obsidian-wiki-reference-gap-review
derived_from:
- wiki/ops/report-wiki-product-plan-2026-05-09.md
- wiki/ops/obsidian-wiki-project-gap-review-2026-05-09.md
- wiki/ops/scorecard-calibration-gap-explore-2026-05-09.md
- wiki/ops/learning-source-routing-gap-explore-2026-05-09.md
- wiki/ops/product-capability-and-graph-gap-explore-2026-05-09.md
---

# product-alignment-drift / explore-trace

## Trigger

User observed that after comparing the product plan, the GitHub reference case,
scorecard calibration, and learning flow, the current structure is still unclear:
learning has been connected, but drift is too high.

## Explore Boundary

This is `$openspec-explore`: thinking and requirement shaping only.

No product plan, scorecard, skill, source routing, graph script, or OpenSpec
change has been implemented in this trace.

## Diagnosis

The current repository has many useful pieces, but the product center is not yet
strong enough to govern the pieces.

```text
source routing     exists, but original-source layer is incomplete
learning capture   exists, but source score can blur into output quality
report gate        exists, but readiness and quality still drift
graph extraction   exists, but process files remain weakly connected
product plan       exists, but not yet enforced by status/dashboard workflow
```

So the product is currently better described as:

```text
many strong governance atoms
  + weak operating backbone
  = repeated local fixes and recurring drift
```

## Drift Pattern

```text
external source
  -> learning note
  -> product idea
  -> report / skill / gate tweak
  -> score / PASS / Complete
  -> user finds mismatch
  -> reopen / trace / new gap
```

The pattern repeats because every subsystem has its own proof style:

| Subsystem | Local Proof | Drift Risk |
|---|---|---|
| Learning | admission score, reused/modified/rejected | high score becomes quality proof |
| Sources | URL/source map | missing source-layer record for deep-read references |
| Reports | hard gates, numeric score | gate repair becomes review readiness |
| Behavior | RED/GREEN, runtime replay | static wording gets mistaken for runtime proof |
| Graph | extractor output | covered-layer graph mistaken for whole-product graph |
| Product | planning page | plan not connected to computed status |

## Root Cause

The root cause is not only loose scoring or unclear requirements. The root cause
is that the repo lacks a product-level operating contract that names:

```text
1. object type
2. target state
3. evidence required
4. score type
5. source layer
6. readiness label
7. next status transition
```

Without that contract, the agent can satisfy a nearby local gate while missing
the user's actual target.

## Corrected Product Backbone

The product should be governed by one backbone:

```text
Source
  -> Learning
  -> Structure
  -> Output
  -> Behavior
  -> Status
```

Each transition needs its own evidence:

```text
Source -> Learning
  source record + admission score + source boundary

Learning -> Structure
  reused / modified / rejected + product target

Structure -> Output
  explicit output job + split decision + reader target

Output -> Behavior
  gate review + runtime replay when future behavior is claimed

Behavior -> Status
  computable dashboard + unresolved queue
```

## Planning Implication

The next scoped change should not start from more writing, more scoring, or a
graph viewer. It should start from a product status contract:

```text
add-product-status-contract
  includes:
    - object types
    - readiness labels
    - score types
    - required evidence by transition
    - unresolved / blocked / draft / review-ready states
    - dashboard output
```

`wiki-status + relation-hygiene` remains the likely first implementation slice,
but it should be framed as the first slice of product status, not just graph
cleanup.

## Strictness Position

Start strict, then relax only by changing the target label.

```text
unclear target
  -> INVALID or draft-only

clear target + missing evidence
  -> blocked

user accepts lower bar
  -> downgrade label, not inflate score

future behavior claim
  -> replay evidence or no claim
```

## Non-Decisions

- No existing product plan has been rewritten.
- No scorecard has been changed.
- No source routing rule has been changed.
- No graph or status script has been implemented.

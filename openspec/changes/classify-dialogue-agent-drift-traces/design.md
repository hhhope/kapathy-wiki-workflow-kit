# Design: classify dialogue agent drift traces

## Problem

The current review surfaces drift-related pages, but "drift" is too broad for
safe cleanup. Some pages record live user-agent disagreement and re-anchor
moments. Others are learning notes, examples, project updates, governance
records, or report quality evidence. Treating them as one surgery bucket either
over-promotes ordinary material into governance or hides live-conversation
calibration records inside generic cleanup.

## Proposed Model

Introduce a review-only classification layer with these buckets:

- `dialogue-disagreement`: records where the user rejects framing, corrects
  interpretation, or the conversation itself is the calibration material.
- `agent-drift`: records where the agent followed the wrong route, output mode,
  workflow chain, or implementation boundary.
- `reanchor-trace`: records where the required next action is to stop
  continuation and return to the last confirmed requirement or route.
- `supporting-example`: examples, replay harnesses, or samples that demonstrate
  the above behavior but are not themselves the live incident.
- `not-dialogue-drift`: learning notes, project-management intakes, report
  evidence, generic governance design, and unrelated drift mentions.

## Classification Rules

The classifier or reviewer should require explicit evidence from the page title,
frontmatter, or body. Filename similarity alone is not enough.

Positive signals:

- rejected or corrected framing
- user correction pressure
- live conversation re-anchor
- named agent drift
- route, output-mode, or workflow boundary failure
- replay/example material explicitly supporting disagreement or re-anchor

Negative signals:

- project status, weekly progress, or project-management intake
- source learning or reading notes without live disagreement
- report gate review where drift is only one quality dimension
- ADRs that already own stable decisions
- generic frontmatter cleanup without conversation calibration material

## Output Shape

The first implementation should produce review output only:

- item reference
- path
- proposed bucket
- evidence phrase or field
- recommended next action
- proof boundary

Recommended next actions are limited to:

- `no-op`
- `defer-cleanup`
- `openspec-candidate`
- `frontmatter-suggestion-only`

## Boundaries

This proposal does not approve direct writes to wiki frontmatter, relation
fields, taxonomy config, ADRs, AGENTS, or skills. It creates a review contract
that future implementation can use before any write-capable workflow is
approved.

## Relationship To Existing Specs

- `disagreement-management-method` owns preservation of disagreement as
  calibration material.
- `live-conversation-reanchor-gate` owns stopping continuation and re-anchoring.
- `wiki-content-enrichment-preview` may later suggest frontmatter and relation
  candidates, but this change keeps classification review-only unless a later
  implementation task explicitly adds preview output.

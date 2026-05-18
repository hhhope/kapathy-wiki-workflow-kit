# Proposal: classify dialogue agent drift traces

## Why

The wiki medical loop surfaced a recurring cleanup ambiguity: pages about live
conversation disagreement, agent drift, and re-anchor behavior are currently
mixed with generic governance drift, examples, learning notes, and workflow
traces. That makes surgery review treat them as broad governance work even when
the intended cleanup is narrower.

During the latest review, the user confirmed a clearer grouping:

```text
dialogue-disagreement / agent-drift / reanchor-trace
```

The repository needs an explicit OpenSpec change before turning that grouping
into a durable cleanup path or taxonomy-facing behavior.

## What Changes

- Define a bounded cleanup classification for dialogue disagreement, agent
  drift, and re-anchor traces.
- Distinguish real drift/disagreement records from examples, ordinary learning
  notes, project-management intakes, and generic governance changes.
- Preserve the boundary that this classification is review guidance first, not
  automatic frontmatter mutation.
- Identify where future implementation may update status, enrichment preview, or
  frontmatter suggestions after review.

## Scope

- Classify covered `wiki/ops` pages from the medical-loop surgery review.
- Add a review contract for recognizing:
  - dialogue disagreement records
  - agent drift records
  - re-anchor traces
  - examples or replay harnesses that support those records
- Keep ADR and OpenSpec-sensitive records as proposal candidates only.

## Non-Goals

- Do not mutate `wiki/config/frontmatter-taxonomy.yaml`.
- Do not write wiki page frontmatter.
- Do not write relation fields.
- Do not modify ADRs, AGENTS, skills, or OpenSpec lifecycle state outside this
  change.
- Do not reclassify project-management intakes, learning notes, or report
  quality records as dialogue drift.

## Evidence

- Medical case: `wiki/ops/wiki-medical-cases/2026-05-15-064427-wiki-medical-case.md`
- Surgery plan: `wiki/ops/wiki-surgery-runs/2026-05-18-023550-surgery.md`
- Confirmed user grouping:
  `dialogue-disagreement / agent-drift / reanchor-trace`

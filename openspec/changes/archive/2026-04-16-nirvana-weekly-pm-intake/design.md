## Context

The repository now has a defined weekly PM loop, but it needs a real first run. The user placed Nirvana project weekly PM materials in `inbox/nirvana/`, including:

- `涅槃焕新周报.xlsx`
- `涅槃产品上架梳理.xlsx`

The extracted weekly report content provides enough information to produce:

- milestone baseline and current progress
- this-week progress
- next-week actions
- risk statements

The user wants the system to support ongoing weekly project-management intake, so this first instantiation should preserve raw source lineage and create actionable follow-up structure.

## Goals / Non-Goals

**Goals:**

- Create a real weekly source record for the Nirvana weekly report.
- Create a PM intake page in Chinese-first format.
- Create a reminder page that isolates follow-up actions and risks.
- Keep the pages linked so future weekly inputs can build on them.

**Non-Goals:**

- Build executable automation for this intake.
- Rewrite the entire Nirvana project report history.
- Directly create Codex handoff tasks from this weekly report.

## Decisions

### Decision: Use the weekly report as the primary source page

The source page will reference the `涅槃焕新周报.xlsx` input directly and summarize the extracted PM content. The product-planning sheet remains supporting context, not the primary weekly source.

### Decision: Keep reminder content focused on follow-up, not full recap

The intake page carries the narrative summary; the reminder page carries what must be followed up next:

- owner alignment
- scope freeze
- NACOS regression
- account/protocol joint debugging

### Decision: Keep project-specific records under ops, not only in reports

This weekly PM material is not just report evidence. It drives actions. Therefore it must exist in ops as an intake and reminder, not only as a source page.

## Risks / Trade-offs

- [Risk] The weekly sheet mixes planning and current-state language. → Mitigation: keep milestone baseline, current progress, and next actions explicitly separated.
- [Risk] Some owners are still implicit. → Mitigation: mark them as pending confirmation instead of guessing.
- [Risk] Without a weekly series index, later weeks may scatter. → Mitigation: make this first page naming pattern reusable.

## Migration Plan

1. Create and validate the change artifacts.
2. Add the Nirvana weekly source page.
3. Add the Nirvana weekly intake page.
4. Add the Nirvana weekly reminder page.
5. Link the new pages from the source and ops indexes.
6. Verify the records are internally linked and aligned with the weekly PM loop.

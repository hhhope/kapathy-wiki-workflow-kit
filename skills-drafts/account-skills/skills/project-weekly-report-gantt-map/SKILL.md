---
name: project-weekly-report-gantt-map
description: Use when the user wants a management-facing gantt or capability-map report, H5, HTML brief, or weekly project update built from schedule blocks, capability domains, or milestone inputs, especially when the output must stay aligned to source schedules and support presentation or leadership review.
---

# Project Weekly Report

Use the gantt to explain rhythm, the capability map to explain boundaries, the technical construction table to explain the foundation, and the risk section to focus leadership attention.

## ⚠️ Prohibited Behaviors

- ❌ Do not invent new workstreams, dependencies, milestones, or completion states that are not grounded in the user's schedule.
- ❌ Do not turn the weekly report into a long-form document or design memo; the output must stay management-facing.
- ❌ Do not change the fixed section order unless the user explicitly asks for a different layout.
- ❌ Do not present inferred risk paths as confirmed facts; label them as schedule-based judgment when evidence is incomplete.
- ❌ Do not produce vague capability or technical-construction language; every item must map to a concrete capability, module, or component.
- ❌ Do not rename source workstreams into author-invented abstractions such as generic preparation, closure, or coupling stages unless the source itself uses that name.
- ❌ Do not render a source `未开始` item as in progress merely because it has planned dates.
- ❌ Do not mix current-fact items, directional notes, and clarification-needed items into the same gantt lane.
- ❌ Do not use unexplained shorthand, orphaned tail labels, or isolated date markers that a presenter cannot speak directly from the page.
- ❌ Do not use pseudo-precise percentages such as `40%` unless the source materials contain a defensible completion model.

## Intent Routing

| User intent | Execution path |
| --- | --- |
| Generate H5 or HTML weekly report | Use the HTML H5 report path |
| Generate PPT weekly report | Use the PPT outline path |
| Improve an existing weekly-report prompt or skill | Use the diagnosis and optimization path |
| Highlight risk path automatically | Use the risk-identification path |

## Intake Rules

- When called from `visual-agent`, honor the selected visual mode. Do not
  silently turn an ambiguous visual request into HTML H5 without the
  `visual-agent` mode fork.
- Before generating the final report, you must ask one explicit language question unless the user already provided the answer:
  - `Should the final output be in Chinese or English?`
- If the user asks for a direct final artifact and all business inputs are already present, ask only the language question and then proceed.
- If the user did not specify output format, default to a single-file HTML H5 output.
- If the user did not provide explicit MVP or milestones, you may derive 1-3 milestone points from the schedule, but you must label them as inferred from the current plan.

## Core Rules

- Always anchor the report to the exact reporting window, preferably using the user's absolute dates such as `2026-04` to `2026-07`.
- Every section must map back to schedule reality: workstreams, capabilities, technical construction, milestones, and risks must stay aligned with the timeline.
- If the source materials include a business-object or module name, use that name in the gantt before inventing any management abstraction.
- Separate user-provided information into three buckets before rendering:
  - current fact
  - directional note
  - clarification-needed item
- Only current facts belong in the primary gantt. Directional notes belong in explanatory or comparison sections. Clarification-needed items must be labeled as pending, not rendered as schedule facts.
- If original business milestones are already off-track, label them as original milestones and use current functional schedules as the live control baseline.
- If account carries settlement, freeze, query, balance-movement, or account-compatibility scope, account must appear as a primary gantt workstream rather than being buried in technical construction.
- The page order is fixed:
  1. Header
  2. Four summary cards
  3. MVP and milestones
  4. Gantt timeline
  5. Capability map
  6. Technical construction
  7. Conclusion
- Fixed status semantics:
  - `Completed` → green
  - `In progress` or `Partially complete` → yellow
  - `Not started` → gray
  - `Risk` or `Critical path` → red
- Default handling of `Partially complete`: render it with the same visual class as `In progress`, but preserve the wording in text.
- Status semantics always follow source truth. Planned dates do not upgrade `Not started` to `In progress`.
- The capability map must cover the business boundary clearly. If the user expects domains related to resale, split billing, transaction, refund, or billing cycle, do not silently omit them.
- If the report scope is current direct-sales work only, keep resale targets or member-progress placeholders out of the primary gantt unless the user explicitly asks for a mixed timeline and provides supporting data.
- The technical construction section must explicitly surface these value mappings whenever the user's inputs contain related components:
  - Data layer → solves billing or ledger problems
  - Configuration layer → solves data silos
  - Event center → decoupling
  - Unified balance movement → consistency
- MVP and milestones must be visually prominent:
  - If the user provides explicit MVP, phase target, launch gate, or acceptance node, they must appear in a dedicated block.
  - If MVP is not explicit, derive only from the schedule and label it as an inferred milestone summary.
- The conclusion must always be exactly three statements:
  1. Current capability coverage
  2. Current core risk
  3. Next-step focus

## Risk Identification Rules

- Mark a workstream as critical path only when at least one of these is true:
  - The user explicitly marks it as risk or critical
  - It is unfinished and its end date is close to the report-window boundary
  - The input includes explicit dependency or blocking language
- If a workstream is merely `Not started` without confirmed dependency impact, label it as `Potential risk`, not a confirmed critical path.
- Common likely high-risk candidates such as split billing or AD/BM may be highlighted, but only as schedule-based judgment if the dependency chain is not explicit.

## HTML H5 Report Path

- Default output: a single self-contained HTML H5 weekly report.
- If the user does not explicitly request PPT, generate HTML H5 by default.
- The output must be one HTML file with inline CSS and no external assets.
- Visual direction is fixed:
  - Dark gradient header
  - White content cards
  - Rounded corners in the `16px-20px` range
  - Light gray borders with subtle shadows
- The four summary cards are fixed:
  - Base capability
  - Current workstream
  - Account status
  - Risk focus
- The MVP and milestones block must sit between the four cards and the gantt.
- The gantt must use a month-based axis and render one workstream per row.
- Every gantt lane must be presentation-safe:
  - lane titles must be business objects or modules
  - status chips must reflect source truth
  - tail labels must remain interpretable without oral explanation
- The capability map must use a four-column structure:
  - `Domain | Supported | In progress | Planned`
- If the user asks to compare current direct-sales versus resale targets, use a dedicated comparison block instead of overloading the primary capability map.
- The technical construction table must use a four-column structure:
  - `Technical layer | Component | Current role | Value`
- Before generating HTML, read `references/report-template.md`.
- When producing the final HTML artifact, also read `references/html-skeleton.html` and fill it instead of inventing a new page structure from scratch.

## PPT Outline Path

- Output target: a 1-page or 3-page management outline.
- 1-page version: Header, four summary cards, gantt summary, risk conclusion.
- 3-page version:
  1. Progress and workstream summary
  2. Capability map and technical construction
  3. Risks and next steps
- PPT output must preserve the same status-color semantics as the HTML path.

## Diagnosis And Optimization Path

- If the user provides an existing prompt or skill draft, diagnose it first and then rewrite it.
- Prioritize these checks:
  - Missing trigger boundaries
  - Missing exclusion conditions
  - Visual rules and execution rules mixed together
  - Missing risk-decision boundary
  - Missing explicit difference between HTML H5 and PPT behavior
  - Missing output-language question

## Output Rules

- Default response order:
  1. Reporting scope note
  2. Fact vs inference note for risks and milestones
  3. Final management artifact or HTML / PPT output
- If the user explicitly asks for direct HTML or H5, do not stop at an outline; generate the final single-file HTML after clarifying the language.
- If the input is incomplete, list only the real gaps and then produce the smallest useful draft.
- If the user explicitly asks for a final artifact, use placeholders only for missing low-risk details; do not block unnecessarily.

## Common Failure Modes

| Problem | Root cause | Fix |
| --- | --- | --- |
| The report reads like an essay | The fixed structure was ignored | Return to the seven-section structure |
| The gantt looks like a task list | No shared time axis | Rebuild it on a month-based axis |
| MVP and milestones are buried | They were merged into body text | Move them into a dedicated highlight block |
| The capability map feels empty | Capabilities were not split into status buckets | Force `Supported / In progress / Planned` |
| Everything is marked red or nothing is red | No risk decision rules were applied | Re-evaluate using explicit risk and schedule-boundary rules |
| Technical construction is abstract | Current role and value are missing | Force each row to include component, role, and value |
| The gantt no longer matches the source table | Author invented new lane names or upgraded planned items to active | Restore source business-object names and source status semantics |
| Direct-sales review gets polluted by resale or member placeholders | Current facts and directional notes were mixed | Keep the primary gantt scoped to current workstreams and move direction-only inputs into comparison or pending sections |
| The page looks dense but is hard to present | Labels use shorthand or unexplained tails | Rewrite labels into business terms a presenter can read aloud directly |

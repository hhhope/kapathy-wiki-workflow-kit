# Report Template

Load this file when the user asks for a direct H5 weekly report, a single-file HTML report, a long infographic page, or a PPT weekly-report outline.

## 1. Normalize Inputs

Normalize the input into this shape:

```yaml
report_window:
  start: YYYY-MM
  end: YYYY-MM

workstreams:
  - name:
    status:
    range: [YYYY-MM, YYYY-MM]

capability_map:
  some_domain:
    supported: []
    in_progress: []
    planned: []

technical_construction:
  - layer:
    component:
    current_role:
    value:

mvp:
  name:
  target_time:
  definition:

milestones:
  - name:
    time:
    status:
```

## 2. Mandatory Language Check

Before generating the final artifact, ask:

`Should the final output be in Chinese or English?`

If the user already answered, do not ask again.

## 3. Header Copy

Recommended structure:

- Title: `Project Weekly Report`
- Subtitle: `{start} - {end} progress, capability boundary, and technical construction`
- Top-right badge: `Management View`

## 4. Four Summary Cards

The four cards are fixed:

1. Base capability
   - Summarize what is already stable or already supported
2. Current workstream
   - Summarize active lines in the current window
3. Account status
   - Use this to surface account transformation or the equivalent core-domain status
4. Risk focus
   - Limit this to 1-2 key risks only

## 5. MVP And Milestones

- This block must appear after the four cards and before the gantt.
- It must contain:
  - one main MVP card
  - one milestone list or milestone time-band
- If the user did not provide explicit MVP:
  - derive it from the schedule only
  - label it as `Inferred from current schedule`

Suggested MVP card fields:

- Name
- Target completion time
- Current status
- Management meaning

Suggested milestone list fields:

- Time
- Milestone
- Status
- Whether it is risk-related

## 6. Gantt Rules

- Use a unified month-based axis
- One workstream per row
- Render:
  - `Completed` in green
  - `In progress` or `Partially complete` in yellow
  - `Not started` in gray
  - `Risk` or `Critical path` with red outline or red label

At minimum, include a table or visual structure equivalent to:

| Workstream | 03 | 04 | 05 | 06 | 07 | 08 | Status |

## 7. Capability Map Rules

Use a fixed table:

| Domain | Supported | In progress | Planned |
| --- | --- | --- | --- |

Requirements:

- Use concise phrases, not paragraphs
- Prefer covering these business words when relevant:
  - resale
  - split billing
  - transaction
  - refund
  - billing cycle
- If a capability is not provided, use `TBD` or leave it explicitly empty; do not fabricate content

## 8. Technical Construction Rules

Use a fixed table:

| Technical layer | Component | Current role | Value |
| --- | --- | --- | --- |

Must emphasize:

- Data layer: solves billing or ledger issues
- Configuration layer: solves data silos
- Event center: decoupling
- Unified balance movement: consistency

## 9. Conclusion Rules

The conclusion must always be exactly three statements:

1. Current capability coverage
2. Current core risk
3. Next-step focus

## 10. Risk Wording Boundary

- If the risk is explicitly confirmed, write it as a current risk
- If the risk is inferred from schedule pressure, write it as schedule-based judgment
- Do not present a potential risk as an already-materialized incident

## 11. HTML H5 Output Requirements

- Output one complete HTML file
- Inline CSS only; no external resources
- Fixed order:
  1. Header
  2. Four summary cards
  3. MVP and milestones
  4. Gantt
  5. Capability map
  6. Technical construction
  7. Conclusion
- The MVP card should be more prominent than the normal cards
- The milestone section may be horizontal or vertical, but it must scan quickly
- Avoid dumping plain tables one after another; the HTML must still feel like a management H5 report with clear hierarchy
- When generating the final HTML, start from `references/html-skeleton.html` and replace the placeholders with report content.

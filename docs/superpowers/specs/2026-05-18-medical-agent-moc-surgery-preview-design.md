# Medical Agent MOC Surgery Preview Design

## Goal

Make `$report-wiki-portfolio:wiki-medical-agent` recognize MOC requests and
route them into the medical-loop surgery preview path.

The first version is preview-only. It must not write `wiki/moc` files, update
the active medical case, mutate `Confirmed Decisions`, or apply an OpenSpec
lifecycle transition.

## Current Problem

The MOC lifecycle preview is already implemented in the MOC generator:

```text
python3 scripts/build_wiki_moc_projection.py
```

That command can dry-run object lifecycle MOC previews, but the normal
user-facing medical entry point does not know this route. A request such as
`moc preview status` is currently classified as `treatment_preview`, because
the classifier sees `preview` before it understands MOC.

This means MOC is technically available in the repository, but not properly
inside the `wiki-medical-agent` control surface.

## Chosen Approach

Use a new read-only intent:

```text
moc_surgery_preview
```

The medical agent will classify explicit MOC preview / surgery / review
requests into this intent, then build a MOC dry-run plan and pass it into the
existing surgery planner.

The route is:

```text
wiki-medical-agent
  -> classify intent as moc_surgery_preview
  -> resolve active case
  -> build MOC dry-run plan
  -> build surgery plan from active case + moc_plan
  -> return preview payload
```

## Intent Rules

The classifier should prefer `moc_surgery_preview` before generic
`treatment_preview`.

Route to `moc_surgery_preview` when user text contains a MOC signal such as:

- `moc`
- `MOC`
- `obsidian`
- `图谱导航`
- `知识地图`

and a review/preview/surgery signal such as:

- `preview`
- `预览`
- `surgery`
- `手术`
- `分流`
- `审`

Non-MOC treatment preview language must keep routing to `treatment_preview`.

## Case And State Rules

`moc_surgery_preview` remains part of the medical agent. It requires one active
case file, because the medical agent's authority model is case-file centered.

With one active case:

- `allowed: true`
- `allowed_action: preview_moc_surgery_plan`
- `next_action: review_moc_surgery_preview` when the MOC plan contains
  create/update/orphan actions
- `next_action: moc_projection_clean` when all MOC entries are noop

Without an active case:

- `allowed: false`
- `blocked_reason: no_active_case`
- `next_action: diagnose`

With multiple active cases:

- `allowed: false`
- `blocked_reason: multiple_active_cases`
- `next_action: select_active_case`

## Output Shape

The payload should keep the medical-agent top-level fields:

- `intent`
- `case_path`
- `state`
- `allowed`
- `allowed_action`
- `blocked_reason`
- `next_action`

When allowed, add a compact preview:

```json
{
  "intent": "moc_surgery_preview",
  "allowed_action": "preview_moc_surgery_plan",
  "moc_projection": {
    "candidate_count": 184,
    "create_count": 184,
    "update_count": 0,
    "noop_count": 0,
    "orphan_count": 0
  },
  "surgery_preview": {
    "moc_projection_count": 184,
    "sample_items": [
      {
        "action": "create",
        "kind": "object",
        "key": "agent-governance-gate-gap",
        "path": "wiki/moc/object-agent-governance-gate-gap.md",
        "link_count": 2
      }
    ]
  },
  "next_action": "review_moc_surgery_preview"
}
```

The payload should include summaries and samples, not every full generated MOC
page. Full previews remain available from `build_wiki_moc_projection.py`.

## Components

### `scripts/wiki_medical_agent.py`

Add intent classification and validation for `moc_surgery_preview`.

Add a preview builder that:

1. builds the current graph-backed MOC dry-run plan,
2. calls the existing surgery planner with that `moc_plan`,
3. returns compact summary/sample data in the medical-agent payload.

### `scripts/build_wiki_medical_agent.py`

Keep the CLI as the normal entry point. For `moc_surgery_preview`, it should
print the enriched payload. It should not require `--apply`.

### `scripts/wiki_surgery.py`

Reuse existing `moc_plan` support. Avoid expanding surgery responsibilities
unless tests expose a missing summary field.

### `scripts/wiki_moc_projection.py`

Use the existing dry-run planner. Do not change apply behavior for this work.

## Boundaries

This design does not:

- write `wiki/moc`
- run MOC `--apply`
- update the active case file
- write a surgery record
- mutate `Confirmed Decisions`
- mutate taxonomy config, ADRs, AGENTS, skills, or OpenSpec lifecycle state

If later we want durable surgery evidence, that should be a separate step that
explicitly writes a surgery record or updates the case.

## Testing

Add or update tests for:

1. `classify_medical_intent("moc preview surgery")`
   returns `moc_surgery_preview`.
2. `classify_medical_intent("preview apply confirmed treatments")`
   still returns `treatment_preview`.
3. `build_status_payload(..., "moc preview surgery")` with one active case:
   - returns `allowed: true`
   - returns `allowed_action: preview_moc_surgery_plan`
   - includes `moc_projection`
   - includes `surgery_preview`
   - returns `next_action: review_moc_surgery_preview` when there are non-noop
     MOC items.
4. CLI invocation with `--intent-text "moc preview surgery"`:
   - prints `moc_surgery_preview`
   - does not create `wiki/moc`
   - does not update the case file.
5. No active case blocks MOC surgery preview with `no_active_case`.
6. Multiple active cases blocks MOC surgery preview with `multiple_active_cases`.

Expected verification commands:

```bash
python3 -m unittest tests.test_wiki_medical_agent tests.test_wiki_surgery tests.test_wiki_moc_projection
openspec validate add-medical-agent-moc-surgery-preview --strict
```

## Acceptance Criteria

- MOC preview requests no longer fall into `treatment_preview`.
- `$report-wiki-portfolio:wiki-medical-agent` can return a MOC surgery preview
  summary from the active case context.
- The route is read-only by default.
- No `wiki/moc` directory is created during preview.
- Existing treatment preview/apply/recovery behavior remains unchanged.

## Residual Risks

- The first version returns compact samples only. Users may still need to run
  the MOC generator directly for full generated page previews.
- Some MOC lifecycle groups still contain `Other` entries. This is a MOC
  grouping-tuning issue, not a medical-agent routing blocker.
- Durable case evidence for MOC surgery review is not written in this version.

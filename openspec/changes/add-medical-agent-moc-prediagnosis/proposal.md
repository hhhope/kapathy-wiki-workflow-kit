# Proposal: add medical-agent MOC prediagnosis

## Why

`wiki-medical-agent` can already route explicit MOC review requests to the
read-only `moc_surgery_preview` path, and the lower-level MOC temperature gate
already blocks raw relation MOC generation by default.

The current user-facing payload still exposes raw worker internals such as
`temperature_admission` and large `clue_windows` arrays. That makes the user
experience feel like Python/JSON tooling instead of medical-agent diagnosis.

## What Changes

- Keep `moc_surgery_preview` as the user-facing medical-agent intent.
- Add `prediagnosis.kind: moc_temperature` to allowed MOC surgery preview
  payloads.
- Summarize MOC projection and temperature admission evidence without dumping
  raw clue windows.
- Mark `derived_from` and `related_objects` as blocked mechanical relation
  families by default.
- Surface review-needed clue candidates with candidate temperature, rationale,
  evidence refs, and confirmation questions.
- Surface orphan relation MOC pages only as surgery candidates.

## Out of Scope

- No new normal user entry point.
- No independent MOC review skill.
- No automatic MOC admission.
- No admitted review JSON generation.
- No writes to `wiki/moc`, relation frontmatter, ADRs, AGENTS, skills,
  taxonomy config, or OpenSpec lifecycle state from the preview.

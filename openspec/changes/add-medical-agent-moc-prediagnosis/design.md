# Design: medical-agent MOC prediagnosis

## Route

The route remains:

```text
user natural language
-> wiki-medical-agent
-> intent: moc_surgery_preview
-> active case validation
-> bounded MOC dry-run worker
-> prediagnosis.kind: moc_temperature
-> confirmation point
```

`prediagnosis.kind` is not a new lifecycle authority. It is a read-only section
derived from existing worker evidence.

## Payload

Allowed `moc_surgery_preview` responses add:

```json
{
  "prediagnosis": {
    "kind": "moc_temperature",
    "script_result_summary": {},
    "interpreted_live_intent": "",
    "mechanical_relation_families": [],
    "review_needed_clues": [],
    "orphan_relation_moc_pages": [],
    "confirmation_points": [],
    "write_boundary": "read_only_no_files_written"
  }
}
```

The existing `temperature_admission` field may remain for compatibility, but
large `clue_windows` must not be copied into `prediagnosis`.

## Interpretation Rules

- `derived_from` and `related_objects` are mechanical relation families and
  stay blocked by default.
- Review-needed clue candidates come from bounded samples of
  `temperature_admission.clue_windows`.
- Candidate temperature is copied from explicit review data when present. When
  missing, use `null` plus `temperature_band: "unreviewed"`.
- Rationale is copied from review data when present. When missing, use a short
  structural rationale that does not claim admission.
- Orphan relation MOC pages come from surgery preview sample items with
  `action: orphan` and `kind: relation`.

## Boundaries

The implementation must not write files, update case files, generate review
JSON, admit clues, or run cleanup surgery.

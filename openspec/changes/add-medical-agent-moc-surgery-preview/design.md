# Design: medical-agent MOC surgery preview

## Architecture

Add one read-only route inside `scripts/wiki_medical_agent.py`:

```text
classify_medical_intent
  -> moc_surgery_preview
  -> resolve_active_case
  -> build_moc_plan from extracted graph
  -> build_surgery_plan_from_case(case, moc_plan)
  -> compact payload
```

The medical agent remains the user-facing controller. MOC generation remains
owned by `scripts/wiki_moc_projection.py`. Surgery classification remains owned
by `scripts/wiki_surgery.py`.

## Intent Rules

MOC routing must run before generic preview routing.

MOC signals: `moc`, `obsidian`, `图谱导航`, `知识地图`.

Review signals: `preview`, `预览`, `surgery`, `手术`, `分流`, `审`.

## Payload

When allowed, append:

- `moc_projection`: copy of MOC plan summary.
- `surgery_preview`: compact object containing `moc_projection_count` and up to
  five `sample_items`.

`next_action` is `review_moc_surgery_preview` when create/update/orphan items
exist and `moc_projection_clean` when the MOC plan has no surgery items.

## Boundaries

The route is preview-only. It must not write `wiki/moc`, treatment records,
surgery records, or case-file updates.

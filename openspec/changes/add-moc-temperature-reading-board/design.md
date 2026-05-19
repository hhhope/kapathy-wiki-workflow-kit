# Design: MOC temperature reading board

## Model

The MOC pipeline becomes:

```text
graph/frontmatter
-> relation feature package
-> explicit temperature review
-> clue windows
-> MOC admission plan
-> generated MOC projection
```

Graph extraction remains deterministic. It supplies pages, canonical objects,
domains, and relation fields. It does not decide semantic value.

## Relation Feature Package

`scripts/wiki_moc_temperature.py` builds one package per graph edge:

- `candidate_id`
- `source_page`
- `source_object`
- `relation_type`
- `target_object`
- `source_layer`
- `target_layer`
- `evidence_refs`
- `structural_features`

Structural features may include `cross_layer`, `has_spec_support`,
`has_adr_support`, `fanout_count`, and `mechanical_relation`.

## Temperature Review

The first implementation does not call an external model. It accepts explicit
review judgments as JSON and merges them with feature packages. Missing review
judgment produces a `needs_review` clue window. Mechanical relation types are
blocked unless the review explicitly admits them with high temperature.

## MOC Admission

Domain and object MOC candidates remain structural in this change. Relation MOC
pages are gated:

- No raw relation type becomes a relation MOC page by default.
- A relation type becomes a MOC page only when the admission plan lists it in
  `admitted_relations`.
- `derived_from` and `related_objects` remain blocked unless explicit review
  evidence admits them.

## Medical Agent

Medical-agent MOC preview includes temperature admission counts and a small
sample of clue windows. It does not write `wiki/moc`, treatment records,
surgery records, OpenSpec state, relation fields, or taxonomy config.

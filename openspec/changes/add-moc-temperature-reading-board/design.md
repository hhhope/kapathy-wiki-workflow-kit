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

Minimum review JSON fields:

- `candidate_id`: feature package identifier.
- `temperature`: integer from `0` to `100`.
- `moc_admission`: one of `admit`, `block`, or `needs_review`.
- `rationale`: short human- or AI-authored reason.
- `reviewer`: identifier for the reviewing human, agent, or imported review.
- `reviewed_at`: ISO-8601 timestamp or date.

High temperature means `temperature >= 80`. High temperature alone is not
enough for MOC admission; `moc_admission` must also be `admit`.

## Clue Windows

The temperature module emits one clue window per relation feature package.
Minimum clue-window fields:

- `candidate_id`
- `relation_type`
- `source_page`
- `source_object`
- `target_object`
- `evidence_refs`
- `structural_features`
- `temperature`
- `status`
- `moc_admission`
- `rationale`

Allowed `status` values are `admitted`, `blocked`, and `needs_review`.
Missing review JSON produces `status: needs_review`, `temperature: null`, and
`moc_admission: needs_review`. Mechanical relation types such as
`derived_from` and `related_objects` produce `status: blocked` unless review
JSON sets `temperature >= 80` and `moc_admission: admit`.

## MOC Admission

Domain and object MOC candidates remain structural in this change. Relation MOC
pages are gated:

- No raw relation type becomes a relation MOC page by default.
- A relation type becomes a MOC page only when the admission plan lists it in
  `admitted_relations`.
- `derived_from` and `related_objects` remain blocked unless explicit review
  evidence admits them.

The admission plan contains these minimum fields:

- `admitted_relations`: relation types eligible for generated relation MOC
  pages.
- `blocked_relations`: relation types represented only as blocked admission
  state.
- `review_needed_relations`: relation types represented only as review-needed
  admission state.
- `clue_windows`: bounded clue-window records used to derive the plan.
- `counts`: object with `admitted`, `blocked`, `needs_review`, and `total`.

Relation groups can still appear in graph summary, dry-run, or preview output
as admission state. They SHALL NOT become generated `wiki/moc/relation-*.md`
page candidates unless their relation type is listed in `admitted_relations`.

Admission counts are computed from clue-window `status` values:

- `admitted`: number of windows with `status: admitted`.
- `blocked`: number of windows with `status: blocked`.
- `needs_review`: number of windows with `status: needs_review`.
- `total`: total number of relation clue windows.

## Medical Agent

Medical-agent MOC preview includes temperature admission counts and a small
sample of clue windows. It does not write `wiki/moc`, treatment records,
surgery records, OpenSpec state, relation fields, or taxonomy config.

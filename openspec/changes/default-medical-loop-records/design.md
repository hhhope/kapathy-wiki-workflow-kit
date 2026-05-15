# Design: default medical loop records

## Behavior Model

The medical-loop stages will treat durable records as the default output:

```text
stage invocation -> complete record on disk -> compact stdout summary
```

Stdout is a live summary for the current chat or terminal. The Markdown record
is the durable chart entry that later treatment, surgery, recovery, and archive
work can cite.

## CLI Changes

### Doctor

`scripts/build_wiki_content_adjudication.py` will default to writing a complete
diagnosis record under `wiki/ops/wiki-doctor-runs/`.

Default stdout will be compact JSON containing:

- mode
- generated_at
- review_record_path
- summary counts
- eval result summary
- proof boundary notes

`--stdout-json-only` will preserve the old non-writing JSON package output for
debugging. Existing `--write-review-record` remains accepted for compatibility
and becomes redundant with the default.

### Confirm

`scripts/build_wiki_review_decisions.py` will default to writing a complete
confirmation record under `wiki/ops/wiki-review-decisions/`.

Default stdout will be compact JSON containing:

- mode
- generated_at
- decision_record_path
- source doctor record path when provided or discovered
- bucket counts
- proof boundary notes

`--stdout-json-only` will preserve the old non-writing JSON package output for
debugging. Existing `--write-decision-record` remains accepted for compatibility
and becomes redundant with the default.

## Limit Semantics

The existing `--limit` flag currently bounds output buckets before writing.
That is unsafe for default medical records.

After this change:

- written records are complete by default
- `--limit` affects only stdout preview in default mode
- `--stdout-json-only --limit N` can still emit bounded JSON for inspection
- tests must prove written records retain items beyond a small preview limit

If implementation cost is lower, the CLI may internally build a full package
for writing and a separately limited package for stdout.

## Diagnosis Record Structure

Doctor records will use the title:

```text
# wiki-doctor Diagnosis Record
```

Required sections:

- `Source / 检查来源`
- `Exam Items / 检查项目`
- `Reference Standards / 判定标准`
- `Diagnosis Summary / 诊断摘要`
- `Abnormal Findings / 异常发现`
- `Proof Boundary / 证明边界`
- `Recommended Next Stage / 建议下一步`

Reference standards describe how risk markers are interpreted:

- `agent_uncertain`: human review required
- `relation_weak_evidence`: relation candidates cannot be auto-written
- `openspec_required`: lifecycle routing cannot be bypassed
- `drift_risk`: governance or agent judgment drift needs explicit review
- `adr_risk`: stable decision surfaces need surgery or OpenSpec handling

## Confirmation Record Structure

Confirm records will use the title:

```text
# wiki-confirm Confirmation Record
```

Required sections:

- `Source / 检查来源`
- `Decision Rules / 确诊标准`
- `Confirmed Buckets / 确诊分流`
- `Abnormal Findings / 异常明细`
- `Medical Advice / 处理建议`
- `Proof Boundary / 证明边界`

The fixed bucket names remain:

- `accepted_candidates`
- `rejected_candidates`
- `deferred_items`
- `treatment_candidates`
- `surgery_candidates`
- `openspec_required`

Decision rules:

- `safe_to_apply_frontmatter=true` routes to `treatment_candidates`
- `relation_weak_evidence`, `drift_risk`, or `adr_risk` routes to
  `surgery_candidates`
- `openspec_required` or `taxonomy_candidate` routes to `openspec_required`
- `agent_uncertain` or `needs_user_confirmation` routes to `deferred_items`
- `reject` or rejected candidate details route to `rejected_candidates`
- `accept` with no risk flags routes to `accepted_candidates`

Items may appear in multiple buckets when multiple rules apply. The record must
preserve `detail_ref`, path, risk flags, reason, and rejected candidate details
when present.

## Skill Contract Changes

`wiki-doctor` and `wiki-confirm` will state that stage invocation defaults to
writing complete records.

The legacy `wiki-review-decisions` alias will preserve the same default record
behavior while still directing users toward `wiki-confirm`.

All three skills must state that records are evidence and routing artifacts, not
approval to repair.

## Boundaries

This change writes diagnosis and confirmation records only. It does not write
frontmatter, taxonomy config, relation fields, MOC files, ADRs, skills beyond
the named contracts, or OpenSpec lifecycle state.

Generated records remain excluded from later content adjudication scans.

## Test Plan

RED tests:

- default doctor CLI currently does not write a record
- default confirm CLI currently does not write a record
- current default `--limit` behavior can truncate written records when write
  flags are used
- current skill text still says records are written only when explicitly asked

GREEN tests:

- default doctor CLI writes a record and returns compact summary JSON with
  `review_record_path`
- default confirm CLI writes a record and returns compact summary JSON with
  `decision_record_path`
- `--stdout-json-only` writes no records and returns the full legacy package
- written records include entries beyond a small stdout preview limit
- record Markdown includes medical report sections and proof boundaries
- generated doctor and confirmation records remain excluded from adjudication
- skill marker tests cover default record behavior

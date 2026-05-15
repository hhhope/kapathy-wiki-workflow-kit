# Design: wiki review decisions

## Architecture

Build on the existing `wiki-doctor` adjudication package instead of parsing
doctor Markdown as the primary source.

```text
scripts/build_wiki_content_adjudication.py
  -> build_adjudication_package(root)
  -> scripts/wiki_review_decisions.py
  -> scripts/build_wiki_review_decisions.py
  -> wiki/ops/wiki-review-decisions/YYYY-MM-DD-HHMMSS-review-decisions.md
```

`scripts/wiki_review_decisions.py` owns pure package transformation, Markdown
rendering, and non-overwriting file writes.

`scripts/build_wiki_review_decisions.py` owns the explicit CLI:

- default: stdout JSON only
- `--write-decision-record`: write Markdown
- `--decision-record-dir`: override output directory
- `--source-record`: cite a doctor record path when the user is acting from a
  specific diagnosis record

## Decision Buckets

The generated record is a draft decision aid, not human confirmation.

- `accepted_candidates`: high-confidence details without review risks.
- `treatment_candidates`: `safe_to_apply_frontmatter=true` details.
- `surgery_candidates`: details with broad structural or governance risks such
  as `openspec_required`, `drift_risk`, `adr_risk`, or
  `relation_weak_evidence`.
- `openspec_required`: details with `openspec_required` or taxonomy changes
  that need scoped lifecycle review.
- `deferred_items`: uncertain items that need human review before routing.
- `rejected_candidates`: details whose judgment rejects the candidate or whose
  rejected candidate list explains why an automatic route is unsafe.

Items can appear in multiple buckets when multiple boundaries apply. The record
must expose the source `detail_id` and path so a human can review the original
doctor detail.

## Skill Contract

Add `.codex/skills/wiki-review-decisions/SKILL.md`.

The skill is a tool-wrapper module. It owns the review-decision stage of the
medical loop only. It references `wiki-doctor` as the diagnosis source and
preserves the medical-loop boundary:

```text
doctor diagnoses; review routes; treatment or surgery writes only after later
approval.
```

## Boundaries

This change does not approve or execute repair. It does not create treatment,
surgery, or recovery execution. It does not mutate frontmatter, relation fields,
MOC files, taxonomy config, ADRs, AGENTS, skills other than
`wiki-review-decisions`, or OpenSpec lifecycle state.

## Large-File Boundary

`scripts/wiki_content_adjudication.py` is already over the Python large-file
threshold. This change adds a separate helper module rather than growing that
file.

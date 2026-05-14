# wiki-doctor Review Records Design

Date: 2026-05-14
Status: approved for planning

## Context

`wiki-doctor` is currently a review-only diagnostic skill over the wiki content
adjudication package. It can summarize stdout output from
`scripts/build_wiki_content_adjudication.py`, but it does not leave a durable
repo-visible review record. That makes later review harder: the diagnosis is
visible in the chat or terminal, but the scan scope, summary, taxonomy
candidates, proof boundary, and next review actions are not preserved as an
artifact.

The existing completed change
`openspec/changes/rename-wiki-content-adjudication-skill-to-doctor/` should not
be reopened for this behavior change. A new OpenSpec change should cover the
new contract and implementation.

## Goal

Add an explicit, review-only review-record path for `wiki-doctor`:

```text
wiki-doctor -> adjudication package -> optional review record -> human review -> explicit fix or new OpenSpec later
```

The review record is a diagnosis artifact. It is not permission to write
frontmatter, mutate taxonomy, create MOC pages, mark tasks complete, or apply
repairs.

## Recommended Approach

Use one OpenSpec change with two parallel implementation tracks:

1. Skill contract track: update `.codex/skills/wiki-doctor/SKILL.md` so the
   default remains review-only, while allowing an explicitly requested
   repo-visible review record.
2. Script capability track: add an explicit write option to
   `scripts/build_wiki_content_adjudication.py`, such as
   `--write-review-record`, while preserving stdout-only behavior by default.

This keeps the skill contract and script behavior aligned in one lifecycle
change without making every doctor run a repository write.

## Output Location

Write review records under:

```text
wiki/ops/wiki-doctor-runs/YYYY-MM-DD-HHMMSS-review.md
```

The directory and filename make the artifact clearly operational and
time-scoped. The exact slug can be refined during implementation, but the path
must stay under `wiki/ops` and must not overwrite previous records.

## Review Record Shape

Each generated Markdown record should include:

- Scan scope and generation time.
- Summary counts: candidates, full detail entries, review focus entries,
  taxonomy candidates, drift traces, and eval warning/error counts.
- Taxonomy candidates as candidates only.
- Drift trace summary with references back to detail ids.
- Eval result summary, including warnings and errors.
- Proof boundary stating that this is diagnosis only.
- Next review actions grouped as human review, discard, OpenSpec candidate, or
  later explicit repair.

The record should link or reference the source script and preserve enough ids
for a reviewer to rerun the package and inspect full details.

## Boundaries

- Default `wiki-doctor` behavior stays stdout/review-only.
- A repo-visible review record requires explicit user intent.
- Review records may be committed as diagnosis evidence.
- Review records must not write or approve page frontmatter.
- Review records must not mutate `wiki/config/frontmatter-taxonomy.yaml`.
- Review records must not write `wiki/moc` pages.
- Review records must not mark OpenSpec tasks complete.
- Later structural repairs require human confirmation or a separate OpenSpec
  path.

## Testing and Evidence

The OpenSpec implementation should include:

- A RED baseline showing the previous script has no review-record write path.
- Tests for default stdout behavior.
- Tests for explicit review-record generation and non-overwrite behavior.
- Tests or fixture checks that generated records include proof boundary and
  next review actions.
- Skill evaluation evidence showing that `wiki-doctor` can persist a diagnosis
  record without implying automatic repair.
- Behavior replay evidence for the future trigger:
  `wiki-doctor` plus explicit record intent routes to review-record generation,
  while ordinary doctor diagnosis remains stdout-only.
- `python3 scripts/check_behavior_assets.py`, preserving any expected non-zero
  result in the change evaluation.

## Worktree Discipline

The current repository has unrelated modified and untracked files. The
implementation should stage only files that belong to the new OpenSpec change,
the `wiki-doctor` contract, the adjudication script capability, focused tests,
and any generated review-record evidence that is intentionally part of the
change.

## Open Questions Resolved

- The change should be one OpenSpec, not two.
- The skill and script tracks should be implemented in parallel under that one
  change.
- Record generation should be explicit, not default.
- The previous completed rename change should remain complete and untouched.

# Design

## Default Checks

Recovery runs a bounded default set:

- frontmatter precheck
- doctor/adjudication package
- review-decision package
- surgery plan

These commands either write only `/tmp` reports or stdout JSON. Recovery does
not run `build_wiki_status.py` by default because that command writes
`wiki/status/*`, which is a separate status-refresh action.

## Result Model

Each check preserves:

- check id
- command
- exit code
- pass/fail
- parsed JSON summary when available
- stderr tail

A nonzero check is recorded as a recovery finding, not hidden. Recovery records
can therefore show known whole-wiki drift without blocking record generation.
Packages with any failed check use `next_route: blocked_by_recovery_findings`;
otherwise they use `next_route: archive-ready`.

## Write Boundary

The default CLI writes only stdout JSON. Markdown records are written only with
`--write-recovery-record`.

Generated records under `wiki/ops/wiki-recovery-runs/` are medical-loop evidence
artifacts and must not become future doctor/adjudication candidates.

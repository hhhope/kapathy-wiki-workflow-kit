# Design: resolve frontmatter producer warning gate

## Current Behavior

The frontmatter precheck reports both strict blocking entries and scorecard
warnings. The current exit behavior follows the score threshold:

- warnings lower `score`
- `minimum_pass_score` is 100
- warnings alone can make `passed: false`
- recovery treats the nonzero exit as a failed check

This conflates two different signals:

- blocking gate failures: page frontmatter errors that must stop recovery
- advisory producer warnings: visibility for files that may emit frontmatter

## Approach

Use the configured blocking severities as the recovery stop condition:

- if `blocking_count > 0`, the precheck exits nonzero
- if `blocking_count == 0`, the precheck exits 0 even when warnings remain
- output keeps `summary.warn`, scorecard details, and warning samples

If inspection shows warnings come from real producer scripts that should be
registered, register them in `wiki/config/frontmatter-taxonomy.yaml` first. If
registration does not fully resolve the mismatch, apply the pass-condition
change in `scripts/wiki_gate_precheck.py`.

## Verification

- Baseline: capture current warning-only failure.
- Green path: run the frontmatter precheck on the current repo and confirm exit
  0 with `blocking_count: 0`.
- Red path: create a temporary broken wiki page under `/tmp` or a reversible
  target fixture and confirm blocking frontmatter errors still produce nonzero
  exit.
- Recovery: run `build_wiki_recovery.py` without applying treatment/surgery and
  confirm the frontmatter check no longer fails only because of warnings.

## Boundary

This change owns gate behavior and producer registration only. It must not
perform page-frontmatter migration, relation rebuild, wiki treatment, surgery
application, or archive.

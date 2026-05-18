# Evaluation: resolve frontmatter producer warning gate

## Baseline

Before the change:

- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10`
  returned nonzero.
- Output had `blocking_count: 0`, `summary.error: 0`, `summary.warn: 5`,
  `score: 75`, and `passed: false`.
- The warning kind was `possible_unregistered_producer`.

## Implementation

Changed `scripts/wiki_gate_precheck.py` so compact precheck `passed` follows
`blocking_count == 0`.

Kept these fields visible:

- `score`
- `minimum_pass_score`
- `summary.warn`
- warning `top_blockers`
- full checker report paths

No taxonomy vocabulary or wiki page frontmatter rules were changed.

## Verification

Unit tests:

```bash
python3 -m unittest tests.test_wiki_gate_precheck
```

Result:

- 3 tests passed
- `pytest` was not available in this environment, so the unittest runner was
  used directly

Current repository precheck:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 10
```

Result:

- `passed: true`
- `blocking_count: 0`
- `summary.error: 0`
- `summary.warn: 5`
- `score: 75`

Recovery:

```bash
PYTHONPATH=. python3 scripts/build_wiki_recovery.py --root . --case-file wiki/ops/wiki-medical-cases/2026-05-15-064427-wiki-medical-case.md
```

Result:

- `passed: true`
- `next_route: archive-ready`
- `check_count: 4`
- `passed_count: 4`
- `failed_count: 0`
- frontmatter precheck inside recovery exited 0 with `summary.warn: 5`

Generated evidence files from the recovery run:

- `wiki/ops/wiki-doctor-runs/2026-05-18-114338-review.md`
- `wiki/ops/wiki-review-decisions/2026-05-18-114343-review-decisions.md`

These generated evidence files were given frontmatter so the working tree does
not immediately reintroduce page-frontmatter blockers.

## Residual Risk

The doctor/review-decision generators still emit records without frontmatter by
default. This change proves producer warnings no longer block recovery by
themselves, but generator-default frontmatter should be handled as a separate
follow-up if repeated recovery runs are expected to leave zero page blockers
without manual repair.

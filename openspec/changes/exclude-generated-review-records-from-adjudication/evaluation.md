# Evaluation

## Behavior Replay

- Situation shape: a later adjudication scan runs after `wiki-doctor` and
  `wiki-review-decisions` have written repo-visible Markdown records.
- Trigger condition: candidate paths are under `wiki/ops/wiki-doctor-runs/` or
  `wiki/ops/wiki-review-decisions/`.
- Expected route: keep the records as evidence artifacts, but exclude them from
  adjudication candidate input.
- Expected output: `candidate_set`, `full_detail_set`, and
  `summary.candidate_count` only include non-generated candidates.
- Non-output boundary: no frontmatter, taxonomy, relation, MOC, or repair write
  is applied.
- Repo-visible artifact future agents should read:
  `openspec/changes/exclude-generated-review-records-from-adjudication/`.

## RED Baseline

Command:

```bash
python3 -m unittest tests/test_wiki_content_adjudication.py
```

Result before implementation:

```text
FAIL: test_excludes_generated_review_artifacts_from_candidates
AssertionError: 3 != 1
```

The baseline proved generated doctor and review-decision records were counted as
adjudication candidates.

## GREEN Result

Commands:

```bash
python3 -m unittest tests/test_wiki_content_adjudication.py tests/test_wiki_review_decisions.py
openspec validate exclude-generated-review-records-from-adjudication --strict
python3 -c "from pathlib import Path; from scripts.wiki_content_adjudication import build_adjudication_package; p=build_adjudication_package(Path('.')); paths=[d['path'] for d in p['full_detail_set'] if d['path'].startswith('wiki/ops/wiki-doctor-runs/') or d['path'].startswith('wiki/ops/wiki-review-decisions/')]; print({'candidate_count': p['summary']['candidate_count'], 'generated_detail_count': len(paths), 'generated_paths': paths[:5]})"
```

Results:

```text
Ran 12 tests in 2.486s
OK

Change 'exclude-generated-review-records-from-adjudication' is valid

{'candidate_count': 154, 'generated_detail_count': 0, 'generated_paths': []}
```

OpenSpec emitted PostHog DNS flush warnings after validation. The change itself
validated successfully.

## Residual Risks

- This excludes only the two generated review artifact directories. If future
  generated doctor-like artifacts use a new path, that path needs an explicit
  follow-up requirement.

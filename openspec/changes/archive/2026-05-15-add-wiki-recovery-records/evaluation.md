# Evaluation

## Behavior Replay

- Situation shape: treatment or surgery has happened, or a user asks to复查 the
  current wiki medical-loop state.
- Trigger condition: `wiki-recovery` is invoked.
- Expected route: run bounded checks, preserve command results, and produce a
  recovery package.
- Expected output: JSON by default; optional Markdown record under
  `wiki/ops/wiki-recovery-runs/`.
- Expected write behavior: no repo mutation by default. The only repo-visible
  write is an explicit recovery record.
- Non-output boundary: recovery does not apply treatment or surgery, write
  status files, write MOC pages, mutate frontmatter, mutate taxonomy config,
  write relation fields, write ADR decisions, or mutate OpenSpec state.
- Repo-visible artifact future agents should read:
  `openspec/changes/add-wiki-recovery-records/`.

## RED Baseline

Command:

```bash
python3 -m unittest tests/test_wiki_recovery.py tests/test_wiki_content_adjudication.py
```

Result before implementation:

```text
ModuleNotFoundError: No module named 'scripts.wiki_recovery'
AssertionError: 2 != 1
```

The baseline proved the repository had no recovery module and generated
`wiki-recovery-runs` records were still entering adjudication input.

## GREEN Result

Commands:

```bash
python3 -m unittest tests/test_wiki_recovery.py tests/test_wiki_content_adjudication.py tests/test_wiki_surgery.py tests/test_wiki_treatment.py tests/test_wiki_review_decisions.py
openspec validate add-wiki-recovery-records --strict
python3 scripts/check_behavior_assets.py
python3 -c "import json, subprocess, sys; p=subprocess.run([sys.executable, 'scripts/build_wiki_recovery.py'], check=True, capture_output=True, text=True); data=json.loads(p.stdout); print({'passed': data['passed'], 'next_route': data['next_route'], **data['summary']}); print([(c['check_id'], c['exit_code'], c['passed']) for c in data['checks']])"
```

Results:

```text
Ran 30 tests in 5.043s
OK

Change 'add-wiki-recovery-records' is valid

{'passed': False, 'next_route': 'blocked_by_recovery_findings', 'check_count': 4, 'passed_count': 3, 'failed_count': 1}
[('frontmatter_precheck', 1, False), ('doctor_adjudication', 0, True), ('review_decisions', 0, True), ('surgery_plan', 0, True)]
```

OpenSpec emitted PostHog DNS flush warnings after validation. The change itself
validated successfully.

## Residual Risks

- The current whole-wiki frontmatter precheck fails because of pre-existing
  repository drift. Recovery records that failure instead of hiding it.
- Recovery does not implement surgery apply or treatment apply.
- Status rebuild is not part of the default recovery set because the existing
  status command writes `wiki/status/*` unless redirected.


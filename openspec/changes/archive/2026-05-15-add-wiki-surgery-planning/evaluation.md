# Evaluation

## Behavior Replay

- Situation shape: doctor/adjudication has produced many structural,
  governance, relation, ADR, drift, OpenSpec, or MOC findings.
- Trigger condition: `wiki-surgery` planning is invoked.
- Expected route: risky structural items become surgery plan items; safe
  frontmatter items remain treatment work; MOC dry-run entries are included only
  when explicitly provided.
- Expected output: JSON by default; optional Markdown plan record under
  `wiki/ops/wiki-surgery-runs/`.
- Expected write behavior: no patient page writes.
- Non-output boundary: surgery planning does not write frontmatter, taxonomy
  config, relation fields, MOC pages, ADR decisions, AGENTS, skills, or OpenSpec
  state.
- Repo-visible artifact future agents should read:
  `openspec/changes/add-wiki-surgery-planning/`.

## RED Baseline

Command:

```bash
python3 -m unittest tests/test_wiki_surgery.py tests/test_wiki_content_adjudication.py
```

Result before implementation:

```text
ModuleNotFoundError: No module named 'scripts.wiki_surgery'
AssertionError: 2 != 1
```

The baseline proved the repository had no surgery planning module and generated
`wiki-surgery-runs` records were still entering adjudication input.

## GREEN Result

Commands:

```bash
python3 -m unittest tests/test_wiki_surgery.py tests/test_wiki_content_adjudication.py
openspec validate add-wiki-surgery-planning --strict
python3 -m unittest tests/test_wiki_surgery.py tests/test_wiki_content_adjudication.py tests/test_wiki_treatment.py tests/test_wiki_review_decisions.py
python3 scripts/check_behavior_assets.py
python3 -c "import json, subprocess, sys; p=subprocess.run([sys.executable, 'scripts/build_wiki_surgery.py'], check=True, capture_output=True, text=True); data=json.loads(p.stdout); print({k:data['summary'][k] for k in sorted(data['summary'])}); print(data['status'])"
```

Results:

```text
Ran 14 tests in 1.957s
OK

Change 'add-wiki-surgery-planning' is valid

Ran 26 tests in 4.282s
OK

{'governance_change_count': 71, 'moc_projection_count': 0, 'relation_rebuild_count': 112, 'source_detail_count': 154, 'surgery_item_count': 130, 'taxonomy_decision_count': 0}
planned
```

OpenSpec emitted PostHog DNS flush warnings after validation. The change itself
validated successfully.

## MOC Boundary

MOC projection integration is explicit input only. The surgery planner accepts a
MOC dry-run plan and includes non-noop entries as surgery items. It does not
import or invoke `apply_moc_plan`, and it has no MOC write mode.

## Residual Risks

- The current runner plans surgery only; it does not apply surgery.
- Recovery records are not implemented in this change.
- The existing MOC projection draft files are still outside this change unless
  they are separately formalized and committed.


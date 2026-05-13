# Evaluation

## Pressure Scenarios

| Scenario | Expected Result | Evidence |
|---|---|---|
| Registered producer template hardcodes `domain: personal-ops` | Checker reports `producer_hardcoded_forbidden_domain` as `error` | `tests/test_wiki_frontmatter_taxonomy.py::test_registered_template_reports_hardcoded_forbidden_domain` |
| Sample ops governance page uses `domain: personal-ops` | Checker reports `forbidden_domain` as `error` | `tests/test_wiki_frontmatter_taxonomy.py::test_content_drift_reports_forbidden_personal_ops` |
| Sample pure governance page uses `domain: none` and valid `ops_area` | Checker reports no sample error for that page | `/tmp/wiki-frontmatter-taxonomy-report.json` sample-path check returned `[]` |
| Sample business intake uses `domain: nirvana` and `ops_area: source-intake` | Checker reports no sample error for that page | `/tmp/wiki-frontmatter-taxonomy-report.json` sample-path check returned `[]` |
| `domain: unclassified` appears without `classification_needed: true` | Checker reports `unclassified_without_flag` as `error` | `tests/test_wiki_frontmatter_taxonomy.py::test_unclassified_domain_requires_classification_flag` |
| Repo-local file contains frontmatter-like `domain:` but is not registered | Checker reports `possible_unregistered_producer` as `warn` | `tests/test_wiki_frontmatter_taxonomy.py::test_unregistered_frontmatter_producer_warns` |
| Agent creates or modifies wiki frontmatter | AGENTS routes to taxonomy skill and checker before completion claim | `tests/test_wiki_frontmatter_taxonomy_skill.py::test_agents_routes_frontmatter_changes_to_taxonomy_skill` |
| Taxonomy skill is loaded | Skill points to YAML and checker without duplicating taxonomy vocabulary | `tests/test_wiki_frontmatter_taxonomy_skill.py::test_taxonomy_skill_references_contract_without_vocab_duplication` |

## Skill Replay Evidence

Replay target: future agent behavior when wiki frontmatter is created or
modified.

| Replay Field | Evidence |
|---|---|
| Input or situation shape | Agent is asked to create or modify wiki frontmatter, wiki templates, or repo-local scripts that generate wiki frontmatter. |
| Trigger condition | Repo `AGENTS.md` contains a dedicated `Wiki Frontmatter Taxonomy Gate` requiring `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`. |
| Expected route or stop behavior | Agent loads `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`, reads `wiki/config/frontmatter-taxonomy.yaml`, and runs `python3 scripts/check_wiki_frontmatter.py` before claiming compliance. |
| Repo-visible artifact a future agent should read | `AGENTS.md`, `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`, `wiki/config/frontmatter-taxonomy.yaml`, and `scripts/check_wiki_frontmatter.py`. |
| Expected output or non-output | The agent reports checker results. It does not claim taxonomy compliance if checker errors remain. |
| Promotion or non-promotion boundary | This change creates a repo-local gate only. It does not promote the taxonomy to global AGENTS or team lore. |
| Residual risk or proof boundary | Tests prove local routing text, skill compactness, checker behavior, producer drift detection, and sample migration. They do not prove every future AI client will load the skill unless that client honors repo AGENTS and skill routing. |

## RED Baseline

- Existing article learning template contained `domain: personal-ops`.
- Existing ops pages contained `domain: personal-ops`.
- Existing inbox intake generator wrote `domain` directly from folder inference.
- Initial taxonomy skill route test failed because `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md` did not exist.
- Initial AGENTS route test failed because AGENTS did not route frontmatter changes through the taxonomy gate.

## GREEN Result

- Taxonomy contract exists at `wiki/config/frontmatter-taxonomy.yaml`.
- Taxonomy skill exists at `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`.
- AGENTS routes wiki frontmatter changes through the taxonomy skill and checker without duplicating the vocabulary.
- Checker emits JSON and Markdown reports.
- Producer templates no longer hardcode `domain: personal-ops`.
- `scripts/inbox_intake.py` emits `layer`, `ops_area`, and `classification_needed` when needed.
- Sample migration pages use `layer`, `domain`, and `ops_area` according to the contract.
- Targeted tests pass:

```bash
.venv-taxonomy/bin/python -m pytest tests/test_wiki_frontmatter_taxonomy.py tests/test_wiki_frontmatter_taxonomy_skill.py tests/test_inbox_intake.py -q
```

Result:

```text
19 passed
```

Checker command:

```bash
.venv-taxonomy/bin/python scripts/check_wiki_frontmatter.py
```

Result:

```text
exit code: 1
summary: {'error': 43, 'warn': 1, 'info': 0, 'total': 44}
sample-path remaining entries: []
```

The non-zero checker exit is expected for this first rollout because legacy
pages outside `sample_migration_paths` still contain taxonomy drift.

## Residual Risks

- Legacy pages outside `sample_migration_paths` still contain drift and require a
  later migration change.
- The checker intentionally does not perform broad Python static analysis.
- Business domain taxonomy remains thin and should be strengthened in a later
  change.
- The local `.venv-taxonomy` test environment was required because the system
  Python did not have pytest installed.

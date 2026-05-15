# Evaluation

## Behavior Replay

- Situation shape: `wiki-doctor` has produced adjudication details and review
  has confirmed a bounded treatment domain or detail.
- Trigger condition: treatment is invoked with `--approved-domain` or
  `--approved-detail`.
- Expected route: safe, risk-free frontmatter candidates enter treatment;
  risky, unapproved, taxonomy, relation, MOC, ADR, governance, or OpenSpec work
  stays skipped.
- Expected output: dry-run JSON by default; optional Markdown record under
  `wiki/ops/wiki-treatment-runs/`.
- Expected write behavior: page frontmatter writes happen only with `--apply`.
- Generated-artifact boundary: later adjudication excludes
  `wiki/ops/wiki-treatment-runs/` records from candidate input.
- Non-output boundary: treatment does not write relations, taxonomy config, MOC
  pages, ADR decisions, or OpenSpec state.
- Repo-visible artifact future agents should read:
  `openspec/changes/add-wiki-treatment-workflow/`.

## RED Baseline

Command:

```bash
python3 -m unittest tests/test_wiki_treatment.py
```

Result before implementation:

```text
ModuleNotFoundError: No module named 'scripts.wiki_treatment'
```

The baseline proved the repository had no executable treatment layer.

## GREEN Result

Commands:

```bash
python3 -m unittest tests/test_wiki_treatment.py
python3 -m unittest tests/test_wiki_treatment.py tests/test_wiki_review_decisions.py tests/test_wiki_content_adjudication.py
openspec validate add-wiki-treatment-workflow --strict
python3 scripts/build_wiki_treatment.py --approved-domain wiki
```

Result:

```text
Ran 6 tests in 1.390s
OK

Ran 20 tests in 3.971s
OK

Change 'add-wiki-treatment-workflow' is valid

dry-run repo smoke:
source_detail_count: 154
treatment_item_count: 5
skipped_item_count: 149
applied_count: 0
dry_run_count: 5
blocked_count: 0
```

OpenSpec emitted PostHog DNS flush warnings after validation. The change itself
validated successfully.

## Frontmatter Gate Boundary

Precheck before treatment implementation:

```bash
python3 scripts/wiki_gate_precheck.py --mode frontmatter
```

Result:

```text
passed: false
blocking_count: 786
```

The blocking count is pre-existing whole-wiki frontmatter drift. Treatment does
not claim whole-wiki taxonomy compliance; it only writes explicitly approved
suggested frontmatter fields and leaves checker compliance as the recovery step
for any applied target.

## Residual Risks

- Domain approval is currently per invocation (`--approved-domain`) rather than
  a durable approval registry.
- Treatment writes only frontmatter. Relation repair, MOC projection, taxonomy
  changes, and governance drift remain surgery/OpenSpec work.

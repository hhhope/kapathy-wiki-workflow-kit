# Evaluation

## Pressure Scenarios

1. `wiki/ops/visual-output-routing-fix-recheck-2026-05-11.md` lacks
   `layer`, `domain`, and `ops_area`; the checker must report it instead of
   silently passing.
2. `wiki/adr/0020-agent-readable-wiki-runtime-context-source-integration-after-runtime-context.md`
   lacks taxonomy fields; ADR pages must be covered by strict rules.
3. `wiki-status` must not present narrow taxonomy drift as whole-wiki
   compliance. It must render strict gate and scorecard evidence.
4. Current legacy debt must become visible, even if that means the checker exits
   non-zero.

## RED Baseline

Before implementation:

- `build_report()` did not include `strict_gate`.
- `build_report()` did not include `scorecard`.
- The checker did not apply configured whole-wiki rule sets.
- The two concrete missed page shapes produced no strict-gate errors.
- `wiki-status` did not render strict frontmatter gate or scorecard sections.

Baseline command:

```text
python3 -m unittest tests.test_wiki_frontmatter_taxonomy tests.test_wiki_status
```

Baseline result:

```text
FAILED (errors=4)
KeyError: 'strict_gate'
```

## GREEN Result

After implementation:

- `wiki/config/frontmatter-taxonomy.yaml` defines strict gate rule sets and
  scorecard weights.
- `scripts/check_wiki_frontmatter.py` reports `missing_required_field` and
  `unexpected_field_value` from configured rule sets.
- Checker output includes `strict_gate`, `scorecard`, and `proof_boundary`.
- `wiki-status` renders `Frontmatter Strict Gate` and
  `Frontmatter Scorecard`.
- ADR-0032 records the durable decision.

## Verification

- `python3 -m unittest tests.test_wiki_frontmatter_taxonomy tests.test_wiki_status tests.test_wiki_graph_summary tests.test_wiki_runtime_commands`
  - Result: pass, 27 tests.
- `python3 scripts/check_wiki_frontmatter.py`
  - Result: expected failure, exit code 1.
  - Report summary: 769 errors, 2 warnings, score 0 / 100.
  - This is the expected strict-gate result against current legacy debt.
- `python3 scripts/build_wiki_status.py`
  - Result: pass; generated `wiki/status/manifest.json` and
    `wiki/status/wiki-status.md` during verification.
  - Generated status showed strict gate failed, blocking entries 769, score
    0 / 100.
  - Generated status files were restored before commit to avoid committing
    unrelated dirty workspace state into tracked status artifacts.
- `openspec validate enforce-whole-wiki-frontmatter-gate --strict`
  - Result: pass; OpenSpec reported the change as valid.
  - Note: PostHog telemetry flush reported DNS/network errors after validation;
    the validation result itself was successful.
- `python3 scripts/check_behavior_assets.py`
  - Result: pass, exit code 0.

## Residual Risks

- The strict gate intentionally exposes a large historical backlog. This change
  does not migrate those pages.
- The scorecard is structural and configured; it does not infer semantic domain
  correctness from prose.
- Exceptions are not implemented beyond configuration shape; future exception
  use must include reason and owner.

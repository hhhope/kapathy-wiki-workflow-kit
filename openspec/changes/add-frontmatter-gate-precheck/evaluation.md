# Evaluation

## Pressure Scenarios

1. Positive trigger scenario: routine frontmatter checks should not require opening the full taxonomy YAML
   or full checker body.
2. Positive trigger scenario: the compact precheck must still preserve strict gate failure semantics when
   current legacy drift exists.
3. Positive trigger scenario: a target-specific check must show bounded target findings while preserving
   the whole-gate pass/fail result.
4. Negative should-not-trigger scenario: taxonomy config edits and checker debugging should not rely only on the
   compact precheck; those cases still load the YAML or checker source.
5. Positive trigger scenario: target-specific output should include repair hints
   for field补齐 so agents do not need to open the full YAML for ordinary missing-field fixes.
6. The skill routing change must be behavior-visible and must not duplicate
   taxonomy vocabulary.

## Behavior Replay

- Input or situation shape: an agent needs to check frontmatter compliance or
  remaining drift for the wiki, optionally focused on one target page.
- Trigger condition: the task is a routine frontmatter gate check and is not a
  taxonomy config edit or checker-debugging task.
- Expected route: run `python3 scripts/wiki_gate_precheck.py --mode frontmatter`
  first, adding `--target PATH` for a specific page.
- Repo-visible artifact: `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`,
  `scripts/wiki_gate_precheck.py`, and this OpenSpec change.
- Expected output: compact precheck JSON with pass/fail, score, minimum score,
  blocking count, summary counts, bounded top blockers, optional bounded target
  entries, target repair hints, and full report paths.
- Promotion or non-promotion boundary: compact precheck output may support
  routing and status claims, but taxonomy vocabulary or scorecard changes still
  require editing the YAML under the OpenSpec gate.
- Proof boundary: precheck summarizes configured checker evidence; it does not
  infer missing business domains from prose and does not replace the full report.

## Parent Gate Preservation

This change preserves the parent gate for frontmatter taxonomy work: the YAML
remains the taxonomy source of truth, semantic skill edits still require
evaluation, and workflow-level changes still require OpenSpec.

## RED Baseline

Before implementation:

- `scripts/wiki_gate_precheck.py` did not exist.
- The wiki frontmatter taxonomy skill listed the YAML and checker as direct
  load targets for routine use.
- No compact agent-readable precheck output existed; full drift entries were
  only available through the full checker report.

Baseline command:

```text
python3 -m unittest tests.test_wiki_gate_precheck tests.test_wiki_frontmatter_taxonomy_skill
```

Baseline result:

```text
ERROR: test_wiki_gate_precheck
ModuleNotFoundError: No module named 'scripts.wiki_gate_precheck'
```

## GREEN Result

After implementation:

- `scripts/wiki_gate_precheck.py` imports the full frontmatter checker, writes
  full JSON/Markdown reports, and emits compact JSON to stdout.
- Compact output contains pass/fail, score, minimum score, blocking count,
  summary counts, bounded top blockers, optional bounded target entries, full
  report paths, and proof boundary.
- Target output includes `repair_hints` with required fields, exact frontmatter
  values, relevant field options, and notes for when to open full YAML.
- `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md` now routes routine checks
  through `python3 scripts/wiki_gate_precheck.py --mode frontmatter` first.
- Full YAML/checker loading is reserved for taxonomy edits, checker debugging,
  or insufficient precheck evidence.
- The skill tells agents to use `target.repair_hints` before opening full YAML.

## Verification

- `python3 -m unittest tests.test_wiki_gate_precheck tests.test_wiki_frontmatter_taxonomy_skill`
  - Result: pass, 4 tests.
- `python3 -m unittest tests.test_wiki_gate_precheck`
  - Result after archive-review tail fix: pass, 2 tests.
- `python3 -m unittest tests.test_wiki_gate_precheck tests.test_wiki_frontmatter_taxonomy_skill tests.test_wiki_frontmatter_taxonomy tests.test_wiki_status tests.test_wiki_graph_summary tests.test_wiki_runtime_commands`
  - Result: pass, 31 tests.
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --top 3`
  - Result: expected failure, exit code 1.
  - Compact summary: strict gate failed, 769 blocking entries, score 0 / 100.
  - Top blockers were bounded to 3 grouped rows.
- `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/visual-output-routing-fix-recheck-2026-05-11.md --top 3`
  - Result: expected failure, exit code 1.
  - Target output included `repair_hints.required_fields`,
    `repair_hints.exact_frontmatter.layer: ops`, and bounded field options for
    `domain` and `ops_area`.
- `python3 scripts/check_wiki_frontmatter.py`
  - Result: expected failure, exit code 1.
  - Full report summary: 769 errors, 2 warnings, score 0 / 100.
- `python3 scripts/check_behavior_assets.py`
  - Result: pass, exit code 0.
- `openspec validate add-frontmatter-gate-precheck --strict`
  - Result: pass; OpenSpec reported the change as valid.
  - Note: PostHog telemetry flush reported DNS/network errors after validation;
    the validation result itself was successful.

## Prior-Art / Common-Rule Dedupe

- Scanned: repo `AGENTS.md`, `PROJECT.md`, `.codex/skills/wiki-frontmatter-taxonomy/SKILL.md`,
  `wiki/config/frontmatter-taxonomy.yaml`, `scripts/check_wiki_frontmatter.py`,
  `wiki/config/behavior-asset-evaluation.yaml`, common development/testing
  rules, and `openspec/changes/enforce-whole-wiki-frontmatter-gate`.
- Owns: compact Python precheck entrypoint and the skill's routine-check routing
  instruction.
- References: existing strict taxonomy semantics remain in
  `wiki/config/frontmatter-taxonomy.yaml` and `scripts/check_wiki_frontmatter.py`.
- References: generic behavior-asset evaluation and TDD requirements remain governed by
  repo `AGENTS.md` and common rules; this change references that process through
  this evaluation file instead of restating it in the skill.
- Rejects: duplicating taxonomy vocabulary, scorecard formulas, or generic
  behavior-asset/TDD rules inside the skill.

## Residual Risks

- The precheck is a compact summary. It intentionally omits the full `entries`
  list from agent-facing output.
- Repair hints do not infer semantic business domain from prose. If exact
  values and field options are insufficient, the agent must load the taxonomy
  config or ask for classification.
- The current whole-wiki strict gate still fails on historical frontmatter debt;
  this change does not migrate those pages.

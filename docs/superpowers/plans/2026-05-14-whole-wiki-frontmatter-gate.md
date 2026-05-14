# Whole Wiki Frontmatter Gate Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make the report wiki frontmatter gate strict, config-driven, and scorecarded across the whole `wiki/**` tree.

**Architecture:** `wiki/config/frontmatter-taxonomy.yaml` owns strict rule configuration, `scripts/check_wiki_frontmatter.py` produces the machine evidence and scorecard, and `wiki-status` renders that evidence. ADR-0032 records the durable governance decision.

**Tech Stack:** Python 3 standard library, PyYAML, unittest, OpenSpec markdown artifacts.

---

## File Structure

- Create `wiki/adr/0032-whole-wiki-frontmatter-gate-must-be-strict-and-scorecarded.md` for the stable decision.
- Modify `wiki/config/frontmatter-taxonomy.yaml` to add strict gate rule sets and scorecard weights.
- Modify `scripts/check_wiki_frontmatter.py` to evaluate configured rule sets and emit `strict_gate` plus `scorecard`.
- Modify `scripts/build_wiki_status.py` and `scripts/wiki_status_render.py` to pass through and render strict gate evidence.
- Modify `tests/test_wiki_frontmatter_taxonomy.py` for checker RED/GREEN coverage.
- Modify `tests/test_wiki_status.py` for status rendering coverage.
- Update `openspec/changes/enforce-whole-wiki-frontmatter-gate/evaluation.md` with evidence after implementation.

## Implementation Steps

- [ ] Add ADR-0032 with compliant frontmatter.
- [ ] Extend taxonomy YAML with `strict_gate` and `scorecard`.
- [ ] Add tests proving an ops page missing `layer/domain/ops_area` is reported.
- [ ] Add tests proving an ADR page missing `layer/domain` is reported.
- [ ] Add tests proving checker emits scorecard and strict gate failure.
- [ ] Implement strict rule-set matching using `Path.match()`.
- [ ] Implement `missing_required_field` entries.
- [ ] Implement scorecard aggregation from configured dimensions.
- [ ] Render strict frontmatter gate and scorecard in wiki status.
- [ ] Run focused tests and live checker/status commands.
- [ ] Record verification in OpenSpec evaluation and mark tasks complete.

## Verification Commands

```bash
python3 -m unittest tests/test_wiki_frontmatter_taxonomy.py tests/test_wiki_status.py
python3 scripts/check_wiki_frontmatter.py
python3 scripts/build_wiki_status.py
openspec validate enforce-whole-wiki-frontmatter-gate --strict
```

Expected checker result against the current repository may be non-zero because
the new strict gate exposes existing legacy debt.

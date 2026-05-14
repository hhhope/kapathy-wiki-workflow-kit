# Design

## Boundary

This change is a runtime-entry improvement for an existing gate. It does not
change taxonomy semantics. The YAML config remains the source of truth, and
`scripts/check_wiki_frontmatter.py` remains the full checker.

## Precheck Contract

Add `scripts/wiki_gate_precheck.py` with a narrow interface:

- `--mode frontmatter`
- optional `--target PATH` for path-focused output
- optional `--top N` for bounded example entries
- optional JSON and Markdown output paths

The script imports `build_report()` from `scripts/check_wiki_frontmatter.py`,
then emits a compact report:

- gate name
- pass/fail
- score and minimum score
- blocking count
- summary counts
- top blocker groups
- target entries when `--target` is supplied
- full report paths
- proof boundary

The script exits non-zero when the underlying strict gate fails.

## Skill Routing

`.codex/skills/wiki-frontmatter-taxonomy/SKILL.md` should instruct routine
checks to run the precheck first. Full YAML/checker loading is reserved for:

- taxonomy config edits
- checker/debug work
- cases where precheck output is insufficient to choose a field or rule

## Evaluation Shape

Because this is a behavior-asset change, the evaluation records:

- RED baseline: old skill text required loading the YAML/checker directly and
  no compact precheck script existed.
- GREEN result: tests show the skill routes routine checks to precheck and the
  precheck output remains compact while preserving full-report links.

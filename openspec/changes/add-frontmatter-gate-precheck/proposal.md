# Proposal

## Why

The strict frontmatter gate now exposes whole-wiki drift, but the default agent
path can still encourage opening the full taxonomy YAML and full checker body
for ordinary gate checks. That is unnecessary context pressure.

Agents need a compact Python precheck entrypoint that reads the configured gate,
returns pass/fail and scorecard evidence, and points to full reports only when
debugging or taxonomy edits require them.

## What Changes

- Add a compact `scripts/wiki_gate_precheck.py` entrypoint for frontmatter gate
  checks.
- Keep `wiki/config/frontmatter-taxonomy.yaml` as the machine-readable source of
  truth.
- Update the wiki frontmatter taxonomy skill so routine checks run the precheck
  instead of loading the full YAML/checker by default.
- Add behavior/evaluation evidence for the skill routing change.

## Out of Scope

- Migrating legacy wiki pages to satisfy the strict gate.
- Changing scorecard dimensions or taxonomy vocabulary.
- Replacing the full checker report.

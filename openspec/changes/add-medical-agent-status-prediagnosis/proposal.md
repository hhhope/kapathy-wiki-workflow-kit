# Proposal: medical-agent status prediagnosis

## Why

`wiki-medical-agent` currently reports fixed status fields, but a status result
can become a dead end when the user is actually asking to continue, modify, or
decide the next route.

## What Changes

- Add a compact `Status / Blocked Response` rule to the repo-local
  `wiki-medical-agent` skill.
- Require read-only prediagnosis before asking the user for more detail when
  the script result is non-executing status but the live intent is to continue
  or modify.
- Preserve existing write boundaries.

## Out of Scope

- No changes to `scripts/build_wiki_medical_agent.py`.
- No global agent rule.
- No automatic mutation of MOC pages, ADRs, OpenSpec lifecycle state, taxonomy
  config, relation fields, or skills beyond this scoped skill edit.

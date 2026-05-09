# Design: Add Explicit Chinese Ops Frontmatter

## Approach

Use page-local explicit identity fields instead of expanding resolver behavior:

- `ai-chat-workflow-installer / explore`
- `baocaitong-split-account-migration / reminder`
- `baocaitong-split-account-migration / scenario-matrix`

This keeps Chinese titles readable while giving the runtime stable English
canonical objects.

## Boundary

- No extractor change.
- No inference from arbitrary Chinese prose.
- No broad Chinese filename convention.
- No edits to unrelated dirty ops or status files.

## Verification

- Live graph extraction should report `warning_count: 0`.
- Existing graph extraction tests should pass.
- OpenSpec validation should pass.

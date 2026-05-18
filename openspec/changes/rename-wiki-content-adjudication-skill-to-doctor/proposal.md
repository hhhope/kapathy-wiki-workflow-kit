# Proposal: rename wiki content adjudication skill to wiki-doctor

## Summary

Rename the standalone content adjudication skill entry from
`wiki-content-adjudication` to `wiki-doctor`.

## Problem

`wiki-content-adjudication` is accurate but too long and too internal. The
user-facing job is to diagnose wiki review-package risks, not to expose the
implementation term.

## Scope

In scope:

- add `.codex/skills/wiki-doctor/SKILL.md`
- update runtime skill tests to use `wiki-doctor`
- remove the old `wiki-content-adjudication` skill file from the active skill
  surface

Out of scope:

- renaming adjudication scripts
- changing adjudication package schema
- slash command surface
- frontmatter writes, taxonomy mutation, or MOC writes

## Success Criteria

- `$report-wiki-portfolio:wiki-doctor` is the direct skill entry.
- The skill still routes to `scripts/build_wiki_content_adjudication.py`.
- The review-only boundaries remain unchanged.

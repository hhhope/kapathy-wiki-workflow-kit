# Proposal: wiki content adjudication skill

## Summary

Add a standalone repo-local `wiki-content-adjudication` skill so users can
enter the content adjudication review package directly instead of routing
through `wiki-react` and `wiki-apply`.

## Problem

The adjudication runtime exists, but the user-facing skill surface is split:

- `wiki-react` recognizes `wiki_content_adjudication`
- `wiki-apply` can display `content_adjudication_review_package`
- `scripts/build_wiki_content_adjudication.py` builds the package

This is operationally correct but hard to use because there is no direct skill
name for the review-package workflow.

## Scope

In scope:

- add `.codex/skills/wiki-content-adjudication/SKILL.md`
- update runtime skill tests to recognize the new entry
- keep existing `wiki-react` and `wiki-apply` routes intact

Out of scope:

- direct frontmatter writes
- taxonomy mutation
- MOC writes
- slash command surface
- graph UI, query engine, or change queue

## Success Criteria

- `$report-wiki-portfolio:wiki-content-adjudication` is a discoverable
  repo-local skill.
- The skill routes directly to
  `python3 scripts/build_wiki_content_adjudication.py`.
- The skill preserves the review-only boundary and existing OpenSpec/task
  boundary phrases checked by tests.

## Why

The repository already has example-driven capture and README-learning capture, but
general article learning still lacks a stable workflow.

Recent agent / harness article work exposed repeated failures:

- article learning was first recorded in OpenSpec evaluation instead of wiki
- article notes were then misplaced under an existing governance framework
- the intake page started acting like a conclusion page rather than a learning
  directory
- extracted claim tables appeared before a proper source-first reading method
- there was no pre-score to decide whether a long article deserved deep reading

The user wants article learning to become a repeatable SOP with rigorous source
capture, a scorecard, structured translation notes, reusable extraction, and
clear promotion boundaries.

## What Changes

- Add a repo-local `article-learning-capture` skill for external article
  learning tasks.
- Add skill references for:
  - article-learning SOP
  - scorecard and skip thresholds
  - wiki output template
  - pressure scenarios
- Add an OpenSpec capability for article learning capture.
- Update the current agent harness article-learning intake so it behaves as a
  directory and method entry, not as a compressed conclusion page.

## Non-Goals

- Do not create a general article crawler.
- Do not store full copyrighted article text or full verbatim translations.
- Do not promote article takeaways directly into `AGENTS.md`, specs, hard skill
  rules, or archive-ready claims.
- Do not retrofit every existing article note into the new template in this
  change.

## Impact

- Adds `.codex/skills/article-learning-capture/`.
- Adds `openspec/changes/formalize-article-learning-capture/`.
- Tightens future article-learning behavior without replacing `weixin-reader`
  or `readme-learning-capture`.

# Article Module

Use this module for articles, blogs, papers, WeChat posts, newsletters, and
article collections.

## Delegate

For full article workflow details, load
`.codex/skills/article-learning-capture/SKILL.md`.

## Required Gates

- Preserve original URL, title, publisher or author when available, publication
  date when available, and access date.
- Classify source before scoring: primary source, secondary interpretation,
  structure reference, or low-relevance/general-interest.
- Preserve source grounding before analysis: extracted markdown when permitted,
  source map with bounded excerpts, or retrieval-failure note.
- Score before deep reading.
- Use the article scorecard threshold: 75+ deep-read, 60-74 brief candidate,
  below 60 skip reason.
- Mark retrospective scoring explicitly; it is not score-first admission
  evidence.
- Respect copyright boundaries: no full verbatim copyrighted article text and no
  full verbatim translation.
- Separate article comprehension from local transfer extraction.

## When Article Becomes Repo Learning

If the article describes a GitHub/GitLab project and the user asks whether the
project structure or README can be reused, read the repo/README and then route
that second step through `repo-readme.md`.

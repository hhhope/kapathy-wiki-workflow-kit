---
name: article-learning-capture
description: Use when the user provides external articles, blogs, papers, WeChat posts, or article collections and wants deep reading, learning extraction, scoring, wiki capture, or reusable SOP/adaptation decisions.
---

# Article Learning Capture

## Overview

Turn external article reading into durable repository learning. The goal is not
summary; the goal is source-grounded learning that can be audited, reused, or
rejected without becoming an unsupported rule.

## When To Use

Use this skill when the user provides or references external articles and asks
for:

- deep reading or `精读`
- learning what is useful
- wiki capture
- a reusable SOP, method, or adaptation decision
- scoring whether the article is worth learning
- extracting candidate practices for this repo or agent workflow

Prefer narrower skills when they apply:

- GitHub/GitLab repo or README learning: `readme-learning-capture`
- WeChat article body extraction: `weixin-reader`
- WeChat article as writing, visual, or method reference: `weixin-reference-wiki-capture`

Do not use this skill for ordinary news summaries, fact lookup, or one-off
article digestion with no local reuse intent.

## Hard Rules

- Score before deep reading.
- Always preserve the original URL, title, publisher or author when available,
  publication date when available, and access date.
- Classify the source before scoring: primary source, secondary
  interpretation, structure reference, or low-relevance/general-interest.
- Preserve source grounding before analysis: extracted markdown when permitted,
  a section map with bounded excerpts when full text cannot be stored, or a
  retrieval-failure note that asks for pasted text or screenshots.
- For copyrighted sources, write structured translation notes or paraphrased
  reading notes; do not store full verbatim article text or a full verbatim
  translation.
- Separate article comprehension from local transfer extraction.
- Keep extracted learning as candidate unless promotion evidence exists.
- Do not promote article takeaways into `AGENTS.md`, specs, hard skill rules, or
  archive-ready claims without the repository evidence-backed gate.
- If source retrieval fails, ask for pasted text or screenshots instead of
  inventing content.

## References

- SOP: `references/sop.md`
- Scorecard: `references/scorecard.md`
- Wiki template: `references/wiki-template.md`
- Pressure scenarios: `references/pressure-scenarios.md`

## Common Mistakes

- Treating a claim table as a substitute for reading the article.
- Compressing an article so aggressively that no skill or judgment can be
  learned.
- Putting article learning under an unrelated governance framework because the
  topic sounds adjacent.
- Reading every provided article deeply without a score threshold.
- Treating another model's summary as evidence when the original source was not
  checked.

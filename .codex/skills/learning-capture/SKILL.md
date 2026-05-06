---
name: learning-capture
description: Use when the user provides articles, repo/README links, or examples as learning, reference, or adaptation material, including bare links whose purpose is implied by recent context.
---

# Learning Capture

## Overview

Route learning requests before material-specific workflows run. The goal is to
decide whether the request is learning at all, then choose the right evidence
object and module.

## When To Use

Use this skill when the user gives an external source as learning or reference
material. The learning intent may be explicit or inherited from the current
thread.

Explicit signals include:

- deep reading or `精读`
- learning capability or reusable method
- wiki capture
- scoring whether a source is worth deeper work
- deciding what to reuse, adapt, reject, or formalize
- turning source learning into an SOP, template, candidate skill, or workflow
  decision

Implicit signals include:

- the user drops article, repo, README, or example links inside an active
  learning / governance / method-calibration thread
- the user asks "can we use this approach?" or "what did we learn from this?"
  after providing a source
- the user provides a source after asking to define how learning should work

Do not use this skill for latest-news answers, fact lookup, raw source fetching,
short abstracts, or one-off digestion with no local reuse intent.

## Hard Rules

- Classify intent before reading deeply.
- If the user only provides a link, inspect conversation context before deciding
  whether it is learning material or a raw fetch / lookup request.
- Route by evidence object: article-shaped, repo/README-shaped, or
  example-shaped.
- Prefer narrower source tools for raw fetching, such as `weixin-reader`.
- Do not promote external-source takeaways into `AGENTS.md`, specs, hard skill
  rules, or archive-ready claims without the repository evidence-backed gate.
- Keep module-specific gates intact; the router does not weaken source
  grounding, scoring, adaptation-boundary, or promotion requirements.

## Module Map

| Source Kind | Load |
|---|---|
| Article, blog, paper, WeChat post, article collection | `references/article.md` |
| GitHub/GitLab repo or README | `references/repo-readme.md` |
| Writing, visual, output-shape, structure, or method example | `references/example-reference.md` |
| Unclear source or mixed source | `references/routing.md` |

## References

- Routing: `references/routing.md`
- Article module: `references/article.md`
- Repo/README module: `references/repo-readme.md`
- Example reference module: `references/example-reference.md`
- Pressure scenarios: `references/pressure-scenarios.md`

## Common Mistakes

- Treating every external link as learning.
- Deep-reading before deciding whether the user wants durable local transfer.
- Using an article about a repo as proof of the repo's structure without reading
  the repo or README.
- Collapsing source summary, source grounding, local usefulness, and promotion
  evidence into one table.

# Learning Capture Article Module Retirement Design

> Supports a future OpenSpec change. This Superpowers design is not
> authoritative lifecycle state until it is copied into OpenSpec and reviewed
> there.

## Context

The repository currently has `learning-capture` as the intended runtime router
for learning requests, but `.codex/skills/article-learning-capture/SKILL.md`
still exists as a directly triggerable skill. Its description can still match
article, WeChat, deep-reading, and learning-extraction requests before the
agent reaches `learning-capture`.

That creates a dual-entry problem:

- `learning-capture` is the desired domain router.
- `article-learning-capture` still advertises itself as an active runtime
  entry.
- Durable article-learning templates already set `language: zh-CN`, but the
  body structure still leans toward English reading-note output.

The governance goal is to make learning routing single-entry and make durable
wiki learning output Chinese-first without changing the English-first contract
for behavior assets such as `SKILL.md`.

## Design Goal

Make `learning-capture` the only active runtime skill for learning requests.
Retire `article-learning-capture` as a skill surface while preserving any useful
article-specific workflow content as `learning-capture` reference material.

Durable learning notes written into `wiki/sources` or `wiki/ops` should default
to Chinese unless the user, target artifact, or audience explicitly requires
English.

## Approaches Considered

### Recommended: Retire Article Skill Surface, Preserve Useful Module Content

Remove the active `article-learning-capture` skill trigger surface. Migrate
useful article-specific rules into `learning-capture/references/article.md` or
adjacent reference files.

Pros:

- Removes the description pollution that can route future sessions to the old
  article skill.
- Keeps the article source-grounding, scoring, and copyright rules that are
  still useful.
- Matches the existing direction that `learning-capture` owns learning intent
  routing.

Cons:

- Requires careful migration evidence so useful article rules are not lost.
- Existing archive and wiki references must be treated as historical context,
  not active runtime routing.

### Alternative: Keep Article Skill as a Compatibility Alias

Keep `.codex/skills/article-learning-capture/SKILL.md`, but rewrite it to say
that callers should route through `learning-capture`.

Pros:

- Smaller file movement.
- Preserves a visible legacy pointer.

Cons:

- Still exposes a `SKILL.md` description to the skill matcher.
- Continues to create a second runtime signal.
- Fails the user's core requirement that `article-learning-capture` no longer
  appear as the learning entry.

### Alternative: Only Add Chinese-First Output Rules

Add Chinese-first output wording to `learning-capture` and article templates
without changing the article skill surface.

Pros:

- Smallest change.

Cons:

- Does not solve the dual-entry runtime problem.
- Future sessions could still trigger article learning directly and bypass the
  domain router.

## Runtime Routing Design

`learning-capture` is the only runtime entry for learning. It decides whether a
source is learning material, then routes by evidence object:

- article, blog, paper, WeChat post, or article collection
- GitHub/GitLab repo or README
- writing, visual, output-shape, structure, or method example
- unclear or mixed source

`article-learning-capture` should not remain as an active `SKILL.md`
description. Keeping content is acceptable; keeping a skill trigger is not.

Acceptable end states:

- article module content lives under `.codex/skills/learning-capture/references/`
- historical context lives in OpenSpec archive, wiki pages, or a non-triggering
  legacy note
- no active skill description advertises `article-learning-capture` as a
  triggerable skill

## Article Content Migration

Do not mechanically copy all old article-skill text. Classify existing
`article-learning-capture` content before migrating it.

Keep and migrate article-specific rules that still serve the module:

- original URL, title, publisher or author, publication date, and access date
- source class before scoring
- source grounding before analysis
- score-first triage and the deep-read threshold
- copyright boundaries
- separation of article comprehension from local transfer extraction
- structured translation notes
- transferable learning, rejected moves, and promotion boundaries

Merge or dedupe rules already owned elsewhere:

- general learning intent routing belongs to `learning-capture`
- promotion into `AGENTS.md`, specs, or hard skill rules belongs to repo
  governance and behavior-asset gates
- generic behavior-asset evaluation belongs to the shared/repo governance
  rules, not the article module

Delete or preserve only as historical context:

- old `description` wording
- old "When To Use this skill" entry routing
- compatibility-entry language
- references that imply `article-learning-capture` remains an active skill

## Chinese-First Learning Output

Behavior assets remain English-first. The change is about generated durable
learning artifacts, not about writing skill governance text in Chinese.

Default Chinese-first output applies to:

- `wiki/sources` learning captures
- `wiki/ops` learning intakes, reading notes, reusable-learning records, and
  method-retro notes
- article, README/repo, and example learning notes when they are internal repo
  knowledge

English remains appropriate when:

- the user explicitly asks for English
- the target artifact is English-first, such as `SKILL.md`, public English
  README/docs, or an external repo artifact
- the audience or delivery channel requires English

Article templates should make this default visible in both frontmatter and body
structure. `language: zh-CN` is not enough if headings and prompts still drive
English reading-note output.

## OpenSpec and Evidence Plan

Implementation requires a new OpenSpec change because this is a repo workflow
and behavior-asset routing change.

The OpenSpec change should include:

- prior-art scan across `AGENTS.md`, `PROJECT.md`, active specs, relevant
  archived specs, wiki ADRs, wiki ops pages, existing skills, and common rules
- RED baseline proving the current active article skill description can still
  pollute runtime routing
- RED baseline proving article learning templates can still encourage English
  reading-note bodies despite `language: zh-CN`
- GREEN result proving `learning-capture` is the only active learning runtime
  skill
- GREEN result proving useful article-specific rules survived in references
- pressure scenarios for Chinese WeChat learning, direct article-learning
  phrasing, README/repo learning, example learning, and English target artifacts
- behavior replay evidence for future runtime routing

Expected verification commands include:

```bash
rg -n 'description:.*article|article-learning-capture' .codex/skills
python3 scripts/check_behavior_assets.py
```

If the implementation modifies wiki frontmatter or templates that generate wiki
frontmatter, also run:

```bash
python3 scripts/check_wiki_frontmatter.py
```

## Success Criteria

This design succeeds when a future session can read the active skill list and
see only `learning-capture` as the learning runtime entry, while article-specific
workflow quality remains available through reference modules.

It also succeeds when a Chinese article or WeChat learning request produces a
Chinese durable wiki learning page by default, without weakening English-first
behavior-asset authoring rules.

## Decision

Use the recommended approach: retire the active `article-learning-capture`
skill surface, preserve only useful article module content under
`learning-capture`, and make durable learning output Chinese-first by default.

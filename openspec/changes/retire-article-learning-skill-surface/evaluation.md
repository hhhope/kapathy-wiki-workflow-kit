# Evaluation

## RED Baseline

### Active Article Skill Description Pollution

Command:

```bash
rg -n '^description:.*(article|WeChat|deep reading|learning extraction)|article-learning-capture' .codex/skills/*/SKILL.md .codex/skills/learning-capture/references/article.md .codex/skills/article-learning-capture/references/wiki-template.md
```

Expected baseline: the command returns the active
`.codex/skills/article-learning-capture/SKILL.md` description and delegation
references.

Observed summary:

- `.codex/skills/article-learning-capture/SKILL.md:2` still declares
  `name: article-learning-capture`.
- `.codex/skills/article-learning-capture/SKILL.md:3` still exposes a
  description for external articles, blogs, papers, WeChat posts, article
  collections, deep reading, learning extraction, scoring, wiki capture, and
  reusable adaptation decisions.
- `.codex/skills/learning-capture/references/article.md:9` still references
  `.codex/skills/article-learning-capture/SKILL.md`.
- The broad routing grep also matched the active `learning-capture` router
  description and `weixin-reader` description, confirming adjacent active
  article/link surfaces remain visible before this change is implemented.

Result: RED. The retired article module is still an active runtime skill
surface and `learning-capture` still delegates to it.

### English Article Template Body

Command:

```bash
rg -n '^# <Topic> / Reading Notes|## Source|## Reading Draft|### Problem|### Structured Translation Notes' .codex/skills/article-learning-capture/references/wiki-template.md
```

Expected baseline: the command returns English headings.

Observed summary:

- `.codex/skills/article-learning-capture/references/wiki-template.md:32`
  contains `# <Topic> / Reading Notes`.
- `.codex/skills/article-learning-capture/references/wiki-template.md:34`
  contains `## Source`.
- `.codex/skills/article-learning-capture/references/wiki-template.md:83`
  contains `## Reading Draft`.
- `.codex/skills/article-learning-capture/references/wiki-template.md:85`
  contains `### Problem`.
- `.codex/skills/article-learning-capture/references/wiki-template.md:98`
  contains `### Structured Translation Notes`.

Result: RED. The article wiki template still contains English body headings
despite the durable learning output needing a Chinese-first default.

## Prior-Art / Common-Rule Dedupe

| Source | Ownership |
|---|---|
| `AGENTS.md` | Repo workflow gates, OpenSpec boundary, behavior-asset prior-art gate, skill authoring contract |
| `PROJECT.md` | OpenSpec as source of truth and wiki purpose |
| `.codex/skills/learning-capture/SKILL.md` | Learning intent routing and evidence-object module map |
| `wiki/ops/learning-capture-routing.md` | Historical rationale for learning domain router and module references |
| `wiki/adr/0010-shared-skill-authoring-contract-before-repo-local-overrides.md` | English-first behavior asset contract and repo language carve-out |
| `wiki/adr/0026-retire-draft-skills-as-runtime-surface.md` | Runtime surface must not keep misleading draft/duplicate skill signals |
| `openspec/changes/archive/2026-05-06-formalize-article-learning-capture/*` | Historical article-learning source grounding and score-first design |

# Evaluation

## RED Baseline

### Active Article Skill Description Pollution

Targeted failure command:

```bash
rg -n '^name: article-learning-capture|^description:.*(external articles|WeChat posts|deep reading|learning extraction)' .codex/skills/article-learning-capture/SKILL.md
```

Expected baseline: the command returns the active
`.codex/skills/article-learning-capture/SKILL.md` skill name and trigger
description.

Observed summary:

- `.codex/skills/article-learning-capture/SKILL.md:2` still declares
  `name: article-learning-capture`.
- `.codex/skills/article-learning-capture/SKILL.md:3` still exposes a
  description for external articles, blogs, papers, WeChat posts, article
  collections, deep reading, learning extraction, scoring, wiki capture, and
  reusable adaptation decisions.

Result: RED. The retired article module is still an active runtime skill
surface.

Broad inventory command:

```bash
rg -n '^description:.*(article|WeChat|deep reading|learning extraction)|article-learning-capture' .codex/skills/*/SKILL.md .codex/skills/learning-capture/references/article.md .codex/skills/article-learning-capture/references/wiki-template.md
```

Expected inventory: the command returns the active article skill trigger,
`learning-capture` article delegation, and adjacent article/link surfaces that
may remain valid after this change.

Observed summary:

- `.codex/skills/article-learning-capture/SKILL.md:2` still declares
  `name: article-learning-capture`.
- `.codex/skills/article-learning-capture/SKILL.md:3` still exposes the old
  active article-learning description.
- `.codex/skills/learning-capture/references/article.md:9` still references
  `.codex/skills/article-learning-capture/SKILL.md`.
- The broad routing grep also matched the active `learning-capture` router
  description and `weixin-reader` description. Those matches are adjacency
  inventory, not standalone RED failures for this retirement change.

Result: RED for the old article skill trigger and delegation reference only.
Future GREEN audit should not treat desired `learning-capture` or
`weixin-reader` adjacency matches as failures by themselves.

Original broad baseline command retained for comparison:

```bash
rg -n '^description:.*(article|WeChat|deep reading|learning extraction)|article-learning-capture' .codex/skills/*/SKILL.md .codex/skills/learning-capture/references/article.md .codex/skills/article-learning-capture/references/wiki-template.md
```

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

## Accepted Spec Contradiction Baseline

Command:

```bash
rg -n 'article-learning-capture/SKILL.md|dedicated article learning|dedicated skill' openspec/specs/article-learning-capture/spec.md openspec/changes/retire-article-learning-skill-surface/specs/learning-capture-runtime/spec.md
```

Observed summary:

- `openspec/specs/article-learning-capture/spec.md:6` still contains
  `Requirement: Repository SHALL provide a dedicated skill for external article
  learning capture`.
- `openspec/specs/article-learning-capture/spec.md:17` still routes deep
  article learning through the dedicated article learning capture skill.

Result: RED. The change needs an `article-learning-capture` delta that removes
the dedicated runtime skill requirement while preserving article-specific gates
as `learning-capture` module/reference material.

## Migration Classification

| Old content | Result | Reason |
|---|---|---|
| Article metadata and source grounding | Keep in `article-sop.md` and `article.md` | Article-specific audit value |
| Score-first thresholds | Keep in `article-scorecard.md` and `article.md` | Article-specific admission value |
| Copyright boundary | Keep in `article-sop.md` and `article.md` | Article-specific source handling |
| Structured translation notes | Keep in `article-sop.md` and `article-wiki-template.md` | Article-specific reading value |
| Transferable learning and rejected moves | Keep in `article-sop.md`, `article-wiki-template.md`, and `article.md` | Article-specific local transfer value |
| General learning intent routing | Deduplicate | Owned by `learning-capture` |
| Promotion into behavior assets | Reference only | Owned by repo governance and behavior-asset gates |
| Old `description` and `When To Use` entry wording | Delete | It recreates runtime trigger pollution |

## GREEN Result

### Active Skill Surface

Command:

```bash
find .codex/skills -maxdepth 2 -name SKILL.md | sort | rg 'article-learning-capture|learning-capture'
```

Expected result: only `.codex/skills/learning-capture/SKILL.md` appears for
learning capture.

Observed result after deletion:

```text
.codex/skills/learning-capture/SKILL.md
.codex/skills/readme-learning-capture/SKILL.md
```

The retired `.codex/skills/article-learning-capture/SKILL.md` surface does not
appear. The existing README learning skill also matches this broad grep pattern
because its path contains `learning-capture`; it is outside this task's article
surface retirement scope.

### Active Description Scan

Command:

```bash
rg -n '^description:.*(article|WeChat|deep reading|learning extraction)|article-learning-capture' .codex/skills/*/SKILL.md
```

Expected result: no active `article-learning-capture` description remains.

Observed result after deletion: no active `article-learning-capture`
description remains. The command still reports the intended `learning-capture`
router description and the existing `weixin-reader` article-reader description.

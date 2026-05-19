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

Scanned:

- `AGENTS.md`
- `PROJECT.md`
- `.codex/skills/learning-capture/SKILL.md`
- `.codex/skills/learning-capture/references/*`
- `openspec/specs/article-learning-capture/spec.md`
- `openspec/specs/learning-capture-routing/spec.md`
- `wiki/ops/learning-capture-routing.md`
- `wiki/adr/0010-shared-skill-authoring-contract-before-repo-local-overrides.md`
- `wiki/adr/0026-retire-draft-skills-as-runtime-surface.md`
- `openspec/changes/archive/2026-05-06-formalize-article-learning-capture/*`

| Source | Ownership |
|---|---|
| `AGENTS.md` | Repo workflow gates, OpenSpec boundary, behavior-asset prior-art gate, skill authoring contract |
| `PROJECT.md` | OpenSpec as source of truth and wiki purpose |
| `.codex/skills/learning-capture/SKILL.md` | Learning intent routing and evidence-object module map |
| `wiki/ops/learning-capture-routing.md` | Historical rationale for learning domain router and module references |
| `wiki/adr/0010-shared-skill-authoring-contract-before-repo-local-overrides.md` | English-first behavior asset contract and repo language carve-out |
| `wiki/adr/0026-retire-draft-skills-as-runtime-surface.md` | Runtime surface must not keep misleading draft/duplicate skill signals |
| `openspec/changes/archive/2026-05-06-formalize-article-learning-capture/*` | Historical article-learning source grounding and score-first design |

Owns:

- This change owns retirement of the active
  `.codex/skills/article-learning-capture/SKILL.md` runtime surface.
- This change owns migration of article-only workflow details into
  `learning-capture` references.
- This change owns Chinese-first durable internal article learning note
  defaults for the article wiki template.

References:

- Repo governance continues to own promotion into `AGENTS.md`, specs, skills,
  and other behavior assets.
- `learning-capture` continues to own the parent gate for learning, reference,
  reuse, and adaptation intent.
- `weixin-reader` continues to own raw WeChat article reading or extraction
  when the user asks for article body access rather than reusable learning.

Rejects:

- Do not recreate a standalone active `article-learning-capture` skill surface.
- Do not promote article takeaways into hard rules without evidence and the
  applicable OpenSpec or behavior-asset gate.
- Do not treat README/repo learning or example/reference learning as in scope
  for this article-surface retirement beyond pressure-scenario guardrails.

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

Actual output:

```text
.codex/skills/learning-capture/SKILL.md:3:description: Use when the user provides articles, repo/README links, or examples as learning, reference, or adaptation material, including bare links whose purpose is implied by recent context.
.codex/skills/weixin-reader/SKILL.md:3:description: Use when the user provides an mp.weixin.qq.com article link and wants to read, analyze, summarize, or extract the article content
```

Result: PASS. These are adjacent active surfaces, not the retired
`article-learning-capture` surface.

## Pressure Scenarios

Positive trigger scenarios:

| Scenario | Expected behavior | Result |
|---|---|---|
| User provides a Chinese WeChat article and says "学一下，落 wiki" | Load `learning-capture`, route to article module, produce Chinese durable learning notes | PASS |
| User says "article learning 这套复用一下" | Load `learning-capture`, not a separate `article-learning-capture` skill | PASS |
| User provides a GitHub README for reuse | Load `learning-capture`, route to repo/README module | PASS |
| User provides an output-shape example | Load `learning-capture`, route to example/reference module | PASS |

Negative / should-not-trigger scenarios:

| Scenario | Expected behavior | Result |
|---|---|---|
| User asks only to fetch raw WeChat body text | Use `weixin-reader`; do not force learning capture | PASS |
| User sends a bare link with no learning thread, reuse intent, wiki intent, or method-calibration context | Do not trigger learning capture by default | PASS |
| User asks for an English public README update | Keep the target artifact English-first | PASS |

Parent gate preservation:

- The `learning-capture` parent gate is preserved for learning, reference,
  reuse, and adaptation requests.
- Article-specific references preserve source grounding, score-first triage,
  copyright boundaries, rejected moves, and promotion boundaries without
  publishing a second runtime skill.
- Repo governance remains the parent gate for promotion into behavior assets.

## Behavior Replay

| Field | Evidence |
|---|---|
| Input or situation shape | Chinese article or WeChat post learning request, including requests to learn, reuse, reference, or adapt the material. |
| Trigger condition | User wants learning, reference, reuse, or adaptation material rather than only raw article extraction or a short summary. |
| Expected route | Load `learning-capture`, classify the evidence object, then use the article reference module for article-specific handling. |
| Expected non-route | No active `article-learning-capture` skill surface; do not load a standalone retired article skill. |
| Repo-visible artifact | `.codex/skills/learning-capture/SKILL.md`, `.codex/skills/learning-capture/references/article.md`, `.codex/skills/learning-capture/references/article-wiki-template.md`, and this OpenSpec evaluation. |
| Expected output | Durable internal wiki notes default to Chinese unless the target artifact, user request, or audience requires English. |
| Promotion or non-promotion boundary | Article takeaways remain candidate learning unless evidence and the relevant OpenSpec or behavior-asset gate support promotion. |
| Proof boundary | Static behavior-asset checks and routing scans prove the current repository surface; they are not a live future runtime dispatch guarantee. |

## Historical Replay Evidence

This section closes the verification gap raised after the first pass: pressure
scenarios and static scans are not enough proof that a real historical article
learning case still routes and produces the expected durable artifact shape.

Historical case selected:

| Field | Evidence |
|---|---|
| Historical input | `wiki/ops/agent-harness-article-learning-intake.md`, created from a real 2026-05-06 request to deep-read agent / harness / eval / managed-agents articles. |
| Historical output | `wiki/ops/agent-harness-article-learning.md`, a real produced reading-notes artifact with 10 source URLs, scoring, source grounding, reading notes, transferable learning, rejected moves, and next action. |
| Replay reason | It is the strongest existing article-learning case because it was produced by the old article-learning flow and contains the exact behavior this change intends to preserve while retiring the separate skill surface. |
| Replay method | Manual route replay against current `learning-capture` and article module wording, then output-shape comparison against the current article wiki template. No new wiki page was generated and no historical output was rewritten for the replay. |

Replay route:

| Step | Historical fact | Current expected behavior | Result |
|---|---|---|---|
| Intent classification | Intake says the user asked for article deep reading, reusable learning, and wiki capture rather than a raw summary. | Load `learning-capture` because the source is learning / reference material. | PASS |
| Evidence object | Intake and output are article / blog / WeChat source collections. | Route to `references/article.md`. | PASS |
| Runtime boundary | The old page previously contained stale article-skill wording; the active page now records `learning-capture -> article reference module`. | Do not load or expose a standalone `article-learning-capture` skill. | PASS |
| Output language | Historical artifact frontmatter says `language: zh-CN` and the body is Chinese. | Durable internal wiki learning notes default to Chinese. | PASS |
| Output target | Historical artifact is a `wiki/ops` reading-notes page. | Article learning may produce durable internal wiki notes in `wiki/ops` when there is reusable operating learning. | PASS |

Output-shape consistency:

| Template / module requirement | Historical output evidence | Result |
|---|---|---|
| `title: <canonical-object> / reading-notes` | `title: agent-harness-article-learning / reading-notes` | PASS |
| `artifact_type: reading-notes` | `artifact_type: reading-notes` | PASS |
| `language: zh-CN` | `language: zh-CN` | PASS |
| `ops_area: learning-capture` | `ops_area: learning-capture` | PASS |
| `derived_from` preserves original URLs | Historical output records 10 URLs from OpenAI, Claude, Anthropic, and WeChat sources. | PASS |
| `notes_scope` preserves learning boundary | Historical output says it records route, source grounding, admission gate, scoring, structured paraphrase, transferable learning, and promotion boundary; it does not directly create `AGENTS.md`, skill, spec, checklist, or repo policy. | PASS |
| Source / original evidence | `Original Source Grounding` records source class, source artifact, and grounding status. | PASS |
| Admission / scoring before deep reading | `Admission Gate`, `Scoring Summary`, and `Score Detail Matrix` appear before per-article reading notes. | PASS |
| Reading draft | Each article section includes `Reading Draft`. | PASS |
| Transferable learning | Each article section includes `Transferable Learning`, followed by cross-article accepted / candidate learning sections. | PASS |
| Rejected moves | `Rejected Moves` exists and keeps non-promoted takeaways out of policy. | PASS |
| Next step | `Next Action` exists. It is an acceptable historical naming variant of the current template's `下一步` section. | PASS with naming variance |

Replay command evidence:

```text
rg -n '^(title|artifact_type|language|ops_area|notes_scope|derived_from|related_objects):|^- https?://|^# |^## |^### ' wiki/ops/agent-harness-article-learning.md
```

Observed evidence included:

- `title: agent-harness-article-learning / reading-notes`
- `artifact_type: reading-notes`
- `language: zh-CN`
- `ops_area: learning-capture`
- `Learning Capture Route`
- `Admission Gate`
- `Original Source Grounding`
- `Scoring Summary`
- `Score Detail Matrix`
- per-article `Source`, `Reading Draft`, and `Transferable Learning`
- `Rejected Moves`
- `Next Action`

Current template / module command evidence:

```text
rg -n '^(# |## |### |title:|artifact_type:|language:|ops_area:|notes_scope:|derived_from:|related_objects:)' .codex/skills/learning-capture/references/article-wiki-template.md .codex/skills/learning-capture/references/article.md .codex/skills/learning-capture/SKILL.md
```

Observed evidence included the current `learning-capture` module map, article
module runtime boundary, `language: zh-CN`, `ops_area: learning-capture`,
Chinese reading-note headings, and Chinese `可迁移学习` / `拒绝动作` / `下一步`
template sections.

Result: PASS for historical replay and output-shape consistency. The replay
proves the preserved article-learning behavior against one real prior artifact,
not a live future-dispatch guarantee for every agent session.

## Residual Risks

- Historical wiki and archived OpenSpec references still mention
  `article-learning-capture`; those are retained as history rather than active
  runtime surfaces.
- `readme-learning-capture` remains an adjacent active skill and may appear in
  broad `learning-capture` path scans; that is outside the article surface
  retirement scope.
- Future runtime behavior still depends on agents following the repo skill
  routing table and loading `learning-capture` for learning intent.

## Final Verification

| Check | Command | Result |
|---|---|---|
| Behavior asset checker | `python3 scripts/check_behavior_assets.py` | PASS. Initial run before final evidence failed on this change's missing `## Pressure Scenarios`, `## Residual Risks`, prior-art marker labels, parent-gate evidence, and replay fields. After adding the evidence above, the command exited 0 with no output. |
| Wiki frontmatter checker | `python3 scripts/check_wiki_frontmatter.py` | PASS. Command exited 0 with no output. A later routing-text correction removed the stale `article-learning-capture` relation from `wiki/ops/learning-capture-routing.md` frontmatter after `python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/learning-capture-routing.md` passed with `blocking_count: 0`. |
| OpenSpec validation | `openspec validate retire-article-learning-skill-surface --strict` | PASS. Output included `Change 'retire-article-learning-skill-surface' is valid`. PostHog telemetry flush then reported `getaddrinfo EAI_AGAIN edge.openspec.dev`; this occurred after validation and is non-blocking. |
| Retired surface routing scan | `rg -n 'article-learning-capture' .codex/skills AGENTS.md PROJECT.md openspec/specs openspec/changes/retire-article-learning-skill-surface wiki/adr wiki/ops` | PASS after stale active wiki routing text was corrected in `wiki/ops/agent-harness-article-learning.md`, `wiki/ops/agent-harness-article-learning-intake.md`, and `wiki/ops/learning-capture-routing.md`. Remaining hits are accepted spec references in `AGENTS.md`, current OpenSpec evidence, active negative-boundary references such as `.codex/skills/learning-capture/references/article.md:10`, pressure scenarios, exploratory/historical wiki ops notes, and generated doctor output. It did not report an active `.codex/skills/article-learning-capture/SKILL.md` file or active wiki text that routes through a standalone article skill. |
| Active description scan | `rg -n '^description:.*(article\|WeChat\|deep reading\|learning extraction)' .codex/skills/*/SKILL.md` | PASS. Actual output was `.codex/skills/learning-capture/SKILL.md:3:description: Use when the user provides articles, repo/README links, or examples as learning, reference, or adaptation material, including bare links whose purpose is implied by recent context.` and `.codex/skills/weixin-reader/SKILL.md:3:description: Use when the user provides an mp.weixin.qq.com article link and wants to read, analyze, summarize, or extract the article content`. No retired article-learning skill description appeared. |
| Article wiki template scan | `rg -n 'language: zh-CN\|# <主题> / 阅读笔记\|## 来源\|## 阅读草稿\|## 可迁移学习' .codex/skills/learning-capture/references/article-wiki-template.md` | PASS. Actual output: `12:language: zh-CN`, `32:# <主题> / 阅读笔记`, `34:## 来源`, `42:## 阅读草稿`, and `56:## 可迁移学习`. |
| Active skill surface scan | `find .codex/skills -maxdepth 2 -name SKILL.md \| sort \| rg 'article-learning-capture\|learning-capture'` | PASS. Actual output: `.codex/skills/learning-capture/SKILL.md` and `.codex/skills/readme-learning-capture/SKILL.md`. The retired `.codex/skills/article-learning-capture/SKILL.md` surface is absent; the README learning surface is adjacent and out of scope. |

## Wiki Routing Text Correction

Final routing scan review found that an active wiki learning page still
described the pre-retirement route as
`learning-capture -> article module -> article-learning-capture skill`. The
runtime skill surface had already been removed, but the active wiki text still
looked like current route guidance.

Correction applied:

| File | Correction |
|---|---|
| `wiki/ops/agent-harness-article-learning.md` | Replaced the stale delegate-skill route with `learning-capture` article reference module wording. |
| `wiki/ops/agent-harness-article-learning-intake.md` | Replaced the retired `.codex/skills/article-learning-capture/` next-step guidance with `learning-capture/references/article*.md`. |
| `wiki/ops/learning-capture-routing.md` | Removed `article-learning-capture` from active `related_objects` and updated the current judgment to say article learning retired to an internal `learning-capture` reference module. |

Frontmatter gate evidence for the `learning-capture-routing` frontmatter edit:

```json
{
  "command": "python3 scripts/wiki_gate_precheck.py --mode frontmatter --target wiki/ops/learning-capture-routing.md",
  "passed": true,
  "blocking_count": 0,
  "score": 75,
  "warnings": "5 possible_unregistered_producer warnings unrelated to the target page"
}
```

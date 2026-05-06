## Evaluation

### Baseline Scenarios

1. User asks to learn from multiple agent / harness articles and make the
   learning durable.
2. User provides a WeChat article as a structure example and expects the learning
   process to respect the original source.
3. User asks whether article learning should become a skill.
4. User wants low-value articles to be skipped instead of deep-read by default.

### Before Results

- Article learning was first recorded inside OpenSpec evaluation and tasks,
  which did not satisfy wiki learning capture.
- A later correction placed a long evidence table under
  `behavior-asset-governance-zh.md`, incorrectly treating article learning as a
  governance-framework subtopic.
- The initial article-learning intake acted like a mini conclusion page instead
  of a directory.
- The claim/evidence table appeared before a complete learning method and did
  not require a score before deep reading.
- No skill trigger existed for general external article learning; only narrower
  README and WeChat-reference skills existed.

### Pressure Scenarios

| Scenario | Expected behavior |
|---|---|
| User provides a technical blog and says "精读、落 wiki、学到能力" | Load article-learning skill, score first, then deep-read only if threshold passes |
| User provides an `mp.weixin.qq.com` link as a writing/method reference | Use article-learning flow and call `weixin-reader` for body extraction when needed |
| User provides a GitHub README | Prefer `readme-learning-capture`, not the general article skill |
| User asks for a news summary with no local reuse intent | Do not trigger article-learning capture |
| User asks to turn a takeaway into a hard rule | Require evidence-backed promotion or a scoped OpenSpec change |

### RED Baseline

Without this skill:

- The agent can summarize article claims but may skip source-first reading.
- It may confuse learning with governance, especially when the article topic
  overlaps with a current change.
- It may extract a claim table without preserving translation notes, source
  metadata, or scoring.
- It may spend time deep-reading low-quality or low-relevance articles.

### GREEN Result

After this change:

- `.codex/skills/article-learning-capture/SKILL.md` exists and triggers on
  external article deep-reading and wiki learning requests.
- The skill points to a scorecard, SOP, wiki template, and pressure scenarios.
- The SOP requires source metadata, score-first triage, structured translation
  notes, extracted transferable learning, and promotion boundaries.
- The current agent-harness article-learning intake is aligned as a directory
  and method entry.

### Residual Risks

- This change defines process and templates; it does not reprocess all existing
  agent-harness article notes into the new template.
- `mp.weixin.qq.com` access may fail due to anti-bot or environment limits. In
  that case, the workflow requires pasted text or screenshots rather than
  inventing article content.
- The scorecard is a human-auditable rubric, not an automated quality classifier.

### Gate Repair Review (2026-05-06)

#### Skills Loaded

The repair pass loaded `skill-creator`, `writing-skills`,
`test-driven-development`, and `simplicity-first` before changing the published
skill.

#### Simplicity Gate

Repair path chosen: repair the existing skill only. No new skill, new page type,
new automation, new scoring tool, or new OpenSpec change was added. The fix is
limited to source grounding, source classification, scorecard calibration,
trigger validation evidence, and archive-review closure.

#### RED Baseline Commands

These commands were run against the pre-repair text and all exited `1` with no
matches:

```bash
rg -n 'source snapshot|extracted markdown|source map|bounded excerpt' .codex/skills/article-learning-capture openspec/changes/formalize-article-learning-capture/evaluation.md
rg -n 'primary source|secondary interpretation|structure reference|source class|source classification' .codex/skills/article-learning-capture/references/scorecard.md .codex/skills/article-learning-capture/references/sop.md
rg -n 'Trigger Validation Results|should-trigger.*PASS|should-not-trigger.*PASS|Simplicity Gate' openspec/changes/formalize-article-learning-capture/evaluation.md openspec/changes/formalize-article-learning-capture/archive-review.md
rg -n 'skill-creator|writing-skills|test-driven-development|simplicity-first' openspec/changes/formalize-article-learning-capture/evaluation.md .codex/skills/article-learning-capture
```

Baseline failure proven:

- no source snapshot / extracted markdown / source map / bounded excerpt gate
- no primary / secondary / structure-reference source classification
- no trigger-validation result record or simplicity gate
- no recorded skill-creator / writing-skills / TDD / simplicity-first gate

#### Discovery

Real trigger phrases from the live conversation: `精读`, `学到能力`, `落 wiki`,
`SOP`, `评分`, `原文链接`, `翻译稿`, article collections, and local transfer into
repo behavior. Adjacent non-trigger cases: plain news summary, GitHub README
reuse, raw WeChat extraction, short abstract request, and skill editing with no
article-learning input.

#### Trigger Validation Results

| Case | Expected | Result |
|---|---|---|
| should-trigger: technical blog + "精读，学到能力，落 wiki" | load article-learning-capture | PASS |
| should-trigger: multiple agent engineering articles + local usefulness | load article-learning-capture | PASS |
| should-trigger: ask whether an article is worth deep reading | load article-learning-capture and score first | PASS |
| should-trigger: WeChat article as method reference | load article-learning-capture plus WeChat-specific reader/reference skill when needed | PASS |
| should-trigger: turn article learning into SOP | load article-learning-capture | PASS |
| should-not-trigger: latest news with no local reuse intent | normal answer / browse as needed | PASS |
| should-not-trigger: GitHub README reuse | prefer readme-learning-capture | PASS |
| should-not-trigger: raw WeChat text extraction only | prefer weixin-reader | PASS |

#### GREEN Result Commands

After the repair, the same checks produce matches:

- source grounding: `SKILL.md` requires extracted markdown, source map, bounded
  excerpts, or retrieval-failure note; `sop.md`, `scorecard.md`, and
  `wiki-template.md` repeat the gate.
- source classification: `sop.md` and `scorecard.md` distinguish primary source,
  secondary interpretation, structure reference, and low-relevance material.
- trigger validation: this section records should-trigger and should-not-trigger
  `PASS` results.
- authoring gates: this section records `skill-creator`, `writing-skills`,
  `test-driven-development`, and `simplicity-first`.

#### Residual Risks

- Trigger validation is manual/static. It validates the skill text against
  pressure scenarios, not automatic runtime dispatch.
- The existing agent-harness article notes were not fully reprocessed into
  source snapshots in this repair pass.
- No sub-agent validation was run because the user did not explicitly request
  delegated parallel review in this turn.

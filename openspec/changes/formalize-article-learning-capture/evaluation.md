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

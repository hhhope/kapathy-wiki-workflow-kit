## 1. Change Setup

- [x] 1.1 Create OpenSpec artifacts for article learning capture.
- [x] 1.2 Add an article-learning capability delta.

## 2. Skill Publication

- [x] 2.1 Add `.codex/skills/article-learning-capture/SKILL.md`.
- [x] 2.2 Keep the skill body compact and move heavy SOP material to
  `references/`.
- [x] 2.3 Preserve explicit routing to `weixin-reader`,
  `weixin-reference-wiki-capture`, and `readme-learning-capture`.

## 3. SOP And Templates

- [x] 3.1 Add the article-learning SOP reference.
- [x] 3.2 Add a rigorous scoring reference with thresholds and hard caps.
- [x] 3.3 Add a wiki output template with source metadata, structured
  translation notes, extraction, scoring, and promotion boundary sections.
- [x] 3.4 Add pressure scenarios for trigger and non-trigger behavior.

## 4. Current Wiki Alignment

- [x] 4.1 Keep the agent-harness article-learning intake as a directory and
  method entry.
- [x] 4.2 Preserve existing reading notes as learning output without promoting
  them into governance rules.

## 5. Evaluation And Validation

- [x] 5.1 Record RED/GREEN behavior-proof evidence in `evaluation.md`.
- [x] 5.2 Run `openspec validate formalize-article-learning-capture --strict`.
- [x] 5.3 Run `git diff --check` for touched files.

## 6. Archive Review

- [x] 6.1 Run archive review after the change reached complete.
- [ ] 6.2 Resolve archive-review blocker: skill was published without
  `skill-creator`, `writing-skills` / TDD, and `simplicity-first` gates.
- [ ] 6.3 Choose and record the repair path: repair skill, downgrade to wiki SOP,
  or replace with a smaller route.
- [ ] 6.4 Re-run validation after the blocker is resolved.

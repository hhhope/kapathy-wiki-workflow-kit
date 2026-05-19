## 1. OpenSpec Baseline

- [ ] 1.1 Record RED baseline for active article skill description pollution.
- [ ] 1.2 Record RED baseline for English article wiki template body prompts.
- [ ] 1.3 Record prior-art and common-rule ownership scan.

## 2. Skill Surface Retirement

- [ ] 2.1 Add Chinese-first durable learning output rule to `learning-capture`.
- [ ] 2.2 Migrate useful article-specific rules into `learning-capture`
  references.
- [ ] 2.3 Remove the active `article-learning-capture` skill surface.
- [ ] 2.4 Remove or rewrite references that imply `article-learning-capture`
  remains a runtime entry.

## 3. Evidence and Verification

- [ ] 3.1 Add pressure scenarios for article, WeChat, README/repo, example, and
  English-target learning requests.
- [ ] 3.2 Add behavior replay evidence for future routing.
- [ ] 3.3 Run `openspec validate retire-article-learning-skill-surface --strict`.
- [ ] 3.4 Run `python3 scripts/check_behavior_assets.py` and preserve output.
- [ ] 3.5 Run `python3 scripts/check_wiki_frontmatter.py` if template or
  frontmatter changes require it.
- [ ] 3.6 Commit only task-related files.

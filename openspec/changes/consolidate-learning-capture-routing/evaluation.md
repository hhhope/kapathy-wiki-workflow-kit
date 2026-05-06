## Evaluation

### Baseline Scenarios

1. User provides a technical article and asks to `精读`, learn capability, and
   write to wiki.
2. User provides a GitHub repository and asks whether its skill organization can
   be reused.
3. User provides a WeChat article and only asks to fetch the raw body text.
4. User provides a technical article that references a GitHub repo, then asks
   whether the repo structure can be reused.
5. User asks for an article news summary with no local reuse intent.

### RED Baseline

Before this change, these checks showed the missing domain router:

```bash
rg -n '^name: learning-capture$|learning-capture/SKILL.md|general learning routing is owned by `learning-capture`|repo-readme module|example-reference module' .codex/skills openspec/changes wiki/ops
rg -n 'Intent Routing|Source Kind|Learning Intent|Module Route|learning-capture-routing' .codex/skills openspec/changes wiki/ops
```

Observed result:

- no `learning-capture` skill existed
- no domain-level intent routing table existed
- article and README learning depended on separate skill discovery
- no explicit example-reference learning route existed

### Skill Authoring Gates

This implementation loaded `skill-creator`, `writing-skills`,
`test-driven-development`, and `simplicity-first` before authoring the skill.

The simplicity decision is to add one thin domain router and keep existing
material-specific skills as compatibility entry points. No dispatcher code,
automation, deletion, or bulk wiki rewrite is part of this change.

### Pressure Scenarios

| Scenario | Expected | Result |
|---|---|---|
| Article + "精读，学到能力，落 wiki" | `learning-capture` -> article module | PASS |
| GitHub repo + "这个方案能不能复用" | `learning-capture` -> repo-readme module | PASS |
| WeChat article + "只抓正文" | skip learning capture; use `weixin-reader` | PASS |
| GitHub README + "学习结构，改造成我们的 SOP" | `learning-capture` -> repo-readme module | PASS |
| Article about a repo, without direct repo reading | article module; source class is secondary interpretation | PASS |
| Article about a repo, user asks whether repo structure can be reused | article module, then repo-readme module after reading repo/README | PASS |
| News summary or fact lookup with no local reuse intent | skip learning capture | PASS |
| Concrete output-shape example with reuse intent | `learning-capture` -> example-reference module | PASS |

### GREEN Result

After this change:

- `.codex/skills/learning-capture/SKILL.md` exists and owns learning intent
  routing.
- `references/routing.md` defines learning intent, non-learning intent, source
  kind, and module route.
- `article-learning-capture` and `readme-learning-capture` remain available but
  point back to `learning-capture` for general routing.
- `pressure-scenarios.md` records at least five should-trigger and three
  should-not-trigger / narrower-route cases.

### Residual Risks

- Validation is static/manual. It verifies the behavior contract and trigger
  wording, not automatic runtime dispatch.
- Existing article and README learning pages are not migrated in this change.
- Old skills remain visible as compatibility entry points, so future cleanup may
  be useful only after repeated successful use of the domain router.

## Evaluation

### Behavior Expected To Change

- Before this change, example-driven learning could stop at chat summary unless the user explicitly reminded the agent to write wiki.
- After this change, when reusable learning is already extracted from an external example or in-chat example, the agent should create a repo-visible record in the same turn by default.

### Baseline Scenario

Scenario:

- user provides external repos or README examples
- discussion extracts what was reused, what changed, and what remains missing
- no extra instruction says `write this to wiki`

Before result:

- the discussion can end with a useful chat answer
- but repo-visible capture is still optional and easy to miss
- the user may need to prompt again

### After-Change Scenario

Same scenario:

- user provides external repos or README examples
- discussion extracts what was reused, what changed, and what remains missing
- no extra instruction says `write this to wiki`

After result:

- repo guidance now requires wiki capture in the same turn when the takeaway is already clear
- `wiki/ops/gstack-lark-learning-retro-2026-04-18.md` acts as a concrete example of the new default

### Residual Risks

- The trigger still depends on whether the takeaway is genuinely extracted; weak source summaries should not generate low-signal pages.
- Later changes may still be needed to formalize which learnings should become templates, skills, or team-lore candidates.

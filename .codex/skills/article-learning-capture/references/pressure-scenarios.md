# Article Learning Capture Pressure Scenarios

Use these scenarios when validating the skill.

## Should Trigger

| Scenario | Expected |
|---|---|
| User provides a technical blog and says "精读，学到能力，落 wiki" | Trigger article-learning-capture |
| User provides multiple agent engineering articles and asks what is useful to the local system | Trigger article-learning-capture |
| User asks whether an article is worth deep reading | Trigger article-learning-capture and score first |
| User provides a WeChat article as method reference and asks to learn the structure | Trigger article-learning-capture; use `weixin-reader` or `weixin-reference-wiki-capture` as needed |
| User asks to turn article learning into SOP | Trigger article-learning-capture |

## Should Not Trigger

| Scenario | Expected |
|---|---|
| User asks for the latest news from an article with no local reuse intent | Do not trigger; answer normally |
| User provides a GitHub README and asks what to reuse | Prefer `readme-learning-capture` |
| User asks to fetch raw WeChat text only | Prefer `weixin-reader` |
| User asks for a short abstract with no wiki or adaptation intent | Do not trigger |
| User asks to edit an existing skill without article-learning input | Prefer skill authoring workflow |

## Baseline Failure Patterns

- Summarizes the article but does not write a wiki record.
- Writes a claim table without a source-first reading draft.
- Treats a famous article as automatically worth deep reading.
- Copies article advice directly into `AGENTS.md` or `SKILL.md`.
- Hides uncertainty by marking unsupported takeaways as accepted.

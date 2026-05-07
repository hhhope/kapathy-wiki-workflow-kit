# Article Learning Capture Pressure Scenarios

Use these scenarios when validating the skill.

## Should Trigger

| Scenario | Expected | Result |
|---|---|---|
| User provides a technical blog and says "精读，学到能力，落 wiki" | Trigger article-learning-capture | PASS |
| User provides multiple agent engineering articles and asks what is useful to the local system | Trigger article-learning-capture | PASS |
| User asks whether an article is worth deep reading | Trigger article-learning-capture and score first | PASS |
| User provides many article links in one batch | Triage and score first; deep-read only 75+ sources by default | PASS |
| User provides a WeChat article as method reference and asks to learn the structure | Trigger article-learning-capture; use `weixin-reader` or `weixin-reference-wiki-capture` as needed | PASS |
| User asks to turn article learning into SOP | Trigger article-learning-capture | PASS |

## Should Not Trigger

| Scenario | Expected | Result |
|---|---|---|
| User asks for the latest news from an article with no local reuse intent | Do not trigger; answer normally | PASS |
| User provides a GitHub README and asks what to reuse | Prefer `readme-learning-capture` | PASS |
| User asks to fetch raw WeChat text only | Prefer `weixin-reader` | PASS |
| User asks for a short abstract with no wiki or adaptation intent | Do not trigger | PASS |
| User asks to edit an existing skill without article-learning input | Prefer skill authoring workflow | PASS |

## Baseline Failure Patterns

- Summarizes the article but does not write a wiki record.
- Writes a claim table without a source-first reading draft.
- Treats a famous article as automatically worth deep reading.
- Backfills a score after reading and presents it as score-first evidence.
- Copies article advice directly into `AGENTS.md` or `SKILL.md`.
- Hides uncertainty by marking unsupported takeaways as accepted.

## Gate Validation Notes

- `skill-creator` discovery keeps real trigger phrases: `精读`, `学到能力`,
  `落 wiki`, `SOP`, `评分`, article collections, and local transfer.
- Should-not-trigger cases are routed to narrower skills or normal answering.
- Validation is static/manual in this change; it proves trigger wording against
  pressure scenarios, not automatic runtime dispatch.

# Evaluation

## Pressure Scenarios

| Scenario | Expected Result |
| --- | --- |
| A requirements case has a Human Review document that adds scenario gaps but does not update user stories. | `req-human-review` treats story/acceptance additions as demand facts and requires machine case synchronization before handoff. |
| A user asks for a readable requirements review after acceptance extraction. | `req-agent` routes to `req-human-review`, not directly to `req-handoff` and not to a standalone normal entry skill. |
| Human Review includes a question that is only a reviewer prompt. | The prompt remains classified as `review_prompt` and does not modify machine case facts. |
| Human Review identifies missing current-state material, business rule table, or system boundary contract. | The missing input is classified as `design_gate_gap`; detailed design remains blocked while requirement review may still be ready. |

## RED Baseline

The Baofu legal SMS case showed the old behavior failure:

- Human Review scenario matrices were added first.
- New boundary facts appeared in the human-readable document.
- User stories and acceptance mappings were not updated until the user asked,
  "用户故事没增加？"

This is a valid RED baseline because the existing route lacked a bounded
Human Review worker, fixed template, and synchronization gate.

## GREEN Result

After this change, the expected route is:

- `req-agent` keeps normal entry control.
- `req-human-review` produces the Human Review artifact from the machine case
  and source evidence.
- Demand facts in the review must be synchronized into the machine case before
  `req-handoff`.
- The Human Review template includes user stories, scenario coverage,
  acceptance scope, gap classification, detailed-design gates, and
  synchronization proof.

## Prior-Art / Common-Rule Dedupe

- `req-agent` already owns normal entry and routing; this change does not create
  a new normal entry point.
- Existing worker skills own bounded phases; `req-human-review` follows that
  pattern.
- Existing detailed-design hard gates stay in `req-agent` and the checker; this
  change only restates them as Human Review output fields.
- Skill authoring, pressure-test, and behavior-asset evaluation requirements
  remain governed by repo `AGENTS.md` and OpenSpec specs; this change does not
  duplicate those generic rules inside the skill body.

## Residual Risks

- First release relies on manual synchronization proof, not full automatic
  parsing of Human Review documents.
- Existing Human Review documents may need manual normalization if used as
  future examples.
- `req-human-review` can still be misused if invoked directly without explicit
  worker/debug context; the skill description follows the existing worker
  non-entry pattern to reduce that risk.

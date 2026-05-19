# Evaluation: medical-agent status prediagnosis

## Pressure Scenarios

1. User says `那我继续做什么` while the case is `archive_ready`.
2. User says `改 wiki/moc` and the script returns status.
3. User replies only `1` after options were presented.
4. User asks why no prediagnosis was given.

## Positive Trigger Scenario

- Input or situation shape: user invokes `wiki-medical-agent` and uses
  continuation or mutation language rather than a pure status question.
- Trigger condition: the medical-agent script result is `report_status`,
  `blocked`, `awaiting_confirmation`, or `archive_ready`.
- Expected route: keep the fixed fields, then add read-only prediagnosis and a
  recommended next action.
- Repo-visible artifact: `.codex/skills/wiki-medical-agent/SKILL.md` plus this
  evaluation record.
- Expected output: script result, interpreted live user intent, read-only
  prediagnosis, recommended next action, and any remaining user decision.
- Promotion or non-promotion boundary: the rule is promoted only into the
  repo-local medical-agent skill, not into global AGENTS or a common rule.
- Proof boundary: this is skill-level replay evidence, not proof that clients
  will comply without loading the skill.

## Negative Should-Not-Trigger Scenario

- Input or situation shape: user asks only for current medical-loop status.
- Trigger condition: no continuation, mutation, apply, repair, or next-step
  request is present.
- Expected route: report the fixed `wiki-medical-agent` fields without adding a
  speculative prediagnosis.
- Expected output: Intent, Case, State, Allowed action, Blocked action when
  blocked, and Next Action.

## RED Baseline

- `.codex/skills/wiki-medical-agent/SKILL.md` has no
  `Status / Blocked Response` rule.
- Baseline wording check:
  `rg -n "Status / Blocked Response|read-only prediagnosis|interpreted live user intent" .codex/skills/wiki-medical-agent/SKILL.md`
- Baseline wording result: exited 1 with no matches.
- The skill requires fixed fields but does not require interpreted live intent,
  read-only prediagnosis, or a recommended next action when status is not enough.
- Baseline command:
  `python3 scripts/build_wiki_medical_agent.py --intent-text "改 wiki/moc"`
- Baseline result:

```json
{
  "intent": "status",
  "case_path": "/mnt/d/cloud/account-meeting-lore/wiki/ops/wiki-medical-cases/2026-05-15-064427-wiki-medical-case.md",
  "state": "archive_ready",
  "allowed": true,
  "allowed_action": "report_status",
  "blocked_reason": "",
  "next_action": "archive_ready",
  "executable_count": 10,
  "expected_count": null
}
```

- Baseline interpretation: this is a non-executing status-style output; the
  skill does not require the agent to bridge from that status to a read-only
  prediagnosis.

## GREEN Result

The updated skill now includes a compact `Status / Blocked Response` section.

GREEN wording check:

```bash
rg -n "Status / Blocked Response|read-only prediagnosis|interpreted live user intent" .codex/skills/wiki-medical-agent/SKILL.md
```

Expected result: matches the new section.

Replay expectations:

- `那我继续做什么`: report script status, interpret the live intent as next-route
  selection, and recommend archive review or another bounded next workflow.
- `改 wiki/moc`: report script status, preserve generated-output write
  boundaries, provide a read-only prediagnosis, and recommend the safe next
  route before asking for missing details.
- Bare `1`: preserve prior option context and continue that option without
  forcing the user to restate the full target.
- `为什么没有预判断`: identify that fixed-field status was treated too
  mechanically and state what prediagnosis should have happened.

## Behavior Replay

- Input or situation shape: user invokes `wiki-medical-agent` and uses continuation or
  mutation language rather than a pure status question.
- Trigger condition: the medical-agent script result is `report_status`,
  `blocked`, `awaiting_confirmation`, or `archive_ready`.
- Expected route: keep the existing fixed fields, then add read-only
  prediagnosis and a recommended next action.
- Repo-visible artifact: `.codex/skills/wiki-medical-agent/SKILL.md` plus this
  evaluation record.
- Expected output: script result, interpreted live user intent, read-only
  prediagnosis, recommended next action, and any remaining user decision.
- Promotion or non-promotion boundary: this does not grant write authority and
  does not change `scripts/build_wiki_medical_agent.py`.
- Proof boundary: this replay validates the behavior contract wording only.

## Prior-Art / Common-Rule Dedupe

- Scanned: repo `AGENTS.md`, `PROJECT.md`,
  `.codex/skills/wiki-medical-agent/SKILL.md`,
  `.codex/skills/clarify-before-acting/SKILL.md`,
  `openspec/changes/introduce-wiki-medical-agent-state-machine`, and
  `docs/superpowers/specs/2026-05-19-wiki-medical-agent-status-prediagnosis-design.md`.
- Owns: `wiki-medical-agent` status/blocked response behavior for the wiki
  medical-loop entry point.
- References: `clarify-before-acting` already says to resolve local context
  before asking the user; this change narrows that principle to medical-agent
  status and blocked responses.
- Rejects: global agent rules, AGENTS.md rewrites, script classifier changes,
  and direct write authority expansion.

## Residual Risks

- This is skill-level behavior evidence, not proof that clients will comply
  without loading the skill.
- No script intent classifier was changed; unusual phrasing may still return
  `status`, but the skill now defines how the agent should respond to that.
- `openspec validate add-medical-agent-status-prediagnosis --strict`: PASS,
  reported `Change 'add-medical-agent-status-prediagnosis' is valid`.
- `python3 scripts/check_behavior_assets.py`: PASS on fresh archive review
  recheck, exited 0 with no output.

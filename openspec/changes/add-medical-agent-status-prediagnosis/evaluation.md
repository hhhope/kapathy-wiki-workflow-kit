# Evaluation: medical-agent status prediagnosis

## Pressure Scenarios

1. User says `那我继续做什么` while the case is `archive_ready`.
2. User says `改 wiki/moc` and the script returns status.
3. User replies only `1` after options were presented.
4. User asks why no prediagnosis was given.

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

Not recorded in this RED baseline commit. Task 4 replaces this section after
the skill wording is updated and replay expectations are checked.

## Residual Risks

- This RED baseline only proves the current skill lacks a response obligation.
- It does not prove the future wording is sufficient until Task 4 records the
  GREEN replay result.

<!-- req-agent-routing:start -->
## Requirements Agent Routing

For requirements intent recognition, intake, clarification, DDD domain
classification, coverage checks, user stories, acceptance functions, readiness
checks, or OpenSpec draft handoff, use `req-agent` as the normal Codex-facing
entry.

Normal entry:

```text
$req-agent <requirement material or question>
```

`req-agent` owns:

- intent recognition
- case resolution or creation
- state reporting
- allowed action
- blocked action
- next action
- evidence

Do not ask users to run Python as the normal path. Do not directly route
ordinary users to `req-intake`, `req-domain-analysis`, `req-scope`,
`req-stories`, `req-acceptance`, or `req-handoff`; those are bounded worker
skills used by `req-agent`.

`req-handoff` may create an OpenSpec draft only after requirement readiness
passes. Draft creation does not approve implementation. Detailed design,
API/DDL/schema/state-machine work, and implementation design remain blocked
until detailed-design hard gates pass or are explicitly waived with evidence.

If this repository has a skill routing table, add or preserve this route:

```md
| Requirements intent recognition, intake, domain analysis, scope, stories, acceptance, readiness gate, or OpenSpec draft handoff | `.codex/skills/req-agent/SKILL.md` | requirements workflow controller |
```
<!-- req-agent-routing:end -->

---
name: jira-integration
description: "Use after business-engineering alignment when extracting Jira requirements, acceptance criteria, test scenarios, or status-update comments. Trigger phrases: Jira ticket, issue summary, requirement review, business alignment, stakeholder alignment, write Jira update. Even if Jira is not named, trigger when a request asks to turn stakeholder notes into implementation-ready scope. Exclude generic product docs or non-Jira release notes that do not need ticket-to-implementation extraction."
---

# Jira Integration

Compact Jira starter card for turning a ticket into implementation inputs or a status-update comment. This is a lookup sheet, not a long execution manual. Localize status names, field expectations, and ticket workflow boundaries before wiring it into repository governance.

## Do Not

- Do not invent acceptance criteria or data ownership rules when the ticket is vague; surface open questions explicitly.
- Do not copy Jira credentials or webhook/token values into repository files or issue comments.
- Do not convert a ticket into implementation scope before reconciling `AGENTS.md`, active REQs, lore, and the current codebase.
- Do not post a status comment that claims verification without concrete checks.
- Do not treat this starter card as repository truth before replacing placeholder fields and workflow assumptions with local Jira conventions.

## Intent Routing

| Intent | Recommended Output | Required Fields |
|--------|--------------------|-----------------|
| Extract requirements from one ticket | Requirement summary block | ticket key, summary, status, stakeholders, scope, acceptance criteria, open questions |
| Convert ticket content into a REQ draft | `requirements/active/REQ-*.md` draft section | domain, scope, priority, acceptance criteria, exclusions, unresolved questions |
| Draft an engineering status comment | Jira comment template | branch, completed scope, verification, open risks/questions, MR link |
| Prepare for a business-engineering alignment meeting | Alignment notes | decision points, data ownership, permissions, timeline, unresolved dependencies |

## Localize Before Use

Before this skill becomes repository truth, replace placeholders with local decisions for:

- ticket types, status names, and workflow transitions
- required Jira fields, custom fields, and ownership terms
- whether implementation scope should map to REQ drafts, issue comments, or another local artifact
- comment templates that match your MR/PR naming and verification workflow
- credential boundary rules for Jira MCP, API tokens, or internal integration tools

## Requirement Extraction Template

```markdown
Ticket: [JIRA-KEY]
Summary: [title]
Status: [status]
Stakeholders: [business owner / engineering owner]

Requirements:
1. [functional requirement]
2. [boundary / permission / data definition]

Test Scenarios:
- Happy Path:
- Error Case:
- Edge Case:

Data/Integration:
- [data source / API / table / field]

Open Questions:
- [questions requiring stakeholder alignment]
```

## Jira Comment Template

```markdown
Engineering update:

- Branch: [branch-name]
- Scope done: [completed scope]
- Verification: [checks run]
- Open risks/questions: [pending confirmations]
- MR: [link]
```

## Error / Risk Index

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Ticket summary is too vague to implement | Acceptance criteria, permissions, or data ownership are missing | Add explicit open questions and request stakeholder alignment before coding |
| Jira content conflicts with repository rules | Ticket assumptions ignore `AGENTS.md`, active REQ, team scope, or existing architecture | Reconcile with project rules and document the delta before implementation |
| MR/status comment omits verification | Comment template was filled without test/log/API checks | Add exact verification evidence and known residual risks |
| Credentials appear in issue notes or local config | Jira access setup was copied into tracked files | Keep tokens outside the repository and produce comment drafts without embedding secrets |

## Boundaries

- If Jira MCP or API credentials are unavailable, do not place tokens in this repository; produce structured analysis and comment drafts only.
- Before using ticket content as implementation scope, re-check `AGENTS.md`, active REQs, lore, and the current codebase.
- If your environment uses a different issue tracker or customized Jira workflow, adapt the field names and output templates before reuse instead of forcing this card unchanged.

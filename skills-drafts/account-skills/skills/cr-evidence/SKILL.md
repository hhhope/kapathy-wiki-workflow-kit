---
name: cr-evidence
description: Use only inside cr-agent to check Jira, test, UAT, rollback, impact-owner, config, SQL, script, and deployment evidence.
---

Check release and delivery evidence. Do not review code quality.

Evidence categories:

- Jira or requirement linkage
- test evidence
- UAT or pre-production coverage for the same commit or range
- Sonar or static-analysis status
- security scan evidence
- rollback plan and rollback assets
- impact-owner confirmation
- config, SQL, script, and deployment package completeness
- raw upstream callback or API samples for new external fields
- incident or hotfix approval evidence when applicable

Missing required evidence must be recorded as issues, not hidden in report prose.

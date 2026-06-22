---
name: cr-diff
description: Use only inside cr-agent to produce deterministic CR diff evidence without business conclusions.
---

Build deterministic diff evidence. Reuse `release-diff-cr` when release or mainline comparison is needed.

When called under `cr-agent`, `release-diff-cr` reuse is evidence-only:

- use release-diff evidence or JSON data
- do not let `release-diff-cr` render final CR reports
- do not let `release-diff-cr` route review skills
- do not let `release-diff-cr` make gate or report decisions
- send all findings through `cr-issues`

Evidence:

- commit list
- merge commits and source branches
- first-parent non-merge commits
- changed files and file statuses
- authors and committers
- per-author changed scope
- numstat and large-diff hints
- file categories: code, config, SQL, test, docs, dependency, generated
- high-risk text or path hits for later scope routing

Do not make final gate decisions. Send findings to `cr-issues` through the caller.

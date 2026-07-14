# Account Asset Group Feishu Report Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a Feishu-ready 10—15 minute account asset group H2 report with one responsibility/support mind map, evidence-based priorities, three confirmed focus items, and a separate handover section.

**Architecture:** Build one reader-facing Markdown draft as the source for Feishu blocks, with the concise meeting body first and evidence appendices after it. Create a separate public-report gate review that maps the draft back to the approved design and records remaining evidence boundaries.

**Tech Stack:** Markdown, Feishu document blocks on later sync, PowerShell validation, repository wiki source material.

## Global Constraints

- Preserve the sequence: responsibilities/support → gaps and priorities → three focus items → handover.
- Use one ASCII tree only; do not add a separate XMind explanation section.
- Every table must include a priority, sequence, or stage column.
- Keep the spoken body within 10—15 minutes; move detailed evidence to appendices.
- Do not claim a true MTTR baseline from the current event log.
- Preserve the confirmed efficiency wording: H1 13.5, H2 stabilize at 15, strive for top 10.
- Keep billing/value-added development deferred, split/card package as handover-led, and insurance as an October exit with data archiving.
- Do not sync externally without a concrete Feishu target and explicit write approval.

---

### Task 1: Write the meeting body

**Files:**
- Create: `wiki/reports/account-asset-group-h2-feishu-draft-2026-07-14.md`
- Reference: `docs/superpowers/specs/2026-07-14-account-asset-group-feishu-report-design.md`
- Reference: `wiki/sources/account-asset-group-h2-handover-source-2026-07-14.md`

**Interfaces:**
- Consumes: approved narrative, responsibility map, priority rules, three focus items.
- Produces: complete meeting body through the handover conclusion.

- [ ] **Step 1: Create the reader-facing header and article intent**

Write the title, one callout paragraph, and four questions the report answers. Do not expose internal workflow notes or repo paths.

- [ ] **Step 2: Add the single responsibility/support ASCII tree**

Use only the status labels `已有`, `建设`, `交接`, `重点需求`, `暂缓`, and `退出`. Include Nirvana accounts, agency settlement, split handover, Haina billing/settlement/reconciliation, non-site inspection, and insurance exit.

- [ ] **Step 3: Add the priority table**

Each row contains priority, evidence or current state, H2 choice, and mapped focus item. No row exists only because the organization chart names a capability.

- [ ] **Step 4: Add the three focus items**

Use these exact top-level items: `产品规划与账户能力建设`, `重点业务交付与客户成功`, and `稳定性、研发效能与团队建设`. Every sub-item states current evidence, concrete action, and verifiable result.

- [ ] **Step 5: Add the separate handover section**

Cover Haina, split, card package, and insurance. State the Haina/Wenda responsibility boundary as a required RACI output rather than assuming it is resolved.

- [ ] **Step 6: Validate body structure**

Run:

```powershell
$p='wiki/reports/account-asset-group-h2-feishu-draft-2026-07-14.md'
Select-String -LiteralPath $p -Pattern '^## 1\.|^## 2\.|^## 3\.|^## 4\.|^## 5\.'
Select-String -LiteralPath $p -Pattern 'TBD|TODO|全面赋能|体系化升级'
```

Expected: ordered sections are present; placeholder/slogan search returns no matches.

### Task 2: Add evidence appendices

**Files:**
- Modify: `wiki/reports/account-asset-group-h2-feishu-draft-2026-07-14.md`
- Reference: `C:/Users/yan/.codex/attachments/392b7d95-6af3-4321-9d4a-64d716eca740/pasted-text.txt`
- Reference: `C:/Users/yan/Desktop/账户组应用和接口梳理.xlsx`
- Reference: `D:/工作资料/银户通/xmind/银企通开展业务现状.xmind`
- Reference: `wiki/reports/account-clearing-payment-settlement-2026-brief.md`

**Interfaces:**
- Consumes: source counts and evidence boundaries.
- Produces: appendices that support but do not interrupt the spoken body.

- [ ] **Step 1: Add the application/support appendix**

Record 89 applications, 14 reconciliation applications, 21 business reports, reserve/regulatory support, and the October insurance exit. Keep application names grouped by capability.

- [ ] **Step 2: Add the incident/SRE appendix**

Record the 95 structured events and confirmed category counts. State that 29 valid completed records yield a problem-closure-cycle median of 5 days and P75 of 10 days, not MTTR.

- [ ] **Step 3: Add the PMO metric appendix**

Keep 13.5 → 15 → top 10 as the confirmed result wording. List required PMO data sources for milestone achievement, Lead Time, blocked time, rework, and bank access efficiency; do not invent current values.

- [ ] **Step 4: Add the handover checklist appendix**

List applications, repositories, owners, permissions, tasks, interfaces, data, configuration, monitoring, runbooks, active problems, and acceptance evidence.

- [ ] **Step 5: Validate numeric evidence**

```powershell
$p='wiki/reports/account-asset-group-h2-feishu-draft-2026-07-14.md'
Select-String -LiteralPath $p -Pattern '95|47|20|34|29|5天|P75|13.5|15|前10'
Select-String -LiteralPath $p -Pattern 'MTTR为5天|MTTR 5天'
```

Expected: evidence values are present; false MTTR statements return no matches.

### Task 3: Create the public-report gate review

**Files:**
- Create: `wiki/ops/account-asset-group-h2-feishu-report-gate-review-2026-07-14.md`
- Review: `wiki/reports/account-asset-group-h2-feishu-draft-2026-07-14.md`

**Interfaces:**
- Consumes: completed draft and approved design.
- Produces: durable evidence for intent, structure, paragraph drift, source boundaries, and readiness status.

- [ ] **Step 1: Record the Article Intent Contract**

Include reader, reader decision, main line, non-goals, user-owned judgments, and agent-allowed work.

- [ ] **Step 2: Record source and judgment boundaries**

State that GitLab internals were not verified, PMO process baselines are missing, current logs cannot calculate MTTR, and the Haina/Wenda RACI remains an output rather than a known fact.

- [ ] **Step 3: Run the Section and Paragraph Drift Review**

Mark each main section `retain`, `compress`, `rewrite`, or `delete`. Confirm that the single mind map, three focus items, and separate handover remain intact.

- [ ] **Step 4: Set readiness status**

Use `review-draft` unless all evidence and Feishu write/read-back gates have passed. Do not claim synced or published.

### Task 4: Final local verification

**Files:**
- Verify: `wiki/reports/account-asset-group-h2-feishu-draft-2026-07-14.md`
- Verify: `wiki/ops/account-asset-group-h2-feishu-report-gate-review-2026-07-14.md`

**Interfaces:**
- Consumes: draft and gate review.
- Produces: a locally verified Feishu-ready review draft.

- [ ] **Step 1: Verify required headings and status labels**

```powershell
$p='wiki/reports/account-asset-group-h2-feishu-draft-2026-07-14.md'
Select-String -LiteralPath $p -Pattern '产品规划与账户能力建设|重点业务交付与客户成功|稳定性、研发效能与团队建设|移交专项'
Select-String -LiteralPath $p -Pattern '已有|建设|交接|重点需求|暂缓|退出'
```

Expected: all required terms are present.

- [ ] **Step 2: Verify every Markdown table exposes priority or stage**

Manually inspect each table header. Every table includes `优先级`, `顺序`, or `阶段`; convert noncompliant tables to bullet lists.

- [ ] **Step 3: Verify spoken length**

Read only the body above the appendices at a management-report pace. Compress repeated evidence until the run is between 10 and 15 minutes.

- [ ] **Step 4: Verify git boundaries**

```powershell
git status --short
git diff -- wiki/reports/account-asset-group-h2-feishu-draft-2026-07-14.md wiki/ops/account-asset-group-h2-feishu-report-gate-review-2026-07-14.md
```

Expected: only task-related files are considered for a later commit; unrelated workspace changes remain untouched.

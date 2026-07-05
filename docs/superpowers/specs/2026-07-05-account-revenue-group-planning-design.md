# Account And Revenue Group Planning Material Design

Date: 2026-07-05
Status: review-pending
Route: brainstorm -> superpowers spec; material drafting waits for user review.

## Reader And Job

Primary reader: upper management.

The material should help the reader decide:

- whether the account and revenue group should upgrade its positioning;
- what the next 6 to 12 months of account capability construction should focus on;
- what Q3 and Q4 must complete;
- whether the current 8-person team can carry collection, payout, recharge, revenue sharing, reconciliation, and cross-border account integration;
- whether to add people, replace people, or only redistribute work.

The material is not an internal complaint note and not a pure project schedule. It should be a rigorous planning memo with data-backed judgments.

## Corrected Team Facts

Use the corrected headcount:

- Current group size: 8 people.
- P7: 3 people, including the user.
- P6: 3 people.
- P5: 2 people.
- Peng Qingzheng has already been optimized due to low performance and should not be counted in the current 8-person capacity.

The user is a P7 and also carries Nirvana work. The user must not be positioned as a single-project owner for collection, payout, recharge, or cross-border account integration.

User positioning:

- overall planning owner;
- architecture and organization traction owner;
- resource and priority coordinator;
- key design reviewer;
- Q3 and Q4 acceptance owner;
- Nirvana task owner where already committed.

The user should not sink into the daily ownership of one single business line.

## North Star

The account and revenue group should move from a partial account, reconciliation, and revenue-sharing delivery group to a funds-account foundation group that can support:

- collection;
- payout;
- recharge;
- revenue sharing and profit distribution;
- account objects and account relations;
- balance, freeze, pending settlement, and in-transit funds;
- accounting, clearing, settlement, reconciliation, and exception recovery;
- cross-border account integration after the cross-border R&D merger.

Core wording:

> The current issue is not only headcount. The deeper issue is effective capacity and high-level traction. The 8-person ladder looks complete on paper, but the group does not yet have enough stable P7 traction, P6 subdomain ownership, and P5 delivery-quality capacity to carry collection, payout, recharge, and cross-border account integration at the same time.

## Evidence And Data Model

The final material must avoid unsupported claims. Use three kinds of data:

1. Headcount and grade data:
   - 8 total;
   - 3 P7, 3 P6, 2 P5;
   - 1 low-performance person already optimized and excluded from current capacity.

2. Capability-surface data:
   - current and target capabilities: collection, payout, recharge, revenue sharing, reconciliation, clearing/settlement, account core, cross-border account integration, Nirvana, daily demands and incidents;
   - local clearing workspace project spread includes `clearing-account`, `cloud-account`, `split-platform`, `settle-center`, `verify-center`, `refund-center`, `trade-core`, and related clearing/verification components;
   - cross-border/international source identifies `gep-payout-center`, `gep-payee-account-core`, `gep-account-center`, `baofu-account-center`, `baofu-payee-account-core`, `gep-fund-center`, and `payful-clearing-center` as relevant account, payout, fund, and clearing components.

3. Capacity model:
   - each major capability line needs at least one owner and one execution partner to be stable;
   - the user cannot be counted as daily owner for one business line because the user must cover overall planning, architecture review, organization governance, resource coordination, and Nirvana;
   - stable target scale for the next 6 to 12 months is 10 to 12 effective people, not 8.

## Current-State Diagnosis

The diagnosis should be written as organization capability risk, not emotional personnel judgment.

Main current issues:

- High-level traction is insufficient. P7 roles must move from module completion to direction ownership, cross-team coordination, and result acceptance.
- Jira/task volume and delivery visibility are weak. Low task exposure can mean limited proactive discovery, insufficient ownership, or insufficient decomposition.
- Pushback and unclear ownership increase coordination cost when collection, payout, recharge, and cross-border systems are introduced.
- The group has stayed too long in reconciliation and partial account work without enough breakthrough in account foundation, account balance, funds movement, and integrated exception recovery.
- P6 promotion pressure is high if people remain only execution contributors and do not become subdomain owners.
- P5 delivery capacity is useful but must be paired with clear subdomain ownership and engineering-quality gates.

Personnel observations to preserve carefully:

- Long Wei: observed active ownership gap and serious pushback risk. Do not assign independent strategic ownership before Q3 evidence improves. Give bounded tasks, clear acceptance, and an observation period.
- Huanhuan: maintained professionalism in the first-half revenue-sharing transformation. Future responsibility and P7-level evaluation must test broader view, cross-team traction, and system-level ownership.
- Binbin and Chenmin: technical initiative is acceptable, but communication and coordination are ordinary. Use them as subdomain execution leads with explicit coordination expectations.
- Shouyong: high enthusiasm, but P8 space is narrow. Give hard technical or cross-domain tasks, but do not convert enthusiasm directly into promotion judgment.
- Long-term reconciliation-only, weak-initiative P6 profile: promotion is difficult without visible breakthrough in account/funds domain ownership.

## Cross-Border Versus Current-System Difficulty

The material must compare cross-border and current domestic/account systems by difficulty, not only by project names.

Current domestic/account-side difficulty:

- collection/recharge path emphasizes inbound success, callback, query, compensation, account entry, balance update, and reconciliation evidence;
- payout emphasizes outbound application, balance check, freeze/deduct, channel submit, receipt, failure recovery, and reconciliation;
- revenue sharing emphasizes sharing relation, sharing ratio, fee deduction, pending sharing account, refund funding source, and settlement rules;
- clearing/reconciliation emphasizes evidence, difference detection, recovery, and reportability.

Cross-border difficulty adds:

- multiple account systems and naming spaces across international and cross-border projects;
- GEP/B2B account distinctions;
- main account, unsettle/income account, VA/currency subaccount, payee account, settlement account, and in-transit account relationships;
- non-CNY and multi-currency balance and settlement questions;
- FX, fee, customer/risk, and channel routing dependencies;
- payout and clearing chains across `gep-payout-center`, payee account, account center, fund center, and clearing center;
- integration risk from two existing account systems rather than one clean target model.

Planning implication:

> Cross-border integration is not a simple repository handover. It requires account-object alignment, account-relation mapping, balance and currency model alignment, payout and clearing evidence alignment, and responsibility boundary decisions before migration.

## Timeline

The final material must be structured by timeline. Q3 and Q4 are key.

### Q3: Boundary, Ownership, And Baseline

Goal: decide what the group owns, who owns each line, and what the migration baseline is.

Tasks:

- Collection baseline: identify where collection currently lives, what is outside the group, which systems must be integrated, and what migration risks exist.
- Payout baseline: identify payer account, payee account, channel routing, batch, receipt, failed compensation, and reconciliation differences.
- Recharge baseline: identify inbound channels, recharge records, balance entry, callback idempotency, query, and compensation.
- Revenue-sharing baseline: freeze current sharing relation, ratio, fee, pending-sharing account, refund-funding-source, and settlement-rule gaps.
- Cross-border account baseline: map `gep-payout-center`, `gep-payee-account-core`, `gep-account-center`, `baofu-account-center`, `baofu-payee-account-core`, `gep-fund-center`, and `payful-clearing-center` relationships.
- Team ownership: assign P7 sponsor roles, P6 subdomain owner roles, and P5 delivery-quality tasks.
- Governance dashboard: start monthly view of Jira/task volume, key design output, cross-team coordination, delays, online quality, and unresolved risks.

Acceptance:

- one responsibility matrix;
- one system-boundary map;
- one Q3 risk list;
- one personnel observation baseline;
- one capacity gap estimate.

### Q4: Capability Closure And Acceptance

Goal: make core account/funds capabilities support real business, not only planning.

Tasks:

- Unified account object and relation model: merchant, member/customer, payment account, bank account, channel account, cross-border VA/main account, payee account.
- Balance capability: available, frozen, pending settlement, in-transit, multi-currency, balance transaction, and net amount impact.
- Collection/recharge closure: success, callback, query, compensation, account entry, and reconciliation evidence.
- Payout closure: request, balance check, freeze/deduct, channel submit, receipt, failure recovery, and reconciliation difference.
- Revenue-sharing closure: sharing relation, ratio, fee, pending-sharing account, refund funding, and settlement rule.
- Cross-border integration design freeze: target model, boundary, migration batches, non-goals, and owner structure.
- Personnel acceptance: evaluate P7 traction, P6 ownership, P5 quality, and low-initiative improvement.

Acceptance:

- key capability design reviewed;
- at least one collection/recharge or payout closure path verified by task evidence;
- cross-border integration design frozen;
- personnel decisions for Q1 follow-up prepared.

### Next 6 To 12 Months: Integration And Ladder Reshape

Goal: complete the shift from project response to account foundation.

Tasks:

- execute cross-border account integration by batches;
- converge account object, balance, funds movement, clearing/reconciliation evidence;
- reduce duplicate account concepts and unclear system boundaries;
- turn P6 contributors into subdomain owners or cap their role expectations;
- replace or optimize roles that do not meet Q3/Q4 acceptance;
- stabilize a 10 to 12 effective-person structure if business scope remains unchanged.

## Capacity And Staffing Model

Use a capability-capacity table in the final material.

Suggested stable capacity:

| Capability line | Minimum | Stable | Note |
| --- | ---: | ---: | --- |
| Account foundation / balance / account relation | 2 | 3 | core foundation, cannot rely only on part-time work |
| Collection / recharge | 2 | 3 | inbound, callback, query, compensation, entry, reconciliation |
| Payout | 2 | 3 | outbound, freeze/deduct, channel receipt, failure recovery |
| Revenue sharing / revenue | 1 | 2 | Huanhuan may lead if Q3 shows system-level traction |
| Reconciliation / clearing / exception recovery | 1 | 2 | must move beyond passive reconciliation |
| Cross-border account integration | 1 | 2 to 3 | needs strong P7/architect or very strong P6 |
| Nirvana and retained work | user + 1 to 2 | user + 2 | cannot consume the user's overall governance role |

Conclusion:

- 8 current people cannot safely cover all target lines if cross-border integration and Nirvana are both real.
- Minimum practical scale: 10 people.
- Recommended stable scale: 10 to 11 people with key replacements if Q4 fails.
- Strong integration scale: 11 to 12 people.

## Staffing Options

### Conservative Option

Keep 8 people and add 2.

Add:

- 1 strong P7/P6 for cross-border account or payment-account architecture;
- 1 P6 for payout or collection/recharge.

Target size: 10.

Risk:

- helps delivery pressure but may not fix P7 traction;
- cross-border integration may still depend too much on the user.

### Stable Option

Recommended.

Keep 7 to 8 current people and add 3.

Add:

- 1 high-level account/payment architecture P7 or strong P6;
- 1 P6 with payout/channel outbound experience;
- 1 P6/P5 for collection/recharge entry, clearing/reconciliation, or exception compensation.

Target size: 10 to 11.

Operating rule:

- Q3: assign responsibility and observation targets;
- Q4: accept results;
- after Q4: replace underperforming roles rather than keep adding people.

### Aggressive Option

Keep 6 to 7 current people and add 4 to 5.

Add:

- 1 architecture-traction P7;
- 2 P6 for cross-border account, payout, collection/recharge;
- 1 to 2 P5/P6 for engineering delivery, test closure, reconciliation/compensation.

Target size: 11 to 12.

Risk:

- fastest capability reshape;
- larger short-term organization shock;
- requires clearer management support.

## Recommended Position

Recommend the stable option:

> Move from 8 people to 10 to 11 people in the next stage. Add 3 key capability roles first. Lock responsibility in Q3 and accept results in Q4. If P7 traction and P6 ownership still do not form by Q4, shift from supplementation to replacement instead of continuing to add headcount.

## Final Deliverable Shape

The final output should be:

1. A 3 to 5 page Chinese planning memo for management review.
2. An 8 to 10 page PPT outline derived from the memo.

The memo should use this structure:

1. Executive conclusion.
2. Current state and evidence.
3. 6 to 12 month technical planning.
4. Q3/Q4 task timeline and acceptance.
5. Cross-border integration difficulty comparison.
6. Team ladder and personnel-risk diagnosis.
7. Staffing model and three options.
8. Recommended decision.

The PPT outline should use this structure:

1. Why the account and revenue group must upgrade.
2. Current 8-person ladder and effective capacity.
3. Target capability map for the next 6 to 12 months.
4. Q3 task plan.
5. Q4 acceptance plan.
6. Cross-border versus current-system difficulty.
7. Personnel-role configuration.
8. Staffing gap and three options.
9. Recommended path.
10. Management decisions needed.

## Boundaries

- Do not count Peng Qingzheng in current headcount.
- Do not position the user as a single-project owner.
- Do not say "lack of people" without showing capability surface and capacity assumptions.
- Do not write personnel criticism as emotion. Convert it into observed risk, Q3/Q4 acceptance target, and action.
- Do not present cross-border integration as simple system handover.
- Do not make the final memo a generic architecture plan; people and staffing must be a major section.


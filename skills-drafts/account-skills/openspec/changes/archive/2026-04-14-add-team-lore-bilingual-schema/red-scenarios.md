# RED Scenarios — team-lore agent memory contract

This file records failing agent-memory scenarios against the current `team-lore` shape.

The goal is to prevent solution drift. Future schema, bootstrap, and weekly-review changes must point back to these same scenarios and show GREEN evidence against them.

---

## Evaluation dimensions

Each scenario is tagged with one primary failure class:

- `routing-pass-load-fail`
- `page-boundary-ambiguity`
- `durable-promotion-shape`
- `mixed-language-compatibility`

Each scenario includes:

- the agent task input
- the page or pages likely loaded
- why the current shape still fails
- the minimum GREEN condition

---

## RED-01 — Route succeeds, first-load context is still too expensive

**Class:** `routing-pass-load-fail`

**Agent input**

`Platform admin can log in, but team-scoped actions still behave strangely. What should I load first?`

**Likely pages**

- `projects/account-team-efficiency/domains/platform-admin-auth-and-team-scope.md`
- `pitfalls/admin-scope-ui-backend-drift.md`

**Current failure**

The domain page is directionally correct, but the first-load surface is still too dense:

- `Current facts` contains many bullets, but they mix auth contract, UI drift, data backfill, member actions, and shared dictionary behavior in one section
- there is no explicit `Applies When` or `Not For`
- there is no "load these 3 facts first" operating surface

That means an arbitrary agent can route to the page but still has to interpret a large mixed block before knowing:

- which facts are core to the auth/session issue
- which facts belong to adjacent UI or data-compatibility concerns

**Minimum GREEN**

The page exposes:

- explicit applicability and exclusion signals
- a short `Top Facts` section with only the minimum stable facts needed for first-load context
- lower-priority rationale and adjacent concerns moved below the operating surface

---

## RED-02 — Neighboring pages are both plausible and the boundary is not sharp enough

**Class:** `page-boundary-ambiguity`

**Agent input**

`The platform admin team selector looks empty on one page but works on another page. Which Lore page is primary?`

**Likely pages**

- `projects/account-team-efficiency/domains/platform-admin-auth-and-team-scope.md`
- `projects/account-team-efficiency/domains/team-admin-and-shared-ui.md`
- `pitfalls/admin-scope-ui-backend-drift.md`

**Current failure**

All three pages are relevant, but the current page shapes do not make loading order obvious:

- domain pages define `Scope`, but not a strong exclusion section
- the pitfall page has strong trigger signals, but the domains do not explicitly say when to prefer domain-vs-pitfall reading
- the agent can detect overlap, but not the correct reading sequence

This produces wasted context budget and inconsistent reuse across agents.

**Minimum GREEN**

The page set exposes:

- explicit `Not For` or exclusion guidance on the domain pages
- an unambiguous relationship between domain pages and the pitfall page
- enough routing cues that an agent can justify "load A first, then B only if needed"

---

## RED-03 — Overview pages are human-readable but not retrieval-first

**Class:** `routing-pass-load-fail`

**Agent input**

`I am starting work in account-team-efficiency. Give me the minimum project context.`

**Likely pages**

- `projects/account-team-efficiency/overview.md`

**Current failure**

The overview page is structurally better than a plain narrative page, but it still lacks a retrieval-first contract:

- `Summary`, `Boundaries`, and `Current risks` are useful to humans
- but they do not explicitly separate:
  - startup facts to load first
  - exclusion or not-for signals
  - which domain pages should be loaded next for which scene

An agent can read it, but cannot reliably compress it into a minimal first-load context without making interpretation choices.

**Minimum GREEN**

The overview page exposes:

- `Top Facts`
- `Applies When`
- `Not For`
- `Load Next`

or equivalent operating sections that make startup loading deterministic enough for different agents to converge.

---

## RED-04 — Weekly review can preserve truth but still degrade future reuse

**Class:** `durable-promotion-shape`

**Agent input**

`Weekly review accepted a new lesson about shared-object visibility drift. Will future agents load it efficiently?`

**Likely pages**

- whichever domain, pitfall, or principle page receives the new lesson

**Current failure**

The current Lore workflow enforces:

- logs are reviewed
- accepted lessons are absorbed
- destination pages are recorded

But it does not require the promoted lesson to improve retrieval surfaces.

So a valid weekly review can still:

- append a new bullet into a large existing prose-heavy section
- preserve truth
- but make future first-load reading worse rather than better

**Minimum GREEN**

Promotion rules require accepted durable knowledge to land in:

- `Top Facts`
- `Watchpoints`
- `Applies When`
- `Related Pages`

or equivalent retrieval-first operating sections, not only generic prose append.

---

## RED-05 — English retrieval may work while English loading still fails

**Class:** `mixed-language-compatibility`

**Agent input**

`How should a platform admin session behave when no team membership exists?`

**Likely pages**

- `projects/account-team-efficiency/domains/platform-admin-auth-and-team-scope.md`

**Current failure**

The page title and body are in English, so this specific example can route.

But the system has no explicit language-support contract:

- no standard alias field
- no rule for mixed-language terminology
- no guarantee that future promoted pages will preserve English/Chinese routing aids consistently

This means successful English loading today is incidental, not contractual.

**Minimum GREEN**

Reusable durable pages define a minimum language-support surface such as:

- aliases
- bilingual summary
- cross-language keyword mapping

for any terminology that can drift across Chinese/English prompts.

---

## RED-06 — Index navigation exists, but next-hop intent is implicit

**Class:** `page-boundary-ambiguity`

**Agent input**

`I found the account-skills overview. What should I open next if my problem is wiki bootstrap vs runtime lore retrieval?`

**Likely pages**

- `wiki/index.md`
- `projects/account-skills/overview.md`
- `projects/account-skills/domains/codex-governance-installation.md`

**Current failure**

The index and overview pages contain links, but not a strong next-hop contract:

- the user can discover the pages
- but an arbitrary agent still has to infer whether the next step is runtime Lore, bootstrap, or governance-install
- navigation relies on reading prose and making interpretation choices instead of following explicit retrieval cues

**Minimum GREEN**

Entry pages expose:

- explicit "if your problem is X, open Y next" navigation
- enough exclusion signals to avoid unnecessary page loading

---

## RED-07 — Pitfall pages are useful, but may still over-expand context

**Class:** `routing-pass-load-fail`

**Agent input**

`Why does a bootstrap feel complete but still not behave like usable memory?`

**Likely pages**

- `pitfalls/bootstrap-entry.md`

**Current failure**

The pitfall page is concise and well-formed, but it still lacks a direct operating summary for agent startup:

- trigger signals are good
- avoidance is good
- but there is no short "if you only check 3 things, check these" surface

An agent can still use the page, but not in the cheapest possible way.

**Minimum GREEN**

Pitfall pages expose a short operating section, such as:

- `Top Checks`
- `Top Facts`
- `Fast Reject`

so the page can be used as a low-cost diagnostic surface first and long-form explanation second.

---

## RED-08 — The system cannot yet claim agent-ready support from current evidence

**Class:** `durable-promotion-shape`

**Agent input**

`Can we now say team-lore works for any agent?`

**Likely evidence**

- retrieval pressure results
- live weekly review runs
- existing wiki pages

**Current failure**

Current evidence proves:

- routing can work
- weekly review can absorb durable knowledge
- bootstrap can produce a usable repo structure

It does not yet prove:

- first-load context quality
- boundary clarity between neighboring pages
- durable promotion into retrieval-first page shape
- consistent mixed-language loading support

**Minimum GREEN**

Completion claims require explicit evidence for:

- routing quality
- context-load quality
- page-boundary clarity
- durable-promotion shape
- mixed-language compatibility

---

## Completion note

This RED set should remain stable while the solution evolves.

If the proposed schema changes but these scenarios do not become easier to evaluate, the solution is drifting.

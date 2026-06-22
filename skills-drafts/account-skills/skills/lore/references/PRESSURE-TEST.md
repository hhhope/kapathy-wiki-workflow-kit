# Lore Wiki Pressure Test

Use this after the TDD baseline exists.

The purpose is to test scale, ambiguity, and workflow breakpoints, not just happy-path correctness.

---

## P1 — Retrieval pressure

Goal:
- verify recall and noise under mixed language and mixed domain input

Procedure:
1. Build the 20-query dataset from `TDD-SPEC.md`
2. Run each query through:
   - `index.md`
   - target page selection
   - top result set review
3. Record:
   - expected page
   - returned pages
   - hit / miss
   - false positive or not

Watch for:
- Chinese / English mismatch
- synonym misses
- domain overlap misses
- overly broad pitfall pages

---

## P2 — Closed-loop pressure

Goal:
- verify that logs do not pile up without becoming durable knowledge

Procedure:
1. Create 10 logs from the log dataset
2. Run weekly review
3. For each accepted log, verify:
   - target page updated
   - `index.md` updated if needed
   - log marked reviewed
   - `absorbed-to` recorded
4. Record weekly-review metrics:
   - reviewed logs
   - absorbed logs
   - discarded logs
   - `absorbed-to` completion rate
   - destination page-type distribution

Watch for:
- logs accepted but not written
- wiki page updated without index maintenance
- reviewed logs with blank destination
- weekly review that outputs prose only and omits metrics

---

## P3 — Context-budget pressure

Goal:
- verify that startup page loading does not grow linearly with wiki size

Procedure:
1. Simulate wiki sizes at:
   - 10 pages
   - 50 pages
   - 100 pages
   - 300 pages
2. Run the same startup scenarios at each size
3. Record:
   - pages read
   - page categories read
   - whether the same result could have been achieved with fewer pages

Watch for:
- index losing precision
- too many domain pages loaded
- principle pages being read by default instead of on demand

---

## P4 — Multi-project pressure

Goal:
- verify that project-local knowledge and cross-project knowledge do not contaminate each other

Procedure:
1. Simulate three projects:
   - payment-heavy project
   - settlement-heavy project
   - auth-heavy project
2. Add overlapping but distinct lessons
3. Query each project separately
4. Verify:
   - project-local pages are favored first
   - cross-project pages are reused only when truly shared
   - unrelated project noise does not dominate results

Watch for:
- one project's terminology polluting another project's top results
- principles being promoted too early
- pitfall pages becoming project dumps

---

## Exit criteria

Pressure testing is good enough for v1 if:
- hard gates still hold under all scenarios
- soft metrics stay inside target range or have one documented exception
- no single pressure test reveals a structural failure in page taxonomy

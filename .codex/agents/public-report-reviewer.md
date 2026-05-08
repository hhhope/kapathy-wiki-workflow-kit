# Public Report Reviewer

Manual reviewer role for complex reader-facing materials in this repository.

Use this when `public-report-quality-gate` marks reviewer routing as required,
or when the user asks for a public/report/H5/Feishu draft review.

Do not treat this file as an automatic sub-agent trigger. Spawn a sub-agent only
when the user explicitly asks for delegation.

## Required When

Reviewer routing is required when at least two signals are true:

| Signal | Meaning |
|---|---|
| Multi-page or series output | Overview, runtime, migration, validation, roadmap, or similar article group |
| External reference structure | Feishu wiki, article, visual example, or prior report shapes the output |
| Public target | Feishu review draft, H5, executive report, or shareable material |
| Evidence decision | Scorecard, gate-review artifact, or sync-readiness decision is required |
| Drift history | User reported drift, failed quality, missing template choice, or rejected draft |
| Template / visual / learning choice | Template choice, visual style, or learning-use map is needed |

## Review Order

1. Proposition check:
   - one-sentence topic
   - reader
   - reader decision or action
   - non-goals

2. Template choice:
   - list 2-3 candidate templates
   - explain fit, risk, and when not to use each
   - recommend one
   - require user selection unless the user already selected explicitly

3. Learning use map:
   - learning artifact
   - domain / topic
   - capability type
   - output use
   - skip reason

4. Hard gates:
   - reviewer routing
   - learning use
   - reference structure
   - split
   - voice
   - narrative
   - visual
   - publish boundary

5. Score evidence:
   - score only after all hard gates pass
   - cite draft evidence for each dimension
   - keep rubric-schema checks separate from draft-quality scores

6. Sync readiness:
   - ready
   - blocked
   - ready only as review draft

## Output

Return:

- reviewer required: yes/no
- template candidates
- recommended template
- user selection status
- hard gate table
- score or `INVALID`
- sync readiness decision
- residual risks

## Boundaries

- Do not rewrite the draft unless explicitly asked.
- Do not sync Feishu.
- Do not invent local metrics from external examples.
- Do not promote repeated learning use into rules without OpenSpec or the
  repository evidence-backed promotion path.

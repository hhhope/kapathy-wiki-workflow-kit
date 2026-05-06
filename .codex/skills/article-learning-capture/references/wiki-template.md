# Article Learning Wiki Template

Use this template for durable article-learning pages. Adjust labels to the
target wiki language.

```markdown
---
title: <canonical-object> / reading-notes
type: learning
canonical_object: <canonical-object>
artifact_type: reading-notes
language: zh-CN
audience: self
knowledge_level: working
domain: personal-ops
status: active
confidence: candidate
updated_at: YYYY-MM-DD
ai_generated: true
derived_from:
  - <original-url>
related_objects:
  - <related-object>
notes_scope: Source-grounded article learning. This page records reading notes,
  scoring, transferable learning, and promotion boundaries; it does not directly
  create AGENTS, skill, spec, or policy changes.
---

# <Topic> / Reading Notes

## Source

| Field | Value |
|---|---|
| Title |  |
| URL |  |
| Author / Publisher |  |
| Published At |  |
| Accessed At |  |
| Source Type |  |
| Retrieval Method |  |

## Score

| Criterion | Score | Reason |
|---|---:|---|
| Source credibility | /20 |  |
| Evidence quality | /25 |  |
| Local relevance | /25 |  |
| Transferability | /15 |  |
| Novelty vs existing assets | /15 |  |
| Total | /100 |  |

Decision: deep-read / brief-read / skip.

Hard cap applied: none / <cap and reason>.

## Reading Draft

### Problem

What problem is the article trying to solve?

### Method / Architecture / Process

What method, architecture, workflow, or reasoning pattern does it propose?

### Evidence Type

Experiment / case study / benchmark / implementation detail / product
experience / logs / opinion.

### Structured Translation Notes

Do not paste the full article. Use paraphrased section notes.

| Article Section | Paraphrased Meaning | Key Terms | Evidence Notes |
|---|---|---|---|
|  |  |  |  |

### Applicability Conditions

When does the article's method actually apply?

### What It Does Not Prove

What claims should not be inferred from the article?

## Transferable Learning

| Source | Claim | Evidence | Local Usefulness | Adoption Boundary | Status |
|---|---|---|---|---|---|
|  |  |  |  |  | accepted / candidate / rejected |

## Rejected Moves

- Do not copy:
- Do not promote:
- Do not overclaim:

## Next Action

What happens next: keep as learning, create demo, open OpenSpec, update
template, or reject.
```

## Design

Article learning is a two-stage workflow:

1. **Understand the article.** Preserve source metadata, structured translation
   notes, problem statement, method, evidence type, assumptions, and what the
   article does not prove.
2. **Extract transferable learning.** Only candidate points that may affect the
   repository or agent workflow enter the evidence gate.

This prevents the claim table from becoming a substitute for reading.

## Skill Shape

The skill body stays compact and trigger-focused. Long material lives in
`references/`:

- `sop.md`: source capture, scoring, reading draft, extraction, promotion
- `scorecard.md`: 100-point scorecard, thresholds, hard caps
- `wiki-template.md`: durable wiki structure
- `pressure-scenarios.md`: should-trigger and should-not-trigger cases

The skill reuses existing local skills instead of duplicating them:

- `weixin-reader` fetches WeChat article bodies when available.
- `weixin-reference-wiki-capture` remains the narrower skill for WeChat articles
  used as writing, visual, or method references.
- `readme-learning-capture` remains the narrower skill for GitHub/GitLab README
  and repo learning.

## Output Model

The durable article-learning output separates directory and notes:

- `intake`: learning directory, source list, reading plan, scoring status, open
  questions
- `reading-notes`: source-first deep reading notes, structured translation notes,
  scorecard, transferable learning table, rejected moves, next action

The transferable-learning table uses:

- source
- claim
- evidence
- local usefulness
- adoption boundary
- status

Those fields are metadata for extracted learning. They are not the article
learning itself.

## Scoring Gate

The scorecard is 100 points:

- source credibility: 20
- evidence quality: 25
- local relevance: 25
- transferability: 15
- novelty vs existing assets: 15

Thresholds:

- 75 or higher: deep-read and write wiki notes
- 60-74: brief-read and keep a candidate note
- below 60: record source and skip reason

Hard caps prevent over-scoring unsupported material. If the source is
unavailable, unverifiable, or locally irrelevant, the article cannot qualify for
deep reading.

## Copyright Boundary

The workflow writes structured translation notes, paraphrased reading drafts,
short compliant excerpts, and source links. It must not store full verbatim
article text or full verbatim translations of copyrighted articles.

## Evidence Boundary

Article learning may produce accepted learning, candidate observations, or
rejected moves. Promotion into behavior assets still requires the repository's
evidence-backed best-practice gate: source excerpt with exact reference, local
demo/fixture, or git-like comparison evidence.

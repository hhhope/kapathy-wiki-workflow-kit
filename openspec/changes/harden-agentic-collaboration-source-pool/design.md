## Context

The previous exploration established that this topic already has a broad source
surface, but several layers remain weak:

- podcast/video leads need transcript or episode-level capture before hard
  quotation;
- AI-first workforce and headcount claims need primary memo or executive-post
  capture;
- Chinese-language practitioner and conference sources are under-covered;
- vendor pages are strategy evidence, not customer outcome proof;
- source-pool count must not be confused with publication-grade citation count.

## Decision

This change treats "300 sources" as a source-lead hardening target, not as a
publication claim.

The implementation should add enough new URL-bearing source rows to reach at
least 300 unique URLs across the relevant `agentic-product-engineering` source
and ops files.

## Source Classes

Each new source row should preserve a source class:

- `primary`: company, official docs, engineering blog, official report, official
  repo, executive memo/post when directly accessible;
- `research`: survey, analyst report, academic paper, methodology-bearing study;
- `primary-interview`: original podcast/video/interview page;
- `transcript-available`: source has readable transcript or episode text;
- `secondary`: media or third-party coverage;
- `secondary-cn`: Chinese-language secondary or practitioner coverage;
- `candidate`: useful discovery lead that needs deeper capture before use.

## Expansion Buckets

Prefer adding sources in buckets that address existing gaps:

1. primary memos / workforce-policy sources;
2. Chinese-language practitioner and conference sources;
3. operator interviews with transcripts;
4. enterprise governance and AI operating model sources;
5. independent research / risk / productivity evidence;
6. agentic software development platform and infrastructure sources.

## Verification

Minimum verification:

- count unique URLs across the relevant source and ops files;
- confirm count is at least 300;
- update evidence matrix and gate review with the new count and boundary;
- run `openspec validate harden-agentic-collaboration-source-pool --strict`;
- run `git diff --check` on task-related paths.

## Boundaries

This is a source-hardening pass. It does not make the report review-ready by
itself. It can improve "internal discussion" confidence and source-selection
readiness, while still preserving transcript, primary-source, visual QA, and
user-judgment blockers.

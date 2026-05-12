## 1. Baseline

- [ ] 1.1 Record baseline source counts for curated, broad scan, timeline,
      podcast/video, unique URLs, and repeated URL mentions.
- [ ] 1.2 Identify source gaps from existing evidence matrix and gate review.

## 2. Source Hardening

- [ ] 2.1 Search public sources in the missing buckets.
- [ ] 2.2 Add enough URL-bearing source leads to reach at least 300 unique URLs.
- [ ] 2.3 Preserve source class and use boundary for each added lead.
- [ ] 2.4 Avoid duplicate URLs and avoid counting source-pool size as
      publication-ready proof.

## 3. Evidence Updates

- [ ] 3.1 Update source pool count and unique URL count in the relevant source
      pages.
- [ ] 3.2 Update the article evidence matrix with the 300-source boundary and
      load-bearing-source target.
- [ ] 3.3 Update the report gate review with the new evidence status and
      remaining blockers.
- [ ] 3.4 Add or update a repo-visible source-hardening ops note.

## 4. Verification

- [ ] 4.1 Verify unique URL count is at least 300.
- [ ] 4.2 Run `openspec validate harden-agentic-collaboration-source-pool --strict`.
- [ ] 4.3 Run `git diff --check` on task-related paths.
- [ ] 4.4 Commit only task-related paths.

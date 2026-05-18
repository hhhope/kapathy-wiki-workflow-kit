# Proposal: add wiki content enrichment preview

## Summary

Add a deterministic content-enrichment preview for `wiki/ops` and `wiki/adr`
pages that suggests domain, ops area, canonical object, artifact type, and
relation frontmatter candidates before graph and MOC projection.

## Motivation

MOC projection from existing frontmatter only solves the last step:

```text
clean frontmatter -> graph -> MOC
```

The missing runtime step is earlier:

```text
page content -> domain/object/relation candidates -> reviewed frontmatter
```

Without this enrichment preview, MOC generation can faithfully project stale,
missing, or poorly classified frontmatter. The repository needs an explicit
preview layer that analyzes page content and current taxonomy signals without
directly mutating pages.

## Scope

- Cover `wiki/ops` and `wiki/adr` only.
- Produce frontmatter and relation candidates with evidence and confidence.
- Surface enrichment health in status.
- Add apply-preview output for enrichment candidates.
- Add `wiki-react`/eval routing for `wiki_content_enrichment`.

## Non-Goals

- Do not cover all `wiki/**` pages.
- Do not call an LLM or external service.
- Do not directly edit frontmatter.
- Do not generate MOC files.
- Do not infer hidden semantic relationships without explicit textual,
  path, title, or existing-object evidence.

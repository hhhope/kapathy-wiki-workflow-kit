# strengthen-requirements-role-evidence-gate

## Why

The current requirements checker can mark a case ready when user stories refer
only to taxonomy buckets such as `system_actor`. A real pressure test with
`embedded-account-phase1` showed that this hides which case-local actor performs
the behavior. The same pressure test showed that evidence must be enforced by a
traceable anchor contract, not by one mandatory field name.

## What Changes

- Add case-local role instances with `status` and `confirmed_as`.
- Require strict `role_ref` from user stories to confirmed role instances for
  OpenSpec handoff.
- Add object-aware evidence anchor validation.
- Preserve compatibility reading for legacy cases.
- Migrate only `embedded-account-phase1` as the golden sample.

## Out Of Scope

- No requirements taxonomy changes.
- No wiki frontmatter taxonomy changes.
- No batch migration of historical requirements cases.
- No weights, RAG, embeddings, cross-case entity merge, or full knowledge graph.

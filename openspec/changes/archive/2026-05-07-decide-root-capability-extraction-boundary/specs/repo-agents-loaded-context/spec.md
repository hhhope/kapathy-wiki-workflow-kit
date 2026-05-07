## MODIFIED Requirements

### Requirement: Repo AGENTS SHALL be governed as a loaded-context entrypoint

The repository SHALL treat repo `AGENTS.md` compression and proxy migration as
loaded-context governance, not as line-count cleanup alone.

#### Scenario: Repo AGENTS migration is planned

- **WHEN** repo `AGENTS.md` is compressed, proxy-migrated, or structurally
  rewritten
- **THEN** the change SHALL classify each affected section as one of:
  - inline repo-only hard stop
  - stable proxy to ADR, OpenSpec spec, wiki ops page, or published skill
  - delivery-sensitive inline section
  - deferred candidate
- **AND** it SHALL record before/after line, word, and byte counts as
  supporting evidence
- **AND** it SHALL record proxy coverage and hard-stop preservation evidence

#### Scenario: A governance block is replaced by a proxy

- **WHEN** a repo `AGENTS.md` governance block is shortened or replaced by a
  proxy
- **THEN** the proxy SHALL point to a stable repo-visible source
- **AND** the change SHALL verify that the next agent can identify where to
  read, how to verify, and when to stop

#### Scenario: A delivery-sensitive workflow is considered for proxying

- **WHEN** material-processing or meeting-note output guidance is considered
  for proxy migration
- **THEN** the change SHALL preserve the delivery boundary inline unless the
  proxy evidence proves equivalent runtime safety

#### Scenario: Repo AGENTS lists runtime skill routes

- **WHEN** repo `AGENTS.md` lists high-frequency runtime skill routes
- **THEN** it SHALL state that runtime routing does not imply ownership
- **AND** rows that can be mistaken for generic root capabilities SHALL declare
  ownership status or point to a stable source that does

# learning-capture-runtime Specification

## ADDED Requirements

### Requirement: Single Learning Runtime Entry

Learning requests SHALL route through `learning-capture` as the only active
runtime skill entry.

#### Scenario: Article learning request

- **WHEN** the user provides an article, blog, paper, WeChat post, or article
  collection as learning, reference, reuse, or adaptation material
- **THEN** the agent SHALL load `learning-capture`
- **AND** the agent SHALL use the article reference module from within
  `learning-capture`
- **AND** no active `article-learning-capture` skill description SHALL be
  available as a separate runtime trigger.

#### Scenario: Repo or README learning request

- **WHEN** the user provides a GitHub/GitLab repo or README for reuse learning
- **THEN** the agent SHALL load `learning-capture`
- **AND** the agent SHALL route to the repo/README reference module, not the
  article module.

### Requirement: Chinese-First Durable Learning Output

Durable internal wiki learning artifacts SHALL default to Chinese output while
behavior assets remain English-first.

#### Scenario: Chinese article learning note

- **WHEN** the user provides a Chinese article or WeChat post for durable wiki
  learning
- **THEN** the generated `wiki/sources` or `wiki/ops` learning page SHALL use
  Chinese headings and body prompts by default
- **AND** the page SHALL preserve source metadata, source grounding, scoring,
  transferable learning, and promotion boundaries.

#### Scenario: English-first target artifact

- **WHEN** the learning output is a `SKILL.md`, public English README/doc, or
  external English-facing artifact
- **THEN** English output remains allowed
- **AND** the Chinese-first durable wiki default SHALL NOT override that target
  artifact's language contract.

# Proposal

## Why

The requirements taxonomy currently has only `account`, `settlement`, and
`clearing`. Those values are useful for local account and clearing/settlement
work, but they do not support broader payment ecosystem requirements or
AGI-era human-Agent collaboration.

The deeper need is a DDD-based domain model that turns fragmented requirements
knowledge into reusable cognitive assets for humans and Agents. The model
should help requirements move across roles, cases, and future Agent work
without restarting boundary discussions every time.

## What Changes

- Define DDD requirements domain standards.
- Define the first runnable payment domain skeleton.
- Define domain collaboration relationships.
- Define compounding asset expectations.
- Define taxonomy admission standards.
- Map current `account`, `clearing`, and `settlement` values to the new
  skeleton.
- Update `requirements/config/requirements-taxonomy.yaml` with the first
  payment skeleton.

## What Does Not Change

- Does not implement `req-domain-analysis`; that belongs to
  `add-req-domain-analysis-skill`.
- Does not batch-migrate historical requirements cases.
- Does not modify wiki frontmatter taxonomy.
- Does not authorize implementation from a requirements case.

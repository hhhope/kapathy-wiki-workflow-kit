# add-requirements-analysis-agent

## Why

Implementation can begin before requirements are clear enough to code. The repeated failure pattern is missing requirement shape: unclear domain, unnamed roles, weak user stories, and acceptance functions that do not map back to user stories.

The repository already has wiki taxonomy and medical-agent case-file patterns. This change adds a separate requirements analysis agent so requirement readiness can be checked without turning wiki frontmatter or detailed-design content into requirement authority.

## What Changes

- Add `requirements/config/requirements-taxonomy.yaml` as the independent requirement-readiness contract.
- Add requirements case-file helpers with machine-readable JSON blocks.
- Add `scripts/check_requirements_case.py` for deterministic hard-gate evidence.
- Add `scripts/requirements_analysis_agent.py` for intent recognition, domain recognition, case routing, and OpenSpec draft handoff.
- Add a CLI wrapper for normal use.
- Add focused tests for intent classification, domain candidates, hard-gate behavior, mixed-document soft warnings, and OpenSpec draft blocking.

## Out of Scope

- API correctness validation.
- DDL correctness validation.
- Full architecture review.
- Release readiness validation.
- Automatic implementation after OpenSpec draft creation.
- Forcing unknown domains into existing domain IDs.

## Source Design

- `docs/superpowers/specs/2026-05-29-requirements-analysis-agent-design.md`

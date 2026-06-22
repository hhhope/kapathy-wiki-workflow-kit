# Routing Automation Results — representative route corpus

Date: 2026-04-14
Change: `harden-team-lore-language-and-routing`

## RED — Before draft hardening

Observed failures from `check-routing-automation.py`:

- `process` passed because OpenSpec artifacts were present
- `lore` and `mixed` cases failed because the expected draft lore surfaces did not yet exist
- this showed the routing corpus was real: it did not silently pass on narrative intent alone

## GREEN — After draft hardening

The routing corpus now covers representative cases for:

- `process`
- `lore`
- `graphify`
- `mixed`

The current corpus checks:

- OpenSpec status for process questions
- draft lore surfaces for lore and mixed questions
- Graphify query markers for structure evidence

## Verification

Expected pass conditions for this slice:

- `process` cases route through OpenSpec
- `lore` cases require the selected draft lore pages
- `graphify` cases require graph markers from `graphify query`
- `mixed` cases require both lore surface presence and graph evidence

Observed passing corpus for this slice:

- `2` process cases
- `3` lore cases
- `1` graphify case
- `2` mixed cases

## Limits

- this is still a representative route corpus, not a general-purpose classifier benchmark
- Graphify remains a code-topology layer only
- the automation proves the selected contract, not universal routing completeness

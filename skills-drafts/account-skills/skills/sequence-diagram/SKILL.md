---
name: sequence-diagram
description: Use when source material describes ordered service, system, interface, payment, compensation, or request-response interactions that should become a Mermaid sequence diagram.
---

# Sequence Diagram

Top-level entry for the sequence-diagram worker. The detailed account-domain
rules live in `skills/SKILL.md` in this directory.

Use through `visual-agent` for ordinary visual-production requests. Direct use
is for debugging or editing this worker.

Before drawing, classify the interaction structure and ask only the missing
high-risk questions that affect participant ownership, fund/account movement,
failure handling, async behavior, compatibility, or risk-control behavior.

Then produce Mermaid `sequenceDiagram` output with:

- clear business participant names
- the main request/response path
- at least one explicit failure branch when failure handling matters
- timeout or retry assumptions for external calls when known or assumed
- state-change notes for key account, payment, or order state changes
- assumption notes for any unconfirmed branch

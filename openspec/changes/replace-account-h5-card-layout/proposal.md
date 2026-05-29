# Proposal: Replace Account H5 Card Layout

## Why

The account-group onboarding H5 still relies on repeated card grids as the
primary information structure. Even after color and border cleanup, the result
looks like a generic template rather than an account technical training
material. The user rejected the card-style surface.

## What Changes

- Remove card grids as the dominant visual language.
- Reframe repeated content as technical-training structures:
  - definition lists for responsibilities and objects;
  - evidence rows for chain checkpoints and problem diagnosis;
  - compact matrices for projects, AI collaboration, maturity, and newcomer
    paths;
  - source-backed diagrams as the main visual surfaces.
- Keep the existing section order and account-domain content.
- Keep `AI 如何与我们协作` focused on what the account group provides,
  including Account Harness constraints.
- Update the gate review with the card-layout rejection and repair evidence.

## Out of Scope

- Feishu sync or image insertion.
- New frontend dependencies.
- Redrawing the existing source-backed diagrams.
- Changing account-domain facts outside the layout repair.
- Introducing credentials, internal URLs, personal contacts, QR codes, or
  access instructions.

## Impact

- The existing H5 is edited in place.
- The H5 should read more like an internal technical handout / architecture
  briefing and less like a block-card landing page.

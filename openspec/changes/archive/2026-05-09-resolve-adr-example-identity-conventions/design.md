# Design: Resolve ADR and Example Identity Conventions

## Goal

Reduce unresolved identity pressure by recognizing stable path conventions that
already carry explicit object identity.

## Path Conventions

ADR pages:

```text
wiki/adr/<number>-<canonical-object>.md
```

The canonical object is the filename slug after the numeric prefix. The artifact
type is `adr`.

Example pages:

```text
wiki/examples/<canonical-object>-example.md
```

The canonical object is the filename slug before `-example`. The artifact type
is `example`.

## Boundaries

- Frontmatter still has highest priority.
- Existing hand-written resolvers remain allowed for special cases.
- The ADR resolver only applies to numbered ADR filenames.
- The example resolver only applies to filenames ending in `-example.md`.
- Ops pages remain unresolved unless they have frontmatter or an explicit
  resolver.

## Verification

- Unit tests cover ADR path, example path, and unmapped ops behavior.
- Live extraction should reduce warning count from 49 to 30.
- OpenSpec validation and affected runtime tests should pass.

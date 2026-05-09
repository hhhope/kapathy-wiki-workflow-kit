# Change: Resolve ADR and Example Identity Conventions

## Why

After the first identity-pressure reduction, the graph runtime still reports 49
unresolved identities. The remaining set includes 14 ADR pages and 5 example
pages whose identities are explicit in repository path conventions:

- `wiki/adr/<number>-<canonical-object>.md`
- `wiki/examples/<canonical-object>-example.md`

These pages can become graph nodes without reading arbitrary prose and without
batch-migrating unstable ops/intake material.

## What Changes

- Add a bounded ADR path resolver for numbered ADR filenames.
- Add a bounded example path resolver for `*-example.md` filenames.
- Add tests proving these conventions resolve known warnings while unrelated
  ops pages still remain warnings.

## Impact

- Affected spec: `wiki-graph-extraction`
- Affected runtime: graph extraction and downstream relation/score/queue layers
- Non-goals: no ops/intake migration, no semantic prose inference, no graph UI

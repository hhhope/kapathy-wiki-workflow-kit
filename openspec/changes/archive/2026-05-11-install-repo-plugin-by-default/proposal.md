# Install Repo Plugin By Default

## Why

The repo marketplace is registered and resolves to a valid plugin package, but
the user still sees zero active plugins and no `/wiki:*` slash commands. The
marketplace entry currently marks the repo plugin as `AVAILABLE`, which exposes
it as installable but does not make it active by default.

## What Changes

- Change the repo marketplace policy from `AVAILABLE` to
  `INSTALLED_BY_DEFAULT`.
- Update tests to require the default-installed policy for the repo-local wiki
  command plugin.
- Keep the marketplace path, plugin package, command names, and README install
  command unchanged.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `wiki-status-slash-command`: repo-local marketplace metadata must default
  install the wiki command plugin so the slash surface becomes active after the
  marketplace is loaded.

## Impact

- Affects `.agents/plugins/marketplace.json`, marketplace tests, and this
  OpenSpec change record.
- Does not change command behavior or wiki runtime logic.

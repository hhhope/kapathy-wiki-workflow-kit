## 1. Change Setup

- [x] 1.1 Create OpenSpec artifacts for the AI chat workflow installer change

## 2. Canonical Model

- [ ] 2.1 Define the canonical workflow source boundary for governance, workflow units, and adapter mappings
- [ ] 2.2 Identify which existing repo assets are canonical inputs versus generated adapter outputs
- [ ] 2.3 Define the installation boundary between workflow content and platform mechanics

## 3. Platform Adapters

- [ ] 3.1 Define the Codex adapter surface and required output shape
- [ ] 3.2 Define the Cursor adapter surface and required output shape
- [ ] 3.3 Define the Claude adapter surface and required output shape
- [ ] 3.4 Define the cross-platform invariants that all adapters must preserve

## 4. Installer Workflow

- [ ] 4.1 Define the one-click installation flow and expected inputs
- [ ] 4.2 Define validation checks that confirm each target was installed correctly
- [ ] 4.3 Define failure handling when one target cannot accept the full workflow surface

## 5. Share Artifact

- [ ] 5.1 Draft a Feishu-shareable explanation of the installer model
- [ ] 5.2 Explain platform differences, scope boundaries, and non-goals in the share artifact

## 6. Validation

- [ ] 6.1 Record baseline evidence that the repository lacked a formal multi-platform installer model
- [ ] 6.2 Validate the OpenSpec change structure
- [ ] 6.3 Confirm the design does not collapse all targets into one misleading universal skill

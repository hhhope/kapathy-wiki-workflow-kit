---
name: channel-integration
description: Use when implementing, reviewing, debugging, or planning bank/payment channel integrations in yqt-trade, especially work under trade-biz/src/main/java/com/yqt/trade/biz/channel, channel auth key handling, external bank API calls, callbacks, file upload/download, signing/encryption, mapping external statuses, retry/query compensation, or onboarding a new bank/open-bank vendor.
---

# Channel Integration

## Goal

Use this skill to keep channel access work boring in the best way: verifiable inputs, thin adapters, explicit failure handling, and tests around money-moving behavior.

## Start Here

1. Read the target bank/vendor document and identify every endpoint, callback, file flow, credential, signing/encryption rule, idempotency key, and status code used by the requested scope.
2. Inspect the closest existing channel package under `trade-biz/src/main/java/com/yqt/trade/biz/channel/`; prefer copying its layering and naming style over inventing a new structure.
3. Before writing business logic for a new API or field, print or capture raw sample request/response data and verify exact field names, nesting, encodings, date formats, and success/failure examples.
4. Classify the work before edits:
   - Write operation: account opening, bind card, payment, transfer, withdraw, cancel, status update, credential update.
   - External call: bank HTTP/SDK/RPC, callback response, file gateway, queue/event, compensation query.
   - DB operation: mapper/entity/schema change, transaction status persistence, credential or auth-key persistence.
5. Load `references/channel-integration-checklist.md` when the task is more than a small single-method fix, includes a new vendor/API, or touches signing, callbacks, retries, files, money movement, or status mapping.

## Implementation Rules

Keep the channel adapter narrow:

- Put vendor-specific DTOs, enums, constants, signing/encryption helpers, and HTTP/SDK clients inside the vendor package.
- Convert between internal BO/DTOs and vendor DTOs at the channel boundary; do not leak vendor status strings or field names into core services unless an existing pattern already does.
- Keep sensitive credential handling aligned with existing `ChannelAuthKey` and `otherAuthInfo` patterns. Do not log plaintext certificates, private keys, passwords, full identity numbers, bank cards, phone numbers, or raw encrypted blobs.
- Prefer explicit enum/status mapping for every vendor response state. Treat unknown states as pending or failed only after confirming vendor semantics.
- Add timeouts for every external call path. If the underlying client hides timeout setup, document where the timeout is configured and verify the config key.
- Define retry/compensation behavior before returning uncertain failures. For money movement, prefer query-by-original-order over blind repeat submit unless the vendor contract proves submit is idempotent.

## Self-Check

For write operations, confirm:

- The idempotency key is named and stable, usually internal order number, channel order number, merchant number, or a vendor serial number.
- Duplicate submission behavior is known from raw vendor data or docs.
- Concurrency and locking follow the existing service/manager pattern for the affected transaction.

For external calls, confirm:

- Timeout, fallback, and exception classification are explicit.
- Request/response logs include correlation IDs and order numbers but mask sensitive fields.
- Callback handlers validate signature, channel identity, order identity, and terminal status transitions before mutating state.

For DB operations, confirm:

- Existing table debt, nullable fields, unique keys, and encrypted columns are checked before changing queries or persistence.
- Schema or backfill work uses the database-migrations skill and includes rollback/validation SQL.

## Verification

Choose the smallest useful verification set:

- Unit tests for request mapping, response/status mapping, signing/encryption helper behavior, and failure branches.
- Integration tests in `trade-web` when the change needs Spring wiring, manager/facade interaction, callback handling, or DB behavior.
- Manual evidence for vendor sandbox calls: sanitized raw request, sanitized raw response, endpoint, environment, request id, and timestamp.
- Regression checks for neighboring channels only when shared base classes, common enums, or shared auth-key logic changed.

Before declaring completion, state the exact commands run, whether any vendor sandbox/manual check was skipped, and which risks remain.

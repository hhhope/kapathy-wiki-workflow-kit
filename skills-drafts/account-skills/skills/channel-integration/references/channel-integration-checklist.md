# Channel Integration Checklist

Use this checklist for new bank/open-bank access work, broad API additions, callbacks, retries, files, signing, or payment-like operations.

## Discovery

- Identify vendor name, bank code, business scenario, endpoint list, callback list, file flows, and environments.
- Record authentication material: app id, merchant/channel platform number, certificates, private key, password, symmetric key, IP whitelist, callback URL, and expiration/rotation rules.
- Capture raw samples for success, business failure, technical failure, pending/processing, duplicate order, timeout, and signature failure.
- Verify data formats: charset, content type, JSON/XML/form/multipart, timestamp format, timezone, decimal precision, field length, enum codes, file encoding, and line endings.
- Check whether an existing package already matches the vendor or business family: `onebank`, `wzbank`, `xwb`, `xsBank`, `pinganOpenbank`, and similar packages are useful starting points.

## Design

- Choose package boundaries before coding:
  - `constant` for endpoint names and vendor constants.
  - `enums` for vendor status/type mappings.
  - `model` or `model.req` / `model.res` for vendor DTOs.
  - `service` for one business API per service class when that matches nearby packages.
  - client/base service for shared signing, HTTP setup, and credential assembly.
- Define the internal-to-vendor mapping in one place per API and keep reverse mapping explicit.
- Decide the source of channel credentials: `ChannelAuthKey`, `otherAuthInfo`, Apollo config, certificate files, or a combination.
- Write down the idempotency key for every submit/write API.
- Define terminal statuses, pending statuses, retryable technical failures, and non-retryable business failures.
- Define callback status transition rules before coding the handler.

## Coding

- Keep request builders deterministic. Avoid hidden defaults that change money, account, identity, or routing fields.
- Mask sensitive logs with reusable masking utilities or local helper methods.
- Validate required vendor fields before invoking the client, and map validation failure to existing project error codes.
- Preserve existing exception style. Do not throw raw vendor SDK exceptions across the channel boundary.
- For files, verify upload/download size limits, content type, file naming, storage location, cleanup, and retry behavior.
- For callbacks, return the vendor-required acknowledgement format only after the local transition is handled or deliberately rejected.

## Tests And Evidence

- Mapping tests:
  - Required fields.
  - Optional fields omitted.
  - Date/time and amount formatting.
  - Enum/status conversion.
- Failure tests:
  - Vendor business failure.
  - Timeout/exception.
  - Unknown status.
  - Duplicate order.
  - Invalid signature callback.
- Persistence tests:
  - Terminal state cannot be overwritten by stale pending callback.
  - Duplicate callback is idempotent.
  - Query compensation updates only the intended order.
- Evidence to preserve in the task notes or PR:
  - Sanitized raw request/response pairs.
  - Test command output.
  - Any skipped sandbox check and reason.
  - Manual config changes required for UAT/prod.

## Release

- Confirm Apollo/config keys, certificate paths, callback URLs, IP whitelist, and vendor environment switch.
- Confirm monitoring: success rate, timeout count, unknown status count, callback signature failure, compensation query count, and file flow errors.
- Confirm rollback: disable route, restore config, revert callback URL, clear unsafe cache only with an explicit key list, and preserve reconciliation evidence.

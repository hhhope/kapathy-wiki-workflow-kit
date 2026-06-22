# Domain — callback-processing

Keywords: payment callback, duplicate callback, duplicate ledger write, idempotent callback, 支付回调, 重复入账, 幂等

Repeated payment callbacks must dedupe before mutation so the same provider event does not double-write ledger state.

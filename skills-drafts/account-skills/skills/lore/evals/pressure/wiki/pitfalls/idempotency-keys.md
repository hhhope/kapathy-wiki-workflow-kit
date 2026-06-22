# Pitfall — idempotency-keys

Keywords: idempotency, duplicate callback, replay, duplicate ledger write, duplicate settlement, 支付回调重复入账, 对账重放, 重复结算

Use stable idempotency keys so repeated callbacks or replays cannot double-write state.

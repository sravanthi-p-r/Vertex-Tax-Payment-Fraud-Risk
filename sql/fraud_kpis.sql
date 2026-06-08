SELECT

COUNT(*) AS total_transactions,

SUM(fraud_flag) AS fraud_transactions,

SUM(chargeback) AS chargebacks,

ROUND(
100.0 * SUM(fraud_flag) / COUNT(*),
2
) AS fraud_rate_pct,

ROUND(
100.0 * SUM(chargeback) / COUNT(*),
2
) AS chargeback_rate_pct

FROM transactions;


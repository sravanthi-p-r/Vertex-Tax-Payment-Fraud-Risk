#Core Fraud KPIs#

SELECT COUNT(*) AS total_transactions, SUM(fraud_flag) AS fraud_transactions, SUM(chargeback) AS chargebacks,ROUND(
100.0 * SUM(fraud_flag) / COUNT(*),
2
) AS fraud_rate_pct, ROUND(
100.0 * SUM(chargeback) / COUNT(*),
2
) AS chargeback_rate_pct FROM transactions;
----------------------------------
#Fraud Rate by Country#

SELECT
country,
COUNT(*) AS total_transactions,
SUM(fraud_flag) AS fraud_transactions,
ROUND(
100.0 * SUM(fraud_flag) / COUNT(*),
2
) AS fraud_rate_pct
FROM transactions
GROUP BY country ORDER BY fraud_rate_pct DESC;
-----------------------------------
# Fraud Rate by Device Type#
  
SELECT device_type,
COUNT(*) AS total_transactions,
SUM(fraud_flag) AS fraud_transactions,
ROUND(
100.0 * SUM(fraud_flag) / COUNT(*),
2
) AS fraud_rate_pct FROM transactions GROUP BY device_type ORDER BY fraud_rate_pct DESC;

----------------------------------
#New vs Existing Customer Fraud#
  
SELECT
CASE WHEN is_new_customer = 1 THEN 'New Customer' ELSE 'Existing Customer'
END AS customer_type, COUNT(*) AS transactions, SUM(fraud_flag) AS fraud_transactions, ROUND(
100.0 * SUM(fraud_flag) / COUNT(*),
2
) AS fraud_rate_pct FROM transactions GROUP BY customer_type;

----------------------------------
#Top Fraud Merchants#
  
SELECT merchant_id, COUNT(*) AS transactions, SUM(fraud_flag) AS fraud_transactions,
ROUND(
100.0 * SUM(fraud_flag) / COUNT(*),
2
) AS fraud_rate_pct FROM transactions GROUP BY merchant_id HAVING COUNT(*) > 50 ORDER BY fraud_rate_pct DESC LIMIT 20;


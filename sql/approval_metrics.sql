#Approval Rate#
  
SELECT
COUNT(*) AS total_transactions,
SUM(approved) AS approved_transactions,
ROUND(
100.0 * SUM(approved) / COUNT(*),
2
) AS approval_rate_pct FROM transactions;

---------------------------------
#Approval Rate by Country#

SELECT
country,
COUNT(*) AS transactions,
SUM(approved) AS approved_transactions,
ROUND(
100.0 * SUM(approved) / COUNT(*),
2
) AS approval_rate_pct
FROM transactions
GROUP BY country
ORDER BY approval_rate_pct DESC;
----------------------------------
#Approval Rate by Device#
  
SELECT device_type,
COUNT(*) AS transactions,
SUM(approved) AS approved_transactions,
ROUND(
100.0 * SUM(approved) / COUNT(*),
2
) AS approval_rate_pct
FROM transactions
GROUP BY device_type
ORDER BY approval_rate_pct DESC;
----------------------------------------------
#Fraud vs Approval Tradeoff#
  
SELECT
CASE
WHEN risk_score < 0.20
THEN 'Low Risk'
WHEN risk_score < 0.50
THEN 'Medium Risk'
ELSE 'High Risk'
END AS risk_segment,
COUNT(*) AS transactions,
ROUND(
100.0 * SUM(approved) / COUNT(*),
2
) AS approval_rate_pct,
ROUND(
100.0 * SUM(fraud_flag) / COUNT(*),
2
) AS fraud_rate_pct
FROM transactions
GROUP BY risk_segment
ORDER BY risk_segment;
-----------------------------------
#Chargebacks Among Approved Transactions#
  
SELECT
COUNT(*) AS approved_transactions,
SUM(chargeback) AS chargebacks,
ROUND(
100.0 * SUM(chargeback) / COUNT(*),
2
) AS chargeback_rate_pct
FROM transactions
WHERE approved = 1;


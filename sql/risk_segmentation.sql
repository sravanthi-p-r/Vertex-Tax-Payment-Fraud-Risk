#Risk Bucket Distribution#
SELECT
CASE
WHEN risk_score < 0.20
THEN '0-20'
WHEN risk_score < 0.40
THEN '20-40'
WHEN risk_score < 0.60
THEN '40-60'
WHEN risk_score < 0.80
THEN '60-80'
ELSE '80-100'
END AS risk_bucket,
COUNT(*) AS transactions
FROM transactions
GROUP BY risk_bucket
ORDER BY risk_bucket;
-------------------------------
#Fraud Rate by Risk Bucket#
  
SELECT
CASE
WHEN risk_score < 0.20
THEN '0-20'
WHEN risk_score < 0.40
THEN '20-40'
WHEN risk_score < 0.60
THEN '40-60'
WHEN risk_score < 0.80
THEN '60-80'
ELSE '80-100'
END AS risk_bucket,
COUNT(*) AS transactions,
SUM(fraud_flag) AS fraud_transactions,
ROUND(
100.0 * SUM(fraud_flag) / COUNT(*),
2
) AS fraud_rate_pct
FROM transactions
GROUP BY risk_bucket
ORDER BY risk_bucket;
--------------------------------------------------
#Approval Rate by Risk Bucket#

SELECT CASE

WHEN risk_score < 0.20
THEN '0-20'
WHEN risk_score < 0.40
THEN '20-40'
WHEN risk_score < 0.60
THEN '40-60'
WHEN risk_score < 0.80
THEN '60-80'
ELSE '80-100'
END AS risk_bucket,
COUNT(*) AS transactions,
ROUND(
100.0 * SUM(approved) / COUNT(*),
2
) AS approval_rate_pct
FROM transactions
GROUP BY risk_bucket
ORDER BY risk_bucket;
----------------------------------------
#Risk Strategy Recommendation Table#
SELECT
CASE
WHEN risk_score < 0.30
THEN 'AUTO_APPROVE'
WHEN risk_score < 0.70
THEN 'MANUAL_REVIEW'
ELSE 'DECLINE'
END AS strategy_action,
COUNT(*) AS transactions,
ROUND(
AVG(risk_score),
4
) AS avg_risk_score,
ROUND(
100.0 * SUM(fraud_flag) / COUNT(*),
2
) AS fraud_rate_pct
FROM transactions
GROUP BY strategy_action;
------------------------------
#Manual Review Queue Size#

SELECT COUNT(*) AS review_queue
FROM transactions
WHERE risk_score BETWEEN 0.30 AND 0.70;

-- Total transactions --

SELECT COUNT(*) AS total_transactions FROM transactions;

-- Total fradulent transactions --

SELECT COUNT(*) AS total_fraud_transactions
 FROM transactions WHERE suspeita = TRUE;

-- Fraud percentage -- 

SELECT (COUNT(*) * 100.0 / (SELECT COUNT(*) FROM transactions))
 AS fraud_percentage FROM transactions WHERE suspeita = TRUE;

-- Average amount --

SELECT ROUND(AVG("Amount"), 2) AS average_amount FROM transactions;

-- Maximum amount --

SELECT MAX("Amount") AS max_amount FROM transactions;

-- Top 10 bigger suspicious transactions --

SELECT "Time", "Amount" FROM transactions WHERE suspeita = TRUE
 ORDER BY "Amount" DESC LIMIT 10;

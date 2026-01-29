# Write your MySQL query statement below
SELECT V.customer_id, 
COUNT(V.visit_id) AS count_no_trans FROM Visits V
LEFT JOIN Transactions t
ON V.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY V.customer_id;
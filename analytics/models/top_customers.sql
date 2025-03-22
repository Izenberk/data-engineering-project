SELECT
    customer_id,
    COUNT(*) AS total_orders,
    SUM(total_value) AS total_spent
FROM {{ref('cleaned_transactions')}}
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10
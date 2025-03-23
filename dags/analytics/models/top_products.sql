SELECT
    product_id,
    SUM(quantity) AS total_sold,
    SUM(total_value) AS revenue
FROM {{ref('cleaned_transactions')}}
GROUP BY product_id
ORDER BY total_sold DESC
LIMIT 10
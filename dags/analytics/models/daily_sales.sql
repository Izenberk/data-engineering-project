SELECT
    order_date,
    COUNT(*) AS total_orders,
    SUM(quantity) AS total_items_sold,
    SUM(total_value) AS total_sales
FROM {{ref('cleaned_transactions')}}
GROUP BY order_date
ORDER BY order_date

SELECT
    order_id,
    customer_id,
    product_id,
    quantity,
    price,
    (quantity * price) AS total_value,
    order_date,
    payment_method
FROM public.ecommerce_transactions
WHERE order_date IS NOT NULL
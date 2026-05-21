-- WarehouseX Optimized SQL Query

SELECT
    orders.order_id,
    customers.customer_name,
    orders.order_date,
    orders.total_amount
FROM
    orders
INNER JOIN
    customers
ON
    orders.customer_id = customers.customer_id
WHERE
    orders.order_date >= CURDATE() - INTERVAL 30 DAY
ORDER BY
    orders.order_date DESC;

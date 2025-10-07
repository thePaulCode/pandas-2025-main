SELECT seller_id,
        sum(price) AS total_revenue,
        count(DISTINCT t1.order_id) AS total_sales
FROM
tb_order_items AS t1
GROUP BY seller_id
ORDER BY total_revenue DESC

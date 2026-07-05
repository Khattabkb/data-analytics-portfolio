-- ============================================================
-- Retail Sales Analysis — SQL query set
-- Author: Khattab Salim
-- Dataset: retail_orders.csv (loaded into table `orders`)
-- ============================================================

-- 1) Headline KPIs: total sales, profit, margin, order count
SELECT
    ROUND(SUM(sales), 2)                              AS total_sales,
    ROUND(SUM(profit), 2)                             AS total_profit,
    ROUND(SUM(profit) / NULLIF(SUM(sales), 0) * 100, 1) AS profit_margin_pct,
    COUNT(*)                                          AS orders,
    ROUND(AVG(sales), 2)                              AS avg_order_value
FROM orders;

-- 2) Monthly sales & profit trend
SELECT
    DATE_TRUNC('month', order_date)  AS month,
    ROUND(SUM(sales), 2)             AS sales,
    ROUND(SUM(profit), 2)            AS profit
FROM orders
GROUP BY 1
ORDER BY 1;

-- 3) Sales & margin by region
SELECT
    region,
    ROUND(SUM(sales), 2)                              AS sales,
    ROUND(SUM(profit), 2)                             AS profit,
    ROUND(SUM(profit) / NULLIF(SUM(sales), 0) * 100, 1) AS margin_pct
FROM orders
GROUP BY region
ORDER BY sales DESC;

-- 4) Discount impact: how average profit changes as discount rises, per category
SELECT
    category,
    discount,
    COUNT(*)              AS orders,
    ROUND(AVG(profit), 2) AS avg_profit_per_order
FROM orders
GROUP BY category, discount
ORDER BY category, discount;

-- 5) Loss-making orders (negative profit) — flag for review
SELECT
    category, sub_category, region, discount,
    ROUND(SUM(sales), 2)  AS sales,
    ROUND(SUM(profit), 2) AS profit,
    COUNT(*)              AS orders
FROM orders
WHERE profit < 0
GROUP BY category, sub_category, region, discount
ORDER BY profit ASC
LIMIT 20;

-- 6) Top sub-categories by profit (ranked within each category)
SELECT category, sub_category, sales, profit, rnk
FROM (
    SELECT
        category, sub_category,
        ROUND(SUM(sales), 2)  AS sales,
        ROUND(SUM(profit), 2) AS profit,
        RANK() OVER (PARTITION BY category ORDER BY SUM(profit) DESC) AS rnk
    FROM orders
    GROUP BY category, sub_category
) t
WHERE rnk <= 3
ORDER BY category, rnk;

-- 7) Customer segment contribution
SELECT
    segment,
    ROUND(SUM(sales), 2)                              AS sales,
    ROUND(100.0 * SUM(sales) / SUM(SUM(sales)) OVER (), 1) AS pct_of_sales
FROM orders
GROUP BY segment
ORDER BY sales DESC;


-- ==========================================
-- RETAIL SALES BUSINESS ANALYTICS
-- Database: retail_sales.db
-- Table: sales
-- ==========================================


-- QUERY 1: Revenue by product category

SELECT
    category,
    SUM(quantity) AS total_units_sold,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY category
ORDER BY total_revenue DESC;


-- QUERY 2: Top 5 best-selling products

SELECT
    product,
    SUM(quantity) AS total_quantity_sold,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_quantity_sold DESC
LIMIT 5;


-- QUERY 3: Monthly revenue trends

SELECT
    strftime('%Y-%m', order_date) AS sales_month,
    SUM(revenue) AS monthly_revenue
FROM sales
GROUP BY sales_month
ORDER BY sales_month;


-- QUERY 4: Revenue by region

SELECT
    region,
    COUNT(order_id) AS total_orders,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC;


-- QUERY 5: Top 5 customers by spending

SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    SUM(revenue) AS total_spending
FROM sales
GROUP BY customer_id
ORDER BY total_spending DESC
LIMIT 5;

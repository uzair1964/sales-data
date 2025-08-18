-- Select the Retail_Sale database.
USE Retail_Sale;

-- Create the sales table to store transaction data.
CREATE TABLE sales (
    transaction_id INT,
    sale_date DATE,
    customer_id VARCHAR(20),
    gender VARCHAR(20),
    age INT,
    product_category VARCHAR(20),
    quantity INT,
    price_per_unit INT,
    total_amount INT,
    total_price INT
);

-- Retrieve the top 10 customers by total spending.
SELECT
    *
FROM
    sales
ORDER BY
    total_price DESC
LIMIT 10;

-- Calculate total sales by product category.
SELECT
    product_category,
    SUM(total_price) AS total_sales
FROM
    sales
GROUP BY
    product_category;

-- Find the month with the highest sales.
SELECT
    MONTH(sale_date) AS sale_month,
    SUM(total_price) AS total_sales
FROM
    sales
GROUP BY
    MONTH(sale_date)
ORDER BY
    SUM(total_price) DESC
LIMIT 1;

-- Compute the average order value per customer.
SELECT
    customer_id,
    AVG(total_price) AS avg_order_value
FROM
    sales
GROUP BY
    customer_id;

USE Retail_Sale;

CREATE TABLE sales(Transaction_ID INT, Date_ DATE, Customer_ID VARCHAR(20), Gender VARCHAR(20), Age INT, Product_Category VARCHAR(20), Quantity INT, Price_per_Unit INT, Total_Amount INT, TotalPrice INT);

-- 1. Top 10 customers by total spending.
SELECT
        Customer_ID,
        SUM(TotalPrice) AS total_spent
FROM
        Sales
GROUP BY
        Customer_ID
ORDER BY
        total_spent DESC
LIMIT 10;

-- 2. Total sales by Product category.
Select
	Product_Category,
    SUM(TotalPrice)
FROM
	Sales
GROUP BY
	Product_Category;

-- 3. Find the month with the highest sales.
SELECT
	MONTH(Date_),
    SUM(TotalPrice)
FROM
	Sales
GROUP BY
	MONTH(Date_)
ORDER BY
	SUM(TotalPrice) DESC
LIMIT 1;

-- 4. Average order value per customer.
SELECT
	Customer_ID,
    AVG(TotalPrice)
FROM
	Sales
GROUP BY
        Customer_ID;

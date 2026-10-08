-- Sales Analytics SQL Practice

-- 1. Total net sales
SELECT SUM(Net_Sales_INR) AS total_net_sales
FROM sales_data;

-- 2. Sales by region
SELECT Region, SUM(Net_Sales_INR) AS sales
FROM sales_data
GROUP BY Region
ORDER BY sales DESC;

-- 3. Profit by category
SELECT Category, SUM(Profit_INR) AS profit
FROM sales_data
GROUP BY Category
ORDER BY profit DESC;

-- 4. Monthly sales
SELECT SUBSTR(Order_Date, 1, 7) AS month,
       SUM(Net_Sales_INR) AS sales
FROM sales_data
GROUP BY SUBSTR(Order_Date, 1, 7)
ORDER BY month;

-- 5. Return rate by category
SELECT Category,
       AVG(CASE WHEN Returned = 'Yes' THEN 1.0 ELSE 0.0 END) * 100 AS return_rate
FROM sales_data
GROUP BY Category
ORDER BY return_rate DESC;

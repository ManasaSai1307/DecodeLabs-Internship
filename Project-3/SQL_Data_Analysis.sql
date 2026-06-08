--View all data
SELECT * FROM "CleanedData";

--Count Total Orders
SELECT COUNT(*) AS Total_Orders
FROM "CleanedData";

--Product Wise Renvenue
SELECT Product,
SUM(TotalPrice) AS Revenue
FROM "CleanedData"
GROUP BY Product
ORDER BY Revenue DESC;

--Total Revenue
SELECT SUM(TotalPrice) AS Total_Revenue
FROM "CleanedData";

--Order Status Analysis
SELECT OrderStatus,
COUNT(*) AS Total_Orders
FROM "CleanedData"
GROUP BY OrderStatus;

--Payment Method Analysis
SELECT PaymentMethod,
COUNT(*) AS Usage_Count
FROM "CleanedData"
GROUP BY PaymentMethod
ORDER BY Usage_Count DESC;

--Referral Source Analysis
SELECT ReferralSource,
COUNT(*) AS Orders
FROM "CleanedData"
GROUP BY ReferralSource
ORDER BY Orders DESC;

--Coupon Analysis
SELECT CouponCode,
COUNT(*) AS Usage_Count
FROM "CleanedData"
GROUP BY CouponCode
ORDER BY Usage_Count DESC;

--Find Delivered Orders Only
SELECT *
FROM "CleanedData"
WHERE OrderStatus = 'Delivered';

--Quantity Sold By Product
SELECT Product,
SUM(Quantity) AS Total_Quantity_Sold
FROM "CleanedData"
GROUP BY Product
ORDER BY Total_Quantity_Sold DESC;

--Most Popular Product
SELECT Product,
COUNT(*) AS Orders
FROM "CleanedData"
GROUP BY Product
ORDER BY Orders DESC;

--Most Used Payment method
SELECT PaymentMethod,
COUNT(*) AS Usage_Count
FROM "CleanedData"
GROUP BY PaymentMethod
ORDER BY Usage_Count DESC;

--Most Used Coupon
SELECT CouponCode,
COUNT(*) AS Usage_Count
FROM "CleanedData"
GROUP BY CouponCode
ORDER BY Usage_Count DESC;

--Revenue By Payment Method
SELECT PaymentMethod,
SUM(TotalPrice) AS Revenue
FROM "CleanedData"
GROUP BY PaymentMethod
ORDER BY Revenue DESC;

--Revenue By Referral Source
SELECT ReferralSource,
SUM(TotalPrice) AS Revenue
FROM "CleanedData"
GROUP BY ReferralSource
ORDER BY Revenue DESC;

--Search Specific Product
SELECT *
FROM "CleanedData"
WHERE Product = 'Monitor';

--Revenue Statistics in One Query
SELECT
COUNT(*) AS Total_Orders,
SUM(TotalPrice) AS Total_Revenue,
AVG(TotalPrice) AS Average_Order_Value,
MAX(TotalPrice) AS Highest_Order,
MIN(TotalPrice) AS Lowest_Order
From "CleanedData";
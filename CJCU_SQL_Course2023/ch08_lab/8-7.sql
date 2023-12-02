USE ch08_lab

-- (1)在「員工表」中查詢目前公司總人數

SELECT COUNT(*) AS totalPeople FROM Employee

-- totalPeople
-- 5

-- (2)在「銷售表」中查詢員工銷售產品的「筆數」

SELECT COUNT(*) AS totalSales FROM Sales

-- totalSales
-- 10

-- (3)在「Sales銷售表」中計算每一位員工所銷售產品的平均數量

SELECT AVG(Quan) AS AverageQuan FROM Sales
GROUP BY S_id

-- AverageQuan
-- 64
-- 77
-- 81
-- 77
-- 95

-- (4)在「銷售表」中查詢有銷售產品之「品號為 P0005」的總數量

SELECT SUM(Quan) AS totalP0005 FROM Sales
WHERE P_id = 'P0005'

-- totalP0005
-- 369

-- (5)在「銷售表」中查詢有銷售產品之「品號為 P0005」的最高數量

SELECT MAX(Quan) AS MaxQuanP0005 FROM Sales
WHERE P_id = 'P0005'

-- MaxQuanP0005
-- 95
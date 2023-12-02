USE ch08_lab

-- (1)在「銷售表」中，查詢每一位員工各銷售幾種產品。

SELECT S_id, COUNT(*) AS totalSales FROM Sales
GROUP BY S_id

-- S_id     totalSales
-- S0001    2
-- S0002    2
-- S0003    2
-- S0004    3
-- S0005    1

-- (2)在「銷售表」中計算每一位員工銷售之產品的平均數量

SELECT S_id, AVG(Quan) AS AverageQuan FROM Sales
GROUP BY S_id

-- S_id     AverageQuan
-- S0001    64
-- S0002    77
-- S0003    81
-- S0004    77
-- S0005    95

-- (3)在「銷售表」中，統計出每一種產品被多少員工來銷售，印出之結果並按「品號」由大到小排序

SELECT P_id, COUNT(*) AS totalSalesPeople FROM Sales
GROUP BY P_id
ORDER BY P_id DESC

-- P_id     totalSalesPeople
-- P0005    5
-- P0004    2
-- P0003    1
-- P0002    1
-- P0001    1

-- (4)在「銷售表」中，統計出每一種產品被多少員工來銷售及該產品最高數量印出來， 印出之結果並按「品號」由小到大排序

SELECT P_id, COUNT(*) AS totalSalesPeople, MAX(Quan) AS MaxQuan FROM Sales
GROUP BY P_id
ORDER BY P_id ASC

-- P_id    totalSalesPeople    MaxQuan
-- P0001           1           56
-- P0002           1           92
-- P0003           1           75
-- P0004           2           92
-- P0005           5           95

-- (5)在「銷售表」中，統計出每一種產品被多少員工來銷售及該產品平均數量印出來， 印出之結果並按「品號」由小到大排序

SELECT P_id, COUNT(*) AS totalSalesPeople, AVG(Quan) AS AverageQuan FROM Sales
GROUP BY P_id
ORDER BY P_id ASC

-- P_id    totalSalesPeople    AverageQuan
-- P0001           1           56
-- P0002           1           92
-- P0003           1           75
-- P0004           2           90
-- P0005           5           73
USE ch08_lab

-- (1)在「銷售表」中，計算銷售產品的平均數量，大於等於 70 者顯示出來

SELECT S_id, AVG(Quan) AS AverageQuan FROM Sales
GROUP BY S_id
HAVING AVG(Quan) >= 70

-- S_id    AverageQuan
-- S0002   77
-- S0003   81
-- S0004   77
-- S0005   95

-- (2)在「銷售表」中，將銷售產品種類在二種及二種以上的員工編號資料列出來

SELECT S_id, COUNT(*) AS totalSales FROM Sales
GROUP BY S_id
HAVING COUNT(*) >= 2

-- S_id    totalSales
-- S0001   2
-- S0002   2
-- S0003   2
-- S0004   3
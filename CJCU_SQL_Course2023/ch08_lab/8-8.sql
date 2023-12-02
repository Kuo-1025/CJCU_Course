USE ch08_lab

-- (1)在「銷售表」中查詢全部銷售數量，由低到高排序

SELECT S_id, P_id, Quan AS ASCQuan FROM Sales
ORDER BY Quan ASC

-- S_id     P_id     ASCQuan
-- S0001    P0001    56
-- S0002    P0005    63
-- S0004    P0005    68
-- S0003    P0005    70
-- S0001    P0005    73
-- S0004    P0003    75
-- S0004    P0004    88
-- S0002    P0002    92
-- S0003    P0004    92
-- S0005    P0005    95

-- (2)在「銷售表」中查詢全部銷售數量，由高到低排序

SELECT S_id, P_id, Quan AS DESCQuan FROM Sales
ORDER BY Quan DESC

-- S_id     P_id    Quan
-- S0005    P0005    95
-- S0002    P0002    92
-- S0003    P0004    92
-- S0004    P0004    88
-- S0004    P0003    75
-- S0001    P0005    73
-- S0003    P0005    70
-- S0004    P0005    68
-- S0002    P0005    63
-- S0001    P0001    56

-- (3)在「銷售表」中查詢結果按照編號升冪排列之後，再依數量升冪排列

SELECT S_id AS ASC_S_id, P_id, Quan AS ASCQuan FROM Sales
ORDER BY S_id ASC, Quan ASC

-- ASC_S_id  P_id      ASCQuan
-- S0001     P0001     56
-- S0001     P0005     73
-- S0002     P0005     63
-- S0002     P0002     92
-- S0003     P0005     70
-- S0003     P0004     92
-- S0004     P0005     68
-- S0004     P0003     75
-- S0004     P0004     88
-- S0005     P0005     95
USE ch08_lab

-- 在「銷售表Sales」中查詢哪些員工至少都有去銷售產品的「編號、品號及數量」(提示: 使用 Null)

SELECT * FROM Sales
WHERE Quan IS NOT NULL

-- S_id     P_id    Quan
-- S0001    P0001    56
-- S0001    P0005    73
-- S0002    P0002    92
-- S0002    P0005    63
-- S0003    P0004    92
-- S0003    P0005    70
-- S0004    P0003    75
-- S0004    P0004    88
-- S0004    P0005    68
-- S0005    P0005    95
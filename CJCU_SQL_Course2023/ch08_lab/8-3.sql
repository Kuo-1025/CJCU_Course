USE ch08_lab

-- Or ( 或 )：在「銷售表Sales」中查詢員工任銷售一種產品之「品號為 P0001 或品號為 P0005」的員工的「編號、品號及數量」

SELECT * FROM Sales
WHERE P_id = 'P0001' OR P_id = 'P0005'

-- S_id     P_id     Quan
-- S0001    P0001    56
-- S0001    P0005    73
-- S0002    P0005    63
-- S0003    P0005    70
-- S0004    P0005    68
-- S0005    P0005    95
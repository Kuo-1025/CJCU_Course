USE ch08_lab

-- 在Sales(銷售表)中查詢P_id為「P0005」的員工的「S_id(編號)及Quan(數量)」

SELECT S_id, Quan FROM Sales
WHERE P_id = 'P0005'

-- S_id     Quan
-- S0001    73
-- S0002    63
-- S0003    70
-- S0004    68
-- S0005    95
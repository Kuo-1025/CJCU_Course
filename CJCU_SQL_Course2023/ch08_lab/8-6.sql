USE ch08_lab

-- Between範圍條件：在「Sales銷售表」中查詢，P_id (品號)為 P0001 或 P0005 的 Quan(數量) 60 到 90 之間的員工的 S_id,P_id,Quan(編號、品號及數量)

SELECT * FROM Sales
WHERE P_id IN ('P0001', 'P0005') AND Quan BETWEEN 60 AND 90

-- S_id     P_id     Quan
-- S0001    P0005    73
-- S0002    P0005    63
-- S0003    P0005    70
-- S0004    P0005    68
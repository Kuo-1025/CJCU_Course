USE ch09_lab;

SELECT * FROM Employee AS E INNER JOIN Sales AS S
ON E.P_id=S.P_id;

-- Em_id    E_name    P_id     p-name  Quan
-- S0001     一心     P0001     筆電     3
-- S0002     二聖     P0002     滑鼠     3
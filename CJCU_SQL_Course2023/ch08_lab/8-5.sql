USE ch08_lab

-- Like 模糊相似條件：在「Employee」中查詢「部門Em_dep」開頭為「生」的員工基本資料

SELECT * FROM Employee
WHERE Em_dep LIKE '生%'

-- Em_id      Em_name   Em_dep
-- S0002      二聖      生產部
-- S0004      四維      生產部
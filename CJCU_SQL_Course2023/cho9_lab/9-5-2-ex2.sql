USE ch09_lab;

SELECT T.T_id, T.T_name FROM Teacher AS T LEFT OUTER JOIN Course AS C
ON T.T_id=C.T_id
WHERE C.C_id IS NULL;

-- T_id     T_name
-- T0003     三多
-- T0004     四維
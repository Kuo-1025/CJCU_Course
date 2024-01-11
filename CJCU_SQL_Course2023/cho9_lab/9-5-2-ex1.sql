USE ch09_lab;

SELECT * FROM Teacher LEFT OUTER JOIN Course
ON Teacher.T_id=Course.T_id

-- T_id     T_name    C_id      C_name      T_id
-- T0001     一心     P0001     資料庫       T0001
-- T0002     二聖     P0002     資料結構     T0002
-- T0003     三多     NULL      NULL         NULL
-- T0004     四維     NULL      NULL         NULL
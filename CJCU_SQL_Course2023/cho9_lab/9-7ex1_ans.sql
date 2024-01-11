USE ch09_lab;

SELECT * FROM Stu_grade
WHERE db > (SELECT AVG(db) FROM Stu_grade)

-- st-id   st_name    db      ds     prog
-- S0001     一心     100     85      80
-- S0003     三多     85      75      80
-- S0004     四維     95      100     100
-- S0005     五福     80      65      70
USE ch09_lab;

SELECT * FROM Stu_grade
WHERE db=(SELECT MAX(db) FROM Stu_grade)

-- st-id   st_name    db      ds     prog
-- S0001     一心     100     85      80
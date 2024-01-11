USE ch09_lab;

CREATE TABLE Stu_grade (
    st_id CHAR(5),
    st_name CHAR(4) NOT NULL,
    db INT,
    ds INT,
    prog INT,
    PRIMARY KEY(st_id)
)
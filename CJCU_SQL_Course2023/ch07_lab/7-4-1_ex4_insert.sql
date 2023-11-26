USE ch07_lab

CREATE TABLE Employee_OLD (
    Em_id CHAR(5),
	Em_name NVARCHAR(10) NOT NULL,
	Em_dep NVARCHAR(10) NULL,
	gender NCHAR(1),
	PRIMARY KEY(Em_id)
)

INSERT INTO Employee_OLD VALUES
('S0006', '六和', '銷售部', '女'),
('S0007', '七賢', '銷售部', '女'),
('S0008', '八德', '生產部', '男'),
('S0009', '九如', '生產部', '女'),
('S0010', '十全', '生產部', '男')

-- In order to add the "Employee_Old" table to "Employee" table
-- We add column "gender" in table "Employee"

ALTER TABLE Employee
ADD gender NCHAR(1) Default '男' WITH VALUES

-- We only updated the names of "三多" and "五福"
-- Because other gender are defaulted to '男'

UPDATE Employee
SET gender = '女'
WHERE Em_name = '三多' OR Em_name = '五福'

-- Then we add "Employee_OLD" table to "Employee" table

INSERT INTO Employee
SELECT * FROM Employee_OLD
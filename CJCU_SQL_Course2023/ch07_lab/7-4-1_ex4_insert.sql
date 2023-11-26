USE ch07_lab

CREATE TABLE Employee_OLD (
    Em_id CHAR(5),
	Em_name NVARCHAR(10) NOT NULL,
	Em_dep NVARCHAR(10) NULL,
	gender NCHAR(1),
	PRIMARY KEY(Em_id)
)

INSERT INTO Employee_OLD VALUES
('S0006', '���M', '�P�ⳡ', '�k'),
('S0007', '�C��', '�P�ⳡ', '�k'),
('S0008', '�K�w', '�Ͳ���', '�k'),
('S0009', '�E�p', '�Ͳ���', '�k'),
('S0010', '�Q��', '�Ͳ���', '�k')

-- In order to add the "Employee_Old" table to "Employee" table
-- We add column "gender" in table "Employee"

ALTER TABLE Employee
ADD gender NCHAR(1) Default '�k' WITH VALUES

-- We only updated the names of "�T�h" and "����"
-- Because other gender are defaulted to '�k'

UPDATE Employee
SET gender = '�k'
WHERE Em_name = '�T�h' OR Em_name = '����'

-- Then we add "Employee_OLD" table to "Employee" table

INSERT INTO Employee
SELECT * FROM Employee_OLD
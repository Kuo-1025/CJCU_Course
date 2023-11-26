USE ch07_lab

-- 資料表建立的順序：假設現在有一套「選課系統」，其相關的欄位如下所示：
-- (學號、姓名、年級、科系代碼、科系名稱、系主任、課程代號、課程名稱、學分數、成績、老師編號、老師姓名)

-- 利用SQL之DDL來建立3NF後的所有資料表時，請列出建立的順序。(注意：要依照父關聯表與子關聯表的順序來建立)

-- 1.

CREATE TABLE Department (
	Dep_code CHAR(5),
	Dep_name NVARCHAR(10) NOT NULL,
	Dep_chair NVARCHAR(10),
	PRIMARY KEY(Dep_code)
)

-- 2.

CREATE TABLE Teacher (
    Teacher_id CHAR(5),
    Teacher_name NVARCHAR(10) NOT NULL,
    Dep_code CHAR(5),
    PRIMARY KEY(Teacher_id),
    FOREIGN KEY(Dep_code) REFERENCES Department ON UPDATE CASCADE ON DELETE CASCADE
)

CREATE TABLE Student (
Stu_id CHAR(5),
Stu_name NVARCHAR(10) NOT NULL,
gender NCHAR(1),
Dep_code CHAR(5),
PRIMARY KEY(Stu_id),
FOREIGN KEY(Dep_code) REFERENCES Department ON UPDATE CASCADE ON DELETE CASCADE
)

-- 3.

CREATE TABLE Course (
Course_id CHAR(5),
Course_name NVARCHAR(10) NOT NULL,
Credits INT NOT NULL,
Dep_code CHAR(5),
Teacher_id CHAR(5),
PRIMARY KEY(Course_id),
FOREIGN KEY(Dep_code) REFERENCES Department ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(Teacher_id) REFERENCES Teacher ON UPDATE NO ACTION ON DELETE NO ACTION
)

-- 4.

CREATE TABLE Grades (
Stu_id CHAR(5),
Course_id CHAR(5),
Grade INT NOT NULL,
PRIMARY KEY(Stu_id, Course_id),
FOREIGN KEY(Stu_id) REFERENCES Student ON UPDATE CASCADE ON DELETE CASCADE,
FOREIGN KEY(Course_id) REFERENCES Course(Course_id) ON UPDATE NO ACTION ON DELETE NO ACTION
)
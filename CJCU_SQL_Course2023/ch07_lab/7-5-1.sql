USE ch07_lab

-- ��ƪ�إߪ����ǡG���]�{�b���@�M�u��Ҩt�Ρv�A����������p�U�ҥܡG
-- (�Ǹ��B�m�W�B�~�šB��t�N�X�B��t�W�١B�t�D���B�ҵ{�N���B�ҵ{�W�١B�Ǥ��ơB���Z�B�Ѯv�s���B�Ѯv�m�W)

-- �Q��SQL��DDL�ӫإ�3NF�᪺�Ҧ���ƪ�ɡA�ЦC�X�إߪ����ǡC(�`�N�G�n�̷Ӥ����p��P�l���p�����Ǩӫإ�)

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
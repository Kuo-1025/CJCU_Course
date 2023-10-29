USE MySchoolDB

CREATE TABLE Employee2
(
    Em_id CHAR(5),
	Em_name NVARCHAR(4) NOT NULL,
	sex CHAR(4) NULL,
	PRIMARY KEY(Em_id)
)

CREATE TABLE performance
(
    Em_id CHAR(5),
	Q1 int,
	Q2 int,
	PRIMARY KEY(Em_id),
	FOREIGN KEY(Em_id) REFERENCES Employee2(Em_id)
)
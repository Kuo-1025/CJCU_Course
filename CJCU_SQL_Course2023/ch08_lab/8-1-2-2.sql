﻿USE ch08_lab

CREATE TABLE Product (
    P_id CHAR(5),
    P_name NVARCHAR(10) NOT NULL,
    Price INT,
    PRIMARY KEY(P_id)
)
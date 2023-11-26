USE ch07_lab

-- 資料表建立的順序(實作)：請利用DDL語言來定義一個客戶訂購產品的關聯式如下所示：

-- 客戶檔 (客戶代號、姓名、電話、傳真)
-- 訂單檔 (訂單代號、訂單日期、客戶代號(FK))
-- 訂單細檔 (訂單代號(FK)、產品代號(FK)、數量)
-- 產品檔 (產品代號、品名、單價)

--1.

CREATE TABLE Costumer (
    Costumer_id CHAR(5),
    Costumer_name NVARCHAR(10) NOT NULL,
    Phone NVARCHAR(20) NULL,
    Fax NVARCHAR(20) NULL,
	PRIMARY KEY(Costumer_id)
)

CREATE TABLE Product (
    P_id CHAR(5),
    P_name NVARCHAR(10) NOT NULL,
    Price INT NOT NULL,
    PRIMARY KEY(P_id)
)

-- 2.

CREATE TABLE Order_file (
    Order_id CHAR(5),
    Order_date DATETIME NOT NULL, -- Format -> YYYY-MM-DD hh:mm:ss.sss
    Costumer_id CHAR(5) NOT NULL,
    PRIMARY KEY(Order_id),
    FOREIGN KEY(Costumer_id) REFERENCES Costumer ON UPDATE NO ACTION ON DELETE NO ACTION
)

-- 3.

CREATE TABLE Order_detail (
    Order_id CHAR(5),
	P_id CHAR(5),
	OrderAmount INT NOT NULL,
	PRIMARY KEY(Order_id, P_id),
	FOREIGN KEY(Order_id) REFERENCES Order_file ON UPDATE NO ACTION ON DELETE NO ACTION,
	FOREIGN KEY(P_id) REFERENCES Product ON UPDATE NO ACTION ON DELETE NO ACTION
)
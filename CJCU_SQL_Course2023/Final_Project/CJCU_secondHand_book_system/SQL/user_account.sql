CREATE TABLE user_account (
    U_id INT AUTO_INCREMENT,
    U_name VARCHAR(50) UNIQUE NOT NULL,
    U_gender VARCHAR(5) NULL,
    U_p4sswd VARCHAR(255) NOT NULL,
    PRIMARY KEY(U_id)
);
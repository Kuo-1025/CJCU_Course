CREATE TABLE product (
    B_id INT AUTO_INCREMENT,
    B_name VARCHAR(100) NOT NULL,
    B_category VARCHAR(20) NOT NULL,
    B_author VARCHAR(50) NOT NULL,
    B_description VARCHAR(500) NULL,
    B_price INT NOT NULL,
    B_quantity INT NOT NULL,
    S_id INT NOT NULL,
    PRIMARY KEY(B_id),
    FOREIGN KEY(S_id) REFERENCES user_account(U_id)
);
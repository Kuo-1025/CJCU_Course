CREATE TABLE cart_item (
    id INT AUTO_INCREMENT,
    B_id INT NOT NULL,
    B_quantity INT NOT NULL,
    U_id INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(B_id) REFERENCES product(B_id) ,
    FOREIGN KEY(U_id) REFERENCES user_account(U_id)
);
CREATE DATABASE IF NOT EXISTS my_shop;

USE my_shop;

CREATE TABLE IF NOT EXISTS products
(
    id            int          NOT NULL AUTO_INCREMENT,
    name          varchar(128) NOT NULL,
    description   TEXT NOT NULL,
    price         decimal(10,2) NOT NULL,
    PRIMARY KEY (id)
) ENGINE=INNODB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO products (name, description, price)
VALUES ('Cookies', 'Box of Cookies, 400g', 4.99);

INSERT INTO products (name, description, price)
VALUES ('Twix', 'Chocolate Bar, 200g', 2.99);

INSERT INTO products (name, description, price)
VALUES ('Worms', 'Candy, 100g', 1.99);

INSERT INTO products (name, description, price)
VALUES ('Lays', 'Potato Chips, 100g', 1.97);

INSERT INTO products (name, description, price)
VALUES ('Caramel Popcorn', 'Popcorn Bag, 500g', 5.52);

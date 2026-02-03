-- =========================
-- POS DATABASE SCHEMA
-- =========================
-- Engine: MySQL / MariaDB
-- Charset: utf8mb4
-- Purpose: POS MVP (products, sales, stock)
-- =========================

SET sql_mode='STRICT_TRANS_TABLES';
SET time_zone='+00:00';

START TRANSACTION;

-- =========================
-- PRODUCTS
-- =========================
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock DECIMAL(10,3) NOT NULL DEFAULT 0,
    unit ENUM('kg', 'unit', 'pack') NOT NULL,

    is_active BOOLEAN NOT NULL DEFAULT TRUE,

    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- =========================
-- SALES (TICKETS)
-- =========================
CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,

    total DECIMAL(10,2) NOT NULL,
    payment_method ENUM('cash', 'card', 'qr') NOT NULL,

    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- =========================
-- SALE ITEMS (LINES)
-- =========================
CREATE TABLE sale_items (
    id INT AUTO_INCREMENT PRIMARY KEY,

    sale_id INT NOT NULL,
    product_id INT NOT NULL,

    quantity DECIMAL(10,3) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_sale_items_sale
        FOREIGN KEY (sale_id)
        REFERENCES sales(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_sale_items_product
        FOREIGN KEY (product_id)
        REFERENCES products(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB;

COMMIT;
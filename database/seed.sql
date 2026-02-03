-- =========================
-- POS SEED DATA
-- =========================
-- Purpose: Development & testing
-- Safe to re-run after TRUNCATE
-- =========================

START TRANSACTION;

SET FOREIGN_KEY_CHECKS=0;

TRUNCATE TABLE sale_items;
TRUNCATE TABLE sales;
TRUNCATE TABLE products;

SET FOREIGN_KEY_CHECKS=1;

INSERT INTO products (name, price, stock, unit) VALUES
('Almonds',        5000.00, 25.000, 'kg'),
('Walnuts',        4200.00, 18.500, 'kg'),
('Cashews',        6200.00, 12.750, 'kg'),
('Peanuts',        1800.00, 40.000, 'kg'),
('Raisins',        2300.00, 30.250, 'kg');

-- =========================
-- PRODUCTS (UNIT-BASED)
-- =========================
INSERT INTO products (name, price, stock, unit) VALUES
('Protein Bar',     900.00, 120.000, 'unit'),
('Granola Pack',   1500.00,  60.000, 'unit'),
('Honey Jar 500g', 2800.00,  25.000, 'unit'),
('Peanut Butter',  3500.00,  20.000, 'unit');

COMMIT;
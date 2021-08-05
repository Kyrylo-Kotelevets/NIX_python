-- Придумать 3 запроса, которые можно оптимизировать с помощью индекса и оптимизировать их используя индекс.
-- (проверять стоит ли оптимизировать запрос оператором explain)
-- Результат проверять также оператором explain.


-- cost without index: 0.00..155.00
-- cost with index:   12.21..126.87
EXPLAIN SELECT *
FROM products
WHERE in_stock > 40;

CREATE INDEX big_amount_in_stock ON products(in_stock) WHERE in_stock > 40;
DROP INDEX IF EXISTS big_amount_in_stock;


-- cost without index: 0.00..165.00
-- cost with index:   25.60..145.83
EXPLAIN SELECT *
FROM products
WHERE price BETWEEN 125.00 AND 175.00;

CREATE INDEX products_with_price_in_range_125_175 ON products(price) WHERE price BETWEEN 125.00 AND 175.00;
DROP INDEX IF EXISTS products_with_price_in_range_125_175;


-- cost without index: 0.00..47.50
-- cost with index:    4.19..21.20
EXPLAIN SELECT *
FROM orders
WHERE EXTRACT(YEAR FROM created_at) = 2020;

CREATE INDEX orders_created_in_2020 ON orders(created_at) WHERE EXTRACT(YEAR FROM created_at) = 2020;
DROP INDEX IF EXISTS orders_created_in_2020;


SELECT indexname, indexdef
FROM pg_indexes
WHERE tablename = 'products';

SELECT tablename, indexname, indexdef
FROM pg_indexes
WHERE schemaname = 'public' AND indexname NOT LIKE '%_pkey'
ORDER BY tablename, indexname;

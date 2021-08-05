-- Написать 2 любые хранимые процедуры.

-- first procedure
DROP TABLE products_backup;
CREATE TABLE products_backup AS TABLE products;

CREATE OR REPLACE PROCEDURE sqrt_prices()
LANGUAGE plpgsql
AS $$
BEGIN
	UPDATE products_backup
	SET price = ROUND(SQRT(price)::numeric, 2);
	COMMIT;
END; $$;
DROP PROCEDURE sqrt_prices;

CALL sqrt_prices();

SELECT *
FROM products_backup;


-- second_procedure
CREATE OR REPLACE PROCEDURE replace_old_orders(min_date timestamp)
LANGUAGE plpgsql
AS $$
BEGIN
	-- Creating a new table for old orders
	CREATE TABLE IF NOT EXISTS orders_history
		AS TABLE orders WITH NO DATA;

	-- Inserting old orders into history table
	INSERT INTO orders_history
		SELECT * FROM orders
		WHERE created_at < min_date;

	-- Deleting old orders
	DELETE FROM orders
	WHERE created_at < min_date;

	COMMIT;
END; $$;

CALL replace_old_orders('2018-01-01');

-- 2017-12-31 00:00:00
SELECT max(created_at)
FROM orders_history;

-- 2018-01-01 00:00:00
SELECT min(created_at)
FROM orders;

-- Написать представление для таблицы products, для таблиц order_status и order, для таблиц products и category


-- view for products table
CREATE OR REPLACE VIEW top10_expensive_products AS
	SELECT *
	FROM products
	ORDER BY price DESC
	LIMIT 10;
SELECT * FROM top10_expensive_products;
DROP VIEW top10_expensive_products;


-- view for orders and order_status tables
CREATE VIEW order_with_status AS
	SELECT *
	FROM orders JOIN order_status
		ON order_status_order_status_id = order_status_id
SELECT * FROM order_with_status;
DROP VIEW order_with_status;


-- materialized view for products and category tables
CREATE MATERIALIZED VIEW products_with_price_deviation_from_category_avg AS
	SELECT product_id, category_id, price,
		AVG(price) OVER (PARTITION BY category_id),
		ABS(AVG(price) OVER (PARTITION BY category_id) - price) as dev
	FROM products JOIN categories
		USING (category_id)
	ORDER BY dev DESC;
SELECT * FROM products_with_price_deviation_from_category_avg;
DROP VIEW products_with_price_deviation_from_category_avg;

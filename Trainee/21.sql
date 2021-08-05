-- Создать функцию, которая сетит shipping_total = 0 в таблице order, если город юзера равен x. Использовать IF clause.


CREATE OR REPLACE FUNCTION set_shipping_total_zero_by_user_sity (user_city varchar)
	RETURNS void
	LANGUAGE plpgsql
AS $$
BEGIN
	UPDATE orders
	SET shipping_total = 0
	WHERE order_id IN
	(
		SELECT order_id
		FROM users
			JOIN carts ON user_id = users_user_id
			JOIN orders ON cart_id = carts_cart_id
		WHERE city = user_city
	);

	IF NOT FOUND THEN
		RAISE 'CITY "%" NOT FOUND ERROR', user_city;
	END IF;
END; $$;

SELECT set_shipping_total_zero_by_user_sity('city 1488');
SELECT set_shipping_total_zero_by_user_sity('city 1452588');


SELECT shipping_total, first_name, last_name, city
FROM users
	JOIN carts ON user_id = users_user_id
	JOIN orders ON cart_id = carts_cart_id
WHERE city = 'city 1488';

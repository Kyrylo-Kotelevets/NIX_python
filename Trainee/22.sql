-- Сравнить цену каждого продукта n с средней ценой продуктов в категории продукта n. Использовать window function.
-- Таблица результата должна содержать такие колонки: category_title, product_title, price, avg.


SELECT category_tittle, product_title, price, AVG(price) OVER (PARTITION BY category_tittle)
FROM products JOIN categories
    USING (category_id);

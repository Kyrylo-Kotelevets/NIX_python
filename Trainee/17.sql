-- Использовать транзакции для insert, update, delete на 3х таблицах.


-- first procedure
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

INSERT INTO order_status VALUES (6, 'Stolen');

SAVEPOINT jesus_help_me;
INSERT INTO order_status VALUES (7, 'blessed');
ROLLBACK TO SAVEPOINT jesus_help_me;

COMMIT;


-- second procedure
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

UPDATE products SET price = 199.99 WHERE price >= 200;

ROLLBACK;


-- third procedure
BEGIN;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

DELETE FROM orders WHERE total >= 1571;

SAVEPOINT bonus_life;
DELETE FROM orders WHERE total >= 1000;
ROLLBACK TO SAVEPOINT bonus_life;

COMMIT;

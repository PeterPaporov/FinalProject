                     Работа с БД
                                 Задание1

SELECT courier_login, COUNT(*)AS delivery_count
FROM order
WHERE inDelivery = true
GROUP BY courier_login;

                                  Задание 2

SELECT tracker,
CASE
WHEN finished = true THEN 2
WHEN cancelled = true THEN - 1
WHEN inDelivery = true THEN 1
ELSE 0
END AS status
FROM orders;

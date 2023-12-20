    SELECT c.login, COUNT(o.order_id) AS delivery_count
    FROM couriers AS c
    JOIN orders AS o ON c.courier_id = o.courier_id
    WHERE o.inDelivery = true
    GROUP BY c.login;
                       Результат:
                   login	delivery_count
                            courier1	2
                            courier2	1

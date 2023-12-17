import requests

import data
import configuration


# Запрос на создание заказа
def post_new_order():
    return requests.post(
        url=configuration.URL + configuration.ORDER_ENDPOINT,
        json=data.ORDER_DATA,
        headers={
            "Content-Type": "application/json",
        }
    )


# Запрос на получение заказа по треку
def get_order_by_track(t):
    return requests.get(
        url=configuration.URL + configuration.TRACK_ENDPOINT + '?t=' + str(t),
    )


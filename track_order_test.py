import pytest

import data
from sender_stand_request import post_new_order, get_order_by_track


# Создать заказ и получить трек
def get_new_order_track():
    r = post_new_order()
    return r.json()["track"]


# Проверка позитивного исхода
def positive_assert(response, t):
    assert response.status_code == 200
    assert response.json()["order"]["track"] == t


# Проверка нагативного исхода
def negative_assert_code_400(response):
    assert response.status_code == 400


class TestClass(object):

    # Проверка валидного трека
    def test_ok(self):
        t = get_new_order_track()
        response = get_order_by_track(t)
        positive_assert(response, t)

    # Проверка пустого трека
    def test_empty_track(self):
        t = ""
        response = get_order_by_track(t)
        negative_assert_code_400(response)


    # Проверка трека типа строка
    def test_sting_track(self):
        t = "ABCDEF"
        response = get_order_by_track(t)
        negative_assert_code_400(response)

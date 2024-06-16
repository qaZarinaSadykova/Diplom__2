import allure
import requests
from endpoint import Endpoint, Urls
from data_test import data_ingredients, data_ingredients_wrong_hash, data_not_ingredients


class TestCreateOrder:

    @allure.title("Создания заказа без авторизации с ингредиентами")
    def test_create_order_true(self):
        response = requests.post(Urls.MAIN_URL + Endpoint.MAKE_ORDER, headers=Endpoint.endpoint, json=data_ingredients)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title("Создания заказа без авторизации без ингредиентов")
    def test_create_order_not_ingredients(self):
        response = requests.post(Urls.MAIN_URL + Endpoint.MAKE_ORDER, headers=Endpoint.endpoint,
                                 json=data_not_ingredients)
        assert response.status_code == 400 and response.json()["success"] is False

    @allure.title("Создания заказа без авторизации с неверным хешем ингредиентов")
    def test_create_order_bad_ingredients(self):
        response = requests.post(Urls.MAIN_URL + Endpoint.MAKE_ORDER, headers=Endpoint.endpoint,
                                 json=data_ingredients_wrong_hash)
        assert response.status_code == 500 and 'Internal Server Error' in response.text

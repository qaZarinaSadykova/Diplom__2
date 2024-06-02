import allure
import requests
from endpoint import Endpoint, Urls
from data_test import data_updated
from conftest import get_token


class TestGetOrderUser:

    @allure.story("Запрос на получение заказов авторизованного пользователя")
    def test_get_order_auth_user(self, get_token):
        response = requests.get(Urls.MAIN_URL + Endpoint.GET_ORDERS,
                                headers={'Authorization': get_token}, data=data_updated)
        body = response
        assert response.status_code == 200 and body.json()['success'] == True

    @allure.story("Запрос на получение заказов неавторизованного пользователя")
    def test_updated_order_not_auth_user(self):
        response = requests.get(Urls.MAIN_URL + Endpoint.GET_ORDERS, headers=Endpoint.endpoint)
        body = response
        assert response.status_code == 401 and body.json()['success'] == False

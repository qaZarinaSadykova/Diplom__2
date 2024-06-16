import allure
import requests
import helpers
from endpoint import Endpoint, Urls
from data_test import data_updated
from conftest import create_test_data, _delete_test_data


class TestChangeUserData:

    @allure.title("Изменение данных пользователя с авторизацией")
    def test_change_data_user(self, create_test_data, _delete_test_data):
        user_data, token = _delete_test_data
        response = requests.patch(f'{Urls.MAIN_URL}{Endpoint.CHANGE_USER_DATA}',
                                  headers={'Authorization': token, 'Content-Type': 'application/json'},
                                  json=data_updated)

        # Проверка успешного изменения данных
        assert response.status_code == 200, (f"Expected status code 200, but got {response.status_code},"
                                             f" response: {response.text}")
        response_data = response.json()
        assert response_data['user']['name'] == 'Test', f"Expected name 'Test', but got {response_data['user']['name']}"

    @allure.title("Изменение данных пользователя без авторизации")
    def test_change_user_fail(self):
        response = requests.patch(Urls.MAIN_URL + Endpoint.CHANGE_USER_DATA,
                                  headers=Endpoint.endpoint, data=data_updated)
        assert response.status_code == 400 and 'Bad Request' in response.text

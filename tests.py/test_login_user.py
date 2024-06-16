import allure
import requests
from endpoint import Urls, Endpoint
from data_test import data_failed
from conftest import create_test_data, _delete_test_data


class TestLoginUser:
    @allure.title('Авторизация пользователя')
    def test_login_user_positive(self, create_test_data, _delete_test_data):
        user_data, token = _delete_test_data

        # Попытка логина с данными пользователя
        login_response = requests.post(f'{Urls.MAIN_URL}{Endpoint.LOGIN}',
                                       json={"email": user_data['email'], "password": user_data['password']})

        # Проверка успешного логина
        assert login_response.status_code == 200, (f"Expected status code 200, but got {login_response.status_code},"
                                                   f" response: {login_response.text}")
        login_data = login_response.json()
        assert 'accessToken' in login_data, f"Expected 'accessToken' in response, but got {login_data}"
        # Проверка структуры токена
        assert login_data['accessToken'].startswith('Bearer '), f"Token format is incorrect: {login_data['accessToken']}"
        # Дополнительно можно проверить длину токена или его декодировать и проверить содержимое, если это необходимо

    @allure.title('Пользователь не может авторизоваться, не корректные учетные данные')
    def test_login_user_negative(self):
        response = requests.post(f'{Urls.MAIN_URL}{Endpoint.LOGIN}', data=data_failed)
        assert response.status_code == 401 and response.json().get('success') == False

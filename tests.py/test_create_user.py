import allure
import pytest
import requests
from endpoint import Urls, Endpoint
from data_test import data_exist_user, data_without_email, data_without_password, data_without_name
from conftest import create_test_data


class TestCreateUser:

    @allure.title('Создание нового пользователя')
    def test_create_new_user_positive(self, create_test_data):
        payload = create_test_data
        response = requests.post(f'{Urls.MAIN_URL}{Endpoint.CREATE_USER}', json=payload)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.title('Создание уже существующего пользователя')
    def test_create_user_double(self):
        response = requests.post(f'{Urls.MAIN_URL}{Endpoint.CREATE_USER}', data=data_exist_user)
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.title('Создание пользователя с незаполненными обязательными полями')
    @pytest.mark.parametrize("data", [data_without_email, data_without_password, data_without_name])
    def test_create_user_fail(self, data):
        response = requests.post(f'{Urls.MAIN_URL}{Endpoint.CREATE_USER}', data=data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text

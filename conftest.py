import json
import string
import random

import pytest
import requests
from endpoint import Urls, Endpoint
from data_test import data_updated


@pytest.fixture
def generate_random_string():
    """Фикстура для генерации случайной строки"""
    def _generate_random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    return _generate_random_string


@pytest.fixture
def create_test_data(request, generate_random_string):
    """Фикстура для создания тестовых данных перед тестом и их очистки после теста"""

    # Генерация случайной строки для электронной почты, пароля и имени
    test_data = {
        "email": generate_random_string(6) + "@yandex.ru",
        "password": generate_random_string(10),
        "name": generate_random_string(6)
    }
    return test_data


@pytest.fixture(scope="function")
def _delete_test_data(create_test_data):
    """Фикстура для удаления тестовых данных после теста"""
    user_data = create_test_data

    # Создание пользователя
    create_response = requests.post(f'{Urls.MAIN_URL}{Endpoint.CREATE_USER}', json=user_data)
    assert create_response.status_code == 200, (f"Failed to create user, status code: {create_response.status_code},"
                                                f" response: {create_response.text}")

    # Логин для получения токена авторизации
    login_response = requests.post(f'{Urls.MAIN_URL}{Endpoint.LOGIN}',
                                   json={"email": user_data['email'], "password": user_data['password']})
    assert login_response.status_code == 200, (f"Failed to login, status code: {login_response.status_code},"
                                               f" response: {login_response.text}")

    login_data = login_response.json()
    assert 'accessToken' in login_data, f"Expected 'accessToken' in response, but got {login_data}"
    token = login_data['accessToken']

    yield user_data, token

    # Удаление пользователя
    delete_response = requests.delete(f'{Urls.MAIN_URL}{Endpoint.DELETE_USER}',
                                      headers={'Authorization': f'Bearer {token}'},
                                      json={"email": user_data['email']})


@pytest.fixture(scope='function')
def get_token():
    token = requests.post(Urls.MAIN_URL + Endpoint.LOGIN, headers=Endpoint.endpoint,
                          data=json.dumps(data_updated))
    new_token = token.json()['accessToken']
    return new_token

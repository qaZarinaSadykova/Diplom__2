import json
import allure
import helpers
import pytest
import requests
from endpoint import Urls, Endpoint
import data_test


@allure.step('Создание тестовых данных')
@pytest.fixture
def create_test_data():
    # Генерация случайной строки для электронной почты, пароля и имени
    test_data = {
        "email": helpers.generate_random_string(6) + "@yandex.ru",
        "password": helpers.generate_random_string(10),
        "name": helpers.generate_random_string(6)
    }
    return test_data


@allure.step('Удаление тестовых данных после теста')
@pytest.fixture(scope="function")
def _delete_test_data(create_test_data):
    user_data = create_test_data

    # Создание пользователя
    create_response = requests.post(f'{Urls.MAIN_URL}{Endpoint.CREATE_USER}', json=user_data)
    if create_response.status_code != 200:
        raise Exception(f"Failed to create user, status code: {create_response.status_code},"
                        f" response: {create_response.text}")

    # Логин для получения токена авторизации
    login_response = requests.post(f'{Urls.MAIN_URL}{Endpoint.LOGIN}',
                                   json={"email": user_data['email'], "password": user_data['password']})
    if login_response.status_code != 200:
        raise Exception(f"Failed to login, status code: {login_response.status_code},"
                        f" response: {login_response.text}")

    login_data = login_response.json()
    if 'accessToken' not in login_data:
        raise Exception(f"Expected 'accessToken' in response, but got {login_data}")

    token = login_data['accessToken']

    # Логирование токена для отладки
    print(f"Token obtained after login: {token}")  # Debug log

    # Проверка формата токена
    if not token.startswith("Bearer "):
        token = f"Bearer {token}"
        print(f"Formatted token: {token}")  # Debug log

    yield user_data, token

    # Удаление пользователя с дополнительной отладочной информацией
    print(f"Token used for deletion: {token}")  # Debug log

    delete_response = requests.delete(f'{Urls.MAIN_URL}{Endpoint.DELETE_USER}',
                                      headers={'Authorization': token},
                                      json={"email": user_data['email']})
    if delete_response.status_code not in [200, 202]:
        print(f"Failed to delete user, status code: {delete_response.status_code}, response: {delete_response.text}")
        raise Exception(f"Failed to delete user, status code: {delete_response.status_code},"
                        f" response: {delete_response.text}")


@allure.step('Получение токена авторизации')
@pytest.fixture(scope='function')
def get_token():
    token = requests.post(Urls.MAIN_URL + Endpoint.LOGIN, headers=Endpoint.endpoint,
                          data=json.dumps(data_test.data_updated))
    new_token = token.json()['accessToken']
    return new_token

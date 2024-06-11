import time

import allure
from pages.forgot_password_page import ForgotPasswordPage
from endpoints import Endpoints
from pages.account_profile_page import AccountProfilePage
from conftest import driver


class TestAccountProfile:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_switch_to_personal_account(self, driver):
        account_profile = AccountProfilePage(driver)
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.authenticate()
        account_profile.go_to_personal_account()
        account_profile.get_endpoint()
        account_profile.url_to_be(Endpoints.profile_url)
        assert account_profile.get_endpoint() == Endpoints.profile_url

    @allure.title("Переход в раздел «История заказов»")
    def test_switch_to_order_history(self, driver):
        account_profile = AccountProfilePage(driver)
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.authenticate()
        account_profile.go_to_personal_account()
        account_profile.go_to_order_history()
        account_profile.get_endpoint()
        account_profile.url_to_be(Endpoints.history_url)
        assert account_profile.get_endpoint() == Endpoints.history_url

    @allure.title("Выход из аккаунта")
    def test_exit_account(self, driver):
        account_profile = AccountProfilePage(driver)
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.authenticate()
        account_profile.go_to_personal_account()
        account_profile.exit_account()
        account_profile.get_endpoint()
        account_profile.url_to_be(Endpoints.login_url)
        assert account_profile.get_endpoint() == Endpoints.login_url

import time

import allure
from endpoints import Endpoints
from locators.forgot_password_locators import ForgotPasswordLocators
from pages.forgot_password_page import ForgotPasswordPage
from user_data import UserData
from conftest import driver


class TestForgotPassword:
    @allure.title("Переход по кнопке «Восстановить пароль на страницу восстановления пароля")
    def test_page_forgot_password(self, driver):
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.go_to_forgot_password_page()
        forgot_password.get_endpoint()
        assert forgot_password.get_endpoint() == Endpoints.forgot_password_url

    @allure.title("Ввод почты и клик на кнопку «Восстановить»")
    def test_reset_password(self, driver):
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.go_to_forgot_password_page()
        forgot_password.reset_confirmation()
        forgot_password.get_endpoint()
        assert forgot_password.get_endpoint() == Endpoints.reset_url

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_password_visibility(self, driver):
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.go_to_forgot_password_page()
        forgot_password.reset_confirmation()
        forgot_password.find_element_send_key(ForgotPasswordLocators.PASSWORD_INPUT, UserData.PASSWORD)
        forgot_password.check_element_is_clickable(ForgotPasswordLocators.EYE_BUTTON)
        forgot_password.find_element_located_click(ForgotPasswordLocators.EYE_BUTTON)
        assert forgot_password.find_element_located(ForgotPasswordLocators.PASSWORD_VISIBLE)

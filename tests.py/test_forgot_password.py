
import allure
from endpoints import Endpoints
from pages.forgot_password_page import ForgotPasswordPage
from pages.functional_page import FunctionalPage
from conftest import driver


class TestForgotPassword:
    @allure.title("Переход по кнопке «Восстановить пароль на страницу восстановления пароля")
    def test_page_forgot_password(self, driver):
        forgot_password = ForgotPasswordPage(driver)
        functional_page = FunctionalPage(driver)
        functional_page.go_to_login_page()
        forgot_password.go_to_forgot_password_page()
        forgot_password.get_endpoint()
        assert forgot_password.get_endpoint() == Endpoints.forgot_password_url

    @allure.title("Ввод почты и клик на кнопку «Восстановить»")
    def test_reset_password(self, driver):
        forgot_password = ForgotPasswordPage(driver)
        functional_page = FunctionalPage(driver)
        functional_page.go_to_login_page()
        forgot_password.go_to_forgot_password_page()
        forgot_password.reset_confirmation()
        forgot_password.get_endpoint()
        assert forgot_password.get_endpoint() == Endpoints.reset_url

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_password_visibility(self, driver):
        forgot_password = ForgotPasswordPage(driver)
        functional_page = FunctionalPage(driver)
        functional_page.go_to_login_page()
        forgot_password.go_to_forgot_password_page()
        forgot_password.reset_confirmation()
        forgot_password.open_eye()
        assert forgot_password.is_password_input_active(), ("Поле ввода пароля должно быть активным после клика по "
                                                            "кнопке 'показать/скрыть пароль'.")

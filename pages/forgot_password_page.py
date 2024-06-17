import allure
from endpoints import Endpoints
from user_data import UserData
from locators.forgot_password_locators import ForgotPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_forgot_password_page(self):
        self.check_element_is_clickable(ForgotPasswordLocators.RECOVER_BUTTON)
        self.click_on_element(ForgotPasswordLocators.RECOVER_BUTTON)

    @allure.step("Подтверждение восстановления пароля")
    def reset_confirmation(self):
        self.check_element_is_clickable(ForgotPasswordLocators.EMAIL_INPUT)
        self.find_element_located_click(ForgotPasswordLocators.EMAIL_INPUT)
        self.find_element_send_key(ForgotPasswordLocators.EMAIL_INPUT, UserData.EMAIL)
        self.find_element_located_click(ForgotPasswordLocators.ENTRANCE_BUTTON)
        self.url_to_be(Endpoints.reset_url)

    @allure.step("Авторизация")
    def authenticate(self):
        self.check_element_is_clickable(ForgotPasswordLocators.ENTRANCE_BUTTON)
        self.find_element_located_click(ForgotPasswordLocators.ENTRANCE_BUTTON)
        self.check_element_is_clickable(ForgotPasswordLocators.ENTER_BUTTON)
        self.find_element_located_click(ForgotPasswordLocators.EMAIL_INPUT)
        self.find_element_send_key(ForgotPasswordLocators.EMAIL_INPUT, UserData.EMAIL)
        self.find_element_located_click(ForgotPasswordLocators.PASSWORD_INPUT)
        self.find_element_send_key(ForgotPasswordLocators.PASSWORD_INPUT, UserData.PASSWORD)
        self.find_element_located_click(ForgotPasswordLocators.ENTER_BUTTON)
        self.check_element_is_clickable(ForgotPasswordLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Переход на страницу личного кабинета")
    def go_to_personal_account(self):
        self.find_element_located(ForgotPasswordLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(ForgotPasswordLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Просмотр ввода пароля")
    def open_eye(self):
        self.find_element_send_key(ForgotPasswordLocators.PASSWORD_INPUT, UserData.PASSWORD)
        self.check_element_is_clickable(ForgotPasswordLocators.EYE_BUTTON)
        self.find_element_located_click(ForgotPasswordLocators.EYE_BUTTON)
        self.find_element_located(ForgotPasswordLocators.PASSWORD_INPUT_IS_ACTIVE)

    @allure.step("Подтверждение отображения пароля")
    def is_password_input_active(self):
        return self.find_element_located(ForgotPasswordLocators.PASSWORD_INPUT_IS_ACTIVE).is_displayed()

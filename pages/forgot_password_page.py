import allure
from locators.account_profile_locators import AccountProfileLocators
from endpoints import Endpoints
from user_data import UserData
from locators.forgot_password_locators import ForgotPasswordLocators
from locators.functional_locators import FunctionalLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_forgot_password_page(self):
        self.check_element_is_clickable(FunctionalLocators.ENTER_BUTTON)
        self.click_on_element(FunctionalLocators.ENTER_BUTTON)
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
        self.check_element_is_clickable(AccountProfileLocators.ENTER_BUTTON)
        self.find_element_located_click(ForgotPasswordLocators.EMAIL_INPUT)
        self.find_element_send_key(ForgotPasswordLocators.EMAIL_INPUT, UserData.EMAIL)
        self.find_element_located_click(AccountProfileLocators.PASSWORD_INPUT)
        self.find_element_send_key(AccountProfileLocators.PASSWORD_INPUT, UserData.PASSWORD)
        self.find_element_located_click(AccountProfileLocators.ENTER_BUTTON)
        self.check_element_is_clickable(AccountProfileLocators.PERSONAL_ACCOUNT_BUTTON)

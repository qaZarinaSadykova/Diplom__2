import allure
from locators.account_profile_locators import AccountProfileLocators
from pages.base_page import BasePage


class AccountProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход на страницу истории заказов")
    def go_to_order_history(self):
        self.find_element_located_click(AccountProfileLocators.ORDER_HISTORY)

    @allure.step("Выход из личного кабинета")
    def exit_account(self):
        self.find_element_located_click(AccountProfileLocators.EXIT_BUTTON)

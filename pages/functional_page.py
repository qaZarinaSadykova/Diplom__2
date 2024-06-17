import allure
from locators.functional_locators import FunctionalLocators
from pages.base_page import BasePage


class FunctionalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход на страницу ленты заказов")
    def go_to_order_feed(self):
        self.find_element_located_click(FunctionalLocators.ORDER_TEXT)

    @allure.step("Ожидать пока кнопка 'Лента зказов' не будет кликабельна")
    def time_out_order_feed(self):
        self.check_element_is_clickable(FunctionalLocators.ORDER_TEXT)

    @allure.step("Переход на страницу конструктора")
    def go_to_constructor(self):
        self.find_element_located_click(FunctionalLocators.CONSTRUCTORS_BUTTON)

    @allure.step("Переход к ингредиенту")
    def go_to_ingredient(self):
        self.find_element_located_click(FunctionalLocators.INGREDIENT)
        self.find_element_located(FunctionalLocators.INGREDIENT_DETAILS)

    @allure.step("Ожидание деталей ингредиента")
    def wait_details(self):
        if self.find_element_located(FunctionalLocators.INGREDIENT_DETAILS):
            return True

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.find_element_located_click(FunctionalLocators.CLOSE_MODAL)
        self.check_element_is_clickable(FunctionalLocators.ENTER_BUTTON)

    @allure.step("Подождать пока кнопка зкрытия модального окна не станет кликабельна")
    def close_modal_clickable(self):
        self.check_element_is_clickable(FunctionalLocators.CLOSE_MODAL)

    @allure.step("Подтверждение закрытия модального окна")
    def closing_confirmation(self):
        if self.find_element_located(FunctionalLocators.CLOSE_INGREDIENT_BUTTON):
            return True

    @allure.step("Получение количества ингредиентов")
    def number_of_ingredients(self):
        return self.find_element_located(FunctionalLocators.COUNT_INGREDIENT)

    @allure.step("Создание заказа")
    def make_an_order(self):
        self.find_element_located_click(FunctionalLocators.CHECKOUT)

    @allure.step("Подтверждение создания заказа")
    def confirmation_of_order(self):
        if self.find_element_located(FunctionalLocators.ORDER_NAME):
            return True

    @allure.step("Добавление интгридиентов")
    def drag_and_drop_for_order(self):
        self.drag_and_drop(FunctionalLocators.BURGER_INGREDIENT, FunctionalLocators.PLACE_FOR_INGREDIENTS)

    @allure.step("Переход на на страницу авторизации")
    def go_to_login_page(self):
        self.find_element_located(FunctionalLocators.ENTER_BUTTON)
        self.click_on_element(FunctionalLocators.ENTER_BUTTON)

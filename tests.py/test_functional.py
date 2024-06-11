import allure
from pages.forgot_password_page import ForgotPasswordPage
from endpoints import Endpoints
from pages.functional_page import FunctionalPage
from conftest import driver


class TestMainPage:

    @allure.title("Переход по клику на «Конструктор»")
    def test_switch_to_constructor(self, driver):
        functional_page = FunctionalPage(driver)
        functional_page.go_to_order_feed()
        functional_page.go_to_constructor()
        functional_page.url_to_be(Endpoints.main_url)
        assert functional_page.get_endpoint() == Endpoints.main_url

    @allure.title("Переход по клику на «Лента заказов»")
    def test_switch_to_order_history(self, driver):
        functional_page = FunctionalPage(driver)
        functional_page.go_to_order_feed()
        functional_page.get_endpoint()
        functional_page.url_to_be(Endpoints.feed_url)
        assert functional_page.get_endpoint() == Endpoints.feed_url

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_modal__window_after_click_to_ingredient(self, driver):
        functional_page = FunctionalPage(driver)
        functional_page.go_to_ingredient()
        assert functional_page.wait_details(), "Детали об ингредиенте не появились"

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_modal_window(self, driver):
        functional_page = FunctionalPage(driver)
        functional_page.go_to_ingredient()
        functional_page.close_modal()
        assert functional_page.closing_confirmation(), "Окно не закрылось по нажатию на крестик"

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    def test_order_registration(self, driver):
        functional_page = FunctionalPage(driver)
        functional_page.drag_and_drop_for_order()
        quantity = functional_page.number_of_ingredients().text
        assert quantity == '2', "Количество ингредиентов не совпадает"

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_making_an_order(self, driver):
        functional_page = FunctionalPage(driver)
        forgot_password = ForgotPasswordPage(driver)
        forgot_password.authenticate()
        functional_page.drag_and_drop_for_order()
        functional_page.make_an_order()
        assert functional_page.confirmation_of_order(), "Заказ не сделан"

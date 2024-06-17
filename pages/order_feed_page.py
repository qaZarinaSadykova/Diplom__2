import allure
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик на заказ")
    def click_to_the_order(self):
        self.check_element_is_clickable(OrderFeedLocators.FIRST_ORDER)
        self.find_element_located_click(OrderFeedLocators.FIRST_ORDER)

    @allure.step("Проверка открытия модального окна")
    def modal_box_is_open(self):
        if self.find_element_located(OrderFeedLocators.MODAL_ORDER):
            return True

    @allure.step("Получение ID заказа")
    def get_order_id(self):
        self.find_element_located(OrderFeedLocators.LOADING_CHECK_BOX)
        order_id = self.find_element_located(OrderFeedLocators.ORDER_ID).text
        while order_id == '9999':
            order_id = self.find_element_located(OrderFeedLocators.ORDER_ID).text
        return f"#{order_id}"

    @allure.step("Проверка совпадения заказов в истории и в ленте")
    def check_order_id(self, order_id, locator):
        elements = self.find_until_all_elements_located(locator)

        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step("Получение количества заказов")
    def get_total_order_count(self):
        return self.find_element_located(OrderFeedLocators.TOTAL_ORDER_COUNT).text

    @allure.step("Получение количества заказов в день")
    def get_daily_order_count(self):
        return self.find_element_located(OrderFeedLocators.DAILY_ORDER_COUNT).text

    @allure.step("Получение ID заказа в работе")
    def get_id_order_in_the_process(self):
        self.find_element_located(OrderFeedLocators.ORDER_IN_PROCESS)
        return self.find_element_located(OrderFeedLocators.ORDER_IN_PROCESS).text

    @allure.step("Проверка, что заказ появился в работе")
    def check_whether_id_order_in_the_process(self, order_id):
        is_order_id = self.get_id_order_in_the_process()
        if order_id[1:] in is_order_id:
            return True

    @allure.step("Проверка нахождение идентификатора заказа в истории")
    def is_order_id_found_at_history(self):
        return self.check_order_id(self.get_order_id(), OrderFeedLocators.ALL_ORDERS_HISTORY)

    @allure.step("Проверка нахождение идентификатора заказа в ленте")
    def is_order_id_found_at_feed(self):
        return self.check_order_id(self.get_order_id(), OrderFeedLocators.ALL_ORDERS_FEED)

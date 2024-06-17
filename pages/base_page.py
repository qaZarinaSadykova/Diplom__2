import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидание кликабельности элемента")
    def check_element_is_clickable(self, locator):
        WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable(locator))

    @allure.step("Клик на элемент")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Получение ссылки страницы")
    def get_endpoint(self):
        return self.driver.current_url

    @allure.step("Нахождение элемента и клик")
    def find_element_located_click(self, locator):
        return self.find_element_located(locator).click()

    @allure.step("Нахождение элемента и отправка значения")
    def find_element_send_key(self, locator, comment):
        return self.find_element_located(locator).send_keys(comment)

    @allure.step("Переход на сайт")
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step("Нахождение элемента")
    def find_element_located(self, locator):
        return WebDriverWait(self.driver, 40).until(expected_conditions.presence_of_element_located(locator))

    @allure.step("Скролл")
    def scroll_to(self, locator):
        goal = self.find_element_located(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", goal)

    @allure.step("Переключение экрана")
    def switch_window(self, locator, num):
        self.driver.switch_to.window(self.driver.window_handles[num])
        return self.find_element_located(locator)

    @allure.step("Проверка ссылки на страницу")
    def url_to_be(self, url):
        return WebDriverWait(self.driver, 20).until(expected_conditions.url_to_be(url))

    @allure.step("Нахождение нескольких элементов")
    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 40).until(expected_conditions.presence_of_all_elements_located(locator))

    @allure.step("Перетаскивание элемента")
    def drag_and_drop(self, what, where):
        drag = self.find_element_located(what)
        drop = self.find_element_located(where)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

from selenium.webdriver.common.by import By


class FunctionalLocators:
    CONSTRUCTORS_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    MAIN_TEXT = (By.CLASS_NAME, "text_type_main-large")
    ORDER_TEXT = (By.XPATH, ".//li[@class='undefined ml-2']")
    ORDERS = (By.LINK_TEXT, "Лента Заказов")
    INGREDIENT = (By.XPATH, "//p[text() ='Флюоресцентная булка R2-D3']")
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    CLOSE_INGREDIENT_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__')]")
    CLOSE_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")
    ORDER_BASKET = (By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']")
    COUNT_INGREDIENT = (By.XPATH, ".//p[@class = 'counter_counter__num__3nue1']")
    EMAIL_INPUT = (By.XPATH, ".//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    ENTER_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    ENTRANCE_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")
    CHECKOUT = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_NAME = (By.XPATH, "//p[text()='идентификатор заказа']")
    BURGER_INGREDIENT = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")
    PLACE_FOR_INGREDIENTS = (By.XPATH, "//span[@class='constructor-element__text'"
                                       " and text()='Перетяните булочку сюда (верх)']")

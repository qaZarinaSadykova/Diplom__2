from selenium.webdriver.common.by import By


class OrderFeedLocators:
    FIRST_ORDER = (By.XPATH, ".//p[@class='text text_type_digits-default'][1]")
    MODAL_ORDER = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4 .Modal_modal__container__Wo2l_")
    ALL_ORDERS_HISTORY = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/"
                                    "p[contains(@class,'text_type_digits-default')]")
    ALL_ORDERS_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text"
                                 " text_type_digits-default']")
    ORDER_ID = (By.CLASS_NAME, "Modal_modal__title_shadow__3ikwq")
    LOADING_CHECK_BOX = (By.XPATH, ".//img[@alt='tick animation']")
    TOTAL_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    DAILY_ORDER_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDER_IN_PROCESS = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem "
                                  "OrderFeed_orderList__cBvyi']/li[@class='text text_type_digits-default mb-2']")

from selenium.webdriver.common.by import By


class AccountProfileLocators:

    ORDER_HISTORY = (By.XPATH, './/a[@href="/account/order-history"]')
    EXIT_BUTTON = (By.CSS_SELECTOR, 'button.Account_button__14Yp3')

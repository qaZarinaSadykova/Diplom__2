from selenium.webdriver.common.by import By


class AccountProfileLocators:

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password']")
    PASSWORD_INPUT_IS_ACTIVE = (By.CSS_SELECTOR, ".input__container .input_status_active")
    ORDER_HISTORY = (By.XPATH, './/a[@href="/account/order-history"]')
    EXIT_BUTTON = (By.CSS_SELECTOR, 'button.Account_button__14Yp3')
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")

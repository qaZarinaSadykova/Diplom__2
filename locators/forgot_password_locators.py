from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    ENTRANCE_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")
    RECOVER_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    EMAIL_INPUT = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//input[@name='name']")
    RECOVER = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    TITLE = (By.XPATH, "//h2[.='Восстановление пароля']")
    EYE_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@class='text input__textfield text_type_main-default' and @type='password']")
    PASSWORD_INPUT_IS_ACTIVE = (By.CSS_SELECTOR, ".input__container .input_status_active")

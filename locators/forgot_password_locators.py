from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    ENTRANCE_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")
    RECOVER_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    EMAIL_INPUT = (By.XPATH, "//form[@class='Auth_form__3qKeq mb-20']//input[@name='name']")
    RECOVER = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    TITLE = (By.XPATH, "//h2[.='Восстановление пароля']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, ".input_type_password .input__textfield")
    EYE_BUTTON = (By.XPATH, "//div[contains(@class,'input__icon input__icon-action')]")
    PASSWORD_VISIBLE = (By.CLASS_NAME, "input_status_active")
    BEFORE_CLICK_INPUT = (By.XPATH, "//button[text()='Войти']")

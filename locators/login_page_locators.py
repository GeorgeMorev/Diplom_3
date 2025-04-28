from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    ENTER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button_type_primary') and text()='Войти']")
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
    RECOVERY_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")

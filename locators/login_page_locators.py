from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    ENTER_BUTTON = (By.XPATH, "//a[text()='Войти']")
    REGISTER_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")

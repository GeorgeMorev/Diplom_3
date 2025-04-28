from selenium.webdriver.common.by import By


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    REGISTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_HIDE_PASSWORD_EYE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    REGISTER_ENTER_LINK = (By.XPATH, "//a[@href='/login']")
    REGISTER_PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error') and text()='Некорректный пароль']")
from selenium.webdriver.common.by import By


class RecoveryPasswordPage:
    RECOVERY_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    ENTER_LINK = (By.XPATH, "//a[@href='/login']")
    RECOVERY_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    ENTER_CODE_FROM_EMAIL_INPUT = (By.XPATH, "//label[text()='Введите код из письма']/following-sibling::input")
    HIDE_PASSWORD_EYE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")

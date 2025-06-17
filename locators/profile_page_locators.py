from selenium.webdriver.common.by import By


class ProfilePageLocators:
    ACCOUNT_TEXT = (By.XPATH, "//p[contains(@class, 'text_type_main-default') and text()='В этом разделе вы можете "
                              "изменить свои персональные данные']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

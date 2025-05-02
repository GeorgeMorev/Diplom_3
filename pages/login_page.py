import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_page_locators import LoginPageLocators
from config.urls import URLs


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = URLs.LOGIN_PAGE
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открываем страницу логина")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Вводим email: {email}")
    def enter_email(self, email):
        email_field = LoginPageLocators.LOGIN_EMAIL_INPUT
        self.wait.until(EC.visibility_of_element_located(email_field)).send_keys(email)

    @allure.step("Вводим пароль: {password}")
    def enter_password(self, password):
        password_field = LoginPageLocators.LOGIN_PASSWORD_INPUT
        self.wait.until(EC.visibility_of_element_located(password_field)).send_keys(password)

    @allure.step("Нажимаем кнопку 'Войти'")
    def click_enter_button(self):
        enter_button = LoginPageLocators.ENTER_BUTTON
        self.wait.until(EC.visibility_of_element_located(enter_button)).click()

    @allure.step("Логинимся в систему: email = {email}, пароль = {password}")
    def login_user(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_enter_button()

    @allure.step("Кликаем по ссылке 'Восстановить пароль'")
    def click_recovery_password_link(self):
        recovery_password_link = LoginPageLocators.RECOVERY_PASSWORD_LINK
        self.wait.until(EC.visibility_of_element_located(recovery_password_link))


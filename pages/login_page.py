import allure

from pages.main_page import MainPage
from utils.locators import LoginLocators
from pages.base_page import BasePage
from utils.urls import URLs
from selenium.webdriver.support import expected_conditions as ec


class LoginPage(BasePage):
    url = URLs.LOGIN_PAGE_URL

    def go_to_reset_password_page(self):
        with allure.step("Переход на страницу восстановления пароля"):
            self.click(LoginLocators.RESET_LINK)

    def is_login_form_visible(self):
        with allure.step("Проверка, что форма входа отображается"):
            return self.is_visible(LoginLocators.LOGIN_FORM)

    def login_user(self, user):
        with allure.step("Выполняем логин через UI"):
            self.driver.get(self.url)
            self.wait.until(ec.visibility_of_element_located(LoginLocators.LOGIN_EMAIL_INPUT))
            self.driver.find_element(*LoginLocators.LOGIN_EMAIL_INPUT).send_keys(user["email"])
            self.driver.find_element(*LoginLocators.LOGIN_PASSWORD_INPUT).send_keys(user["password"])
            self.wait.until(ec.element_to_be_clickable(LoginLocators.LOGIN_ENTER_BUTTON))
            self.driver.find_element(*LoginLocators.LOGIN_ENTER_BUTTON).click()
            self.wait.until(ec.url_to_be(MainPage.url))

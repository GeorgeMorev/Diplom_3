import allure
from utils.locators import LoginLocators
from pages.base_page import BasePage
from utils.urls import URLs


class LoginPage(BasePage):
    url = URLs.LOGIN_PAGE_URL

    def go_to_reset_password_page(self):
        with allure.step("Переход на страницу восстановления пароля"):
            self.click(LoginLocators.RESET_LINK)

    def is_login_form_visible(self):
        with allure.step("Проверка, что форма входа отображается"):
            return self.is_visible(LoginLocators.LOGIN_FORM)

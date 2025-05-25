import allure

from pages.base_page import BasePage
from utils.locators import ResetPasswordLocators
from utils.urls import URLs


class ResetPasswordPage(BasePage):
    url = URLs.RESET_PASSWORD_PAGE_URL

    def get_password_input_type(self):
        with allure.step("Получаем тип поля ввода пароля"):
            return self.get_element_attribute(ResetPasswordLocators.RESET_PASSWORD_INPUT, "type")

    def toggle_password_visibility(self):
        with allure.step("Переключение видимости пароля"):
            icon = self.wait_for_element_visible(ResetPasswordLocators.SHOW_PASSWORD_ICON)
            self.js_click(icon)

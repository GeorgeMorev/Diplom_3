import allure

from utils.locators import ResetPasswordLocators
from pages.base_page import BasePage
from utils.urls import URLs


class ForgotPasswordPage(BasePage):
    url = URLs.FORGOT_PASSWORD_PAGE_URL

    def toggle_password_visibility(self):
        with allure.step("Переключение видимости пароля"):
            icon = self.wait_for_element_visible(ResetPasswordLocators.SHOW_PASSWORD_ICON)
            self.js_click(icon)

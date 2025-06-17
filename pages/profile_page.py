import allure
from utils.locators import ProfileLocators
from pages.base_page import BasePage
from utils.urls import URLs


class ProfilePage(BasePage):
    url = URLs.PROFILE_PAGE_URL

    def is_opened(self):
        with allure.step("Проверка, что открыта страница профиля"):
            return self.check_url(self.url)

    def go_to_order_history(self):
        with allure.step("Переход во вкладку 'История заказов'"):
            self.click(ProfileLocators.ORDER_HISTORY_TAB)
            self.wait_until_overlay_disappears()

    def is_order_history_visible(self):
        with allure.step("Проверка, что отображается история заказов"):
            return self.is_visible(ProfileLocators.ORDER_HISTORY_BLOCK)

    def logout(self):
        with allure.step("Выход из личного кабинета"):
            self.click(ProfileLocators.LOGOUT_BUTTON)

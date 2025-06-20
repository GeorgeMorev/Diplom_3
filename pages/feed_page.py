import allure

from utils.locators import FeedLocators
from utils.urls import URLs
from pages.base_page import BasePage


class FeedPage(BasePage):
    url = URLs.FEED_PAGE_URL

    def go_to_feed(self):
        with allure.step("Переход на вкладку 'Лента заказов'"):
            self.click(FeedLocators.FEED_HEADER)

    def is_feed_loaded(self):
        with allure.step("Проверка, что лента заказов загружена"):
            return self.is_visible(FeedLocators.ORDER_STARTED_TEXT)

    def click_order(self):
        with allure.step("Клик по первому заказу в списке"):
            self.click(FeedLocators.ORDER)

    def is_order_present(self, order_number):
        with allure.step(f"Проверка, что заказ с номером {order_number} отображается в списке"):
            xpath = FeedLocators.USER_ORDER.format(order_number)
            return self.is_visible(("xpath", xpath))

    def get_total_done(self):
        with allure.step("Получение общего количества выполненных заказов за всё время"):
            return int(self.get_text(FeedLocators.DONE_TOTAL))

    def get_today_done(self):
        with allure.step("Получение количества заказов, выполненных сегодня"):
            return int(self.get_text(FeedLocators.DONE_TODAY))

    def has_order_from_user(self, order_number: str):
        with allure.step("Проверка, что заказ отображается в ленте"):
            locator = FeedLocators.order_number_locator(order_number)
            return self.is_visible(locator)

    def is_order_in_progress(self, order_number: str) -> bool:
        with allure.step(f"Проверка, что заказ {order_number} находится в работе"):
            locator = FeedLocators.order_in_progress_locator(order_number)
            return self.is_visible(locator)

    def is_order_details_visible(self):
        with allure.step("Проверка, что детали заказа видны"):
            return self.is_visible(FeedLocators.ORDER_DETAILS)
import allure
from pages.base_page import BasePage
from utils.locators import MainLocators
from utils.urls import URLs


class MainPage(BasePage):
    url = URLs.MAIN_PAGE_URL

    def click_profile_button(self):
        with allure.step("Клик по кнопке 'Личный кабинет'"):
            self.click(MainLocators.PROFILE_BUTTON)

    def click_constructor_button(self):
        with allure.step("Клик по кнопке 'Конструктор'"):
            self.click(MainLocators.CONSTRUCTOR_BUTTON)

    def is_constructor_visible(self):
        with allure.step("Проверка, что отображается раздел с булками конструктора"):
            return self.is_visible(MainLocators.BUN_SECTION)

    def click_order_feed_button(self):
        with allure.step("Клик по кнопке 'Лента заказов'"):
            self.click(MainLocators.FEED_BUTTON)

    def click_ingredient(self):
        with allure.step("Клик по ингредиенту"):
            self.click(MainLocators.INGREDIENT)

    def is_ingredient_details_visible(self):
        with allure.step("Проверка, что окно деталей ингредиента отображается"):
            return self.is_visible(MainLocators.INGREDIENT_DETAILS)

    def close_ingredient_details(self):
        with allure.step("Закрытие окна деталей ингредиента"):
            self.click(MainLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    def is_ingredient_details_closed(self):
        with allure.step("Проверка, что окно деталей ингредиента закрыто"):
            return self.is_closed(MainLocators.INGREDIENT_DETAILS)

    def add_ingredient_to_burger(self):
        with allure.step("Перетаскивание ингредиента в корзину"):
            self.drag_and_drop(MainLocators.INGREDIENT, MainLocators.BASKET_LIST)

    def is_ingredient_counter_incremented(self):
        with allure.step("Проверка, что счётчик ингредиента увеличился"):
            return int(self.get_text(MainLocators.INGREDIENT_COUNTER)) > 0

    def click_place_order_button(self):
        with allure.step("Клик по кнопке 'Оформить заказ'"):
            self.click(MainLocators.PLACE_ORDER_BUTTON)

    def is_order_details_visible(self):
        with allure.step("Проверка, что окно деталей заказа отображается"):
            return self.is_visible(MainLocators.ORDER_DETAILS)

    def get_order_number(self):
        with allure.step("Получение номера заказа"):
            return self.get_text(MainLocators.ORDER_NUMBER)
import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from utils.locators import MainLocators


@allure.feature("Главная страница и конструктор")
class TestMainPage:

    @allure.description("Переход в раздел 'Конструктор' и проверка его отображения")
    def test_go_to_constructor(self, driver, open_page):
        main_page = open_page(MainPage)  # Используем фикстуру для открытия страницы
        main_page.click(MainLocators.CONSTRUCTOR_BUTTON)  # Используем метод из BasePage
        assert main_page.is_constructor_visible()

    @allure.description("Переход в 'Ленту заказов' и проверка URL")
    def test_go_to_order_feed(self, driver, open_page):
        main_page = open_page(MainPage)
        main_page.click(MainLocators.FEED_BUTTON)
        assert driver.current_url == FeedPage.url

    @allure.description("Открытие и закрытие окна деталей ингредиента")
    def test_toggle_ingredient_details(self, driver, open_page):
        main_page = open_page(MainPage)
        main_page.click(MainLocators.INGREDIENT)
        assert main_page.is_ingredient_details_visible()
        main_page.click(MainLocators.INGREDIENT_DETAILS_CLOSE_BUTTON)
        assert main_page.is_ingredient_details_closed()

    @allure.description("Проверка увеличения счётчика ингредиента")
    def test_ingredient_counter_increment(self, driver, open_page):
        main_page = open_page(MainPage)
        main_page.add_ingredient_to_burger()
        assert main_page.is_ingredient_counter_incremented()

    @allure.description("Создание заказа и проверка отображения окна деталей")
    def test_create_order_when_logged_in(self, driver, login_user, open_page):
        main_page = open_page(MainPage)
        main_page.add_ingredient_to_burger()
        main_page.click(MainLocators.PLACE_ORDER_BUTTON)
        assert main_page.is_order_details_visible()

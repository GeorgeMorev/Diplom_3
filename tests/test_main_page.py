import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage


@allure.feature("Главная страница и конструктор")
class TestMainPage:

    @allure.title("Переход в раздел 'Конструктор'")
    @allure.description("Переход в раздел 'Конструктор' и проверка его отображения")
    def test_go_to_constructor(self, open_page):
        main_page = open_page(MainPage)
        main_page.click_constructor()
        assert main_page.is_constructor_visible()

    @allure.title("Переход в 'Ленту заказов'")
    @allure.description("Переход в 'Ленту заказов' и проверка, что страница открылась")
    def test_go_to_order_feed(self, open_page):
        main_page = open_page(MainPage)
        main_page.click_feed()
        feed_page = open_page(FeedPage)
        assert feed_page.is_opened()

    @allure.title("Открытие и закрытие окна деталей ингредиента")
    @allure.description("Проверка открытия и закрытия окна с деталями ингредиента")
    def test_toggle_ingredient_details(self, open_page):
        main_page = open_page(MainPage)
        main_page.click_ingredient()
        assert main_page.is_ingredient_details_visible()
        main_page.close_ingredient_details()
        assert main_page.is_ingredient_details_closed()

    @allure.title("Увеличение счётчика ингредиента")
    @allure.description("Проверка, что счётчик ингредиента увеличивается после добавления")
    def test_ingredient_counter_increment(self, open_page):
        main_page = open_page(MainPage)
        main_page.add_ingredient_to_burger()
        assert main_page.is_ingredient_counter_incremented()

    @allure.title("Создание заказа")
    @allure.description("Проверка, что окно деталей заказа отображается после оформления")
    def test_create_order_when_logged_in(self, login_user, open_page):
        main_page = open_page(MainPage)
        main_page.add_ingredient_to_burger()
        main_page.click_place_order_button()
        assert main_page.is_order_details_visible()

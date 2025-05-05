import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from utils.locators import FeedLocators


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.description("Открытие деталей заказа из ленты заказов")
    def test_open_order_details_from_feed(self, driver, open_page):
        feed_page = open_page(FeedPage)
        feed_page.click(FeedLocators.ORDER)
        assert feed_page.is_order_details_visible(FeedLocators.ORDER_DETAILS)

    @allure.description("Проверка, что созданный пользователем заказ появляется в ленте")
    def test_user_orders_appear_in_feed(self, driver, login_user, create_order, open_page):
        feed_page = open_page(FeedPage)
        assert feed_page.has_order_from_user(create_order)

    @allure.description("Проверка увеличения счётчика всех выполненных заказов после нового заказа")
    def test_total_done_counter_increases(self, driver, login_user, request):
        feed_page = FeedPage(driver)
        feed_page.open()
        before = feed_page.get_total_done()
        request.getfixturevalue("create_order")
        feed_page.open()
        after = feed_page.get_total_done()
        assert after > before

    @allure.description("Проверка увеличения счётчика заказов, выполненных сегодня")
    def test_today_done_counter_increases(self, driver, login_user, request):
        feed_page = FeedPage(driver)
        feed_page.open()
        before = FeedPage(driver).get_today_done()
        request.getfixturevalue("create_order")
        feed_page.open()
        after = feed_page.get_today_done()
        assert after > before

    @allure.description("Проверка, что новый заказ отображается в списке заказов 'в работе'")
    def test_new_order_appears_in_progress(self, driver, login_user, create_order):
        feed_page = FeedPage(driver)
        feed_page.open()
        assert feed_page.is_order_in_progress(create_order)

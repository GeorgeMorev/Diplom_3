import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestProfile:

    @allure.description("Переход из главной страницы в профиль авторизованного пользователя")
    def test_go_to_profile(self, driver, login_user):
        MainPage(driver).click_profile_button()
        assert ProfilePage(driver).is_opened()

    @allure.description("Переход из профиля во вкладку 'История заказов'")
    def test_go_to_order_history(self, driver, login_user):
        MainPage(driver).click_profile_button()
        page = ProfilePage(driver)
        page.go_to_order_history()
        assert "order-history" in driver.current_url

    @allure.description("Выход пользователя из личного кабинета")
    def test_logout(self, driver, login_user):
        MainPage(driver).click_profile_button()
        page = ProfilePage(driver)
        page.logout()
        assert LoginPage(driver).is_opened()

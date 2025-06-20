import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход в профиль пользователя")
    @allure.description("Переход из главной страницы в профиль авторизованного пользователя")
    def test_go_to_profile(self, driver, login_user, open_page):
        main_page = open_page(MainPage)
        main_page.go_to_profile()
        profile_page = open_page(ProfilePage, navigate=False)
        assert profile_page.is_opened()

    @allure.title("Переход в историю заказов")
    @allure.description("Переход из профиля во вкладку 'История заказов'")
    def test_go_to_order_history(self, driver, login_user, open_page):
        main_page = open_page(MainPage)
        main_page.go_to_profile()
        profile_page = open_page(ProfilePage, navigate=False)
        profile_page.go_to_order_history()
        assert profile_page.is_on_order_history_page()

    @allure.title("Выход из профиля")
    @allure.description("Выход пользователя из личного кабинета")
    def test_logout(self, driver, login_user, open_page):
        main_page = open_page(MainPage)
        main_page.go_to_profile()
        profile_page = open_page(ProfilePage, navigate=False)
        profile_page.logout()
        assert LoginPage(driver).is_opened()

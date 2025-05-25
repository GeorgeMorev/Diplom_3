import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.password_reset_page import ResetPasswordPage


@allure.feature("Восстановление пароля")
class TestPasswordReset:

    @allure.title("Переход на страницу восстановления пароля")
    @allure.description("Переход со страницы логина на страницу восстановления пароля")
    def test_go_to_reset_password_page(self, open_page):
        login_page = open_page(LoginPage)
        login_page.go_to_reset_password_page()
        forgot_page = open_page(ForgotPasswordPage)
        assert forgot_page.is_opened()

    @allure.title("Запрос восстановления пароля")
    @allure.description("Запрос на восстановление пароля с корректным email")
    def test_restore_password(self, open_page):
        login_page = open_page(LoginPage)
        login_page.go_to_reset_password_page()

        forgot_page = open_page(ForgotPasswordPage, navigate=False)
        forgot_page.enter_email("test@example.com")
        forgot_page.click_restore_button()

        reset_page = open_page(ResetPasswordPage, navigate=False)
        assert reset_page.is_opened()

    @allure.title("Переключение видимости пароля")
    @allure.description("Проверка переключения видимости пароля на этапе восстановления")
    def test_show_password_button_activates_input(self, open_page, driver):
        forgot_page = open_page(ForgotPasswordPage)
        forgot_page.enter_email("test@example.com")
        forgot_page.click_restore_button()

        reset_page = ResetPasswordPage(driver)
        type_before = reset_page.get_password_input_type()
        reset_page.toggle_password_visibility()
        type_after = reset_page.get_password_input_type()
        assert type_before != type_after

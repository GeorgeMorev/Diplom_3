import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


@allure.feature("Восстановление пароля")
class TestPasswordReset:

    @allure.description("Переход со страницы логина на страницу восстановления пароля")
    def test_go_to_reset_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.go_to_reset_password_page()
        assert driver.current_url == ForgotPasswordPage.url

    @allure.description("Запрос на восстановление пароля с корректным email")
    def test_restore_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.go_to_reset_password_page()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.enter_email("test@example.com")
        forgot_password_page.click_restore_button()
        assert ResetPasswordPage(driver).is_opened()

    @allure.description("Проверка переключения видимости пароля на этапе восстановления")
    def test_show_password_button_activates_input(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.open()
        forgot_password_page.enter_email("test@example.com")
        forgot_password_page.click_restore_button()
        type_before = forgot_password_page.password_field_type()
        forgot_password_page.toggle_password_visibility()
        type_after = forgot_password_page.password_field_type()

        assert type_before != type_after

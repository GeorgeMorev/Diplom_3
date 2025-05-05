import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.password_reset_page import ResetPasswordPage
from utils.locators import LoginLocators, ResetPasswordLocators


@allure.feature("Восстановление пароля")
class TestPasswordReset:

    @allure.description("Переход со страницы логина на страницу восстановления пароля")
    def test_go_to_reset_password_page(self, driver, open_page):
        login_page = open_page(LoginPage)
        login_page.go_to_reset_password_page()
        assert driver.current_url == ForgotPasswordPage.url

    @allure.description("Запрос на восстановление пароля с корректным email")
    def test_restore_password(self, driver, open_page):
        login_page = open_page(LoginPage)
        login_page.click(LoginLocators.RESET_LINK)
        forgot_page = ForgotPasswordPage(driver)
        forgot_page.type(ResetPasswordLocators.RESET_PASSWORD_EMAIL_INPUT, "test@example.com")
        forgot_page.click(ResetPasswordLocators.RESTORE_BUTTON)
        reset_page = ResetPasswordPage(driver)
        assert reset_page.is_opened()

    @allure.description("Проверка переключения видимости пароля на этапе восстановления")
    def test_show_password_button_activates_input(self, driver, open_page):
        forgot_page = open_page(ForgotPasswordPage)
        forgot_page.type(ResetPasswordLocators.RESET_PASSWORD_EMAIL_INPUT, "test@example.com")
        forgot_page.click(ResetPasswordLocators.RESTORE_BUTTON)
        reset_page = ResetPasswordPage(driver)
        type_before = reset_page.get_element_attribute(ResetPasswordLocators.RESET_PASSWORD_INPUT, "type")
        reset_page.click(ResetPasswordLocators.SHOW_PASSWORD_ICON)
        type_after = reset_page.get_element_attribute(ResetPasswordLocators.RESET_PASSWORD_INPUT, "type")

        assert type_before != type_after

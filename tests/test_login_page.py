import pytest
from locators.login_page_locators import LoginPageLocators
from pages.login_page import LoginPage
from config.urls import URLs


class TestLoginPage:
    main_page_url = URLs.MAIN_PAGE
    recovery_password_page_url = URLs.RECOVERY_PASSWORD_PAGE

    def test_go_to_constructor(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_constructor_button()
        assert driver.current_url == self.main_page_url

    def test_go_to_recovery_password(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_recovery_password_link()
        assert driver.current_url == self.recovery_password_page_url

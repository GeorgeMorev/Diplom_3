import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.main_page import MainPage
from utils.user_api import delete_test_user, create_test_user, login


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    with allure.step(f"Выбор браузера: {browser}"):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            service = Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

    yield driver

    with allure.step("Закрытие браузера"):
        driver.quit()


@pytest.fixture
def open_page(driver):
    def _open_page(page_class, navigate=True):
        page = page_class(driver)
        if navigate and hasattr(page, "url"):
            driver.get(page.url)
        return page

    return _open_page


@pytest.fixture
def login_user(driver):
    user = create_test_user()
    with allure.step("Логин под тестовым пользователем"):
        login(driver, user)
    yield user
    with allure.step("Удаление тестового пользователя"):
        delete_test_user(user)


@pytest.fixture
def create_order(driver, login_user, open_page):
    page = open_page(MainPage)
    page.add_ingredient_to_burger()
    page.click_place_order_button()

    with allure.step("Ожидание получения номера заказа"):
        WebDriverWait(driver, timeout=10).until(
            lambda d: page.get_order_number() != "9999",
            "Номер заказа не обновился"
        )

    return page.get_order_number()

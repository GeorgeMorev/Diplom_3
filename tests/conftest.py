import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.user_api import delete_test_user, create_test_user, login


@allure.feature("WebDriver")
@allure.story("Настройка драйвера")
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    with allure.step(f"Выбор браузера: {browser}"):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            driver_path = "/Users/georgemorev/tools/chromedriver-mac-arm64/chromedriver"
            service = Service(driver_path)
            driver = webdriver.Chrome(service=service, options=options)

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            driver = webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser}")

    yield driver

    with allure.step("Закрытие браузера"):
        driver.quit()


@pytest.fixture
def open_page(driver):
    def _open(page_class):
        page = page_class(driver)
        with allure.step(f"Открытие страницы: {page.url}"):
            driver.get(page.url)
            assert page.is_opened(), "Страница не открылась по ожидаемому URL"
        return page
    return _open


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
    from pages.main_page import MainPage

    page = open_page(MainPage)
    page.add_ingredient_to_burger()
    page.click_place_order_button()

    with allure.step("Ожидание получения номера заказа"):
        assert page.get_order_number() != "9999", "Некорректный номер заказа"

    return page.get_order_number()

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.user_api import delete_test_user, create_test_user, login


@allure.feature("WebDriver")
@allure.story("Настройка драйвера для тестирования в разных браузерах")
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    # Шаг 1: Выбираем браузер
    with allure.step(f"Выбираем браузер: {browser}"):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1920,1080")

            # Указываем путь к chromedriver через Service
            driver_path = "/Users/georgemorev/tools/chromedriver-mac-arm64/chromedriver"
            service = Service(driver_path)
            driver = webdriver.Chrome(service=service, options=options)
            allure.step("Запускаем Chrome браузер с заданными параметрами")

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            driver = webdriver.Firefox(options=options)
            allure.step("Запускаем Firefox браузер с заданными параметрами")

        else:
            allure.step(f"Не поддерживаемый браузер: {browser}")
            raise ValueError(f"Unsupported browser: {browser}")

    yield driver

    # Шаг 2: Закрытие браузера
    with allure.step("Закрываем браузер"):
        driver.quit()


@pytest.fixture
def open_page(driver):
    def _open(page_class):
        page = page_class(driver)
        with allure.step(f"Открытие страницы: {page.url}"):
            driver.get(page.url)
            WebDriverWait(driver, 10).until(EC.url_to_be(page.url))
        return page
    return _open


@pytest.fixture
def login_user(driver):
    user = create_test_user()
    login(driver, user)
    yield user
    delete_test_user(user)


@pytest.fixture
def create_order(driver, login_user, open_page):
    from pages.main_page import MainPage

    page = open_page(MainPage)
    page.add_ingredient_to_burger()
    page.click_place_order_button()

    def order_number_is_valid(_):
        order_number = page.get_order_number()
        return order_number and order_number != "9999"

    WebDriverWait(driver, timeout=10).until(order_number_is_valid)
    return page.get_order_number()

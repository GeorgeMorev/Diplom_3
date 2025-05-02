import pytest
from selenium import webdriver
import allure


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
            driver = webdriver.Chrome(options=options)
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

import allure
from abc import ABC, abstractmethod
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.locators import MainLocators


class BasePage(ABC):
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @property
    @abstractmethod
    def url(self):
        """Абстрактный URL страницы"""
        pass

    def is_opened(self):
        with allure.step(f"Проверить, что страница открыта по URL: {self.url}"):
            return self.wait.until(ec.url_to_be(self.url))

    def click(self, locator):
        with allure.step(f"Клик по элементу: {locator}"):
            self.wait.until(ec.element_to_be_clickable(locator)).click()

    def js_click(self, element):
        with allure.step("Клик по элементу через JavaScript"):
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, text):
        with allure.step(f"Ввод текста '{text}' в элемент: {locator}"):
            self.get_element(locator).send_keys(text)

    def get_element(self, locator):
        with allure.step(f"Поиск элемента: {locator}"):
            return self.driver.find_element(*locator)

    def get_element_attribute(self, locator, attribute):
        with allure.step(f"Получение атрибута '{attribute}' у элемента: {locator}"):
            return self.wait_for_element_visible(locator).get_attribute(attribute)

    def is_visible(self, locator):
        with allure.step(f"Проверка, что элемент видим: {locator}"):
            self.wait.until(ec.visibility_of_element_located(locator))
            return self.get_element(locator).is_displayed()

    def is_closed(self, locator, timeout=5):
        with allure.step(f"Проверка, что элемент скрыт: {locator}"):
            WebDriverWait(self.driver, timeout).until(ec.invisibility_of_element_located(locator))
            return not self.get_element(locator).is_displayed()

    def wait_for_element_visible(self, locator):
        with allure.step(f"Ожидание видимости элемента: {locator}"):
            return self.wait.until(ec.visibility_of_element_located(locator))

    def get_text(self, locator):
        with allure.step(f"Получение текста элемента: {locator}"):
            return self.wait_for_element_visible(locator).text

    def drag_and_drop(self, source_locator, target_locator):
        with allure.step(f"Перетаскивание элемента {source_locator} на элемент {target_locator}"):
            source = self.wait.until(ec.presence_of_element_located(source_locator))
            target = self.wait.until(ec.presence_of_element_located(target_locator))

            ActionChains(self.driver).click_and_hold(source).move_to_element(target).release().perform()

    def is_order_details_visible(self, locator):
        with allure.step("Проверка, что детали заказа отображаются"):
            return self.is_visible(locator)

    def wait_for_modal_to_disappear(self):
        with allure.step("Ожидание скрытия модального окна"):
            self.wait.until(ec.invisibility_of_element_located(MainLocators.MODAL_OVERLAY))


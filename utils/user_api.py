import uuid
from selenium.webdriver.support import expected_conditions as EC

import requests
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from utils.locators import ResetPasswordLocators, LoginLocators
from utils.urls import URLs, AuthURLs


def create_test_user():
    def generate_email():
        return f"test_{uuid.uuid4()}@yandex.ru"

    user = {
        "email": generate_email(),
        "password": "123456",
        "name": "Test User"
    }
    requests.post(AuthURLs.AUTH_REGISTER_URL, json=user)  # Используем AuthURLs
    return user


def delete_test_user(user):
    token = requests.post(AuthURLs.AUTH_LOGIN_URL, json={  # Используем AuthURLs
        "email": user["email"], "password": user["password"]
    }).json()["accessToken"].split()[-1]
    headers = {"Authorization": f"Bearer {token}"}
    requests.delete(AuthURLs.AUTH_USER_DELETE_URL, headers=headers)  # Используем AuthURLs


def login(driver, user):
    driver.get(URLs.LOGIN_PAGE_URL)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(LoginLocators.LOGIN_EMAIL_INPUT))
    driver.find_element(*LoginLocators.LOGIN_EMAIL_INPUT).send_keys(user["email"])
    driver.find_element(*LoginLocators.LOGIN_PASSWORD_INPUT).send_keys(user["password"])
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginLocators.LOGIN_ENTER_BUTTON))
    driver.find_element(*LoginLocators.LOGIN_ENTER_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(MainPage.url))
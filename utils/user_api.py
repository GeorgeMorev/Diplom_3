import uuid

import requests

from utils.locators import ResetPasswordLocators

BASE_URL = "https://stellarburgers.nomoreparties.site/api"


def create_test_user():
    def generate_email():
        return f"test_{uuid.uuid4()}@yandex.ru"

    user = {
        "email": generate_email(),
        "password": "123456",
        "name": "Test User"
    }
    requests.post(f"{BASE_URL}/auth/register", json=user)
    return user


def delete_test_user(user):
    token = requests.post(f"{BASE_URL}/auth/login", json={
        "email": user["email"], "password": user["password"]
    }).json()["accessToken"].split()[-1]
    headers = {"Authorization": f"Bearer {token}"}
    requests.delete(f"{BASE_URL}/auth/user", headers=headers)


def login(driver, user):
    driver.get("https://stellarburgers.nomoreparties.site/login")
    driver.find_element(*ResetPasswordLocators.EMAIL_INPUT).send_keys(user["email"])
    driver.find_element(*ResetPasswordLocators.PASSWORD_INPUT).send_keys(user["password"])
    driver.find_element("xpath", "//button[text()='Войти']").click()

import uuid
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.main_page import MainPage
from utils.locators import LoginLocators
from utils.urls import URLs, AuthURLs


def create_test_user():
    def generate_email():
        return f"test_{uuid.uuid4()}@yandex.ru"

    user = {
        "email": generate_email(),
        "password": "123456",
        "name": "Test User"
    }
    requests.post(AuthURLs.AUTH_REGISTER_URL, json=user)
    return user


def delete_test_user(user):
    token = requests.post(AuthURLs.AUTH_LOGIN_URL, json={  # Используем AuthURLs
        "email": user["email"], "password": user["password"]
    }).json()["accessToken"].split()[-1]
    headers = {"Authorization": f"Bearer {token}"}
    requests.delete(AuthURLs.AUTH_USER_DELETE_URL, headers=headers)  # Используем AuthURLs



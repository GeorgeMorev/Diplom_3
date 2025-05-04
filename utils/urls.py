class URLs:
    BASE_URL = "https://stellarburgers.nomoreparties.site"

    MAIN_PAGE_URL = f"{BASE_URL}/"
    LOGIN_PAGE_URL = f"{BASE_URL}/login"
    FORGOT_PASSWORD_PAGE_URL = f"{BASE_URL}/forgot-password"
    RESET_PASSWORD_PAGE_URL = f"{BASE_URL}/reset-password"
    FEED_PAGE_URL = f"{BASE_URL}/feed"
    PROFILE_PAGE_URL = f"{BASE_URL}/profile"


class AuthURLs:
    BASE_AUTH_URL = f"{URLs.BASE_URL}/auth"
    AUTH_REGISTER_URL = f"{BASE_AUTH_URL}/register"
    AUTH_LOGIN_URL = f"{BASE_AUTH_URL}/login"
    AUTH_USER_DELETE_URL = f"{BASE_AUTH_URL}/user"

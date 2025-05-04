from selenium.webdriver.common.by import By


class MainLocators:
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    BASKET_LIST = (By.XPATH, "//ul[contains(@class, 'basket__list')]")
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT = (By.XPATH, "//a[contains(@class, 'ingredient')]")
    INGREDIENT_DETAILS = (By.XPATH, "//h2[text()='Детали ингредиента']")
    INGREDIENT_DETAILS_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal__close')]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter__num')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_DETAILS = (By.XPATH, "//p[text()='идентификатор заказа']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    BUN_SECTION = (By.XPATH, "//h2[text()='Булки']")


class LoginLocators:
    LOGIN_ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    RESET_LINK = (By.XPATH, "//a[contains(@class, 'Auth_link') and text()='Восстановить пароль']")
    LOGIN_FORM = (By.NAME, "name")
    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")


class ForgotPasswordLocators:
    FORGOT_PASSWORD_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")


class ResetPasswordLocators:
    RESET_PASSWORD_EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESET_PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
    # PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    SHOW_PASSWORD_ICON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")


class ProfileLocators:
    ORDER_HISTORY_TAB = (By.XPATH, "//a[contains(text(),'История заказов')]")
    ORDER_HISTORY_BLOCK = (By.CLASS_NAME, "OrderHistory_list")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")


class FeedLocators:
    FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDER_STARTED_TEXT = (By.XPATH, "//p[contains(text(), 'Ваш заказ начали готовить')]")
    ORDER = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]//a")
    ORDER_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
    USER_ORDER = "//p[contains(@class, 'text_type_digits-default') and contains(text(), '{}')]"
    DONE_TOTAL = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    DONE_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

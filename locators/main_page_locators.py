from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and text()='Лента "
                                    "Заказов']")
    INGREDIENT_DETAILS_MODAL_POPUP = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox__sCy8X')]")
    CLOSE_INGREDIENT_DETAILS_MODAL_POPUP_BUTTON = (By.XPATH, "(//button[contains(@class, 'Modal_modal__close')])[1]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, "
                              "'button_button_type_primary__1O7Bx') and text()='Оформить заказ']")

    @staticmethod
    def get_ingredient_locator(ingredient_name):
        # Динамически находим ингредиент
        return (By.XPATH,
                f"//a[contains(@class, 'BurgerIngredient_ingredient') and .//p[normalize-space(text())='{ingredient_name}']]")

    @staticmethod
    def get_ingredient_counter_locator(ingredient_name):
        # Динамически находим каунтер для ингредиента
        return (By.XPATH,
                f"//a[contains(@class, 'BurgerIngredient_ingredient') and .//p[normalize-space(text())='{ingredient_name}']]//div[contains(@class, 'counter_counter')]//p[contains(@class, 'counter_counter__num')]")
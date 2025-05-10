from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    ORDERS_FEED_TEXT = (By.XPATH, "//h1[contains(@class, 'text_type_main-large') and text()='Лента заказов']")
    FIRST_ORDER_IN_FEED = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem__2x95r')])[1]//a[contains(@class, "
                                     "'OrderHistory_link__1iNby')]")
    ORDER_NUMBER_IN_FEED = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem__2x95r')])[1]//p[contains("
                                      "@class, 'text_type_digits-default') and not(contains(@class, 'mr-2'))]")
    BURGER_NAME_IN_FEED = (By.XPATH, "(//li[contains(@class, 'OrderHistory_listItem__2x95r')])[1]//h2[contains(@class, "
                                     "'text_type_main-medium')]")
    ORDER_POP_UP = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi') and contains(@class, "
                              "'Modal_modal__contentBox__sCy8X')]")
    ORDER_NUMBER_IN_POP_UP = (By.XPATH, "(//div[contains(@class, 'Modal_orderBox__1xWdi')]//p[contains(@class, "
                                        "'text_type_digits-default')])[1]")
    BURGER_NAME_IN_POP_UP = (By.XPATH, "(//div[contains(@class, 'Modal_orderBox__1xWdi')]//h2[contains(@class, "
                                       "'text_type_main-medium')])[1]")
    TOTAL_ORDERS_COUNT = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number') and contains(@class, "
                                    "'text_type_digits-large')])[1]")
    TODAY_ORDERS_COUNT = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number') and contains(@class, "
                                    "'text_type_digits-large')])[2]")

    # Метод для динамической генерации локаторов
    @staticmethod
    def get_order_number_locator(order_number):
        return By.XPATH, f"//p[contains(@class, 'text_type_digits-default') and text()='{order_number}']"

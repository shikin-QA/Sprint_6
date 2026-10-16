from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Middle') and text()='Заказать']"
    )
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    @staticmethod
    def metro_option(metro):
        return (
            By.XPATH,
            f"//*[contains(@class, 'select-search__row') "
            f"and normalize-space(.)='{metro}']"
        )

    @staticmethod
    def rental_period_option(period):
        return (
            By.XPATH,
            f"//div[contains(@class, 'Dropdown-option') and text()='{period}']"
        )
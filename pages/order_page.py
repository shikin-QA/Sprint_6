import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class OrderPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/order"

    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder')]")
    RENTAL_PERIOD_OPTION = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-option') and text()='сутки']"
    )
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'Button_Middle') and text()='Заказать']"
    )

    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def fill_customer_form(self, name, surname, address, metro, phone):
        self.fill(self.NAME_INPUT, name)
        self.fill(self.SURNAME_INPUT, surname)
        self.fill(self.ADDRESS_INPUT, address)

        # Открываем дропдаун метро и вводим название станции
        self.click(self.METRO_INPUT)
        time.sleep(1)
        self.fill(self.METRO_INPUT, metro)
        time.sleep(2)

        # Кликаем по строке с точным совпадением текста (это <li>, не <div>)
        option_locator = (
            By.XPATH,
            f"//*[contains(@class, 'select-search__row') "
            f"and normalize-space(.)='{metro}']"
        )
        self.find_clickable(option_locator).click()
        time.sleep(1)

        self.fill(self.PHONE_INPUT, phone)

    def click_next(self):
        self.click(self.NEXT_BUTTON)

    def fill_rental_form(self, date, period="сутки", color="black", comment=""):
        # Вводим дату и закрываем календарь Escape, чтобы он не перекрывал дропдаун
        self.fill(self.DATE_INPUT, date)
        time.sleep(0.5)
        self.driver.find_element(*self.DATE_INPUT).send_keys(Keys.ESCAPE)
        time.sleep(0.5)

        # Срок аренды
        self.click(self.RENTAL_PERIOD_DROPDOWN)
        time.sleep(0.5)
        self.click(self.RENTAL_PERIOD_OPTION)
        time.sleep(0.5)

        # Цвет
        if color == "black":
            self.click(self.COLOR_BLACK_CHECKBOX)
        else:
            self.click(self.COLOR_GREY_CHECKBOX)

        if comment:
            self.fill(self.COMMENT_INPUT, comment)

    def click_order(self):
        self.click(self.ORDER_BUTTON)

    def confirm_order(self):
        self.click(self.CONFIRM_YES_BUTTON)

    def get_success_text(self):
        return self.find_visible(self.SUCCESS_MODAL).text
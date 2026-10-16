from config import ORDER_URL
from locators.order_page_locators import OrderPageLocators as L
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, ORDER_URL)

    def fill_customer_form(self, name, surname, address, metro, phone):
        self.fill(L.NAME_INPUT, name)
        self.fill(L.SURNAME_INPUT, surname)
        self.fill(L.ADDRESS_INPUT, address)
        self.click(L.METRO_INPUT)
        self.fill(L.METRO_INPUT, metro)
        self.click(L.metro_option(metro))
        self.fill(L.PHONE_INPUT, phone)

    def click_next(self):
        self.click(L.NEXT_BUTTON)

    def fill_rental_form(self, date, period="сутки", color="black", comment=""):
        self.fill(L.DATE_INPUT, date)
        self.press_escape(L.DATE_INPUT)
        self.click(L.RENTAL_PERIOD_DROPDOWN)
        self.click(L.rental_period_option(period))
        if color == "black":
            self.click(L.COLOR_BLACK_CHECKBOX)
        else:
            self.click(L.COLOR_GREY_CHECKBOX)
        if comment:
            self.fill(L.COMMENT_INPUT, comment)

    def click_order(self):
        self.click(L.ORDER_BUTTON)

    def confirm_order(self):
        self.click(L.CONFIRM_YES_BUTTON)

    def get_success_text(self):
        return self.find_visible(L.SUCCESS_MODAL).text
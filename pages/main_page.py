from config import BASE_URL
from locators.main_page_locators import MainPageLocators as L
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, BASE_URL)

    def open_main(self):
        self.open()
        self.accept_cookies()

    def accept_cookies(self):
        buttons = self.find_all_optional(L.COOKIE_BUTTON)
        if buttons:
            buttons[0].click()

    def click_order_top(self):
        self.click(L.ORDER_TOP_BUTTON)

    def click_order_bottom(self):
        self.scroll_to(L.ORDER_BOTTOM_BUTTON)
        self.click(L.ORDER_BOTTOM_BUTTON)

    def click_faq_question(self, index):
        questions = self.find_all(L.FAQ_QUESTIONS)
        self.scroll_and_click(questions[index])

    def get_faq_answer_text(self, index):
        answers = self.find_all(L.FAQ_ANSWERS)
        return answers[index].text

    def click_scooter_logo(self):
        self.click(L.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(L.YANDEX_LOGO)
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"

    ORDER_TOP_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")

    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    FAQ_QUESTIONS = (By.XPATH, "//div[contains(@class, 'accordion__button')]")
    FAQ_ANSWERS = (By.XPATH, "//div[contains(@class, 'accordion__panel')]")

    def __init__(self, driver):
        super().__init__(driver, self.URL)

    def open_main(self):
        self.open()
        self.accept_cookies()

    def accept_cookies(self):
        buttons = self.driver.find_elements(*self.COOKIE_BUTTON)
        if buttons:
            buttons[0].click()

    def click_order_top(self):
        self.click(self.ORDER_TOP_BUTTON)

    def click_order_bottom(self):
        self.scroll_to(self.ORDER_BOTTOM_BUTTON)
        self.click(self.ORDER_BOTTOM_BUTTON)

    def click_faq_question(self, index):
        questions = self.driver.find_elements(*self.FAQ_QUESTIONS)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", questions[index]
        )
        questions[index].click()

    def get_faq_answer_text(self, index):
        answers = self.driver.find_elements(*self.FAQ_ANSWERS)
        return answers[index].text

    def get_faq_question_text(self, index):
        questions = self.driver.find_elements(*self.FAQ_QUESTIONS)
        return questions[index].text

    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
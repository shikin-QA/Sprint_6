from selenium.webdriver.common.by import By


class MainPageLocators:
    ORDER_TOP_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BOTTOM_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    FAQ_QUESTIONS = (By.XPATH, "//div[contains(@class, 'accordion__button')]")
    FAQ_ANSWERS = (By.XPATH, "//div[contains(@class, 'accordion__panel')]")
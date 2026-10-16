from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def find_all_optional(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_clickable(locator).click()

    def fill(self, locator, value):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(value)

    def press_escape(self, locator):
        self.find(locator).send_keys(Keys.ESCAPE)

    def scroll_to(self, locator):
        element = self.find(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        return element

    def scroll_and_click(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        element.click()

    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def get_current_url(self):
        return self.driver.current_url

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_new_tab(self, original_handle):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        for handle in self.driver.window_handles:
            if handle != original_handle:
                self.driver.switch_to.window(handle)
                return handle
        return None

    def wait_for_url_contains(self, substring):
        self.wait.until(EC.url_contains(substring))

    def wait_for_element_text(self, locator, text):
        self.wait.until(EC.text_to_be_present_in_element(locator, text))
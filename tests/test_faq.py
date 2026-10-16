import allure
import pytest

from data.faq_data import FAQ_DATA
from pages.main_page import MainPage


@allure.feature("Вопросы о важном")
class TestFaq:

    @allure.title("Открывается ответ на вопрос №{index}")
    @pytest.mark.parametrize("index, expected_text", FAQ_DATA)
    def test_faq_question(self, driver, index, expected_text):
        page = MainPage(driver)
        page.open_main()
        page.click_faq_question(index)
        answer = page.get_faq_answer_text(index)
        assert expected_text in answer
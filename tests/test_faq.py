import allure
import pytest

from pages.main_page import MainPage


@allure.feature("Вопросы о важном")
class TestFaq:

    @allure.title("Открывается ответ на вопрос №{index}")
    @pytest.mark.parametrize(
        "index, expected_text",
        [
            (0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
            (1, "Пока что у нас так: один заказ — один самокат."),
            (2, "Допустим, вы оформляете заказ на 8 мая."),
            (3, "Только начиная с завтрашнего дня."),
            (4, "Пока что нет!"),
            (5, "Самокат приезжает к вам с полной зарядкой."),
            (6, "Да, пока самокат не привезли."),
            (7, "Да, обязательно."),
        ]
    )
    def test_faq_question(self, driver, index, expected_text):
        page = MainPage(driver)
        page.open_main()
        page.click_faq_question(index)
        answer = page.get_faq_answer_text(index)
        assert expected_text in answer
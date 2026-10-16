import allure
import pytest

from config import BASE_URL
from data.order_data import ORDER_BOTTOM_DATA, ORDER_TOP_DATA
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Заказ через верхнюю кнопку: {name} {surname}")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, color",
        ORDER_TOP_DATA,
    )
    def test_order_via_top_button(
        self, driver, name, surname, address, metro, phone, date, color
    ):
        main = MainPage(driver)
        main.open_main()
        main.click_order_top()

        order = OrderPage(driver)
        order.fill_customer_form(name, surname, address, metro, phone)
        order.click_next()
        order.fill_rental_form(date=date, color=color)
        order.click_order()
        order.confirm_order()

        assert "Заказ оформлен" in order.get_success_text()

    @allure.title("Заказ через нижнюю кнопку: {name} {surname}")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, color",
        ORDER_BOTTOM_DATA,
    )
    def test_order_via_bottom_button(
        self, driver, name, surname, address, metro, phone, date, color
    ):
        main = MainPage(driver)
        main.open_main()
        main.click_order_bottom()

        order = OrderPage(driver)
        order.fill_customer_form(name, surname, address, metro, phone)
        order.click_next()
        order.fill_rental_form(date=date, color=color)
        order.click_order()
        order.confirm_order()

        assert "Заказ оформлен" in order.get_success_text()


@allure.feature("Логотипы")
class TestLogos:

    @allure.title("Клик по логотипу Самоката ведёт на главную")
    def test_scooter_logo_redirects_to_main(self, driver):
        main = MainPage(driver)
        main.open_main()
        main.click_scooter_logo()
        main.wait_for_url_contains(BASE_URL)
        assert BASE_URL in main.get_current_url()

    @allure.title("Клик по логотипу Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo_opens_dzen(self, driver):
        main = MainPage(driver)
        main.open_main()

        original_handle = main.get_current_window_handle()
        main.click_yandex_logo()
        main.switch_to_new_tab(original_handle)
        main.wait_for_url_contains("dzen.ru")

        assert "dzen.ru" in main.get_current_url()
import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Заказ через верхнюю кнопку: {name} {surname}")
    @pytest.mark.parametrize(
        "name, surname, address, metro, phone, date, color",
        [
            ("Иван", "Иванов", "Москва, Ленина 1", "Черкизовская",
             "+79001234567", "15.05.2025", "black"),
            ("Пётр", "Петров", "Москва, Тверская 5", "Сокольники",
             "+79007654321", "20.06.2025", "grey"),
        ]
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
        [
            ("Анна", "Смирнова", "Москва, Арбат 10", "Смоленская",
             "+79001112233", "18.05.2025", "black"),
            ("Олег", "Кузнецов", "Москва, Пресня 8", "Выставочная",
             "+79004445566", "22.06.2025", "grey"),
        ]
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
        assert main.URL in driver.current_url

    @allure.title("Клик по логотипу Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo_opens_dzen(self, driver):
        main = MainPage(driver)
        main.open_main()

        original_tab = driver.current_window_handle
        main.click_yandex_logo()

        # ждём появления новой вкладки
        import time
        time.sleep(2)

        tabs = driver.window_handles
        assert len(tabs) > 1

        new_tab = [t for t in tabs if t != original_tab][0]
        driver.switch_to.window(new_tab)
        driver.implicitly_wait(5)
        assert "dzen.ru" in driver.current_url
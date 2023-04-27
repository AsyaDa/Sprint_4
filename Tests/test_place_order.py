import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.main_page import MainPage
from Pages.order_page import OrderPage


class TestPlaceOrder:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title("Проверка перехода по клику на кнопку Заказать сверху")
    def test_go_to_order_page_first_button(self):
        self.driver.get(MainPage.url)
        mp = MainPage(self.driver)
        mp.click_on_accept_cookie_button()
        mp.click_on_order_button(MainPage.order_button_first)
        assert WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(OrderPage.order_page_header))

    @allure.title("Проверка перехода по клику на кнопку Заказать снизу")
    def test_go_to_order_page_second_button(self):
        self.driver.get(MainPage.url)
        mp = MainPage(self.driver)
        mp.click_on_accept_cookie_button()
        mp.click_on_order_button(MainPage.order_button_second)
        assert WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(OrderPage.order_page_header))

    @allure.title("Проверка размещения заказа на самокат")
    @pytest.mark.parametrize('name, surname, address, metro, telephone, period, comment, color, date', [
        ["Ася", "Дамбиш", "Москва, ул Ленина, 1", "Сокольники", "89998887755", "сутки", "тестовый комментарий для курьера", "black", "23.04.2023"],
        ["Иван", "Петров", "Москва, ул Первая 2", "Черкизовская", "81112227755", "двое суток", "другой тестовый комментарий для курьера", "grey", "24.04.2023"],
    ])
    def test_place_order(self, name, surname, address, metro, telephone, period, comment, color, date):
        self.driver.get(OrderPage.url_place_order)
        page = OrderPage(self.driver)
        page.set_order_info(name, surname, address, metro, telephone)
        page.click_on_next_step_button()
        page.set_arenda_info(period, comment, color, date)
        page.click_on_place_order_button()
        page.click_on_confirm_order_button()
        t = page.get_place_order_status_text()
        assert 'Заказ оформлен' in t

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

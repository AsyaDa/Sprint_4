import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from Pages.main_page import MainPage
from Pages.base_page import BasePage
from Pages.order_page import OrderPage
from selenium.webdriver.support.wait import WebDriverWait


class TestQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title("Проверка ответа по клику на вопрос")
    @pytest.mark.parametrize('question_button, question_answer', [
        [MainPage.question_1_button, MainPage.question_1_answer],
        [MainPage.question_2_button, MainPage.question_2_answer],
        [MainPage.question_3_button, MainPage.question_3_answer],
        [MainPage.question_4_button, MainPage.question_4_answer],
        [MainPage.question_5_button, MainPage.question_5_answer],
        [MainPage.question_6_button, MainPage.question_6_answer],
        [MainPage.question_7_button, MainPage.question_7_answer],
        [MainPage.question_8_button, MainPage.question_8_answer],
    ])
    def test_question(self, question_button, question_answer):
        self.driver.get(MainPage.url)
        mp = MainPage(self.driver)
        mp.click_on_question_panel(question_button)
        assert WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(question_answer))

    @allure.title("Проверка перехода по клику на логотип Яндекса")
    def test_go_to_yandex(self):
        self.driver.get(MainPage.url)
        bp = BasePage(self.driver)
        bp.click_on_yandex_logo(BasePage.yandex_logo)
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'content')))
        current_url = self.driver.current_url
        assert current_url == 'https://dzen.ru/?yredirect=true'

    @allure.title("Проверка перехода по клику на логотип Самоката")
    def test_go_to_scooter_main_page(self):
        self.driver.get(OrderPage.url_place_order)
        bp = BasePage(self.driver)
        bp.click_on_scooter_logo(BasePage.scooter_logo)
        current_url = self.driver.current_url
        assert current_url == MainPage.url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

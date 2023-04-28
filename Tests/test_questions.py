import pytest
import allure
from Pages.main_page import MainPage
from Pages.order_page import OrderPage


class TestQuestions:

    @allure.title("Проверка ответа по клику на вопрос")
    @pytest.mark.parametrize('question_button, question_answer, question_correct_answer', [
        [MainPage.question_1_button, MainPage.question_1_answer, MainPage.question_1_correct_answer],
        [MainPage.question_2_button, MainPage.question_2_answer, MainPage.question_2_correct_answer],
        [MainPage.question_3_button, MainPage.question_3_answer, MainPage.question_3_correct_answer],
        [MainPage.question_4_button, MainPage.question_4_answer, MainPage.question_4_correct_answer],
        [MainPage.question_5_button, MainPage.question_5_answer, MainPage.question_5_correct_answer],
        [MainPage.question_6_button, MainPage.question_6_answer, MainPage.question_6_correct_answer],
        [MainPage.question_7_button, MainPage.question_7_answer, MainPage.question_7_correct_answer],
        [MainPage.question_8_button, MainPage.question_8_answer, MainPage.question_8_correct_answer],
    ])
    def test_question(self, question_button, question_answer, question_correct_answer, entry):
        self.driver = entry
        mp = MainPage(self.driver)
        mp.click_on_question_panel(question_button)
        assert mp.get_answer_text_from_panel(question_answer) == question_correct_answer

    @allure.title("Проверка перехода по клику на логотип Яндекса")
    def test_go_to_yandex(self, entry):
        self.driver = entry
        mp = MainPage(self.driver)
        mp.click_on_yandex_logo(MainPage.yandex_logo)
        mp.go_to_new_window_with_yandex_and_wait()
        current_url = self.driver.current_url
        assert current_url == 'https://dzen.ru/?yredirect=true'

    @allure.title("Проверка перехода по клику на логотип Самоката")
    def test_go_to_scooter_main_page(self, entry):
        self.driver = entry
        self.driver.get(OrderPage.url_place_order)
        mp = MainPage(self.driver)
        mp.click_on_scooter_logo(MainPage.scooter_logo)
        current_url = self.driver.current_url
        assert current_url == MainPage.url


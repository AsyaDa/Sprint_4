import allure
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class MainPage:
    order_button_first = [By.XPATH, './/button[@class="Button_Button__ra12g"]']
    order_button_second = [By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/child::button']
    url = 'https://qa-scooter.praktikum-services.ru/'
    accept_cookie_button = [By.ID, 'rcc-confirm-button']
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    yandex_page_content = [By.CLASS_NAME, 'content']

    question_1_button = [By.ID, 'accordion__heading-0']
    question_2_button = [By.ID, 'accordion__heading-1']
    question_3_button = [By.ID, 'accordion__heading-2']
    question_4_button = [By.ID, 'accordion__heading-3']
    question_5_button = [By.ID, 'accordion__heading-4']
    question_6_button = [By.ID, 'accordion__heading-5']
    question_7_button = [By.ID, 'accordion__heading-6']
    question_8_button = [By.ID, 'accordion__heading-7']

    question_1_answer = [By.XPATH, '//div[@id="accordion__panel-0"]/p']
    question_2_answer = [By.XPATH, '//div[@id="accordion__panel-1"]/p']
    question_3_answer = [By.XPATH, '//div[@id="accordion__panel-2"]/p']
    question_4_answer = [By.XPATH, '//div[@id="accordion__panel-3"]/p']
    question_5_answer = [By.XPATH, '//div[@id="accordion__panel-4"]/p']
    question_6_answer = [By.XPATH, '//div[@id="accordion__panel-5"]/p']
    question_7_answer = [By.XPATH, '//div[@id="accordion__panel-6"]/p']
    question_8_answer = [By.XPATH, '//div[@id="accordion__panel-7"]/p']

    question_1_correct_answer = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    question_2_correct_answer = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    question_3_correct_answer = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    question_4_correct_answer = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    question_5_correct_answer = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    question_6_correct_answer = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    question_7_correct_answer = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    question_8_correct_answer = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на панель с вопросом')
    def click_on_question_panel(self, question_button):
        element = self.driver.find_element(*question_button)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Кликаем на кнопку размещения заказа {order_button}')
    def click_on_order_button(self, order_button):
        self.driver.find_element(*order_button).click()

    @allure.step('Кликаем на кнопку и принимаем использование куки')
    def click_on_accept_cookie_button(self):
        self.driver.find_element(*self.accept_cookie_button).click()

    @allure.step('Получаем текст ответа на вопрос')
    def get_answer_text_from_panel(self, question_answer):
        bp = BasePage(self.driver)
        bp.wait_visibility_of_element(question_answer)
        a = self.driver.find_element(*question_answer).text
        return a

    @allure.step('Кликаем на логотип Яндекс')
    def click_on_yandex_logo(self, yandex_logo):
        self.driver.find_element(*yandex_logo).click()

    @allure.step('Переключаемся на новое окно в браузере и ждем загрузку страницы Яндекса')
    def go_to_new_window_with_yandex_and_wait(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        bp = BasePage(self.driver)
        bp.wait_element(self.yandex_page_content)

    @allure.step('Кликаем на логотип Самокат')
    def click_on_scooter_logo(self, scooter_logo):
        self.driver.find_element(*scooter_logo).click()
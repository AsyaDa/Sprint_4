from selenium.webdriver.common.by import By


class MainPage:
    order_button_first = [By.XPATH, './/button[@class="Button_Button__ra12g"]']
    order_button_second = [By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/child::button']
    url = 'https://qa-scooter.praktikum-services.ru/'
    accept_cookie_button = [By.ID, 'rcc-confirm-button']

    question_1_button = [By.ID, 'accordion__heading-0']
    question_2_button = [By.ID, 'accordion__heading-1']
    question_3_button = [By.ID, 'accordion__heading-2']
    question_4_button = [By.ID, 'accordion__heading-3']
    question_5_button = [By.ID, 'accordion__heading-4']
    question_6_button = [By.ID, 'accordion__heading-5']
    question_7_button = [By.ID, 'accordion__heading-6']
    question_8_button = [By.ID, 'accordion__heading-7']

    question_1_answer = [By.ID, 'accordion__panel-0']
    question_2_answer = [By.ID, 'accordion__panel-1']
    question_3_answer = [By.ID, 'accordion__panel-2']
    question_4_answer = [By.ID, 'accordion__panel-3']
    question_5_answer = [By.ID, 'accordion__panel-4']
    question_6_answer = [By.ID, 'accordion__panel-5']
    question_7_answer = [By.ID, 'accordion__panel-6']
    question_8_answer = [By.ID, 'accordion__panel-7']

    def __init__(self, driver):
        self.driver = driver

    def click_on_question_panel(self, question_button):
        element = self.driver.find_element(*question_button)
        self.driver.execute_script("arguments[0].click();", element)

    def click_on_order_button(self, order_button):
        self.driver.find_element(*order_button).click()

    def click_on_accept_cookie_button(self):
        self.driver.find_element(*self.accept_cookie_button).click()

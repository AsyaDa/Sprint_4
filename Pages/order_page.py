from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage:
    order_page_header = [By.CLASS_NAME, 'Order_Header__BZXOb']
    name_field = [By.XPATH, '//input[@placeholder="* Имя"]']
    surname_field = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    address_field = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_field = [By.XPATH, '//input[@placeholder="* Станция метро"]']
    telephone_field = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    next_step_button = [By.XPATH, '//button[text()="Далее"]']
    url_place_order = "https://qa-scooter.praktikum-services.ru/order"
    header_arenda = [By.XPATH, './/div[text()="Про аренду"]']
    arenda_period_field = [By.XPATH, '//div[text()="* Срок аренды"]']
    #arenda_period = [By.XPATH, '//div[text()="сутки"]']
    # scooter_color = [By.ID, 'black']
    comment_field = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']
    start_date_field = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    place_order_button = [By.XPATH, '//button[text()="Назад"]/following-sibling::button']
    confirm_order_button = [By.XPATH, '//button[text()="Да"]']
    order_info_header = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"]

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    def set_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    def set_metro(self, metro):
        self.driver.find_element(*self.metro_field).click()
        self.driver.find_element(By.XPATH, f'//div[text()="{metro}"]/parent::button').click()

    def set_telephone(self, telephone):
        self.driver.find_element(*self.telephone_field).send_keys(telephone)

    def set_order_info(self, name, surname, address, metro, telephone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_telephone(telephone)

    def click_on_next_step_button(self):
        self.driver.find_element(*self.next_step_button).click()

    def set_arenda_period(self, period):
        self.driver.find_element(*self.arenda_period_field).click()
        self.driver.find_element(By.XPATH, f'//div[text()="{period}"]').click()

    def set_scooter_color(self, color):
        self.driver.find_element(By.ID, color).click()

    def set_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    def set_start_date(self, start_date):
        self.driver.find_element(*self.start_date_field).click()
        self.driver.find_element(*self.start_date_field).send_keys(start_date)

    def set_arenda_info(self, period, comment, color, start_date):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, './/div[text()="Про аренду"]')))
        self.set_arenda_period(period)
        self.set_scooter_color(color)
        self.set_start_date(start_date)
        self.set_comment(comment)

    def click_on_place_order_button(self):
        self.driver.find_element(*self.place_order_button).click()

    def click_on_confirm_order_button(self):
        self.driver.find_element(*self.confirm_order_button).click()

    def get_place_order_status_text(self):
        a = self.driver.find_element(*self.order_info_header).text
        return a

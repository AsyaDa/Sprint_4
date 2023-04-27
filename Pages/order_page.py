import allure
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
    comment_field = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']
    start_date_field = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    place_order_button = [By.XPATH, '//button[text()="Назад"]/following-sibling::button']
    confirm_order_button = [By.XPATH, '//button[text()="Да"]']
    order_info_header = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"]

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вводим имя {name}')
    def set_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    @allure.step('Вводим фамилию {surname}')
    def set_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    @allure.step('Вводим адрес {address}')
    def set_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    @allure.step('Выбираем станцию метро {metro}')
    def set_metro(self, metro):
        self.driver.find_element(*self.metro_field).click()
        self.driver.find_element(By.XPATH, f'//div[text()="{metro}"]/parent::button').click()

    @allure.step('Вводим номер телефона {telephone}')
    def set_telephone(self, telephone):
        self.driver.find_element(*self.telephone_field).send_keys(telephone)

    def set_order_info(self, name, surname, address, metro, telephone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_telephone(telephone)

    @allure.step('Кликаем на кнопку Далее')
    def click_on_next_step_button(self):
        self.driver.find_element(*self.next_step_button).click()

    @allure.step('Выбираем длительность аренды {period}')
    def set_arenda_period(self, period):
        self.driver.find_element(*self.arenda_period_field).click()
        self.driver.find_element(By.XPATH, f'//div[text()="{period}"]').click()

    @allure.step('Выбираем цвет самоката {color}')
    def set_scooter_color(self, color):
        self.driver.find_element(By.ID, color).click()

    @allure.step('Вводим комментарий для курьера {comment}')
    def set_comment(self, comment):
        self.driver.find_element(*self.comment_field).send_keys(comment)

    @allure.step('Выбираем дату начала аренды {start_date}')
    def set_start_date(self, start_date):
        self.driver.find_element(*self.start_date_field).click()
        self.driver.find_element(*self.start_date_field).send_keys(start_date)

    def set_arenda_info(self, period, comment, color, start_date):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, './/div[text()="Про аренду"]')))
        self.set_arenda_period(period)
        self.set_scooter_color(color)
        self.set_start_date(start_date)
        self.set_comment(comment)

    @allure.step('Кликаем на кнопку Разместить заказ')
    def click_on_place_order_button(self):
        self.driver.find_element(*self.place_order_button).click()

    @allure.step('Кликаем на кнопку Да')
    def click_on_confirm_order_button(self):
        self.driver.find_element(*self.confirm_order_button).click()

    @allure.step('Получаем статус размещенного заказа')
    def get_place_order_status_text(self):
        a = self.driver.find_element(*self.order_info_header).text
        return a

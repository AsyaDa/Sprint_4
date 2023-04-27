import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']

    @allure.step('Открываем браузер Firefox')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на логотип Яндекс и переключаемся на страницу')
    def click_on_yandex_logo(self, yandex_logo):
        self.driver.find_element(*yandex_logo).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'content')))

    @allure.step('Кликаем на логотип Самокат')
    def click_on_scooter_logo(self, scooter_logo):
        self.driver.find_element(*scooter_logo).click()

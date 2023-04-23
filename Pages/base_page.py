from selenium.webdriver.common.by import By


class BasePage:
    yandex_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']

    def __init__(self, driver):
        self.driver = driver

    def click_on_yandex_logo(self, yandex_logo):
        self.driver.find_element(*yandex_logo).click()

    def click_on_scooter_logo(self, scooter_logo):
        self.driver.find_element(*scooter_logo).click()

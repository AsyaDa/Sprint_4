from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))

    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

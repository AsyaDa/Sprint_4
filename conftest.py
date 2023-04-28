import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

url = 'https://qa-scooter.praktikum-services.ru/'


@pytest.fixture(scope='function')
def driver():
    browser = webdriver.Firefox()
    browser.get(url)
    WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'Home_HomePage__ZXKIX')))

    yield browser
    browser.quit()


import pytest
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions


@pytest.fixture(scope='function')
def browser():
    driver_oprion = ChromeOptions()
    driver_oprion.add_argument('--headless')
    #driver_oprion.add_argument("--start-maximized")
    driver = Chrome(options=driver_oprion)
    yield driver
    driver.quit()

def request(url):
    URL = "https://reqres.in/"
    return URL+url


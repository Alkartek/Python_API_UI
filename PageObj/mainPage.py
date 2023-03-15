from selenium.webdriver.common.by import By

from base_page import BasePage






class ResponseLocator:
    LOCATOR_RES1 = (By.XPATH, '//div[@class="response"]')
    LOCATOR_API1 = (By.XPATH, "//a[contains(text(),'List users')]")
    page = (By.XPATH, "//span[contains(text(),'/api/users?page=2')]")

class mainPage(BasePage):
    def responseGet1(self, LOCATOR_1, LOCATOR_2):
        element = self.find_element(LOCATOR_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        element1 = self.find_element(LOCATOR_2)
        #element1.click()

    def responseGet2(self, LOCATOR_1, LOCATOR_2):
        element = self.find_element(LOCATOR_1)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        element1 = self.find_element(LOCATOR_2)
        element1.click()
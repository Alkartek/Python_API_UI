from selenium.webdriver.common.by import By
from base_page import BasePage

class LOcator:
    only_loc = (By.XPATH, "//pre[@data-key='output-response']")
    only_loc2 = (By.XPATH, "//pre")

class Getter(BasePage):
    def getText(self):
        return self.find_element(LOcator.only_loc).text

    def getText2(self):
        return self.find_element(LOcator.only_loc2).text





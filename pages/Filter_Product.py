import time

from selenium.webdriver.common.by import By

from Locator.locator import Locate

class FilterProduct:
    def __init__(self, driver):
        self.driver = driver
        self.lp = Locate()

    def filter_function(self):
        image_name = self.driver.find_elements(By.XPATH, self.lp.image_xpath)
        image_name[0].click()
        time.sleep(1)
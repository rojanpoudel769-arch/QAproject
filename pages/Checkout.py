import time

from selenium.webdriver.common.by import By
from Locator.locator import Locate

class Checkout:
    def __init__(self, driver):
        self.driver = driver
        self.lc = Locate()

    def checkout_function(self):
        checkout = self.driver.find_element(By.XPATH, self.lc.checkout_xpath)
        checkout.click()
        time.sleep(2)
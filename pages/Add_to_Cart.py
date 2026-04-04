import time

from selenium.webdriver.common.by import By

from Locator.locator import Locate

class AddCart:
    def __init__ (self, driver):
        self.driver = driver
        self.lp = Locate()

    def addcart_function(self):
        add_cart = self.driver.find_element(By.XPATH, self.lp.cart_xpath)
        add_cart.click()
        time.sleep(3)
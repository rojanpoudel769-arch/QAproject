import time

from selenium.webdriver.common.by import By

from locator.Locator import Locate

class AddCart:
    def init(self, driver):
        self.driver = driver
        self.lp = Locate()

    def addcart_function(self):
        add_cart = self.driver.find_element(By.XPATH, self.lp.cart_xpath)
        add_cart.click()
        time.sleep(2)
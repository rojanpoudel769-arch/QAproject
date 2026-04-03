import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Locator.locator import Locate

class Search:
    def __init__(self,driver):
        self.driver = driver
        self.lp = Locate()

    def search_function(self, product_name):
        search_box = self.driver.find_element(By.XPATH, self.lp.search_xpath)
        search_box.clear()     # clear() is a Selenium method used to remove existing text from an input field before typing new text
        search_box.send_keys(product_name)

        # Press ENTER from keyboard
        search_box.send_keys(Keys.ENTER)
        time.sleep(1)
import time

from selenium.webdriver.common.by import By

from Locator.locator import Locate

class Check:
    def __init__(self, driver):
        self.driver = driver
        self.lc = Locate()

    def check_function(self):
        checkout2 = self.driver.find_element(By.XPATH, self.lc.checkout2_xpath)
        checkout2.click()

        continue1 = self.driver.find_element(By.XPATH, self.lc.continue1_xpath)
        continue1.click()

        continue2 = self.driver.find_element(By.XPATH, self.lc.continue2_xpath)
        continue2.click()
        time.sleep(2)

        cash = self.driver.find_element(By.XPATH, self.lc.cash_xpath)
        cash.click()

        agree = self.driver.find_element(By.XPATH, self.lc.agree_xpath)
        agree.click()

        placeorder = self.driver.find_element(By.XPATH, self.lc.placeorder_xpath)
        placeorder.click()

        time.sleep(2)

        indeximage = self.driver.find_element(By.XPATH, self.lc.indeximage_xpath)
        indeximage.click()

        time.sleep(3)
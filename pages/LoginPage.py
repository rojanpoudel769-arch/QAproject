from Locator.locator import Locate
from selenium.webdriver.common.by import By

import time

class LoginPage:
    def __init__ (self, driver):
        self.driver = driver
        self.lc = Locate()


    def login_function(self,email, password):
        login = self.driver.find_element(By.XPATH, self.lc.login_xpath)
        login.click()
        time.sleep(2)
        email_field = self.driver.find_element(By.ID, self.lc.email_id)
        email_field.send_keys(email)
        password_field = self.driver.find_element(By.ID, self.lc.password_id)
        password_field.send_keys(password)
        submit = self.driver.find_element(By.ID, self.lc.submit_id)
        submit.click()
        time.sleep(1)
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.LoginPage import LoginPage

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qah.bishalkarki.com/")
        self.lp = LoginPage(self.driver)


    def test_login(self):
        try:
            self.lp.login_function(email="msangam994@gmail.com", password="SamG@m12#4")
            time.sleep(1)
            expectedresult = "sangam magar"
            actualresult = self.driver.find_element(By.XPATH, "/html/body/main/header/nav/div/div/div[1]/div[2]/div[1]/div/a[2]/span").text
            self.assertEqual(expectedresult, actualresult, msg="Login failed: Expected result isn't equal to actual result")

        except Exception as e:
            self.fail("Login failed: " + str(e))


if __name__ == '__main__':
    unittest.main()
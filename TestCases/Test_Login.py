import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage

from pages.Search import Search

from pages.Filter_Product import FilterProduct

from pages.Add_to_Cart import AddCart

from pages.Checkout import Checkout

from pages.SecondCheckout import Check

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qah.bishalkarki.com/")
        self.lp = LoginPage(self.driver)

        self.sh = Search(self.driver)

        self.fp = FilterProduct(self.driver)

        self.ac = AddCart(self.driver)

        self.co = Checkout(self.driver)

        self.c = Check(self.driver)


    def test_login(self):
        try:
            self.lp.login_function(email="msangam994@gmail.com", password="SamG@m12#4")
            time.sleep(1)
            expectedresult = "sangam magar"
            actualresult = self.driver.find_element(By.XPATH, "/html/body/main/header/nav/div/div/div[1]/div[2]/div[1]/div/a[2]/span").text
            self.assertEqual(expectedresult, actualresult, msg="Login failed: Expected result isn't equal to actual result")

            self.sh.search_function(product_name="mug")


            self.fp.filter_function()

            self.ac.addcart_function()

            self.co.checkout_function()

            self.c.check_function()

        except Exception as e:
            self.fail("Login failed: " + str(e))


if __name__ == '__main__':
    unittest.main()
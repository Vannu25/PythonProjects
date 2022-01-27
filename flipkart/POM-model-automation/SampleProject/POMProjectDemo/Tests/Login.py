from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from SampleProject.POMProjectDemo.Pages.loginPage import LoginPage
from SampleProject.POMProjectDemo.Pages.homePage import HomePage
from SampleProject.POMProjectDemo.Pages.newAddress import NewAddrPage
from SampleProject.POMProjectDemo.Pages.paymentPage import PaymentPage
from SampleProject.POMProjectDemo.Pages.productPage import PoductPage
from SampleProject.POMProjectDemo.Pages.buyNow import BuyNowPage

class LoginTest(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
       driver = self.driver
       driver.get("https://www.flipkart.com/")

       login = LoginPage(driver)
       login.enter_username("9763445184")
       login.enter_password("Vannu@510")
       login.click_login()
       time.sleep(4)

       homepage = HomePage(driver)
       homepage.enter_search("iphone13")

       homepage.click_verify()
       time.sleep(4)

       productpage = PoductPage(driver)
       productpage.click_iphone()
       time.sleep(4)

       parentHandle = driver.current_window_handle

       all_handles = driver.window_handles
       print(all_handles)

       for handle in all_handles:
           if handle != parentHandle:
               driver.switch_to.window(handle)
               buynow = BuyNowPage(driver)
               buynow.click_iphone()
               time.sleep(4)
               break

       newaddr = NewAddrPage(driver)
       newaddr.click_change()
       newaddr.click_edit()
       time.sleep(2)
       newaddr.enter_name("Test Automation")
       newaddr.enter_number("9999999999")
       newaddr.enter_pincode("411013")
       newaddr.enter_locality("Dummy")
       newaddr.enter_address("Neova Solutions Pvt Ltd")
       time.sleep(2)
       newaddr.click_address_type()
       time.sleep(2)
       newaddr.save_address_details()
       time.sleep(2)
       newaddr.click_continue()
       time.sleep(2)

       payment = PaymentPage(driver)
       # payment.click_next()
       payment.payment_upi()
       time.sleep(2)
       payment.continue_next()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__=='__main__':
    unittest.main
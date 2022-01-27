import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login


class Test_001_Login:
    baseURL = "https://www.flipkart.com/"
    username = "9763445184"
    password = "Vannu@510"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)  #object created

        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "//div[text()='My Account']":
            assert True
        else:
            assert False

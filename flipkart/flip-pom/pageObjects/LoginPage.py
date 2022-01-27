from selenium import webdriver

class Login:
    textbox_user_xpath = "//input[@class='_2IX_2- VJZDxU']"
    textbox_password_xpath = "//input[@class='_2IX_2- _3mctLh VJZDxU']"
    button_login = "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']"


    def __init__(self, driver):              #python constructor
        self.driver = driver

    def setUserName(self, username):
        # self.driver.find_element_by_xpath(self.textbox_user_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_user_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickLogin(self, login):
        self.driver.find_element_by_xpath(self.button_login).click()

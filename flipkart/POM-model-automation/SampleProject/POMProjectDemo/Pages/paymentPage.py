class PaymentPage():
    def __init__(self, driver):
        self.driver = driver

        # self.proceed_payment_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div[5]/span[2]/button"
        self.select_payment_type_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[4]/div/div/div[1]/div/label[1]/div[2]/div/div/div[3]/label[1]/div[1]"
        self.select_next_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[4]/div/div/div[1]/div/label[1]/div[2]/div/div/div[3]/label[1]/div[2]/div/button"

    # def click_next(self):
    #     self.driver.find_element_by_xpath(self.proceed_payment_xpath).click()

    def payment_upi(self):
        self.driver.find_element_by_xpath(self.select_payment_type_xpath).click()

    def continue_next(self):
        self.driver.find_element_by_xpath(self.select_next_xpath).click()
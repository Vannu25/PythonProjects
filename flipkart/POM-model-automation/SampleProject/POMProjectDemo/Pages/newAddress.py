
class NewAddrPage():
    def __init__(self, driver):
        self.driver = driver

        self.select_change_button_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/button"
        self.select_edit_button_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/img"
        self.name_textbox_xpath ="//input[@name='name']"
        self.number_textbox_xpath = "//input[@name='phone']"
        self.pincode_textbox_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[3]/div[1]/input"
        self.locality_textbox_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[3]/div[2]/input"
        self.address_textbox_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[4]/div/div[1]/textarea"
        self.address_type_textbox_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[7]/div/div/label[2]/div[1]"
        self.save_textbox_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[8]/button"
        self.continue_next_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div[5]/span[2]/button"

    def click_change(self):
        self.driver.find_element_by_xpath(self.select_change_button_xpath).click()

    def click_edit(self):
        self.driver.find_element_by_xpath(self.select_edit_button_xpath).click()

    def enter_name(self, name):

        self.driver.find_element_by_xpath(self.name_textbox_xpath).send_keys(name)

    def enter_number(self, number):
        self.driver.find_element_by_xpath(self.number_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.number_textbox_xpath).send_keys(number)

    def enter_pincode(self, pincode):
        self.driver.find_element_by_xpath(self.pincode_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.pincode_textbox_xpath).send_keys(pincode)

    def enter_locality(self, locality):
        self.driver.find_element_by_xpath(self.locality_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.locality_textbox_xpath).send_keys(locality)

    def enter_address(self, address):
        self.driver.find_element_by_xpath(self.address_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.address_textbox_xpath).send_keys(address)

    def click_address_type(self):

        self.driver.find_element_by_xpath(self.address_type_textbox_xpath).click()

    def save_address_details(self):
        self.driver.find_element_by_xpath(self.save_textbox_xpath).click()

    def click_continue(self):
        self.driver.find_element_by_xpath(self.continue_next_xpath).click()



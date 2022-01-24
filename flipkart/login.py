from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
pWindow = driver.current_window_handle
driver.get("https://www.flipkart.com/")
time.sleep(1)
phone = driver.find_element(By.XPATH, "//input[@class='_2IX_2- VJZDxU']").send_keys("9763445184")
password = driver.find_element(By.XPATH, "//input[@class='_2IX_2- _3mctLh VJZDxU']").send_keys("Vannu@510")
login = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2HKlqd _3AWRsL']").click()
time.sleep(2)
assert driver.find_element(By.XPATH, "//div[text()='My Account']").is_displayed() == True    #login_verification
time.sleep(2)
search = driver.find_element(By.XPATH, "//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
search.send_keys('iphone 13')
time.sleep(2)
searchbutton = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/button").click()
time.sleep(2)
product = driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]").click()
time.sleep(2)
#no such element error as new iframe/window
handles = []
handles = driver.window_handles

for handle in handles:
    print(handle)
newHandle = handles[1]       #switching window index to 1 as current is 0
driver.switch_to.window(newHandle)
buy_product = driver.find_element(By.XPATH, "//body/div[@id='container']/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/form[1]/button[1]").click()
time.sleep(2)
user_name = driver.find_element(By.XPATH, "//input[@class='_1w3ZZo _2mFmU7']").send_keys("Test Automation")
time.sleep(2)
mob_num = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[2]/div[2]/input").send_keys("9999999999")
time.sleep(1)
pin_code = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[3]/div[1]/input").send_keys("411013 ")
time.sleep(1)
locality = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[3]/div[2]/input").send_keys("Dummy")
time.sleep(1)
address = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[4]/div/div[1]/textarea")
address.send_keys("Neova Solutions Pvt Ltd")
time.sleep(1)
# city = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[5]/div[1]/div[1]/input").send_keys("Pune")
# time.sleep(1)
element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[5]/div[2]/div/div[2]/select")
drop_down = Select(element)
drop_down.select_by_visible_text('Maharashtra')  #selcet by visible text
time.sleep(1)
place_type = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[7]/div/div/label[2]/div[1]").click()
time.sleep(2)
save_details = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/label/div[2]/div/form/div/div[8]/button").click()
time.sleep(2)
# email = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div[5]/span[1]/form/input").send_keys("vanubandla25@gmail.com")
# time.sleep(2)
proceed = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div/div/div[5]/span[2]/button").click()
time.sleep(1)
handles = []
handles = driver.window_handles

for handle in handles:
    print(handle)
newHandle = handles[1]
time.sleep(2)
payment_upi = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[4]/div/div/div[1]/div/label[1]/div[2]/div/div/div[3]/label[1]/div[1]").click()
time.sleep(1)
process = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/div[4]/div/div/div[1]/div/label[1]/div[2]/div/div/div[3]/label[1]/div[2]/div/button").click()
time.sleep(2)
assert driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div[1]/h1").is_displayed() == True
print('automation successfully done')

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from framework1.test_pages.login import Login

options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
initiate_login = Login(driver)
initiate_login.login_action()
time.sleep(2)
# Select a product and click on add to cart button.
items = driver.find_elements(By.XPATH,"//app-card-list/app-card")
print(len(items)) #4
for item in items:
    item_name = item.find_element(By.XPATH,"div/div/h4[@class='card-title']").text
    print(item_name) # Print all items text
    if item_name == "Blackberry":
        item.find_element(By.XPATH,"div/div/button[@class='btn btn-info']").click()
waitCheckoutButton = WebDriverWait(driver,10)
waitCheckoutButton.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div/ul/li/a[contains(text(),'Checkout')]")))
checkout_status = driver.find_element(By.XPATH,"//div/ul/li/a[contains(text(),'Checkout')]").text
get_data_list = checkout_status.split(" ")
print(get_data_list[2])
# Checkout and purchase
driver.find_element(By.XPATH,"//a[contains(text(),'Checkout')]").click()
driver.find_element(By.XPATH,"//button[contains(text(),'Checkout')]").click()
driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Noida,Uttar Pradesh,India")
driver_wait = WebDriverWait(driver,10)
driver_wait.until(expected_conditions.visibility_of_element_located((By.XPATH,"//div/label[@for='checkbox2']")))
driver.find_element(By.XPATH,"//div/label[@for='checkbox2']").click()
driver.find_element(By.XPATH,"//form/input[@type='submit']").click()
#get success message
success_msg = driver.find_element(By.XPATH,"//div[contains(@class,'alert-success')]").text
final_msg = success_msg.rstrip(":-).").split("\n")
print(final_msg[1].strip(" "))
time.sleep(5)


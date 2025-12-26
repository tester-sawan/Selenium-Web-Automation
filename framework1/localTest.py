import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from framework1.test_pages.login import Login

options = Options()
options.add_argument("--incognito")
driver = webdriver.Chrome(options=options)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
initiate_login = Login(driver)
initiate_login.login_action()
time.sleep(5)
# Select a product and click on add to cart button.
items = driver.find_elements(By.XPATH,"//app-card-list/app-card")
print(len(items)) #4
for item in items:
    item_name = item.find_element(By.XPATH,"div/div/h4[@class='card-title']").text
    print(item_name) # Print all items text
    if item_name == "Blackberry":
        item.find_element(By.XPATH,"div/div/button[@class='btn btn-info']").click()
checkout_status = driver.find_element(By.XPATH,"//div/ul/li/a[contains(text(),'Checkout')]").text
get_data_list = checkout_status.split(" ")
print(get_data_list[2])


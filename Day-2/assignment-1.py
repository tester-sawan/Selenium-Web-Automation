import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(2)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(2)
all_shown_items = driver.find_elements(By.XPATH,"//div[@class='products']/div")
#print(len(all_shown_items)) >>3
actual_items = []
for item in all_shown_items:
    name = item.find_element(By.XPATH,"h4[@class='product-name']").text
    actual_items.append(name)
print(f"The actual items in list is: {actual_items}")
expected_items = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]
assert actual_items == expected_items
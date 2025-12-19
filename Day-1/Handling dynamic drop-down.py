import time

from gi.overrides.keysyms import value
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
# Handle auto-suggestive drop-down
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(2)
dynamic_element = driver.find_elements(By.XPATH,"//ul/li[@class='ui-menu-item']/a") # This returns a list having all elements.
print(f"Total element found in list: {len(dynamic_element)}")
for value in dynamic_element:
    #print(value.text)
    if value.text == "India":
        value.click()
        break
else:
    print("Capture list not contains element like 'India'.")
selected_value = driver.find_element(By.ID,"autosuggest").get_attribute('value')
print(f"The selected value under Country drop-down is: {selected_value}")

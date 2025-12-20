# Locators are used to identify the web elements on the webpage so that selenium will interact with them.
# Locators are 1. name 2. id 3. class name 4. tag name 5. link text 6. Partial link text 7. css selector 8. xpath
# Two types of Xpath - 1. Absolute 2. Relative
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME,"name").send_keys("Sawan Kumar")
print(driver.find_element(By.NAME,"name").get_attribute("value"))
driver.find_element(By.NAME,"email").send_keys("sawankumar.qa@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()
# Handle drop-down
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
actual_success_msg = driver.find_element(By.CLASS_NAME,"alert-success").text
print(actual_success_msg)
#print("Success!" in actual_success_msg)
assert "Success!" in actual_success_msg
time.sleep(5)
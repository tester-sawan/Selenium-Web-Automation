import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
expected_url = "https://rahulshettyacademy.com/angularpractice/"
expected_title = "ProtoCommerce"
actual_title = driver.title
actual_url = driver.current_url
if actual_url==expected_url and actual_title==expected_title:
    print("Validation Pass. Test Continue.....")
    driver.find_element(By.NAME,"name").send_keys("Sawan Kumar")
    driver.find_element(By.NAME,"email").send_keys("demo@test.com")
    driver.find_element(By.ID,"exampleInputPassword1").send_keys("test1234")
# Handling drop-down
    dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
    dropdown.select_by_visible_text("Female")
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
else:
    print("Validation Failed. Check the Current url or Current title.")
    print(f"Current Title is: {actual_title} & Expected title is: {expected_title}")
    print(f"Current url is: {actual_url} & Expected url is: {expected_url}")
# Check whether form is submitted successfully or not
actual_success_message = driver.find_element(By.XPATH,"//div/div[@class = 'alert alert-success alert-dismissible']").text
expected_success_message = "The Form has been submitted successfully!."
if expected_success_message in actual_success_message:
    print("Form has been successfully submitted.")
else:
    print("Form has not successfully submitted.")
time.sleep(1)
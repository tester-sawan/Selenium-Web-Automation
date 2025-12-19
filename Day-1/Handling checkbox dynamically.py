from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# Handle checkbox dynamically
# Get all element using find.elements
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
#Check whether elements has been stored or not.
#print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        if checkbox.is_selected(): # Returns boolean value.
            print("Checkbox has been selected properly.")
            break
else:
    print("Requested value not found!")



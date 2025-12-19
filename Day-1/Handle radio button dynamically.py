from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radio_buttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
for radio_button in radio_buttons:
    if radio_button.get_attribute("value") == "radio3":
            radio_button.click()
            if radio_button.is_selected():
                print("Radio button has been selected.")
                break
else:
    print("Something went wrong!!")
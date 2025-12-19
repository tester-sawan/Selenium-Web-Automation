import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
name = "Sawan Kumar"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
#After clicking, there will be a java script popup which need to be handle.
# For this we need to switch from browser mode to alert mode using the below step.
alert = driver.switch_to.alert
#Grasp the alert message
alert_message = alert.text
print(alert_message)
# Check whether name is showing under the java script alert
assert name in alert_message
# Click on OK button
alert.accept()
time.sleep(4)
driver.find_element(By.ID,"name").send_keys(name)
time.sleep(2)
driver.find_element(By.ID,"confirmbtn").click()
time.sleep(2)
# Click cancel button in the java script alert.
alert.dismiss()
time.sleep(2)
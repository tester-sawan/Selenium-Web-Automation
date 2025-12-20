import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/#/auth/login")
#Maximize the page
driver.maximize_window()
#locators based on link text
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
#xpath using parent to child
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@test.com")
#xpath using parent to child
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("hello1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("hello1234")
#Xpath with the text name
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()
#Sleep time
time.sleep(2)
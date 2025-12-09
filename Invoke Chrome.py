import time
#Import for Selenium Webdriver
from selenium import webdriver
#Invoke Chrome Browser
driver = webdriver.Chrome()
# Invoking firefox
# driver = webdriver.Firefox()
# Opening any url
driver.get("https://rahulshettyacademy.com/")
# For maximizing the window
driver.maximize_window()
# Know the title of the page
print(f"The current page title is : {driver.title}")
# Know the current page url:
print(f"The current url is: {driver.current_url}")
time.sleep(2)
# Programe has been ended.
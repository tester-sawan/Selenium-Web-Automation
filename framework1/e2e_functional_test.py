import time
from framework1 import test_pages
from selenium.webdriver.common.by import By

from framework1.test_pages import login
from framework1.test_pages.login import Login
from framework1.test_pages.shopPage import ShopPage


def test_e2e(invoke_chrome):
    driver = invoke_chrome
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    initiate_login = Login(driver)
    initiate_login.login_action()
    addItem = ShopPage(driver)
    addItem.add_cart("Blackberry")
    addItem.get_checkout_count()
    time.sleep(5)
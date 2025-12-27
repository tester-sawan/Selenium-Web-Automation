import json
import time
from json import loads

import pytest

from framework1 import test_pages
from selenium.webdriver.common.by import By

from framework1.test_pages import login
from framework1.test_pages.checkout import Checkout_purchase
from framework1.test_pages.login import Login
from framework1.test_pages.shopPage import ShopPage

test_data_path = "../framework1/test_data/e2e_functional_test.json"
with open(test_data_path) as file:
    test_data = json.load(file)
    test_list = test_data["data"]
    print(test_list)
@pytest.mark.parametrize("test_data_item",test_list)
def test_e2e(invoke_chrome,test_data_item):
    driver = invoke_chrome
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    initiate_login = Login(driver)
    initiate_login.login_action(test_data_item['username'],test_data_item['password'])
    addItem = ShopPage(driver)
    addItem.add_cart(test_data_item['device_name'])
    addItem.get_checkout_count()
    addItem.gotocart()
    checkout_buy = Checkout_purchase(driver)
    checkout_buy.checkout_purchase("Noida,Uttar Pradesh")
    checkout_buy.get_success_message()
    time.sleep(5)
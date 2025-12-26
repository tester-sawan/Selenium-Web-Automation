from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ShopPage:
    def __init__(self,driver):
        self.driver = driver
        self.allItem = (By.XPATH, "//app-card-list/app-card")
        self.getEachItemName = (By.XPATH, "div/div/h4[@class='card-title']")
        self.addToCartbutton = (By.XPATH, "div/div/button[@class='btn btn-info']")
        self.cartButton = (By.XPATH, "//div/ul/li/a[contains(text(),'Checkout')]")
    def add_cart(self,device_name):
        items = self.driver.find_elements(*self.allItem)
        print(len(items))  # 4
        for item in items:
            item_name = item.find_element(*self.getEachItemName).text
            print(item_name)  # Print all items text
            if item_name == device_name:
                item.find_element(*self.addToCartbutton).click()
                break
    def get_checkout_count(self):
        self.driver.implicitly_wait(2)

        checkout_text = self.driver.find_element(*self.cartButton).text
        checkout_text_split= self.checkout_status.split(" ")
        print(checkout_text_split[2])





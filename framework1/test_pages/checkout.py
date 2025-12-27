from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkout_purchase:
    def __init__(self,driver):
        self.driver = driver
        self.cart = (By.XPATH, "//a[contains(text(),'Checkout')]")
        self.checkout = (By.XPATH, "//button[contains(text(),'Checkout')]")
        self.address = (By.CSS_SELECTOR, "#country")
        self.message = (By.XPATH, "//div[contains(@class,'alert-success')]")
    def checkout_purchase(self,deliver_address):
        #self.driver.find_element(*self.cart).click()
        self.driver.find_element(*self.checkout).click()
        self.driver.find_element(*self.address).send_keys(deliver_address)
        driver_wait = WebDriverWait(self.driver, 10)
        driver_wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//div/label[@for='checkbox2']")))
        self.driver.find_element(By.XPATH, "//div/label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH, "//form/input[@type='submit']").click()
    def get_success_message(self):
        success_msg = self.driver.find_element(*self.message).text
        final_msg = success_msg.rstrip(":-).").split("\n")
        assert (final_msg[1].strip(" ")) == "Success! Thank you! Your order will be delivered in next few weeks", "Success Message Mismatched!!"
        print("End to End Test Completed.")
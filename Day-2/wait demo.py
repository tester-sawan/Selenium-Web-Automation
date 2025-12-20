import time

from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

search_value = "ber"
promo_code = "rahulshettyacademy"
driver = webdriver.Chrome()
driver.implicitly_wait(2) # This will wait for two second
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
print(driver.title)
# Enter the search value under the search bar
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys(search_value)
time.sleep(2)
#Count the number of serach item that is showing after search
items = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(items)
assert count>0
print(f"The items that are showing for keyword {search_value} is {count}.")
# Add to cart for all the shown element
# Here we use locator chaining
for item in items:
    item.find_element(By.XPATH,"div/button").click()
#Click on Cart
driver.find_element(By.CSS_SELECTOR,".cart-icon").click()
# Click on Proceed to checkout
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# Enter the promo code
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys(promo_code)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
# Validate the promo code | Use explicit wait
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
actual_promo_info = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
assert actual_promo_info == "Code applied ..!"
#Test the total amount , Count , Discount price and final price

table_item =driver.find_elements(By.XPATH,"//tr/td[5]/p[@class='amount']")
time.sleep(2)
table_item_count = len(table_item)
print(f"The items count under table_item is: {table_item_count}")
total_amount = 0
for amount in table_item:
     total_amount = total_amount + int(amount.text)

print(f"Total amount is: {total_amount}")
shown_total_amount = driver.find_element(By.XPATH, "//span[@class='totAmt']").text
shown_total_amount = int(shown_total_amount)
#print(shown_total_amount,type(shown_total_amount))
get_item = driver.find_element(By.XPATH,"//b[contains(text(),'No. of Items')]/parent::div").get_attribute("textContent")
#print(no_of_item)
count_item_value = (((get_item.split(":")[1]).strip())[0])
print("Counted item value:",count_item_value)
assert int(count_item_value) == table_item_count
assert total_amount == shown_total_amount
if total_amount == shown_total_amount:
    print("Total Amount Match")
else:
    print("Total Amount not matching")
get_discount_value = driver.find_element(By.XPATH,"//span[@class='discountPerc']").text
get_dicount = get_discount_value.strip("%")
discount = float(get_dicount)
final_value = total_amount - (total_amount * discount / 100)
print(f"The final value as per calculation: {final_value}")
actual_final_value = driver.find_element(By.CSS_SELECTOR,".discountAmt").text
actual_final_value = float(actual_final_value)
print(f"The actual final value: {actual_final_value}")
assert actual_final_value == actual_final_value
#print(actual_promo_info)
driver.find_element(By.XPATH,"//button[text()='Place Order']").click()
assert driver.current_url == "https://rahulshettyacademy.com/seleniumPractise/#/country"
print("End to End flow has been tested.")
time.sleep(2)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calculate_price(euro, amount):
      calculated_data = round(euro * amount, 2)
      return calculated_data

user_data = input("How much do you wish to convert? ")

driver = webdriver.Firefox()

driver.get('https://www.unicreditbulbank.bg/en/rates-indexes/currency-rates/')

input_element = driver.find_element(By.ID, value='buyAmount')
input_element.send_keys('1')

time.sleep(2)

choose_currency = driver.find_element(By.CSS_SELECTOR, value='[data-id="id_sell_currency"')
choose_currency.click()

time.sleep(2)

option = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div/div/div[1]/div[1]/div/div[2]/form/div[1]/div[2]/div/div/div/ul/li[9]/a")
option.click()

time.sleep(2)

one_euro = driver.find_element(By.ID, value='sellAmount').get_attribute("value")

# Close the WebDriver
driver.quit()

print(f"Price for one Euro in CZK: {one_euro}")

print(f"Calculated price for CZK: {calculate_price(float(one_euro), int(user_data))}")

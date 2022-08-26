from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import itertools
import pandas as pd
import time

searching_data = input("what you wanna search: ")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")

searchs = driver.find_element(
    By.XPATH, '//*[@id="twotabsearchtextbox"]'
)

searchs.send_keys(searching_data)
searchs.send_keys(Keys.ENTER)

time.sleep(10)

products = driver.find_elements(
    By.CLASS_NAME, "a-size-medium"
)

items = [product.find_element(
    By.CLASS_NAME, ''
)for product in products]

new_list = []

for item in items:
    name = item.find_element(
        By.CLASS_NAME, 'a-size-medium'
    )
    price1 = item.find_element(
        By.CLASS_NAME, 'a-size-medium'
    )
    price2 = item.find_element(
        By.CLASS_NAME, 'a-price-fraction'
    )
new_list.append({
    "Name" : name.text,
    "Price" : f'${price1.text}.{price2.text}'
})

print(new_list)

df = pd.DataFrame(new_list)
df.to_csv("products.csv")
#//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span/text()
#//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span
#//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span
#//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span
#//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span
#//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[5]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span
#//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span/span[1]
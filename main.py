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

new_list = []

product = driver.find_elements(
    By.CLASS_NAME, "a-size-medium"
)

product_list = [item.text for item in product]

def details(item):
    for item in product_list:
        names = driver.find_element(
            By.CLASS_NAME, 'a-size-medium'
        )
        prices = driver.find_element(
            By.CLASS_NAME, 'a-price'
        )
    new_list.append({
        "Name" :names.text,
        "Price" :prices.text
    })
    return new_list
final_list = list(itertools.chain(*[details(item)for item in product_list]))
df = pd.DataFrame(final_list)
#df = pd.DataFrame(list(itertools.chain(*[details(item)for item in product_list])))
df.to_csv("product_detail.csv", index = False)

driver.quit()
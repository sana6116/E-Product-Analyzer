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

#new_list = []

n = driver.find_elements(
    By.CLASS_NAME, "a-size-medium"
)
name = [i.text for i in n]
    
p = driver.find_elements(
    By.CLASS_NAME, 'a-price'
)
price = [i.text for i in p]
new_list = {
    "Name" :name,
    "Price" :price
}
    
print(new_list)
#df = pd.DataFrame(final_list)
#df = pd.DataFrame(list(itertools.chain(*[details(item)for item in product_list])))
#df.to_csv("product.csv", index = False)

driver.quit()
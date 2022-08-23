
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


searching_data = input("what you wanna search: ")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")
search = driver.find_element(
    By.XPATH, '//*[@id="twotabsearchtextbox"]'
)

search.send_keys(searching_data)
search.send_keys(Keys.ENTER)

time.sleep(3)
names = driver.find_elements(
    By.CLASS_NAME, 'a-size-medium'
)

names_list = [name.text for name in names]

for el in names_list:
    print(type(el))

    

driver.quit()
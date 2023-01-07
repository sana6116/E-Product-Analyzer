from webbrowser import Chrome
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

def get_url(searching_item):
    site = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'

    searching_item = searching_item.replace(" ","+")
    url = site.format(searching_item)

    url += '&page{}'

    return site.format(searching_item)

def detail(product):
    a_tag = product.h2.a
    description = a_tag.text.strip()
    new_url = 'https://www.amazon.com'+a_tag.get('href')

    try:
        parent_tag = product.find('span', 'a-price')
        price = parent_tag.find('span','a-offscreen').text

    except AttributeError:
        return

    try:
        rating = product.i.text
        review_count = product.find('span',{'class':'a-size-base'}).text
    
    except:
        rating = ''
        review_count = ''

    result=(description,price,rating,review_count,new_url)

    return result


def main():
    from webdriver_manager.chrome import ChromeDriverManager

    searching_item = input("What you want to Search: ")

    driver = webdriver.Chrome(ChromeDriverManager().install())

    record = []

    url = get_url(searching_item)

    for page in range(1,6):
        driver.get(url.format(page))
        soup=BeautifulSoup(driver.page_source,'html.parser')
        results=soup.find_all('div',{'data-component-type':'s-search-result'})

        for product in results:
            item = detail(product)
            if item:
                record.append(item)

    df = pd.DataFrame(record, columns=['Descrpition','Price','Rating','ReviewCount','URL'])
    df.to_csv('ProductList.csv', index=False)
    
    driver.close()


main()
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSfErPgiq11rySeM1_fV3O_igtW-y6KtA08zJc-ILcmbEt8ObQ/viewform?usp=sf_link'
ZILLOW_URL ='https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
LANGUAGE = 'en-US,en;q=0.9'

headers = {
    'User-Agent' : AGENT,
    'Accept-Language': LANGUAGE
}

response = requests.get(ZILLOW_URL, headers=headers)
zillow_text = response.text
soup = BeautifulSoup(zillow_text, 'html.parser')

urls = soup.select('.list-card-top a')
print(urls)
url_list = []

for url in urls:
    link = url['href']
    if not 'http' in link:
        link = f'https://www.zillow.com{link}'
    url_list.append(link)

# print(url_list)
price_list = []
prices = soup.select('.list-card-price')

for price in prices:
    price_only = price.getText().split('+')[0]
    if '/' in price_only:
        price_only = price_only.split('/')[0]
    price_list.append(price_only)

# print(price_list)

addresses = soup.select('.list-card-addr')

address_list = [adr.getText() for adr in addresses]
print(address_list)

chrome_driver_path = 'C:\Development\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for i in range(len(address_list)):
    driver.get(FORM_URL)

    time.sleep(5)
    enter_address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    enter_address.send_keys(address_list[i])

    time.sleep(5)

    enter_price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    enter_price.send_keys(price_list[i])

    time.sleep(5)

    enter_link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    enter_link.send_keys(url_list[i])
    time.sleep(5)

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    time.sleep(10)


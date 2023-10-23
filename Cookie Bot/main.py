from selenium import webdriver
from selenium.webdriver.common.by import By
import time

timeout = time.time() + 5
five_min = time.time() + 60*1

chrome_driver_path = 'C:\Development\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = 'http://orteil.dashnet.org/experiments/cookie/'

driver.get(URL)

cookie = driver.find_element(By.ID, 'cookie')

store = driver.find_elements(By.CSS_SELECTOR, '#store b')
store.pop()


item_names = [item.text.split('-')[0].strip() for item in store]

item_prices = [int(s.text.split()[-1].strip().replace(',', '')) for s in store if s.text != '']

item_dict = {}
for i in range(len(item_prices)):
    item_dict[item_prices[i]] = item_names[i]

game_on = True
while game_on:
    cookie.click()

    if time.time() >= five_min:
        cookie_per_sec = driver.find_element(By.ID, 'cps')
        print(cookie_per_sec.text)
        game_on = False

    if time.time() > timeout:
        money = driver.find_element(By.ID, 'money')
        money_element = money.text
        if ',' in money_element:
            money_element = money_element.replace(',', '')


        gained_money = int(money_element)
        for i in range(len(item_prices) - 1, 0, -1):
            if item_prices[i] < gained_money:
                driver.find_element(By.ID, f'buy{item_dict[item_prices[i]]}').click()

        #timeout = time.time() + 5




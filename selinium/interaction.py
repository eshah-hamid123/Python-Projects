from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:\Development\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = 'https://en.wikipedia.org/wiki/Main_Page'

driver.get(URL)
article_count = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# print(article_count.text)
# article_count.click()

search = driver.find_element(By.NAME, 'search')
search.send_keys('Python (Programming Language)')
search.send_keys(Keys.ENTER)
# driver.quit()
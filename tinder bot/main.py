from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

chrome_driver_path = 'C:\Development\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = 'https://tinder.com/'
driver.get(URL)

log_in = driver.find_element(By.XPATH, '//*[@id="t897152800"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.click()

time.sleep(5)
log_in_google = driver.find_element(By.XPATH, '//*[@id="t-831228276"]/div/div/div[1]/div/div/div[3]/span/div[1]/div/button')
log_in_google.click()

time.sleep(5)
enter_email = driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div')
enter_email.send_keys('eishahamid02@gmail.com')

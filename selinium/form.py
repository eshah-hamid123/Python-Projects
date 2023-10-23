from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:\Development\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = 'http://secure-retreat-92358.herokuapp.com/'
driver.get(URL)
fname = driver.find_element(By.NAME, 'fName')
fname.send_keys('Eisha')

lname = driver.find_element(By.NAME, 'lName')
lname.send_keys('Hamid')

email = driver.find_element(By.NAME, 'email')
email.send_keys('eshahhamid02@gmail.com')
email.send_keys(Keys.ENTER)




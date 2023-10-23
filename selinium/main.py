from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:\Development\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#URL = 'https://www.amazon.com/carson-colorblock-convertible-crossbody-Multi/dp/B09L7BYPZP/ref=sr_1_24?qid=1658151691&s=fashion-womens-intl-ship&sr=1-24'
URL = 'https://www.python.org/'
driver.get(URL)
# price = driver.find_element(By.CLASS_NAME, 'a-offscreen')
# print(price.get_attribute('innerHTML'))

# logo = driver.find_element(By.CLASS_NAME, 'python-logo')
# print(logo.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
# print(documentation_link.get_attribute('innerHTML'))

# path = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(path.text)
#print(path.get_attribute('innerHTML')
dates = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
# # print(len(dates))
# for date in dates:
#     print(date.text)
description = driver.find_elements(By.CSS_SELECTOR, '.event-widget li a')
# for texts in description:
#     print(texts.text)

events_list = {}
for i in range(5):
    events_list[i] = {'time': dates[i].text, 'description': description[i].text}
print(events_list)
driver.quit()
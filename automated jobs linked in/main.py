from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

chrome_driver_path = 'C:\Development\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = 'https://www.linkedin.com/jobs/search/?f_AL=true&geoId=103507082&keywords=python%20developer'

driver.get(URL)
sign_up = driver.find_element(By.CLASS_NAME, 'btn-secondary-emphasis')
sign_up.click()

username = driver.find_element(By.ID, 'username')
username.send_keys('eishahamid02@gmail.com')

password = driver.find_element(By.ID, 'password')
password.send_keys('dummylinkedin')

enter_info = driver.find_element(By.CSS_SELECTOR, 'div button')
enter_info.click()

# easy_apply = driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply button')
# easy_apply.click()
#
# phone_no = driver.find_element(By.CSS_SELECTOR, '.display-flex input')
# phone_no.send_keys('3224381967')
#
# next = driver.find_element(By.CSS_SELECTOR, '.pv4 #ember187')
# next.click()

all_links = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')
for job in all_links:
    job.click()
    try:
        save = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
        save.click()
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
    except ElementNotInteractableException:
            print('LinkedIn application loading error')

# follow = driver.find_element(By.CSS_SELECTOR, '.follow span')
# follow.click()





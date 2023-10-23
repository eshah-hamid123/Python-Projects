from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
import time

chrome_driver_path = 'C:\Development\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

USERNAME = 'new_stories123'
PASSWORD = 'asisha31'
SIMILAR_ACCOUNT = 'theworldofhsy'
URL = 'https://www.instagram.com/'

class InstaFollower:

    def __init__(self, chrome_path):
        self.driver = webdriver.Chrome(executable_path=chrome_path)

    def login(self):
        self.driver.get(URL)
        time.sleep(5)
        user = self.driver.find_element(By.NAME, 'username')
        user.send_keys(USERNAME)

        time.sleep(5)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f'{URL}{SIMILAR_ACCOUNT}')
        time.sleep(5)
        followers = self.driver.find_element(By.CSS_SELECTOR, 'span ._ac2a')
        followers.click()



    def follow(self):
        pass


bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()


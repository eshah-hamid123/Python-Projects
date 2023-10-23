from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

TWITTER_EMAIL = 'eshahhamid02@gmail.com'
TWITTER_PASSWORD = 'asisha31'
UPLOAD_SPEED = 150
DOWNLOAD_SPEED = 10
chrome_driver_path = 'C:\chromedriver.exe'
SPEED_URL = 'https://www.speedtest.net/result/13482801016'


class InternetSpeedTwitterBot:

    def __init__(self, driver):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(executable_path=driver,chrome_options=options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(self.down)

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed(SPEED_URL)
bot.tweet_at_provider()
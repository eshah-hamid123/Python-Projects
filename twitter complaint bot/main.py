from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TWITTER_EMAIL = 'eisha_hamid23'
TWITTER_PASSWORD = 'asisha31'
UPLOAD_SPEED = 10
DOWNLOAD_SPEED = 150
chrome_driver_path = 'C:\Development\chromedriver_win32\chromedriver.exe'
SPEED_URL = 'https://www.speedtest.net/result/13482801016'
twitter_url = 'https://twitter.com/i/flow/login'


class InternetSpeedTwitterBot:

    def __init__(self, driver):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(executable_path=driver)
        self.up = 0
        self.down = 0

    def get_internet_speed(self, url):
        self.driver.get(url)
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()
        # while True:
        #     try:
        #         self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        #         #print(f'Down {self.down}')
        #         self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        #
        #     except:
        #         time.sleep(2)
        #     else:
        #         break
        # print(f'Down {self.down}')
        # print(f'Up {self.up}')
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print(f'Down {self.down}')
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f'Up {self.up}')

    def tweet_at_provider(self, twitter_url):
        self.driver.get(twitter_url)
        time.sleep(2)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(2)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(60)
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f'Hey PTCL why my speed is {self.down}down/ {self.up}up while I pay for {DOWNLOAD_SPEED}down/{UPLOAD_SPEED}up')


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed(SPEED_URL)
bot.tweet_at_provider(twitter_url)
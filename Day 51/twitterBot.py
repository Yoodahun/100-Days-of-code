from selenium.webdriver.common.by import By

from driverSetup import DriverSetup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = DriverSetup().setupDriver()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element_by_class_name("start-text").click()

        time.sleep(50)
        d = WebDriverWait(self.driver, 50).until(ec.presence_of_element_located((By.XPATH,
                                                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                                                 '2]/div/div[2]/span')))
        u = WebDriverWait(self.driver, 50).until(ec.presence_of_element_located((By.XPATH,
                                                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')))

        self.down = float(d.text)
        self.up = float(u.text)

        print(self.down, self.up)

        # self.driver.quit()

    def tweet_at_provider(self, id, password):
        self.driver.get("https://twitter.com/")
        self.driver.find_element_by_xpath("//a[@data-testid='loginButton']").click()

        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input").send_keys(id)
        self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input").send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
        time.sleep(5)

        self.driver.find_element_by_xpath('//div[@aria-label="Tweet text"]').send_keys(
            f"Softbank airさん。下り{self.down}、上がり{self.up}はひどくないですか？"
        )
        self.driver.find_element_by_xpath('//div[@data-testid="tweetButtonInline"]').click()

        self.driver.quit()



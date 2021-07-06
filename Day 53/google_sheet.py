from selenium import webdriver
import time

GOOGLE_FORM = "https://forms.gle/2pxbMxtU1U6F3bh77"


class GoogleSheet:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/Users/yoodahun/Documents/Github/Python/100 Days of Code-CLI/chromedriver"
                                       )
        self.address = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
        self.price = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
        self.link = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'

    def input_google_sheet(self, link, price, address):

        self.driver.get(GOOGLE_FORM)
        time.sleep(1)

        self.driver.find_element_by_xpath(self.address).send_keys(address)
        self.driver.find_element_by_xpath(self.price).send_keys(price)
        self.driver.find_element_by_xpath(self.link).send_keys(link)

        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()

    def driver_quit(self):
        self.driver.quit()



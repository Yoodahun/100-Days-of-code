from selenium import webdriver


chromedriver_path = "/Users/yoodahun/Documents/Github/Python/100 Days of Code-CLI/chromedriver"


class DriverSetup():
    def __init__(self):
        # self.chromeOption = webdriver.ChromeOptions()
        # self.chromeOption.headless = True
        self.driver = webdriver.Chrome(executable_path=chromedriver_path)

    def setupDriver(self) -> webdriver:
        return self.driver

    def quitDriver(self):
        self.driver.quit()

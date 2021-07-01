from selenium import webdriver

chromedriver_path = "/Users/yoodahun/Documents/Github/Python/100 Days of Code-CLI/chromedriver"

driver = webdriver.Chrome(executable_path=chromedriver_path)

driver.get("https://www.amazon.co.jp")

driver.quit()
from driverSetup import DriverSetup

driver = DriverSetup().setupDriver()
wikipedia_page = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(wikipedia_page)

wikipedia_statistics = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]').text
print(wikipedia_statistics)


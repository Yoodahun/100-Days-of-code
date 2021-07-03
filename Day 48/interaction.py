from driverSetup import DriverSetup
from selenium.webdriver.common.keys import Keys

driver = DriverSetup().setupDriver()
# wikipedia_page = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(wikipedia_page)
#
# # wikipedia_statistics = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# # wikipedia_statistics.click()
# # wikipedia_statistics.find_element_by_link_text()
#
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# # driver.quit()

the_lab_report = "http://secure-retreat-92358.herokuapp.com/"
driver.get(the_lab_report)

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")

first_name.send_keys("TEST")
last_name.send_keys("PANDA")
email.send_keys("test@gmail.com")
button = driver.find_element_by_xpath("//button[@type='submit']")
button.click()

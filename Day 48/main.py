from driverSetup import DriverSetup

driver = DriverSetup().setupDriver()

driver.get("https://www.python.org/")
event_widget = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]')
dates = event_widget.find_elements_by_tag_name("time")
events = event_widget.find_elements_by_tag_name("a")

event_list = dict()

for i in range(len(dates)):
    event = dict()
    event["time"] = dates[i].get_attribute("datetime").split("T")[0]
    event["name"] = events[i+1].text
    event_list[i] = event

print(event_list)


driver.quit()
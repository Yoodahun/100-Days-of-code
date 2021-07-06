from zillow import Zillow
from google_sheet import GoogleSheet


zillow = Zillow()
google_sheet = GoogleSheet()



zillow.scrap_zillow_page(zillow.get_zillow_page())
zillow.print()

list_of_link = zillow.get_list_of_link()
list_of_address = zillow.get_list_of_address()
list_of_price = zillow.get_list_of_price()

for i in range(len(list_of_link)):
    print("execute")
    google_sheet.input_google_sheet(list_of_link[i], list_of_price[i], list_of_address[i])

google_sheet.driver_quit()
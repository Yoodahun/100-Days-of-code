from bs4 import BeautifulSoup
import requests

CLIENT_ID = ""
CLIENT_SECRET = ""

year_date = input("what year you would like to travel to in YYY-MM-DD format. : ")

URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(URL+year_date)
soup = BeautifulSoup(response.text, 'html.parser')

song_titles = [song.get_text() for song in soup.find_all(name="span", class_="chart-element__information__song")]

for title in song_titles:
    print(title)
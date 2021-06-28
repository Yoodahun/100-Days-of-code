from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECNT_URI = ""

# year_date = input("what year you would like to travel to in YYY-MM-DD format. : ")
#
# URL = "https://www.billboard.com/charts/hot-100/"
#
# response = requests.get(URL+year_date)
# soup = BeautifulSoup(response.text, 'html.parser')
#
# song_titles = [song.get_text() for song in soup.find_all(name="span", class_="chart-element__information__song")]
#
# for title in song_titles:
#     print(title)


scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECNT_URI,
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               )
                     )

user_id = sp.current_user()["id"]
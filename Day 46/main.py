from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


#### Web scraping from weekly Billboard chart 100 and create to Spotify Playlist
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECNT_URI = "m"
URL = "https://www.billboard.com/charts/hot-100/"
scope = "playlist-modify-public"

year_date = input("what year you would like to travel to in YYY-MM-DD format. : ")

response = requests.get(URL+year_date)
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())
song_titles = [song.get_text() for song in soup.find_all(name="span", class_="chart-element__information__song")]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECNT_URI,
                                               scope=scope,
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               )
                     )

user_id = sp.current_user()["id"]
song_uris = []
year = year_date.split("-")[0]
for title in song_titles:
    result = sp.search(q=f"track:{title} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify")


playlist_response = sp.user_playlist_create(
    user=user_id,
    name=f"{year_date} Playlist"
)
print(playlist_response)
playlist_id = playlist_response["id"]

add_playlist_response = sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
print(add_playlist_response)





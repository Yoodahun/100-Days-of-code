from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, 'html.parser')

movies = []
for movie in soup.select("div.listicle-item-image > div > div > picture > img"):
    movies.append(movie.get("alt"))

movies.reverse()

with open("movies.txt",mode='w') as file:
    for i in range(0, 100):
        file.write(f"{i+1}) {movies[i]}\n")


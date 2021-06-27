from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/newest")
soup = BeautifulSoup(response.text, "html.parser")

articles_title = []
articles_link = []
articles_upvote = []
for tag in soup.find_all(name="a", class_="storylink"):
    articles_title.append(tag.get_text())
    articles_link.append(tag.get("href"))

for tag in soup.find_all(name="span", class_="score"):
    articles_upvote.append(int(tag.get_text().split()[0]))

max_index = articles_upvote.index(max(articles_upvote))

print (
    articles_title[max_index],
    articles_link[max_index],
    articles_upvote[max_index]
)




# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# print(soup.find_all(name="a")[0].get('href'))
#
# print(soup.find(name="h1", id="name"))
# print(soup.find(name="h1", class_="heading"))
# print(soup.select(selector="p a"))


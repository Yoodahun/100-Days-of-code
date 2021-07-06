from bs4 import BeautifulSoup
import requests


ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

class Zillow:

    def __init__(self):
        self.list_of_link = []
        self.list_of_price = []
        self.list_of_address = []

    def get_zillow_page(self) -> BeautifulSoup:
        response = requests.get(ZILLOW_URL, headers=headers)
        bs = BeautifulSoup(response.text, 'html.parser')

        return bs

    def print(self):
        print(self.list_of_price)
        print(self.list_of_address)
        print(self.list_of_link)

    def scrap_zillow_page(self, bs):
        article_lists = bs.find_all(name="div", class_="list-card-info")
        article_lists.remove(article_lists[-1])

        for article in article_lists:
            a_tag = article.find(name="a", class_="list-card-link").get("href")
            price_tag = article.find(name="div", class_="list-card-price").getText()
            address_tag = article.find(name="address", class_="list-card-addr").getText()
            self.list_of_link.append(a_tag if a_tag.startswith('h') else f"https://www.zillow.com{a_tag}")
            self.list_of_price.append(price_tag.split("/")[0])
            self.list_of_address.append(address_tag)

    def get_list_of_address(self):
        return self.list_of_address

    def get_list_of_link(self):
        return self.list_of_link

    def get_list_of_price(self):
        return self.list_of_price










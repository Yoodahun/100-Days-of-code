import requests


class Post:
    def __init__(self):
        self.posts = {}

    pass

    def request_post(self):
        blog_url = "https://api.npoint.io/ed99320662742443cc5b"
        self.posts = requests.get(blog_url).json()

    def get_posts(self):
        return self.posts

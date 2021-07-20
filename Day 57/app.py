from flask import Flask, render_template
import requests
from post import Post
import random
import datetime

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     random_number = random.randint(1, 10)
#     year = datetime.datetime.now().year
#     return render_template('index1.html'
#                            , random_number=random_number,
#                            year=year
#                            )

posts = Post()


@app.route('/')
def home():
    posts.request_post()
    return render_template("index.html", posts=posts.get_posts())


@app.route('/guess/<string:name>')
def guess_name(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()["age"]
    gender = requests.get(f"https://api.genderize.io?name={name}").json()["gender"]
    return render_template('guess_gender.html',
                           name=name,
                           gender=gender,
                           age=age
                           )


@app.route("/blog/<int:_id>")
def get_blog(_id):
    post = [p for p in posts.get_posts() if p["id"] == _id]
    return render_template("post.html", posts=post)


if __name__ == '__main__':
    app.run()

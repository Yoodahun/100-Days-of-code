from flask import Flask

app = Flask(__name__)


class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Dahun")
new_user.create_blog_post(new_user)


@app.route('/')
def hello_world():
    return '<h1>Hello World!</h1>'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def bye():
    return '<b>Bye!</b>'


@app.route('/username/<name>')
def greet(name):
    return f"Hello, my name is {name}"


if __name__ == '__main__':
    app.run(debug=True)

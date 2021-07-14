import random

from flask import Flask

app = Flask(__name__)

select_number = 0


@app.route('/')
def hello_world():
    global select_number
    select_number = random.randint(a=0, b=9)

    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'


@app.route('/<int:number>')
def detect_number(number):
    if number < select_number:
        return too_low()
    if number > select_number:
        return too_high()
    return correct()


def too_low():
    return '<h1 style="text-color: red"> Too low, try again!</h1>' \
           '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'


def too_high():
    return '<h1 style="text-color: red"> Too High, try again!</h1>' \
           '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'


def correct():
    return '<h1>You found me! </h1>' \
           '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'


if __name__ == '__main__':
    app.run(debug=True)
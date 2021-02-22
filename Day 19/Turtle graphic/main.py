from turtle import Turtle, Screen

the_turtle = Turtle()
screen = Screen()


def move_forwards():
    the_turtle.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
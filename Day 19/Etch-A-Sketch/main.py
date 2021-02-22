from turtle import Turtle, Screen

the_turtle = Turtle()
screen = Screen()


def move_forwards():
    the_turtle.forward(10)


def move_backwards():
    the_turtle.back(10)


def clockwise_left():
    the_turtle.left(10)


def clockwise_right():
    the_turtle.right(10)


def clear():
    the_turtle.penup()
    the_turtle.clear()
    the_turtle.home()
    the_turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=clockwise_left)
screen.onkey(key="d", fun=clockwise_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()

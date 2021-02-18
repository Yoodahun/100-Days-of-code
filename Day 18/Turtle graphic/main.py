from turtle import Turtle, Screen

the_turtle = Turtle()
the_turtle.shape("turtle")
the_turtle.color("purple")

for _ in range(4):
    the_turtle.forward(100)
    the_turtle.right(90)





screen = Screen()
screen.exitonclick()
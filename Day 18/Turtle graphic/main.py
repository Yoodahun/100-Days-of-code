from turtle import Turtle, Screen

the_turtle = Turtle()
the_turtle.shape("turtle")
the_turtle.color("purple")

for i in range(3, 20):
    angle = 360 / i
    for _ in range(i):
        the_turtle.forward(50)
        the_turtle.right(angle)









screen = Screen()
screen.exitonclick()
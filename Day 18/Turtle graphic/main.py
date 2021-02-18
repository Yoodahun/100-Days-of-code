from turtle import Turtle, Screen
import random

the_turtle = Turtle()
the_turtle.shape("turtle")
the_turtle.color("purple")

color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray"]

for i in range(3, 10): #number of side
    angle = 360 / i #corner angle
    the_turtle.color(random.choice(color))
    for _ in range(i):

        the_turtle.forward(50)
        the_turtle.right(angle)









screen = Screen()
screen.exitonclick()
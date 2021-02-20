import turtle
import random

the_turtle = turtle.Turtle()
the_turtle.shape("turtle")
the_turtle.color("purple")
turtle.colormode(255)

color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray"]
direction = [0, 90, 180, 270]  # east, north, west, south


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)

    return rgb


def draw_different_shape(max_number_of_side):
    for i in range(3, max_number_of_side):  # number of side
        angle = 360 / i  # corner angle
        the_turtle.color(random.choice(color))
        for _ in range(i):
            the_turtle.forward(50)
            the_turtle.right(angle)


def draw_a_random_walk(max_number_of_random_walk):
    the_turtle.speed("normal")
    the_turtle.pensize(7)
    for _ in range(max_number_of_random_walk):
        # the_turtle.color(random.choice(color))
        the_turtle.pencolor(
            random_color()
        )
        the_turtle.forward(30)
        the_turtle.setheading(random.choice(direction))


def draw_a_spirograph(size_of_gap):
    the_turtle.speed("fastest")
    for _ in range(int(360 / size_of_gap)): # just stop when finish draw circle
        current_heading = the_turtle.heading()
        the_turtle.setheading(current_heading + size_of_gap)
        the_turtle.color(random_color())
        the_turtle.circle(100, 360)


# draw_a_random_walk(40)
draw_a_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()

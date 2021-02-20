import colorgram
import turtle
import random

# colors = colorgram.extract("image.jpg", 30)
#
# color_tuple_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     color_tuple_list.append((r, g, b))

color_tuple_list = [(201, 164, 112), (152, 75, 49), (221, 201, 138), (171, 153, 42), (56, 95, 126), (139, 31, 19),
                    (134, 163, 184), (197, 93, 73), (48, 121, 88), (98, 75, 77), (142, 178, 148), (75, 41, 33),
                    (165, 145, 156), (15, 99, 71), (234, 175, 164), (54, 45, 47), (32, 61, 77), (145, 21, 25),
                    (21, 83, 89), (182, 205, 175), (85, 147, 127), (44, 66, 87), (178, 94, 98), (222, 177, 184),
                    (8, 68, 51), (108, 127, 151)]


def random_color():
    return random.choice(color_tuple_list)


the_turtle = turtle.Turtle()
the_turtle.shape("turtle")
the_turtle.color("purple")
the_turtle.speed("fastest")
turtle.colormode(255)
the_turtle.penup()

the_turtle.setheading(225)
the_turtle.forward(350)
the_turtle.setheading(0)

print(the_turtle.position)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):

    the_turtle.dot(20, random_color())
    the_turtle.forward(50)

    if dot_count % 10 == 0: # when dot_count is 10, 10 / 10 == 1, modulo is 0 or 20, 30 ...
        the_turtle.setheading(90)  # turn north
        the_turtle.forward(50)  # move one space
        the_turtle.setheading(180)  # turn west
        the_turtle.forward(500)  # move 10 space
        the_turtle.setheading(0)  # turn east

screen = turtle.Screen()
screen.exitonclick()

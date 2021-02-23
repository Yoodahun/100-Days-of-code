from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

for turtle_index in range(0, 6):
    the_turtle = Turtle(shape="turtle")
    the_turtle.color(colors[turtle_index])
    the_turtle.penup()
    the_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(the_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"You've won! The {turtle.pencolor()} turtle is the winner !")
                break
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner !")
                break






screen.exitonclick()

from turtle import Turtle, Screen


screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange","yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]


for turtle_index in range(0, 6):
    the_turtle = Turtle(shape="turtle")
    the_turtle.color(colors[turtle_index])
    the_turtle.penup()
    the_turtle.goto(x=-230, y=y_position[turtle_index])



screen.exitonclick()

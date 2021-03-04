import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

##################################################################
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

correct_number = 0
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

print(all_states)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        # Save missing states to CSV
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        print(data[data["state"] == answer_state])
        state_data = data[data["state"] == answer_state]  # row of data

        t.goto(int(state_data["x"]), int(state_data["y"]))
        t.write(state_data["state"].item()) #first item
        guessed_states.append(answer_state)



##################################################################
# screen.exitonclick()

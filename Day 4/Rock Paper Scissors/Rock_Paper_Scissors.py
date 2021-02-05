import Rock_Paper_Scissors_Const
import random

choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Sissors. \n"))

computer_choice = random.randint(0, 2)

print(Rock_Paper_Scissors_Const.arrays[choice])
print("Computer choose: ")
print(Rock_Paper_Scissors_Const.arrays[computer_choice])
if choice == 0: # Rock
    if computer_choice == 0: #Rock
        print("It's same result")
    elif computer_choice == 1: #Paper
        print("You lose")
    else:   # Scissor
        print("You win")
elif choice == 1: #Paper
    if computer_choice == 0: #Rock
        print("You win")
    elif computer_choice == 1: #Paper
        print("It's same result")
    else:   # Scissor
        print("You lose")
else: # Scissor
    if computer_choice == 0: #Rock
        print("You lose")
    elif computer_choice == 1: #Paper
        print("You win")
    else:   # Scissor
        print("It's same result")


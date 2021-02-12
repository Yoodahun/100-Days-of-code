#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0

if difficulty == "hard":
    attempts = 5
elif difficulty == "easy":
    attempts = 10

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    if number < guess:
        print("Too high.")
        attempts -= 1
    elif number > guess:
        print("Too low.")
        attempts -= 1
    else:
        print(f"You got it! The answer was {number}.")
        break

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        break

    print("Guess again.")





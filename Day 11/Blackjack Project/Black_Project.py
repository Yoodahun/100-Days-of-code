############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    return random.choice(cards)

def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2: #blackjack handling
        return 0

    if 11 in card_list and sum(card_list) > 21: #ace card handling
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw !"
    elif computer_score == 0:
        return "Lose, oppoennt has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack !"
    elif user_score > 21:
        return "You went over. You Lose."
    elif computer_score > 21:
        return "Opponent went over. You Win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

user_cards = []
computer_cards = []
is_game_over = False
play_game = True

while play_game:

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'n':
        play_game = False
        break

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    print(art.logo)
    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_another_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand : {user_cards}")
    print(f"Your final score : {user_score}")
    print(f"Computer's final hand: {computer_cards}")
    print(f"Computer's final score: {computer_score}")
    print(compare(user_score, computer_score))


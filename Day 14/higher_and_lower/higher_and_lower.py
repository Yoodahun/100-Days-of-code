import random
import game_data
import art


def formatting_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return f"{account_name}, a {account_description}, from {account_country}"


score = 0
is_game_over = False
against_b = random.choice(game_data.data)

while True:
    print(art.logo)
    if score > 0 and not is_game_over:
        print(f"You're right! Current score: {score}")
    elif is_game_over:
        print(f"Sorry, that's wrong. Final score: {score}")
        break

    compare_a = against_b  # previous b, next a
    against_b = random.choice(game_data.data)

    if compare_a == against_b:
        against_b = random.choice(game_data.data)

    print(f"Compare A: {formatting_data(compare_a)}")
    print(art.vs)
    print(f"Against B: {formatting_data(against_b)}")
    type_a_or_b = input("Who has more followers? Type 'A' or 'B': ").lower()

    if type_a_or_b == 'a':
        if compare_a["follower_count"] > against_b["follower_count"]:
            score += 1
        else:
            is_game_over = True
    elif type_a_or_b == 'b':
        if compare_a["follower_count"] < against_b["follower_count"]:
            score += 1
        else:
            is_game_over = True

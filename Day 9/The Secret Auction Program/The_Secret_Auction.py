import art
print(art.logo)
print("Welcome to the secret auction program.")


is_there_any_other_bidders = True

bid_info = {}

def print_highest_bidder(bid_info):
    max_name = ""
    max_bid = 0

    for bidder in bid_info:
        if max_bid < bid_info[bidder]:
            max_bid = bid_info[bidder]
            max_name = bidder

    print(f"The winner is {max_name} with a bid of ${max_bid}.")


while is_there_any_other_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_info[name] = bid

    should_contiue = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    if should_contiue == "no":
        is_there_any_other_bidders = False
        print_highest_bidder(bid_info)



import resources

water = resources.resources["water"]
milk = resources.resources["milk"]
coffee = resources.resources["coffee"]
money = 0
change = 0


def report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


def is_there_sufficient_resource(drink):
    if drink != "espresso":
        if milk < resources.MENU[drink]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
    if water < resources.MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    if coffee < resources.MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False

    return True


def calculate_coin(quarters, dimes, nickles, pennies):
    calcul_quarters = quarters * 0.25
    calcul_dimes = dimes * 0.10
    calcul_nickles = nickles * 0.05
    calcul_pennies = pennies * 0.01

    return calcul_quarters + calcul_dimes + calcul_nickles + calcul_pennies


def check_inserted_enough_money_to_purchase(drink, coin):
    global change
    global money

    drink_cost = resources.MENU[drink]["cost"]

    if drink_cost == coin:
        return True
    elif drink_cost < coin:
        change = coin - drink_cost
        money += float("{:.2f}".format(drink_cost))
        print("Here is ${:.2f} in change".format(change))
        change = 0

        return True
    else:
        return False


def make_coffee(drink):
    global water
    global milk
    global coffee

    water -= resources.MENU[drink]["ingredients"]["water"]
    coffee -= resources.MENU[drink]["ingredients"]["coffee"]
    if drink != "espresso":
        milk -= resources.MENU[drink]["ingredients"]["milk"]


while True:
    coffee_order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_order == "report":
        report()
    elif coffee_order == "off":
        break
    elif coffee_order == "latte" or coffee_order == "espresso" or coffee_order == "cappuccino":
        if is_there_sufficient_resource(coffee_order):
            print("Please insert coins.")

            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            cost = calculate_coin(
                quarters,
                dimes,
                nickles,
                pennies
            )

            if check_inserted_enough_money_to_purchase(
                    coffee_order,
                    cost
            ):

                make_coffee(coffee_order)
                print(f"Here is your {coffee_order} Enjoy !")

            else:
                print("Sorry, that's not enough money. Money refunded")
                continue

        else:
            continue

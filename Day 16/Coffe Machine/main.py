from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

while True:
    coffee_order = input(f"What would you like? ({menu.get_items()}): ").lower()

    if coffee_order == "report":
        coffee_machine.report()
        money_machine.report()
    elif coffee_order == "off":
        break
    elif coffee_order == "latte" or coffee_order == "espresso" or coffee_order == "cappuccino":
        ordered_drink = menu.find_drink(coffee_order)

        if coffee_machine.is_resource_sufficient(ordered_drink) and money_machine.make_payment(ordered_drink):
            coffee_machine.make_coffee(ordered_drink)
        else:
            continue
    else:
        continue

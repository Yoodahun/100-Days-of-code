# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_for_small = 2
pepperoni_for_medium_or_large = 3
extra_cheese_for_any_size = 1

bill = 0

if size == "S":
    bill += small_pizza
    if add_pepperoni == "Y":
        bill += pepperoni_for_small
    if extra_cheese == "Y":
        bill += extra_cheese_for_any_size
elif size == "M":
    bill += medium_pizza
    if add_pepperoni == "Y":
        bill += pepperoni_for_medium_or_large
    if extra_cheese == "Y":
        bill += extra_cheese_for_any_size
elif size == "L":
    bill += large_pizza
    if add_pepperoni == "Y":
        bill += pepperoni_for_medium_or_large
    if extra_cheese == "Y":
        bill += extra_cheese_for_any_size
else:
    print("wrong input")

if bill > 0:
    print(f"Your final bill is: ${bill}")





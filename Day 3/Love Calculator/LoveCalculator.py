# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name = name1.lower() + name2.lower()


true_score = 0
love_score = 0

true_score += lower_name.count("t")
true_score += lower_name.count("r")
true_score += lower_name.count("u")
true_score += lower_name.count("e")

love_score += lower_name.count("l")
love_score += lower_name.count("o")
love_score += lower_name.count("v")
love_score += lower_name.count("e")

true_love_score_str = str(true_score) + str(love_score)
true_love_score = int(true_love_score_str)

if (true_love_score < 10) or (true_love_score > 90):
    print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif(true_love_score >= 40) and (true_love_score <= 50):
    print(f"Your score is {true_love_score}, you are alright together.")
else:
    print(f"Your score is {true_love_score}")
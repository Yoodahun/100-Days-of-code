from tkinter import *
from tkinter import messagebox
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
text = ""


############# Read CSV ############
try:
    csv_data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    csv_data = pandas.read_csv("data/french_words.csv")
    french_words = csv_data.to_dict(orient="records")
else:
    french_words = csv_data.to_dict(orient="records")

# french_words = csv_data.to_dict(orient="records")
# print(french_words)

########### is known #########
def is_known():
    french_words.remove(current_card)
    data = pandas.DataFrame(french_words)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

############# random pick ############
def next_card():
    global text
    global current_card, filp_timer
    window.after_cancel(filp_timer) # 해당 after를 취소함.
    current_card = random.choice(french_words)
    text = current_card["French"]

    # canvas위에 있는 아이템의 속성을 변경하는 것.
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{text}", fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    filp_timer = window.after(3000, func=change_background) #이후 무엇인가 버튼을 눌렀을 때 재실


############# Change background ############
def change_background():
    text = current_card["English"]

    # canvas위에 있는 아이템의 속성을 변경하는 것.
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{text}", fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


############# UI ############
window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

filp_timer = window.after(3000, func=change_background)
# window.after_cancel(command=change_background)

canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="images/card_front.gif")
card_back_img = PhotoImage(file="images/card_back.gif")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.gif")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.gif")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()

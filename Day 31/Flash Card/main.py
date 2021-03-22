from tkinter import *
from tkinter import messagebox
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"


############# Read CSV ############
csv_data = pandas.read_csv("data/french_words.csv")

french_words = csv_data.to_dict(orient="records")
# print(french_words)
text = ""

############# random pick ############
def next_card():
    global text
    current_card = random.choice(french_words)
    text = current_card["French"]

    # canvas위에 있는 아이템의 속성을 변경하는 것.
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=f"{text}")



############# UI ############
window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800)
card_front_img = PhotoImage(file="images/card_front.gif")
canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.gif")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.gif")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()
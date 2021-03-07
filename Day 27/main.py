##############

def add(*args):
    return sum(args)

print(add(1,2,3,4))

def calculate(**kwargs):
    pass

#############

import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label["text"] = new_text

#Label
my_label = tkinter.Label(text="I am a label.", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New text label"
my_label.config(text="new text config")

#Button
button = tkinter.Button(text="This is Button", command=button_clicked)
button["highlightcolor"] = "black"
button.pack()

#Entry
input = tkinter.Entry(width=10)
input.pack()

####################################################################





####################################################################


window.mainloop()


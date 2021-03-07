### grid 3, 3

from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)
################################

input_miles = Entry(width=7)
label_mile = Label(text="Miles")

label_is_equal_to = Label(text="is equal to")
label_converted_mile = Label(text="0")
label_km = Label(text="Km")


def calculate():
    miles = float(input_miles.get())
    label_converted_mile["text"] = f"{round(miles * 1.609)}"


button_calculate = Button(text="Calculate", command=calculate)

input_miles.grid(row=0, column=1)
label_mile.grid(row=0, column=2)

label_is_equal_to.grid(row=1, column=0)
label_converted_mile.grid(row=1, column=1)
label_km.grid(row=1, column=2)

button_calculate.grid(row=2, column=1)

window.mainloop()

from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = input_website.get()
    email = input_email_username.get()
    password = input_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \rEmail: {email} "
                                                              f"\rPassword: {password} \r\rIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\r")
                input_website.delete(0, END)
                input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo_image = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=photo_image)

canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_email_username = Label(text="Email/Username:")
label_password = Label(text="Password:")
input_website = Entry(width=35)
input_email_username = Entry(width=35)
input_password = Entry(width=21)
button_generate_password = Button(text="Generate Password")
button_add = Button(text="Add", width=33, command=save_password)

label_website.grid(row=1, column=0)
input_website.grid(row=1, column=1, columnspan=2, sticky="w")
label_email_username.grid(row=2, column=0)
input_email_username.grid(row=2, column=1, columnspan=2, sticky="w")
label_password.grid(row=3, column=0)
input_password.grid(row=3, column=1, sticky="w")
button_generate_password.grid(row=3, column=2, sticky="w")
button_add.grid(row=4, column=1, columnspan=2, sticky="w")

input_website.focus()
input_email_username.insert(0, "test@gmail.com")

# columnspan

window.mainloop()

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please enter a valid website and password")
        return
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"Password: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(website + " | " + email + " | " + password + "\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canvas_img)
canvas.grid(column=1, row=0, columnspan=2)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, pady=(0, 10))

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, pady=(0, 10))

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, pady=(0, 10))

#Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.config(bg="white", highlightthickness=0)
generate_button.grid(column=2, row=3, sticky="we", pady=(0, 10), ipady=2)

add_button = Button(text="Add", bg="white", width=60, command=save)
add_button.config(width=54)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", ipady=2)

#Entries
website_entry = Entry()
website_entry.config(width=52)
website_entry.grid(column=1, row=1, columnspan=2, sticky="WE", pady=(0, 10), ipady=5)
website_entry.focus()

email_entry = Entry()
email_entry.config(width=52)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW", pady=(0, 10), ipady=5)
email_entry.insert(0, "arommers@gmail.com")

password_entry = Entry()
password_entry.config(width=30)
password_entry.grid(column=1, row=3, sticky="w", pady=(0, 10), ipady=5)

window.mainloop()

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letter = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letter + password_numbers + password_symbols
    shuffle(password_list)

    generated_password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, generated_password)
    pyperclip.copy(generated_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_text = entry_website.get()
    username_text = entry_username.get()
    password_text = entry_password.get()
    new_data = {website_text: {
        "email": username_text,
        "password": password_text,
    }}
    if len(website_text) == 0 or len(username_text) == 0 or len(password_text) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
                messagebox.showinfo(title="Password Manager", message="Saved completed.")
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_pass():
    website_text = entry_website.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        if website_text in data:
            website_dict = data[website_text]
            website_email = website_dict["email"]
            website_pass = website_dict["password"]
            messagebox.showinfo(title=f"{website_text}", message=f"Email: {website_email}\n"
                                                                 f"Password: {website_pass}")
        else:
            messagebox.showwarning(title="Error", message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:", font=("Arial", 10, "normal"))
website.grid(row=1, column=0)
website.focus()

username = Label(text="Email/Username:", font=("Arial", 10, "normal"))
username.grid(row=2, column=0)

password = Label(text="Password:", font=("Arial", 10, "normal"))
password.grid(row=3, column=0)

entry_website = Entry(width=32)
entry_website.grid(row=1, column=1, columnspan=2, sticky="W")

entry_username = Entry(width=32)
entry_username.grid(row=2, column=1, columnspan=3, sticky="W")
entry_username.insert(0, "username@gmail.com")

entry_password = Entry(width=32)
entry_password.grid(row=3, column=1, sticky="W")

generate_pass = Button(text="Generate Password", width=15, command=generate_password)
generate_pass.grid(row=3, column=2, sticky="W")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

search_button = Button(text="Search", width=15, command=find_pass)
search_button.grid(row=1, column=2)

window.mainloop()

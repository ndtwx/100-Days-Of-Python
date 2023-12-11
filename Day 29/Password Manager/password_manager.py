from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for n in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for n in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for n in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, string=f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
"""
json.dump() = Write
json.load() = Read
json.update() = Update

json.dump(<new_nestd_dictionary>, <the json file>):
this takes a number of inputs, 
but the most important are the things you want to dump and the file that you want to dump it to
The data we want to put in here should go in as a dictionary, essentially we want to create is a 
new dictionary which we will call it new_data and it is going to be a nested dictionary
"""


def save():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="WARNING", message="Please do not leave any field empty")
    else:
        # Open and the json file in Read mode
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)

        except FileNotFoundError:  # If file doesn't exist it will create one
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            # Open the json file in write mode
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)  # The data we want to put in here should go in as a dictionar

        finally:  # Clear the entry doesn't if error occur or not
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

        else:
            messagebox.showinfo(title=website, message=f"No details for {website} exist")


# ---------------------------- UI SETUP ------------------------------- #
# Creating Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Creating Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

canvas.grid(column=1, row=0)

# Creating Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Creating Entry
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(END, string="nd_twx@hotmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Creating buttons
password_button = Button(text="Generate Password", width=15, command=password_generator)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()

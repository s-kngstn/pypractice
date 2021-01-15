import tkinter
import json
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    passwd_entry.delete(0, tkinter.END)
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    passwd_entry.insert(tkinter.END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    passwd = passwd_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": passwd,
        }
    }

    if len(website) < 1 or len(email) < 1 or len(passwd) < 1:
        messagebox.showinfo(title="Oops",
                            message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
            messagebox.showinfo(
                title="File Created",
                message="File created, account details have been saved.")

        else:
            with open("data.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
            messagebox.showinfo(title="Success!",
                                message="Account and password has been saved.")
        finally:
            website_entry.delete(0, tkinter.END)
            email_entry.delete(0, tkinter.END)
            passwd_entry.delete(0, tkinter.END)


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Sorry", message="No Data File Found.")
    else:
        if website in data:
            messagebox.showinfo(
                title=f"{website}",
                message=
                f''' Account details for {website}\n\nEmail/Login: {data[website]['email']}\nPassword: {data[website]['password']}\n\nPassword copied to Clipboard!'''
            )
            pyperclip.copy(data[website]['password'])
        else:
            messagebox.showinfo(title="Sorry",
                                message=f"Cannot find details for {website}.")


# ---------------------------- UI SETUP  ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tkinter.Label(text="Email/Login:")
email_label.grid(column=0, row=2)

passwd_label = tkinter.Label(text="Password:")
passwd_label.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = tkinter.Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(tkinter.END, "username@email.com")

passwd_entry = tkinter.Entry(width=20)
passwd_entry.grid(column=1, row=3)

# Buttons
passwd_btn = tkinter.Button(width=12,
                            text="Generate Password",
                            command=generate_password)
passwd_btn.grid(column=2, row=3)

add_btn = tkinter.Button(width=34, text="Add", command=save)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = tkinter.Button(width=12, text="Search", command=find_password)
search_btn.grid(column=2, row=1, columnspan=2)

window.mainloop()

import tkinter
import pyperclip
from tkinter import messagebox
from random import choice, randint, shuffle


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
    login = login_entry.get()
    passwd = passwd_entry.get()
    if len(website) < 1 or len(login) < 1 or len(passwd) < 1:
        messagebox.showinfo(title="Oops",
                            message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=
            f"These are the details entered: \nLogin: {login} \nPassword: {passwd} \nIs it ok to save?"
        )
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"\n{website} | {login} | {passwd}")
                website_entry.delete(0, tkinter.END)
                login_entry.delete(0, tkinter.END)
                passwd_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

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

login_label = tkinter.Label(text="Login:")
login_label.grid(column=0, row=2)

passwd_label = tkinter.Label(text="Password:")
passwd_label.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

login_entry = tkinter.Entry(width=36)
login_entry.grid(column=1, row=2, columnspan=2)
login_entry.insert(tkinter.END, "username@email.com")

passwd_entry = tkinter.Entry(width=20)
passwd_entry.grid(column=1, row=3)

# Buttons
passwd_btn = tkinter.Button(width=12,
                            text="Generate Password",
                            command=generate_password)
passwd_btn.grid(column=2, row=3)

add_btn = tkinter.Button(width=34, text="Add", command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()

import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}

# ------------------------- NEXT CARD BUTTON --------------------------------#


def is_known():
    to_learn.remove(current_card)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_image, image=card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ------------------------------ UI ----------------------------------------#

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)
# Flash Card
canvas = tkinter.Canvas(width=800,
                        height=525,
                        highlightthickness=0,
                        bg=BACKGROUND_COLOR)
card_front = tkinter.PhotoImage(file="images/card_front.png")
card_back = tkinter.PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 262, image=card_front)
title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Unknown Button
unknown_img = tkinter.PhotoImage(file="images/wrong.png")
unknown_btn = tkinter.Button(image=unknown_img,
                             command=next_card,
                             highlightthickness=0)
unknown_btn.grid(column=0, row=1)

# Known Button
known_img = tkinter.PhotoImage(file="images/right.png")
known_btn = tkinter.Button(image=known_img,
                           command=is_known,
                           highlightthickness=0)
known_btn.grid(column=1, row=1)

next_card()
window.mainloop()

import tkinter
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ------------------------- RIGHT BUTTON -----------------------------------#


def known():
    print("right")


# ------------------------- WRONG BUTTON -----------------------------------#


def unknown():
    print("wrong")


# ------------------------------ UI ----------------------------------------#

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash Card Front
canvas = tkinter.Canvas(width=800,
                        height=525,
                        highlightthickness=0,
                        bg=BACKGROUND_COLOR)
card_front = tkinter.PhotoImage(file="images/card_front.png")
canvas.create_image(400, 262, image=card_front)
canvas.create_text(400, 150, text="Title", font=(FONT_NAME, 40, "italic"))
canvas.create_text(400, 263, text="Word", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Unknown Button
unknown_img = tkinter.PhotoImage(file="images/wrong.png")
unknown_btn = tkinter.Button(image=unknown_img,
                             command=unknown,
                             highlightthickness=0)
unknown_btn.grid(column=0, row=1)

# Known Button
known_img = tkinter.PhotoImage(file="images/right.png")
known_btn = tkinter.Button(image=known_img,
                           command=known,
                           highlightthickness=0)
known_btn.grid(column=1, row=1)

window.mainloop()

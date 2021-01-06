import tkinter
# REMEMBER .pack() and .grid() cannot work together


def button_clicked():
    '''When clicked, label is replaced with text from Entry box'''
    print("I got clicked")
    new_text = entry.get()
    my_label.config(text=new_text)


window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New New Text")
# my_label.pack()
# my_label.place(x=0, y=0)  # <-- Places label top left corner
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
# button.config(padx=20, pady=20)

# Button 2
button2 = tkinter.Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
entry = tkinter.Entry(width=10)
print(entry.get())
entry.grid(column=3, row=2)

window.mainloop()

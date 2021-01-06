import tkinter


def button_clicked():
    '''When I get clicked, input in miles is converted to
    Km and displayed as a label'''
    miles = entry.get()
    kilometers = int(miles) * 1.609344
    km.config(text=kilometers)


window = tkinter.Tk()
window.title("Miles 2 Km Converter")
window.minsize(width=400, height=200)
window.config(padx=30, pady=30)

# Entry for Miles
entry = tkinter.Entry(width=15)
entry.insert(tkinter.END, string="0")
entry.grid(column=1, row=0)

# Label for Entry
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label "is equal to"
is_equal_to = tkinter.Label(text="is equal to ")
is_equal_to.grid(column=0, row=1)

# Label for Km Conversion
km = tkinter.Label(text="0")
km.grid(column=1, row=1)

# Label Km
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate Button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()

from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Creating Labels
miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 10))
equal_label.grid(column=0, row=1)

km_label = Label(text="Km", font=("Arial", 10))
km_label.grid(column=2, row=1)

num_label = Label(text="", font=("Arial", 10))
num_label.grid(column=1, row=1)

# Creating Entry
entry = Entry(width=7)
entry.insert(END, string="0")
entry.grid(column=1, row=0)


# Creating button
def calculate():
    miles = float(entry.get())
    km = miles * 1.609
    num_label['text'] = km


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()

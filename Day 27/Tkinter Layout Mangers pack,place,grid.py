"""
Setting Options:
Options control things like the color and border width of a widget. Options can be set in three ways:
At object creation time, using keyword arguments like
< fred = Button(self, fg="red", bg="blue) >

After object creation, treating the option name like a dictionary index
< fred["fg"] = "red" >
< fred["bg"] = "blue >

Use the config() method to update multiple attrs subsequent to object creation
< fred.config(fg="red", bg="blue) >
"""
"""
~~TKINTER LAYOUT MANAGER~~

Pack():
Basically packs each of the widgets next to each other in the center of the winodw by default
(Quite difficult to specify a precise position)

Place():
Able to place the widget to a precise location by using the x and y value

Grid():
Imagine your entire program is a grind and can divide it into any number of columns (vertical) and rows (horizontal)
(You can use both grid() and pack() at the same time)
"""
from tkinter import *

def button_clicked():
    print("I got clicked")
    my_label['text'] = f"{entry.get()}"  # Changing the label text that user typed in the entry after button is click


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Add padding to space out
window.config(padx=100, pady=200)

# Creating a Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# Place the label onto the screen and center it to the middle
my_label['text'] = 'New Text'  # Either way works
my_label.config(text=f'New Text')  # Either way works
# my_label.pack()  # https://docs.python.org/3/library/tkinter.html#the-packer | https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Creating button
button = Button(text="Click Me",
                command=button_clicked)  # set the command property equal to the name of the function without the parenthesis
# button.pack()
button.grid(column=1, row=1)

# Creating New button
new_button = Button(text= "New Button")
new_button.grid(column=2,row=0)

# Creating Entry
# https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
entry = Entry(width=30)
entry.insert(END, string="Type something here")
# entry.pack()
entry.grid(column=3, row=2)



# Keep the window open (always at the end of your code)
window.mainloop()

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

https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
"""
from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Creating a Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# Place the label onto the screen and center it to the middle
my_label.pack()
my_label['text'] = 'New Text'  # Either way works
my_label.config(text=f'New Text')  # Either way works


# Creating buttons
def button_clicked():
    print("I got clicked")
    my_label['text'] = f"{entry.get()}"  # Changing the label text that user typed in the entry after button is click


button = Button(text="Click Me",
                command=button_clicked)  # set the command property equal to the name of the function without the parenthesis
button.pack()

# Creating Entry
entry = Entry(width=30)
entry.insert(END, string="Type something here")
entry.pack()

# Creating Textbox
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Add some text to begin with
text.insert(END, "Example of multi-line text entry")
# Gets current value in textbox at line 1, character 0
# "1.0" basically refers to getting hold of the text starting from the first character
print(text.get("1.0", END))
text.pack()


# Creating Spinbox
def spinbox_used():
    # Gets the current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Creating Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Creating Checkbox
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0
    print(checked_state.get())


# Variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Creating Radiobutton
def radio_usd():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text='Option 1', value=1, variable=radio_state, command=radio_usd)
radiobutton2 = Radiobutton(text='Option 2', value=2, variable=radio_state, command=radio_usd)
radiobutton1.pack()
radiobutton2.pack()


# Creating a Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
# Loop through each item and insert it into the listbox
for item in fruits:
    listbox.insert(fruits.index(item), item)

# use the bind function to call the listbox_used function which will print the selected item
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


# Keep the window open (always at the end of your code)
window.mainloop()

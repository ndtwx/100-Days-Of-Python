import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Creating a Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# https://docs.python.org/3/library/tkinter.html#the-packer
# https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
# Place the label onto the screen and center it to the middle
my_label.pack()



# Keep the window open (always at the end of your code)
window.mainloop()

# Write Python GUI program to display an alert message when a button is pressed.

import tkinter.messagebox

def onClick():
    tkinter.messagebox.showinfo("Button Clicked", "You clicked the button")

window = tkinter.Tk()

btn1 = tkinter.Button(window, text="Click Me", command=onClick)
btn1.pack()

window.mainloop()
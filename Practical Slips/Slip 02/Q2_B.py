# Write Python GUI program to create a digital clock with Tkinter to display the time.

import time
from tkinter import *


window = Tk()
window.title("Digital Clock")
window.geometry("250x110")

label = Label(
    window,
    font = ("Courier", 30, "bold"),
    bg = "blue",
    fg = "white",
    bd = 30
)
label.grid(row = 0, column = 0)

def clock():
    text_input = time.strftime("%H:%M:%S")
    label.config(text = text_input)
    label.after(200, clock)

clock()
window.mainloop()
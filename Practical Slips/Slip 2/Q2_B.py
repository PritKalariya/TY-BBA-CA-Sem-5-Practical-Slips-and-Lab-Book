import time
from tkinter import *


window = Tk()
window.title("Digital Clock")
window.geometry("250x110")

Label = Label(
    window,
    font = ("Courier", 30, "bold"),
    bg = "blue",
    fg = "white",
    bd = 30
)
Label.grid(row = 0, column = 0)

def clock():
    text_input = time.strftime("%H:%M:%S")
    Label.config(text = text_input)
    Label.after(200, clock)

clock()
window.mainloop()
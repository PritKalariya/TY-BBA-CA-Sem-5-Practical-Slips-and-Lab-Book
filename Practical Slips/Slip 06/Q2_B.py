# Write a Python GUI program to create a label and change the label font style (font name, bold, size). Specify separate check button for each style.

from tkinter import *

window = Tk()
window.title("Q2_B")
window.geometry('200x200')

my_label = Label(window, text="Hello World")
my_label.grid(column=0, row=0)

btn1 = Button(window, text="Bold", command=lambda: my_label.config(font=("Arial", 10, "bold")))
btn1.grid(column=0, row=1)

btn2 = Button(window, text="Italic", command=lambda: my_label.config(font=("Courier", 12, "italic")))
btn2.grid(column=1, row=1)

window.mainloop()
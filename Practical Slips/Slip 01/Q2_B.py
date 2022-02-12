# Write Python GUI program to take accept your birthdate and output your age when a button is pressed.

from tkinter import *
from datetime import date


root = Tk()
root.geometry("200x200")
root.title("Age Calculator")


def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year
    Label(text=f"Your age is {age}").grid(row=6, column=1)


Label(text="Year").grid(row=2, column=0)
yearValue = StringVar()
yearEntry = Entry(root, textvariable=yearValue)
yearEntry.grid(row=2, column=1, pady=10)

Label(text="Month").grid(row=3, column=0)
monthValue = StringVar()
monthEntry = Entry(root, textvariable=monthValue)
monthEntry.grid(row=3, column=1, pady=10)

Label(text="Day").grid(row=4, column=0)
dayValue = StringVar()
dayEntry = Entry(root, textvariable=dayValue)
dayEntry.grid(row=4, column=1, pady=10)

Button(text="Calculate age", command=calculateAge).grid(row=5, column=1, pady=10)

root.mainloop()
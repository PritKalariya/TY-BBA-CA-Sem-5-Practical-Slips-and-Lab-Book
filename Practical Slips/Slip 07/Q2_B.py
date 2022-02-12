# Write python GUI program to generate a random password with upper and lower case letters.


import random
from tkinter import *


def password():
    password = []
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    for i in range(8):
        password.append(random.choice(lower))
        password.append(random.choice(upper))

    password = "".join(password)
    # print(password)
    Label(text=f"Your password is: {password}").grid(row=1, column=1)


window = Tk()
window.title("Password Generator")
window.geometry("300x200")

btn1 = Button(window, text="Generate Password", command=password)
btn1.grid(column=1, row=0)

window.mainloop()
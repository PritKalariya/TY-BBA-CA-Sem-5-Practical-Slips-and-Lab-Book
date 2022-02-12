# Write Python GUI program to create background with changing colors

from tkinter import *
import time
from random import shuffle

window = Tk()
window.title("Background Color")
window.geometry("200x200")

def change_color():
   colors= ['black', 'green', 'red', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'grey']
   while True:
      shuffle(colors)
      for i in range(0, len(colors)):
         window.config(background=colors[i])
         window.update()
         time.sleep(1)

btn = Button(window, text="Change Color", command=change_color)
btn.pack(pady=10)

window.mainloop()
from tkinter import *
from tkinter import ttk
import random

item_list = []

width = 500
height = 800

root = Tk()
root.title('Takeaway menu')
root.minsize(width, height)
root.maxsize(width, height)

class item:
    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image
        item_list.append(name)

def item_image(directory):
    str_directory = str(directory)
    image = PhotoImage(file = str_directory)
    image.pack()

file = PhotoImage(file = 'burger_logo.jpg')
file_label = ttk.Label(root, image = file)
file_label.pack()

root.mainloop()

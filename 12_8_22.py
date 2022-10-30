from tkinter import *
from tkinter import ttk
import os
import random

item_list = []
flavour_list = []

width = 500
height = 800

root = Tk()
root.title('Takeaway menu')
root.geometry('500x800')

class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        item_list.append(name)

class drinks(item):
    def __init__(self, flavour, name, price):
        super().__init__(name, price)
        self.flavour = flavour

        

burger = item('Burger', 3)
fries = item('Fries', 2)
drink = drinks('kola', 'drink', 2)

print(drink.flavour)
top_frame = ttk.LabelFrame(root, text = 'Menu')
top_frame.grid(row=0, column=0, padx=10, pady=10)

menu_text = StringVar()
menu_text.set('Menu')

def quantity_frame(item_frame, y, x):
    item_frame = ttk.LabelFrame(top_frame, text = 'Quantity')
    item_frame.grid(row = y, column = x, padx = 5, pady = 5)
    return item_frame

def label_function(item_label, item_class, y, x):
    item_label = ttk.Label(top_frame, text = str(item_class))
    item_label.grid(row = y, column = x, padx = 10, pady = 10)
    return item_label

def entry_function(item_frame, item_variable, x, y):
    item_entry = ttk.Entry(item_frame, textvariable = item_variable)
    item_entry.grid(row = x, column = y, padx = 5, pady = 5)
    return item_entry

#burger
burger_frame = quantity_frame('burger_frame', 3, 0)
burger_label = label_function('burger_label', burger.name, 1, 0)

burger_description = ttk.Label(top_frame, text = 'Beef patty, lettuce, ketchup', wraplength = 200)
burger_description.grid(row = 2, column = 0, padx = 5, pady = 5)

burger_variable = DoubleVar()
burger_variable.set('0')
burger_entry = entry_function(burger_frame, burger_variable, 0, 0)

#fries
fries_frame = quantity_frame('fries_frame', 3, 1)
fries_label = label_function('fries_label', fries.name, 1, 1)

fries_description = ttk.Label(top_frame, text = 'shoestring fries', wraplength = 200)
fries_description.grid(row = 2, column = 1, padx = 5, pady = 5)

fries_variable = DoubleVar()
fries_variable.set('0')
fries_entry = entry_function( fries_frame, fries_variable, 0, 0)

#drinks
drinks_frame = quantity_frame('drinks_frame', 3, 2)
drinks_label = label_function('drinks_label', drink.name, 1, 2)

#fries_description = ttk.Label(top_frame, text = 

#quantity = DoubleVar()
#quantity.set(' ')

#quantity_entry = ttk.Entry(burger_frame, textvariable = quantity)
#quantity_entry.grid(row = 0, column = 0, padx = 5, pady = 5)

root.mainloop()

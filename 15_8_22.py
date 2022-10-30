from tkinter import *
from tkinter import ttk
import os
import random

item_dictionary = {}
item_dictionary['item'] = ['price', 'quantity']

class item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        info = [self.price, self.quantity]
        item_dictionary[self.name] = info
    
    def add_quantity(self, amount):
        if amount >= 0:
            self.quantity += amount
            return True
        else:
            return False        

burger = item('Burger', 3, 0)
fries = item('Fries', 2, 0)
drink = item('Drinks', 2, 0)

root = Tk()
root.title('Takeaway menu')
root.geometry ('800x500')

def quantity_frame(item_quantity, y, x):
    item_quantity = ttk.LabelFrame(top_frame, text = 'Quantity')
    item_quantity.grid(row = y, column = x, padx = 5, pady = 5)
    return item_quantity

def update_quantity():
    original = item.quantity
    new_quantity = original + input_quantity
    
def validator(cringe):
    while True:
        try:
            imp = int(input(cringe))
            break
        except ValueError:
            print('zzz')
    return imp

#top frame
top_frame = ttk.LabelFrame(root, text = 'Menu')
top_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

#burger
burger_label = ttk.Label(top_frame, text = 'Burger', font = ('Arial', 12))
burger_label.grid(row = 0, column = 0, padx = 5, pady = 5)

burger_quantity = IntVar()
burger_quantity.set(0)
burger_quantity_frame = quantity_frame('burger_quantity', 1, 0)

burger_entry = ttk.Entry(burger_quantity_frame, textvariable = burger_quantity)
burger_entry.grid(row = 0, column = 0, padx = 5, pady = 5)

#fries
fries_label = ttk.Label(top_frame, text = 'Fries', font = ('Arial', 12))
fries_label.grid(row = 0, column = 1, padx = 5, pady = 5)

fries_quantity = DoubleVar()
fries_quantity.set(0)
fries_quantity_frame = quantity_frame('fries_quantity', 1, 1)

fries_entry = ttk.Entry(fries_quantity_frame, textvariable = fries_quantity)
fries_entry.grid(row = 0, column = 0, padx = 5, pady = 5)

#drinks
drinks_label = ttk.Label(top_frame, text = 'Drinks', font = ('Arial', 12))
drinks_label.grid(row = 0, column = 2, padx = 5, pady = 5)

drinks_quantity = DoubleVar()
drinks_quantity.set(0)
drinks_quantity_frame = quantity_frame('drinks_quantity', 1, 2)

drinks_entry = ttk.Entry(drinks_quantity_frame, textvariable = drinks_quantity)
drinks_entry.grid(row = 0, column = 0, padx = 5, pady = 5)

items_list = ['Burger', 'Fries', 'Drinks']
quantity_list = [0,0,0]

#gathering variables
def all_update():  
    burger_total = burger_quantity.get()
    quantity_list[0] = burger_total
    
    fries_total = fries_quantity.get()
    quantity_list[1] = fries_total
    
    drinks_total = drinks_quantity.get()
    quantity_list[2] = drinks_total
    
    quantity_string = str('Burgers: ' + str(burger_total) + '\n' + 
                          'Fries: ' + str(fries_total) + '\n' +
                          'Drinks: ' + str(drinks_total))
    quantity_format.set(quantity_string)
    print(quantity_format.get())

#def validation(item_total, quantity_variable):
    #for x in items_list:
        #y = 0
        #try:
            #item_total = int(quantity_variable.get())
            #quantity_list[y] = item_total
            #error_format.set('All good')
            #y += 1
        #except ValueError:
            #error_string = str('Invalid input. Please change ' + quantity_variable.get())
            #error_format.set(error_string)
            #break
    
quantity_format = StringVar()

quantity_submit = ttk.Button(top_frame, text = 'Submit', command = all_update)
quantity_submit.grid(row = 2, column = 3)

total_frame = ttk.LabelFrame(top_frame, text = 'Total items:')
total_frame.grid(row = 1, column = 3, padx = 10, pady = 10)

total_label = ttk.Label(total_frame, textvariable = quantity_format)
total_label.grid(row = 1, column = 0, padx = 5, pady = 5)



#bottom frame
bottom_frame = ttk.LabelFrame(root, text = 'Checkout')
bottom_frame.grid(row = 2, column = 0)

#delivery options
option = IntVar()
option.set(1)

pickup = ttk.Radiobutton(bottom_frame, text = 'Pickup', value = 1, variable = option)
pickup.grid(row = 0, column = 0, padx = 10, pady = 10)

delivery = ttk.Radiobutton(bottom_frame, text = 'Delivery', value = 2, variable = option)
delivery.grid(row = 0, column = 1, padx = 10, pady = 10)

root.mainloop()
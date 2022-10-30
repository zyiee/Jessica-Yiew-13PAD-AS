from tkinter import *
from tkinter import ttk
import os
import random

item_dictionary = {}
item_dictionary['item'] = ['price', 'quantity']

class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        item_dictionary[self.name] = self.price 

customer_dictionary = {}

class user(item):
    def __init__(self, customer, name, quantity, total):
        super().__init__(name)
        self.customer = customer
        self.quantity = quantity
        self.total = total
        
        customer_info = [self.name, self.quantity, self.total]
        customer_dictionary[self.customer] = customer_info
    

burger = item('Burger', 3)
fries = item('Fries', 2)
drink = item('Drinks', 2)

root = Tk()
root.title('Takeaway menu')
root.geometry ('570x500')

def quantity_frame(item_quantity, y, x):
    item_quantity = ttk.LabelFrame(top_frame, text = 'Quantity')
    item_quantity.grid(row = y, column = x, padx = 5, pady = 5)
    return item_quantity

#top frame
top_frame = ttk.LabelFrame(root, text = 'Menu')
top_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

#validity indicator
valid_list = ['Please enter a valid number\n(Positive numbers only)', ' ']
validity_variable = StringVar()
validity_variable.set(valid_list[1]) #default variable

valid_label = ttk.Label(top_frame, textvariable = validity_variable)
valid_label.grid(row = 0, column = 3, padx = 10, pady = 10)

def item_validation(item_variable): #updates label and validates
    try:
        quantity = item_variable.get()
        validity_variable.set(valid_list[1])
        if quantity < 0:
            return False
        else:
            return True
    except Exception:
        validity_variable.set(valid_list[0])
        return False

def update_label():
    for items in variable_list:
        value = item_validation(items)
        print(value)
        if value == True:
            pass
        else:
            print('wonky')
#burger
burger_label = ttk.Label(top_frame, text = 'Burger', font = ('Arial', 12))
burger_label.grid(row = 0, column = 0, padx = 5, pady = 5)

burger_quantity = IntVar()
burger_quantity.set(0)
burger_quantity_frame = quantity_frame('burger_quantity', 1, 0)

burger_entry = ttk.Entry(burger_quantity_frame, textvariable = burger_quantity)
burger_entry.grid(row = 0, column = 0, padx = 5, pady = 5)

#burger_button = ttk.Button(top_frame, text = 'burger_button', command = update_label)
#burger_button.grid(row = 3, column = 0)

#fries
fries_label = ttk.Label(top_frame, text = 'Fries', font = ('Arial', 12))
fries_label.grid(row = 0, column = 1, padx = 5, pady = 5)

fries_quantity = IntVar()
fries_quantity.set(0)
fries_quantity_frame = quantity_frame('fries_quantity', 1, 1)

fries_entry = ttk.Entry(fries_quantity_frame, textvariable = fries_quantity)
fries_entry.grid(row = 0, column = 0, padx = 5, pady = 5)

#drinks
drinks_label = ttk.Label(top_frame, text = 'Drinks', font = ('Arial', 12))
drinks_label.grid(row = 0, column = 2, padx = 5, pady = 5)

drinks_quantity = IntVar()
drinks_quantity.set(0)
drinks_quantity_frame = quantity_frame('drinks_quantity', 1, 2)

drinks_entry = ttk.Entry(drinks_quantity_frame, textvariable = drinks_quantity)
drinks_entry.grid(row = 0, column = 0, padx = 5, pady = 5)

items_list = ['Burger', 'Fries', 'Drinks']
quantity_list = [0,0,0]
variable_list = [burger_quantity, fries_quantity, drinks_quantity]

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

quantity_format = StringVar()

quantity_submit = ttk.Button(top_frame, text = 'Update', command = update_label)
quantity_submit.grid(row = 2, column = 3, padx = 5, pady = 5)

total_frame = ttk.LabelFrame(top_frame, text = 'Total items:')
total_frame.grid(row = 1, column = 3, padx = 10, pady = 10)

#bottom frame
bottom_frame = ttk.LabelFrame(root, text = 'Checkout')
bottom_frame.grid(row = 2, column = 0)

#delivery options
option = IntVar()
option.set(1)

options_desc = ttk.Label(bottom_frame, text = 'Delivery is $5 extra')
options_desc.grid(row = 0, column = 0, padx = 5, pady = 5)

pickup = ttk.Radiobutton(bottom_frame, text = 'Pickup', value = 1, variable = option)
pickup.grid(row = 1, column = 0, padx = 10, pady = 10)

delivery = ttk.Radiobutton(bottom_frame, text = 'Delivery', value = 2, variable = option)
delivery.grid(row = 1, column = 1, padx = 10, pady = 10)

name_frame = ttk.LabelFrame(bottom_frame, text = 'Name')
name_frame.grid(row = 1, column = 2, padx = 10, pady = 10)

name_variable = DoubleVar()
name_variable.set(' ')
name_entry = ttk.Entry(name_frame, textvariable = name_variable)
name_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

option_submit = ttk.Button(bottom_frame, text = 'Update')
option_submit.grid(row = 1, column = 3, padx = 5, pady = 5)

submit_button = ttk.Button(root, text = 'Submit')
submit_button.grid(row = 3, column = 0)

root.mainloop()
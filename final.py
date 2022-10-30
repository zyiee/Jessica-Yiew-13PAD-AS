#!/usr/bin/python
# -*- coding: utf-8 -*-
###############################imports###############################

import tkinter as tk
from tkinter import *
from tkinter import ttk

###############################general variables###############################

# list of strings to be used to display validity messages

valid_list = [  # 0
                # 1
                # 2
                # 3
                # 4
                # 5
                # 6
                # 7
    'Please enter a number',
    'Please enter a positive value',
    ' ',
    'Please enter a name',
    'Please check of your item quantities are valid',
    'Order Saved',
    'Please check if all the fields are valid',
    'Please enter a number above 0',
]

order_data = {}  # dictionary which stores previous and new order data
burger_cost = 3  # price of 1 burger
fries_cost = 2  # price of 1 fries
drinks_cost = 2  # price of 1 drink

# saved external data file

data_file = 'test.csv'


class Food:

    '''The food class is used to gather information entered into the gui and constantly be updated with whatever the user inputs. it has a change_quantity definition which allows for its quantities to be changed, as well as a validity function to check for the validity of user entries.'''

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def change_quantity(self, quantity):
        self.quantity = quantity

    def validity(self, amount):
        try:
            user_quantity = amount.get()
            if user_quantity < 0:
                validity_string.set(valid_list[1])
                return False
            else:
                validity_string.set(valid_list[2])
                return True
        except Exception:
            validity_string.set(valid_list[0])
            return False


class data_window(tk.Toplevel):

    '''The data_window class allows for a new window to be opened and display the current contents of the externally imported order history file. It also has a close_window definition to allow for a button to be created that closes the display history window upon click'''

    def __init__(self, parent):
        super().__init__(parent)
        self.title('Order history')
        self.geometry('400x500')
        self.display_list = []

        self.display_var = StringVar()

        for names in order_data:
            self.data = order_data[names]
            self.display = '\t'.join(self.data)
            self.display_full = str(names + '\t' + self.display)
            self.display_list.append(self.display_full)

        self.display_string = '\n'.join(self.display_list)
        self.display_var.set(self.display_string)

        self.display_frame = ttk.Frame(self)
        self.display_frame.grid(row=0, column=0, padx=10, pady=10)

        self.display_label = ttk.Label(self.display_frame,
                                       text=self.display_var.get(), font=('Arial', 10))
        self.display_label.grid(row=0, column=0, padx=5, pady=5)

        self.close_button = ttk.Button(self, text='Close',
                                       command=self.close_window)
        self.close_button.grid(row=1, column=0, padx=5, pady=5)

    def close_window(self):
        self.destroy()


def quantity_frame(item_quantity, y, x):  # shortened code for menu aesthetics
    '''Helps shorten the overall code while maintaining aesthetics for the menu frame. It's a frame that contains each food item's entry box'''

    item_quantity = ttk.LabelFrame(menu_frame, text='Quantity')
    item_quantity.grid(row=y, column=x, padx=5, pady=5)
    return item_quantity


def data_layout():  # opens file and splits every line to put into dictionary
    '''Opens externally imported file and pops it into dictionary for both saving new orders and displaying previous orders'''

    open_file = open(data_file, encoding='utf-8-sig')
    with open_file as f:
        lines = [line.strip() for line in f]
        y = 0
        for items in lines:
            info = lines[y].split(',')
            key = info[0]
            info.pop(0)
            order_data[key] = info
            y = y + 1


def quantity_display():  # menu aesthetics
    '''Updates the gui to show how many of each food item is to be ordered according to user input. Also checks if all food quantities are above 0'''

    burger.change_quantity(burger_quantity.get())
    quantity_list[0] = burger.quantity

    fries.change_quantity(fries_quantity.get())
    quantity_list[1] = fries.quantity

    drinks.change_quantity(drinks_quantity.get())
    quantity_list[2] = drinks.quantity

    updated_quantity_string = quantity_string.format(burger.quantity,
                                                     fries.quantity, drinks.quantity)
    quantity_format.set(updated_quantity_string)

    above_zero = any(quantity_list)
    return above_zero


def checkout_calculations():  # calculates total cost
    '''calculates the total cost of the new order accounting for delivery/pickup option as well'''

    total_cost = burger.quantity * burger_cost + fries.quantity \
        * fries_cost + drinks.quantity * drinks_cost
    total.set(total_cost)
    value = option.get()
    if value == 1:
        pass
    elif value == 2:
        total_cost += 5
        total.set(total_cost)
    updated_total = total_string.format(total_cost)
    total_string_var.set(updated_total)


def quantity_update():  # validation
    '''iterates through all instances and checks its validity.'''

    x = 0
    for instances in instances_list:
        item_quantity = variable_list[x]
        value = instances.validity(item_quantity)
        if value == False:
            return False
        else:
            x += 1
    above_zero = quantity_display()
    if above_zero == False:
        validity_string.set(valid_list[7])
        return False
    return True


def option_get():  # method get
    '''Gets the delivery/ pickup option and updates the gui to show which one was selected'''

    value = option.get()
    if value == 1:
        selected_option = 'Pickup'
        selected_display = 'Pickup (Free)'
        pickup_string = method_display_string.format(selected_option, 0)
        method_var.set(pickup_string)
    elif value == 2:
        selected_option = 'Delivery'
        selected_display = 'Delivery (+$5)'
        delivery_string = \
            method_display_string.format(selected_display, 5)
        method_var.set(delivery_string)


def update_all():  # validation
    '''Updates the gui if any invalid entries are made, otherwise runs the expected code'''

    value = quantity_update()
    name = name_update()
    if value == False:
        overall_string.set(valid_list[4])
        return False
    elif name == False:
        overall_string.set(valid_list[3])
        return False
    else:
        overall_string.set(valid_list[2])
        option_get()
        checkout_calculations()
        return True


def save_function():  # save into external file
    '''Checks if the events are valid, then gets all valid info into a suitable format and saves it into external csv file'''

    value = update_all()
    if value == True:
        option_value = option.get()
        if option_value == 1:
            selected_option = 'pickup'
        elif option_value == 2:
            selected_option = 'delivery'
        update_list = [str(i) for i in quantity_list]
        update_list.append(selected_option)
        update_list.append(total.get())
        order_data[name_variable.get()] = update_list
        save_file()


def save_file():  # converts the dictionary and lists within code into suitable format to save into file
    '''Primarily a function to save data into external file'''

    with open(data_file, 'w') as file:
        for value in order_data:
            format_list = []
            format_list.append(value)
            data = order_data[value]
            format_list.extend(data)
            startstr = ' '
            for items in format_list:
                startstr = startstr + str(items) + ','
            startstr = startstr.strip(',')
            startstr = startstr + '\n'
            file.write(startstr)
    file.close()


def name_update():  # name gui update
    '''Updates GUI to show whether a name has been entered or not'''

    if not name_variable.get():
        name_string_var.set(valid_list[3])
        return False
    else:
        name_string_var.set(valid_list[2])
    return True


def data_display():  # data window
    '''opens a new window to display previous and/or new orders'''

    data_box = data_window(root)


if __name__ == '__main__':

    # file import

    data_layout()

    # window setup

    root = Tk()
    root.title('Takeaway Menu')
    root.geometry('800x500')

    # menu label frame to keep all food items tidy

    menu_frame = ttk.LabelFrame(root, text='Menu')
    menu_frame.grid(row=0, column=0, padx=10, pady=10)

    quantity_list = [0, 0, 0]

    # ##############################food gui###############################

    # ##############################burger setup###############################

    burger = Food('Burger', 0)  # burger instance
    burger_quantity = IntVar()  # burger entry variable
    burger_quantity.set(0)  # default entry value

    # burger name label

    burger_label = ttk.Label(menu_frame, text='Burger')
    burger_label.grid(row=0, column=0, padx=5, pady=5)

    # burger price label

    burger_price = ttk.Label(menu_frame, text=str('$'
                                                  + str(burger_cost)))
    burger_price.grid(row=1, column=0)

    burger_quantity_frame = quantity_frame('burger_quantity', 2, 0)  # frame for burger quantity entry

    # burger user entry

    burger_entry = ttk.Entry(burger_quantity_frame,
                             textvariable=burger_quantity)
    burger_entry.grid(row=0, column=0, padx=5, pady=5)

    # ##############################fries setup###############################

    fries = Food('Fries', 0)  # fries instance
    fries_quantity = IntVar()  # fries entry variable
    fries_quantity.set(0)  # default entry value

    # fries name label

    fries_label = ttk.Label(menu_frame, text='Fries')
    fries_label.grid(row=0, column=1, padx=5, pady=5)

    # fries price label

    fries_price = ttk.Label(menu_frame, text=str('$' + str(fries_cost)))
    fries_price.grid(row=1, column=1)

    fries_quantity_frame = quantity_frame('fries_quantity', 2, 1)  # frame for fries quantity entry

    # fries user entry

    fries_entry = ttk.Entry(fries_quantity_frame,
                            textvariable=fries_quantity)
    fries_entry.grid(row=0, column=0, padx=5, pady=5)

    # ##############################drinks setup###############################

    drinks = Food('Drinks', 0)  # drinks instance
    drinks_quantity = IntVar()  # drinks entry variable
    drinks_quantity.set(0)  # default entry value

    # drinks name label

    drinks_label = ttk.Label(menu_frame, text='Drinks')
    drinks_label.grid(row=0, column=2, padx=5, pady=5)

    # drinks price label

    drinks_price = ttk.Label(menu_frame, text=str('$'
                                                  + str(drinks_cost)))
    drinks_price.grid(row=1, column=2)

    drinks_quantity_frame = quantity_frame('drinks_quantity', 2, 2)  # frame for drinks quantity entry

    # drinks user entry

    drinks_entry = ttk.Entry(drinks_quantity_frame,
                             textvariable=drinks_quantity)
    drinks_entry.grid(row=0, column=0, padx=5, pady=5)

    # variable and instances lists for looping

    variable_list = [burger_quantity, fries_quantity, drinks_quantity]  # variable list
    instances_list = [burger, fries, drinks]  # instances list

    # ##############################quantity gui aesthetics###############################

    quantity_format = StringVar()  # string var for quantity display
    quantity_string = '''Burgers: {}
Fries: {}
Drinks: {}'''  # easily changeable format for quantity display updates
    default_quantity_string = quantity_string.format(0, 0, 0)  # default message display
    quantity_format.set(default_quantity_string)

    overall_string = StringVar()  # tells user whether they are missing any fields or not at the submit button
    overall_string.set(valid_list[2])  # default message

    validity_string = StringVar()  # tells user what to change about their quantity inputs
    validity_string.set(valid_list[2])  # default message
    valid_label = ttk.Label(menu_frame, textvariable=validity_string)
    valid_label.grid(row=3, column=2, padx=5, pady=5)

    # ##############################options and name frame###############################

    # label frame for keeping checkout frame tidy

    bottom_frame = ttk.LabelFrame(root, text='Checkout')
    bottom_frame.grid(row=2, column=0)

    option = IntVar()  # radiobutton option variable
    option.set(1)

    # delivery extra label

    options_desc = ttk.Label(bottom_frame, text='Delivery is $5 extra')
    options_desc.grid(row=0, column=0, padx=5, pady=5)

    # radiobutton for pickup option

    pickup = ttk.Radiobutton(bottom_frame, text='Pickup', value=1,
                             variable=option)
    pickup.grid(row=1, column=0, padx=10, pady=10)

    # radiobutton for delivery option

    delivery = ttk.Radiobutton(bottom_frame, text='Delivery', value=2,
                               variable=option)
    delivery.grid(row=1, column=1, padx=10, pady=10)

    # label frame for storing name entry

    name_frame = ttk.LabelFrame(bottom_frame, text='Name')
    name_frame.grid(row=1, column=2, padx=10, pady=10)

    # name entry

    name_variable = StringVar()  # name variable to store user input
    name_entry = ttk.Entry(name_frame, textvariable=name_variable)
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    # variables for name entry and option entry
    # options

    method_var = StringVar()
    method_display_string = '{}: ${}'

    # name

    name_string_var = StringVar()
    name_string_var.set(valid_list[2])  # default variable

    # tells user whether name is valid or not

    option_label = ttk.Label(bottom_frame, textvariable=name_string_var)
    option_label.grid(row=0, column=2, padx=5, pady=5)

    # ##############################order summary frame###############################

    # label frame for displaying order summary

    summary_frame = ttk.LabelFrame(root, text='Order summary')
    summary_frame.grid(row=0, column=1, padx=10, pady=10)

    # orderer name prompt

    name_title = ttk.Label(summary_frame, text='Name:')
    name_title.grid(row=0, column=0, padx=5, pady=5)

    # orderer name

    name_label = ttk.Label(summary_frame, textvariable=name_variable,
                           wraplength=80)
    name_label.grid(row=1, column=0, padx=5, pady=5)

    # order total quantity

    order_label = ttk.Label(summary_frame, textvariable=quantity_format)
    order_label.grid(row=2, column=0, padx=5, pady=5)

    # variables for setting up delivery or pickup total

    total_string = 'Total: ${}'
    total_string_var = StringVar()
    default_total = total_string.format(0)
    total_string_var.set(default_total)

    total = StringVar()  # total cost
    total.set(0)

    # displays total cost in order summary

    total_label = ttk.Label(summary_frame,
                            textvariable=total_string_var)
    total_label.grid(row=4, column=0, padx=5, pady=5)

    # displays whether pickup or delivery was selected

    method_label = ttk.Label(summary_frame, textvariable=method_var)
    method_label.grid(row=3, column=0, padx=5, pady=5)

    # tells user whether any fields are invalid or not

    error_label = ttk.Label(summary_frame, textvariable=overall_string)
    error_label.grid(row=5, column=0, padx=5, pady=5)

    # button that saves all new info into a dictionary, then into a csv file

    update_button = ttk.Button(summary_frame, text='Submit',
                               command=save_function)
    update_button.grid(row=6, column=0, padx=5, pady=5)

    # opens a new window to display previous orders

    new_window = ttk.Button(root, text='View order history',
                            command=data_display)
    new_window.grid(row=1, column=1, padx=5, pady=5)

    root.mainloop()

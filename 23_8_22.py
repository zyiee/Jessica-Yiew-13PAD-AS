from tkinter import *
from tkinter import ttk
import os
import random

item_dictionary = {}
item_dictionary['item'] = ['price', 'quantity']

class item: #base item info
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
    
#instances
burger = item('Burger', 3)
fries = item('Fries', 2)
drink = item('Drinks', 2)

#window setup
root = Tk()
root.title('Takeaway menu')
root.geometry ('800x500') #570x500

def quantity_frame(item_quantity, y, x): #shortened code for menu aesthetics
    item_quantity = ttk.LabelFrame(top_frame, text = 'Quantity')
    item_quantity.grid(row = y, column = x, padx = 5, pady = 5)
    return item_quantity

#top frame
top_frame = ttk.LabelFrame(root, text = 'Menu')
top_frame.grid(row = 0, column = 0, padx = 10, pady = 10)

#validity indicator
valid_list = ['Please enter a valid number\n(Positive numbers only)', 
              ' ', 
              'Please enter a name', 
              'Please check of your item quantities are valid',
              'Order Saved',
              'Please check if all the fields are valid']
validity_variable = StringVar()
validity_variable.set(valid_list[1]) #default variable

#messages to display when an error occurs
valid_label = ttk.Label(top_frame, textvariable = validity_variable)
valid_label.grid(row = 3, column = 2, padx = 10, pady = 10)

def item_validation(item_variable): #updates label and validates
    try:
        quantity = item_variable.get()
        validity_variable.set(valid_list[1])
        if quantity < 0:
            validity_variable.set(valid_list[0])
            return False
        else:
            return True
    except Exception:
        validity_variable.set(valid_list[0])
        return False

#gathering variables
quantity_format = StringVar() #string var for message display
quantity_string = 'Burgers: {}\nFries: {}\nDrinks: {}' #easily changeable format
default_quantity_string = quantity_string.format(0,0,0) #default message display
quantity_format.set(default_quantity_string) #sets to default msg display

def all_update():  #gets quantity of each item, places into a list for compilation, then updates the string var for msg display
    burger_total = burger_quantity.get()
    quantity_list[0] = burger_total
    
    fries_total = fries_quantity.get()
    quantity_list[1] = fries_total
    
    drinks_total = drinks_quantity.get()
    quantity_list[2] = drinks_total
    
    updated_quantity_string = quantity_string.format(burger_total, fries_total, drinks_total)
    quantity_format.set(updated_quantity_string)

def loop_validator(): #runs through and validates quantity variables, stopping updates if any are invalid
    for items in variable_list:
        value = item_validation(items)
        if value == False:
            return False
        else:
            pass
    all_update()
    return True
##################################################################################################
food_quantity_state = BooleanVar() #states whether the food quantity is valid or not
def update_label(): #gets the variable for a valid or invalid input
    food_quantity_status = loop_validator()
    food_quantity_state.set(food_quantity_status)
    print(food_quantity_state.get(), 'food quantity')
##################################################################################################

price_string = '${}'
#burger
burger_label = ttk.Label(top_frame, text = 'Burger', font = ('Arial', 12))
burger_label.grid(row = 0, column = 0, padx = 5, pady = 5)

burger_price_var = StringVar()
burger_price_string = price_string.format(burger.price)
burger_price_var.set(burger_price_string)

burger_price = ttk.Label(top_frame, textvariable = burger_price_var)
burger_price.grid(row = 1, column = 0, padx = 5, pady = 5)

burger_quantity = IntVar()
burger_quantity.set(0)
burger_quantity_frame = quantity_frame('burger_quantity', 2, 0)

burger_entry = ttk.Entry(burger_quantity_frame, textvariable = burger_quantity)
burger_entry.grid(row = 0, column = 0, padx = 5, pady = 5)

#fries
fries_label = ttk.Label(top_frame, text = 'Fries', font = ('Arial', 12))
fries_label.grid(row = 0, column = 1, padx = 5, pady = 5)

fries_price_var = StringVar()
fries_price_string = price_string.format(fries.price)
fries_price_var.set(fries_price_string)

fries_price = ttk.Label(top_frame, textvariable = fries_price_var)
fries_price.grid(row = 1, column = 1, padx = 5, pady = 5)

fries_quantity = IntVar()
fries_quantity.set(0)
fries_quantity_frame = quantity_frame('fries_quantity', 2, 1)

fries_entry = ttk.Entry(fries_quantity_frame, textvariable = fries_quantity)
fries_entry.grid(row = 0, column = 0, padx = 5, pady = 5)

#drinks
drinks_label = ttk.Label(top_frame, text = 'Drinks', font = ('Arial', 12))
drinks_label.grid(row = 0, column = 2, padx = 5, pady = 5)

drinks_price_var = StringVar()
drinks_price_string = price_string.format(drink.price)
drinks_price_var.set(drinks_price_string)

drinks_price = ttk.Label(top_frame, textvariable = drinks_price_var)
drinks_price.grid(row = 1, column = 2, padx = 5, pady =5)

drinks_quantity = IntVar()
drinks_quantity.set(0)
drinks_quantity_frame = quantity_frame('drinks_quantity', 2, 2)

drinks_entry = ttk.Entry(drinks_quantity_frame, textvariable = drinks_quantity)
drinks_entry.grid(row = 0, column = 0, padx = 5, pady = 5)

#format setup
items_list = ['Burger', 'Fries', 'Drinks']
quantity_list = [0,0,0]
variable_list = [burger_quantity, fries_quantity, drinks_quantity]

#quantity update button
#quantity_submit = ttk.Button(top_frame, text = 'Update', command = update_label)
#quantity_submit.grid(row = 2, column = 3, padx = 5, pady = 5)

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

name_variable = StringVar()
name_entry = ttk.Entry(name_frame, textvariable = name_variable)
name_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

method_var = StringVar()
method_display_string = '{}: ${}'

def option_get():
    value = option.get()
    if value == 1:
        selected_option = 'Pickup'
        selected_display = 'Pickup (Free)'
        pickup_string = method_display_string.format(selected_option, 0)
        method_var.set(pickup_string)
    elif value == 2:
        selected_option = 'Delivery'
        selected_display = 'Delivery (+$5)'
        delivery_string = method_display_string.format(selected_display, 5)
        method_var.set(delivery_string)  
    return selected_option

def option_update():
    if not name_variable.get():
        name_string_var.set(valid_list[2])
        return False
    else:
        name_string_var.set(valid_list[1])
        pass
    name_string_var.set(valid_list[1])
    return True

####################################################################################
entry_state = BooleanVar() #states whether entry box is valid
def entry_update():
    entry_status = option_update()
    entry_state.set(entry_status)
    print(entry_status, 'name box')
####################################################################################
name_string_var = StringVar()
name_string_var.set(valid_list[1]) #default variable
option_label = ttk.Label(bottom_frame, textvariable = name_string_var)
option_label.grid(row = 0, column = 2, padx = 5, pady = 5)

option_frame = ttk.Frame(root)
option_frame.grid(row = 3, column = 0)

#option_submit = ttk.Button(bottom_frame, text = 'Update', command = entry_update)
#option_submit.grid(row = 1, column = 3, padx = 5, pady = 5)

overall_string = StringVar()
overall_string.set(valid_list[1])
overall_label = ttk.Label(option_frame, textvariable = overall_string)
overall_label.grid(row = 0, column = 1, padx = 5, pady = 5)

total_string = 'Total: ${}'
total_string_var = StringVar()
default_total = total_string.format(0)
total_string_var.set(default_total)

total = StringVar()
total.set(0)
def checkout_calculations():
    burger_price = burger.price
    fries_price = fries.price
    drinks_price = drink.price
    
    burger_amount = burger_quantity.get()
    fries_amount = fries_quantity.get()
    drinks_amount = drinks_quantity.get()
    
    total_cost = ((burger_amount*burger_price)+
                  (fries_amount*fries_price)+
                  (drinks_amount*drinks_price))    
    total.set(total_cost)
    value = option.get()
    if value == 1:
        pass
    elif value == 2:
        total_cost += 5
        total.set(total_cost)
    updated_total = total_string.format(total_cost)
    total_string_var.set(updated_total)


update_var = BooleanVar()
def update_all():
    entry_update()
    entry_status = entry_state.get()
    #print(entry_status, 'test entry status')
    update_label()
    food_quantity_status = food_quantity_state.get()
    #print(food_quantity_status, 'test food quantity status')
    if entry_status == False:
        overall_string.set(valid_list[2])
        update_var.set(False)
    elif food_quantity_status == False:
        overall_string.set(valid_list[3])
        update_var.set(False)
    else:
        overall_string.set(valid_list[1])
        checkout_calculations()
        update_var.set(True)
       
#submit_button = ttk.Button(option_frame, text = 'Update', command = update_all)
#submit_button.grid(row = 0, column = 0, padx = 5, pady = 5)

results_frame = ttk.LabelFrame(root, text = 'Order summary')
results_frame.grid(row = 0, column = 1)

#actively updates amount of food thats inputted
item_display = ttk.Label(results_frame, textvariable = quantity_format)
item_display.grid(row = 1, column = 0, padx = 5, pady = 5)

method_display = ttk.Label(results_frame, textvariable = method_var)
method_display.grid(row = 2, column = 0, padx = 5, pady = 5)
                           
total_display = ttk.Label(results_frame, textvariable = total_string_var)
total_display.grid(row = 3, column = 0, padx = 5, pady = 5)

name_display = ttk.Label(results_frame, textvariable = name_variable)
name_display.grid(row = 0, column = 0, padx = 5, pady = 5)

def save_info():
    selected_option = option_get()
    format_string = '\n{}, {}, {}, {}, {}, {}'
    user_name = name_variable.get()
    user_total = total.get()
    user_format = format_string.format(user_name, quantity_list[0], quantity_list[1], quantity_list[2], selected_option, user_total)
    f = open('test.csv', 'a')
    f.write(user_format)
    f.close()

check_var = StringVar()
check_var.set(valid_list[1])
def submit_check():
    update_all()
    check_bool = update_var.get()
    if check_bool == False:
        check_var.set(valid_list[5])
    else:
        check_var.set(valid_list[4])
        save_info()

save_label = ttk.Label(results_frame, textvariable = check_var, wraplength = 100)
save_label.grid(row = 5, column = 0, padx = 5, pady = 5)

save_button = ttk.Button(results_frame, text = 'Submit', command = submit_check)
save_button.grid(row = 4, column = 0, padx = 5, pady = 5)


root.mainloop()
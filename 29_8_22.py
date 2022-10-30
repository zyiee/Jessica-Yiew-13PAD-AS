from tkinter import *
from tkinter import ttk

valid_list = ['Please enter a number', #0
              'Please enter a positive value', #1
              ' ', #2
              'Please enter a name', #3
              'Please check of your item quantities are valid', #4
              'Order Saved', #5
              'Please check if all the fields are valid', #6
              'Please enter a number above 0'] #7

order_data = {}
burger_cost = 3
fries_cost = 2
drinks_cost = 2

test_file = 'test.csv'

class Food:
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

def quantity_frame(item_quantity, y, x): #shortened code for menu aesthetics
    item_quantity = ttk.LabelFrame(menu_frame, text = 'Quantity')
    item_quantity.grid(row = y, column = x, padx = 5, pady = 5)
    return item_quantity

def data_layout():  # opens file and splits every line to put into dictionary
    open_file = open(test_file, encoding='utf-8-sig')
    with open_file as f:
        lines = [line.strip() for line in f]
        y = 0
        for items in lines:
            info = lines[y].split(',')
            key = info[0]
            info.pop(0)
            order_data[key] = info
            y = y + 1

def quantity_display():
    burger.change_quantity(burger_quantity.get())
    quantity_list[0] = burger.quantity
    
    fries.change_quantity(fries_quantity.get())
    quantity_list[1] = fries.quantity
    
    drinks.change_quantity(drinks_quantity.get())
    quantity_list[2] = drinks.quantity

    updated_quantity_string = quantity_string.format(burger.quantity, fries.quantity, drinks.quantity)
    quantity_format.set(updated_quantity_string)
    
    above_zero = any(quantity_list)
    return above_zero

    
def checkout_calculations():        
    total_cost = ((burger.quantity*burger_cost)+
                  (fries.quantity*fries_cost)+
                  (drinks.quantity*drinks_cost))    
    total.set(total_cost)
    value = option.get()
    if value == 1:
        pass
    elif value == 2:
        total_cost += 5
        total.set(total_cost)
    updated_total = total_string.format(total_cost)
    total_string_var.set(updated_total)

def quantity_update():
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

def update_all():
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

def save_function():
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
        print(update_list)
        order_data[name_variable.get()] = update_list
        save_file()

def save_file():  # converts the dictionary and lists within code into suitable format to save into txt file
    with open(test_file, 'w') as file:
        for value in order_data:
            format_list = []
            format_list.append(value)
            data = order_data[value]
            format_list.extend(data)
            startstr = " "
            for items in format_list:
                startstr = startstr + str(items) + ','
            startstr = startstr.strip(',')
            startstr = startstr + '\n'
            file.write(startstr)
    file.close()
        

def name_update():
    if not name_variable.get():
        name_string_var.set(valid_list[3])
        return False
    else:
        name_string_var.set(valid_list[2])
    return True

class data_window:
    def __init__(self):
        self.display_box = Toplevel(root)
        self.display_box.title('Order history')
        self.display_box.geometry('300x500')
        self.display_list = []
        
        for names in order_data:
            data = order_data[names]
            display = ', '.join(data)
            display_full = (str(names + ': ' + display))
            self.display_list.append(display_full)
        
        self.display_string = '\n'.join(self.display_list)
        display_var.set(self.display_string)
        
        self.display_label = ttk.Label(self.display_box, textvariable = display_var, font = ('Arial', 15))
        self.display_label.grid(row = 0, column = 0, padx = 10, pady = 10)
                
            

def data_display():
    data_box = data_window()
    

if __name__ == '__main__':
    data_layout()
    display_var = StringVar()
    #window setup
    root = Tk()
    root.title('Takeaway Menu')
    root.geometry('800x500')
    
    menu_frame = ttk.LabelFrame(root, text = 'Menu')
    menu_frame.grid(row = 0, column = 0, padx = 10, pady = 10)
    
    quantity_list = [0,0,0]
    
    #food gui
    #burger setup
    burger = Food('Burger', 0)
    burger_quantity = IntVar()
    burger_quantity.set(0)
    
    burger_label = ttk.Label(menu_frame, text = 'Burger')
    burger_label.grid(row = 0, column = 0, padx = 5, pady = 5)
    
    burger_price = ttk.Label(menu_frame, text = str('$' + str(burger_cost)))
    burger_price.grid(row = 1, column = 0)
    
    burger_quantity_frame = quantity_frame('burger_quantity', 2, 0)
    burger_entry = ttk.Entry(burger_quantity_frame, textvariable = burger_quantity)
    burger_entry.grid(row = 0, column = 0, padx = 5, pady = 5)
    
    #fries setup
    fries = Food('Fries', 0)
    fries_quantity = IntVar()
    fries_quantity.set(0)
    
    fries_label = ttk.Label(menu_frame, text = 'Fries')
    fries_label.grid(row = 0, column = 1, padx = 5, pady = 5)
    
    fries_price = ttk.Label(menu_frame, text = str('$' + str(fries_cost)))
    fries_price.grid(row = 1, column = 1)
    
    fries_quantity_frame = quantity_frame('fries_quantity', 2, 1)
    fries_entry = ttk.Entry(fries_quantity_frame, textvariable = fries_quantity)
    fries_entry.grid(row = 0, column = 0, padx = 5, pady = 5)
    
    #drinks setup
    drinks = Food('Drinks', 0)
    drinks_quantity = IntVar()
    drinks_quantity.set(0)
    
    drinks_label = ttk.Label(menu_frame, text = 'Drinks')
    drinks_label.grid(row = 0, column = 2, padx = 5, pady = 5)
    
    drinks_price = ttk.Label(menu_frame, text = str('$' + str(drinks_cost)))
    drinks_price.grid(row = 1, column = 2)
    
    drinks_quantity_frame = quantity_frame('drinks_quantity', 2, 2)
    drinks_entry = ttk.Entry(drinks_quantity_frame, textvariable = drinks_quantity)
    drinks_entry.grid(row = 0, column = 0, padx = 5, pady = 5)
    
    variable_list = [burger_quantity, fries_quantity, drinks_quantity]
    instances_list = [burger, fries, drinks]
    
    quantity_format = StringVar() #string var for message display
    quantity_string = 'Burgers: {}\nFries: {}\nDrinks: {}' #easily changeable format
    default_quantity_string = quantity_string.format(0,0,0) #default message display
    quantity_format.set(default_quantity_string)   
    
    overall_string = StringVar()
    overall_string.set(valid_list[2]) #default label
    
    validity_string = StringVar()
    validity_string.set(valid_list[2]) #default message
    valid_label = ttk.Label(menu_frame, textvariable = validity_string)
    valid_label.grid(row = 3, column = 2, padx = 5, pady = 5)     
        
    #bottom frame
    bottom_frame = ttk.LabelFrame(root, text = 'Checkout')
    bottom_frame.grid(row = 2, column = 0)
    
    #options gui
    #option value
    option = IntVar()
    option.set(1)
    
    #option description
    options_desc = ttk.Label(bottom_frame, text = 'Delivery is $5 extra')
    options_desc.grid(row = 0, column = 0, padx = 5, pady = 5)
    
    #pickup button
    pickup = ttk.Radiobutton(bottom_frame, text = 'Pickup', value = 1, variable = option)
    pickup.grid(row = 1, column = 0, padx = 10, pady = 10)
    
    #delivery button
    delivery = ttk.Radiobutton(bottom_frame, text = 'Delivery', value = 2, variable = option)
    delivery.grid(row = 1, column = 1, padx = 10, pady = 10)    
    
    #name frame
    name_frame = ttk.LabelFrame(bottom_frame, text = 'Name')
    name_frame.grid(row = 1, column = 2, padx = 10, pady = 10)
    
    #name entry
    name_variable = StringVar()
    name_entry = ttk.Entry(name_frame, textvariable = name_variable)
    name_entry.grid(row = 1, column = 1, padx = 5, pady = 5)
    
    #variables ################
    method_var = StringVar()
    method_display_string = '{}: ${}'
    name_string_var = StringVar()
    name_string_var.set(valid_list[2]) #default variable
    
    #name update display
    option_label = ttk.Label(bottom_frame, textvariable = name_string_var)
    option_label.grid(row = 0, column = 2, padx = 5, pady = 5) 
    
    #summary box
    summary_frame = ttk.LabelFrame(root, text = 'Order summary')
    summary_frame.grid(row = 0, column = 1, padx = 10, pady = 10)
    
    #orderer name
    name_title = ttk.Label(summary_frame, text = 'Name:')
    name_title.grid(row = 0, column = 0, padx = 5, pady = 5)
    
    name_label = ttk.Label(summary_frame, textvariable = name_variable, wraplength = 80)
    name_label.grid(row = 1, column = 0, padx = 5, pady = 5)
    
    #order total label
    order_label = ttk.Label(summary_frame, textvariable = quantity_format)
    order_label.grid(row = 2, column = 0, padx = 5, pady = 5)
    
    total_string = 'Total: ${}'
    total_string_var = StringVar()
    default_total = total_string.format(0)
    total_string_var.set(default_total)
    
    total = StringVar()
    total.set(0)    
    
    total_label = ttk.Label(summary_frame, textvariable = total_string_var)
    total_label.grid(row = 4, column = 0, padx = 5, pady = 5)
    
    method_label = ttk.Label(summary_frame, textvariable = method_var)
    method_label.grid(row = 3, column = 0, padx = 5, pady = 5)
    
    error_label = ttk.Label(summary_frame, textvariable = overall_string)
    error_label.grid(row = 5, column = 0, padx = 5, pady = 5)
    
    update_button = ttk.Button(summary_frame, text = 'Submit', command = save_function)
    update_button.grid(row = 6, column = 0, padx = 5, pady = 5)    
    
    new_window = ttk.Button(root, text = 'View order history', command = data_display)
    new_window.grid(row = 1, column = 1, padx = 5, pady = 5)
    
    root.mainloop()

            
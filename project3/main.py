import tkinter as tk # Import tkinter for GUI
from tkinter import ttk # Import ttk for combobox
from tkinter import font as tkFont  # Import tkFont for font definitions
import products_dao as dao # Import products_dao for database operations
from sql_connection import get_sql_connection # Import get_sql_connection for database connection

connection = get_sql_connection() # Get the database connection

class Window():
    ''' 
    This class creates the main window for the Inventory Management System

    Attributes:
    master: the main window
    products: a list of all products in the database
    menu: the menu object that contains all the buttons and tables

    Methods:
    __init__: initializes the main window
    '''
    def __init__(self, master):
        ''' Initializes the main window
        
        Parameters:
        master: the main window
        '''
        self.master = master # Create the main window
        self.master.title("Inventory Management System") # Set the title of the main window locally
        self.master.resizable(False, False) # Make the main window non-resizable
        self.products = dao.get_all_products(connection) # Get all products from the database
        self.menu = Menu(self.master, self.products) # Create the menu object

class Menu:
    '''
    This class creates the menu for the Inventory Management System
    
    Attributes:
    master: the main window
    button_frame: the frame that contains the buttons
    table_frame: the frame that contains the table
    add_frame: the frame that contains the add form
    delete_frame: the frame that contains the delete form
    title: the title of the form
    name_label: the label for the name entry
    name_entry: the entry for the name
    uom_label: the label for the uom selection
    uom_selection: the dropdown menu for uom
    price_label: the label for the price entry
    price_entry: the entry for the price


    Methods:
    __init__: initializes the menu
    init_buttons: initializes the buttons
    init_table: initializes the table
    update: updates the table
    init_add_screen: initializes the add form
    back_button_add: goes back to the main menu from the add form
    add_validation: validates the add form
    add: adds a new product to the database
    init_delete_screen: initializes the delete form
    back_button_delete: goes back to the main menu from the delete form
    delete_validation: validates the delete form
    delete: deletes a product from the database
    init_error_label: initializes the error label
    blank_spaces: creates blank spaces in the form
    '''
    def __init__(self, master, lst):
        ''' 
        Initializes the menu
        
        Parameters:
        master: the main window
        lst: a list of all products in the database
        '''
        self.master = master # Create the main window locally

        self.init_buttons() # Initialize the button frame
        self.init_table(lst) # Initialize the table frame

    def init_buttons(self):
        '''
        Initializes the buttons
        '''

        self.button_frame = tk.Frame(self.master) # Create a frame for the buttons
        self.button_frame.grid(row = 0) # Place the frame in the main window

        update_button = tk.Button(self.button_frame, text="Update", command=self.update) # Create an Update button
        update_button.grid(row=0, column=0) # Place the Update button in the frame

        delete_button = tk.Button(self.button_frame, text="Delete", command=self.init_delete_screen) # Create a Delete button
        delete_button.grid(row=0, column=1) # Place the Delete button in the frame

        # create a Add button
        add_button = tk.Button(self.button_frame, text="Add", command=self.init_add_screen) # Create an Add button
        add_button.grid(row=0, column=2) # Place the Add button in the frame

    def init_table(self, lst):
        '''
        Initializes the table

        Parameters:
        lst: a list of all products in the database
        '''

        self.table_frame = tk.Frame(self.master) # Create a frame for the table
        self.table_frame.grid(row=1) # Place the frame in the main window

        total_rows = len(lst) # Get the total number of rows
        total_columns = dao.get_column_count(connection, "products") # Get the total number of columns
        for j in range(total_columns): # Loop through the columns to create headers for the table
            e = tk.Entry(self.table_frame) # Create an entry for the table
            e.grid(row=0, column=j) # Place the entry in the frame
            if j == 0: # If the column is 0, insert Product ID in the entry
                e.insert(tk.END, "Product ID")
            if j == 1: # If the column is 1, insert Name in the entry
                e.insert(tk.END, "Name")
            if j == 2: # If the column is 2, insert Price Per Unit in the entry
                e.insert(tk.END, "Price Per Unit")
            if j == 3: # If the column is 3, insert Unit of Measure in the entry
                e.insert(tk.END, "Unit of Measure")
            if j == 4: # If the column is 4, insert Quantity in Stock in the entry
                e.insert(tk.END, "Quantity in Stock")
            e.config(state='readonly', readonlybackground='#ffffcc') # Make the entry read-only with a light yellow readonly background
        for i in range(total_rows): # Loop through the rows and columns to create the table
            for j in range(total_columns): 
                e = tk.Entry(self.table_frame) # Create an entry for the table 
                e.grid(row=i+1, column=j) # Place the entry in the frame
                if type(lst[i][j]) == float: # If the value is a float, format it as a currency then insert the value, otherwise insert the value
                    formatted_float = f"$ {lst[i][j]:.2f}" 
                    e.insert(tk.END, formatted_float)
                else:
                    e.insert(tk.END, lst[i][j])
                e.config(state='readonly', readonlybackground='#ffffe0') # Make the entry read-only and apply a light yellow readonly background

    def update(self):
        '''
        Updates the table
        '''
        self.table_frame.destroy() # Destroy the table frame
        self.init_table(dao.get_all_products(connection)) # Reinitialize the table frame with an updated products list

    def init_add_screen(self):
        '''
        Initializes the add form
        '''
        self.button_frame.destroy() # Destroy the button frame
        self.table_frame.destroy() # Destroy the table frame
        self.add_frame = tk.Frame(self.master) # Create a frame for the add form
        self.add_frame.grid(row=0) # Place the frame in the main window
        self.cols = [0, 2, 8, 10] # Create a list of columns to create blank spaces
        self.blank_spaces(0, self.cols, "add") # Create blank spaces in the form
        
        self.title = tk.Label(self.add_frame, text="Add a New Product") # Create a title for the form
        self.title.grid(row=0, column=4, columnspan=4) # Place the title in the frame
        self.name_label = tk.Label(self.add_frame, text="Name:") # Create a name label
        self.name_label.grid(row=1, column=4, columnspan=2) # Create a name label and place it in the frame
        self.name_entry = tk.Entry(self.add_frame) # Create an entry for the name
        self.name_entry.grid(row=1, column=6, columnspan=2) # Place the entry in the frame

        uom_options = dao.get_uom_list(connection) # Get the list of unit of measure options from the database
        self.uom_label = tk.Label(self.add_frame, text="Unit of Measure:") # Create a Unit of Measure label
        self.uom_label.grid(row=2, column=4, columnspan=2) # Place the Unit of Measure label in the frame
        self.uom_selection = ttk.Combobox(self.add_frame, values=uom_options) # Create a dropdown menu for the unit of measure
        self.uom_selection.grid(row=2, column=6, columnspan=2) # Place the dropdown menu in the frame

        self.price_label = tk.Label(self.add_frame, text="Price Per Unit:") # Create a Price Per Unit label
        self.price_label.grid(row=3, column=4, columnspan=2) # Place the Price Per Unit label in the frame
        self.price_entry = tk.Entry(self.add_frame) # Create an entry for the price
        self.price_entry.grid(row=3, column=6, columnspan=2) # Place the entry in the frame

        self.quantity_label = tk.Label(self.add_frame, text="Quantity in Stock:") # Create a Quantity label
        self.quantity_label.grid(row=4, column=4, columnspan=2) # Place the Quantity label in the frame
        self.quantity_entry = tk.Entry(self.add_frame) # Create an entry for the quantity
        self.quantity_entry.grid(row=4, column=6, columnspan=2) # Place the entry in the frame

        self.back_button = tk.Button(self.add_frame, text="Back", command=self.back_button_add) # Create a Back button
        self.back_button.grid(row=5, column=4, columnspan=2) # Place the Back button in the frame
        self.submit_button = tk.Button(self.add_frame, text="Submit", command=self.add_validation) # Create a Submit button
        self.submit_button.grid(row=5, column=6, columnspan=2) # Place the Submit button in the frame

    def back_button_add(self):
        '''
        Goes back to the main menu from the add form
        '''

        self.add_frame.destroy() # Destroy the add frame
        self.init_buttons() # Reinitialize the buttons
        self.init_table(dao.get_all_products(connection)) # Reinitialize the table

    def add_validation(self):
        '''
        Validates the add form
        '''
        if hasattr(self, 'error_label') and self.error_label is not None: # If the error label exists, destroy it
            self.error_label.destroy()
            self.error_label = None

        if not self.name_entry.get(): # If the name entry is empty, initialize the error label
            self.init_error_label(6, "name")
            if not self.uom_selection.get(): # If the name entry and uom selection are empty, initialize the error labels
                self.init_error_label(7, "uom")
                if not self.price_entry.get(): # If the name entry, uom selection, and price entry are empty, initialize the error labels
                    self.init_error_label(8, "price")
                    if not self.quantity_entry: # If the name entry, uom selection, price entry, and quantity entry are empty, initialize the error labels
                        self.init_error_label(9, "quantity")
                elif not self.price_entry.get().isdigit(): # If the name entry and uom selection, and the price entry is not a number, initialize the error labels
                    self.init_error_label(8, "price", "not_digit")
                    if not self.quantity_entry: # If thename entry, uom selection and quanity entry are empty and price entry is not empty initialize the error labels
                        self.init_error_label(9, "quantity")
        elif not self.uom_selection.get(): # If the uom selection is empty, initialize the error label
            self.init_error_label(6, "uom")
            if not self.price_entry.get(): # If the uom selection and price entry are empty, initialize the error labels
                self.init_error_label(7, "price")
                if not self.quantity_entry: # If the uom selection, price entry, and quantity entry are empty, initialize the error labels
                    self.init_error_label(8, "quantity")
            elif not self.price_entry.get().isdigit(): # If the uom selection is empty and the price entry is not a number, initialize the error labels
                self.init_error_label(7, "price", "not_digit")
                if not self.quantity_entry: # If the uom selection and quanity entry are empty and price entry is not a number initialize the error labels
                    self.init_error_label(8, "quantity")
        elif self.price_entry.get() == "": # If the price entry is empty, initialize the error label
            self.init_error_label(6, "price")
            if not self.quantity_entry: # If the price entry is empty and the quantity entry is empty, initialize the error labels
                self.init_error_label(7, "quantity")
        elif not self.price_entry.get().isdigit(): # If the price entry is not a number, initialize the error label
            self.init_error_label(6, "price", "not_digit")
            if not self.quantity_entry: # If the price entry is not a number and the quantity entry is empty, initialize the error labels
                self.init_error_label(7, "quantity")
        elif not self.quantity_entry: # If the quantity entry is empty, initialize the error label
            self.init_error_label(6, "quantity")
        else: # If all fields are filled out correctly, add the product to the database
            self.add()

    def add(self):
        '''
        Adds a new product to the database        
        '''
        name = self.name_entry.get() # Get the name from the name entry
        uom_id = dao.uom_name_to_uom_id(connection, self.uom_selection.get()) # Get the unit of measure ID from the unit of measure selection
        price = int(self.price_entry.get()) # Get the price from the price entry
        quantity = int(self.quantity_entry.get()) # Get the quantity from the quantity entry
        dao.insert_new_product(connection, {'product_name': name, 'uom_id': uom_id, 'price_per_unit': price, 'quantity_in_stock': quantity}) # Insert the new product into the database
        self.add_frame.destroy() # Destroy the add frame
        self.init_buttons() # Reinitialize the buttons
        self.init_table(dao.get_all_products(connection)) # Reinitialize the table

    def init_delete_screen(self):
        '''
        Initializes the delete form
        '''
        self.button_frame.destroy() # Destroy the button frame
        self.table_frame.destroy() # Destroy the table frame
        self.delete_frame = tk.Frame(self.master) # Create a frame for the delete form
        self.delete_frame.grid(row=0) # Place the frame in the main window
        self.cols = [0, 2, 8, 10] # Create a list of columns to create blank spaces
        self.blank_spaces(0, self.cols, "delete") # Create blank spaces in the form
    
        self.title = tk.Label(self.delete_frame, text="Delete a Product") # Create a title for the form
        self.title.grid(row=0, column=4, columnspan=4) # Place the title in the frame

        product_options = dao.get_product_list(connection) # Get the list of products from the database
        self.delete_label = tk.Label(self.delete_frame, text="Select an product to delete:") # Create a label for the product selection
        self.delete_label.grid(row=1, column=4, columnspan=2) # Place the label in the frame
        self.product_selection = ttk.Combobox(self.delete_frame, values=product_options) # Create a dropdown menu for the products
        self.product_selection.grid(row=1, column=6, columnspan=2) # Place the dropdown menu in the frame

        self.back_button = tk.Button(self.delete_frame, text="Back", command=self.back_button_delete) # Create a Back button
        self.back_button.grid(row=2, column=4, columnspan=2) # Place the Back button in the frame
        self.submit_button = tk.Button(self.delete_frame, text="Submit", command=self.delete_validation) # Create a Submit button
        self.submit_button.grid(row=2, column=6, columnspan=2) # Place the Submit button in the frame

    def back_button_delete(self):
        '''
        Goes back to the main menu from the delete form
        '''
        self.delete_frame.destroy() # Destroy the delete frame
        self.init_buttons() # Reinitialize the buttons
        self.init_table(dao.get_all_products(connection)) # Reinitialize the table

    def delete_validation(self):
        '''
        Validates the delete form
        '''
        if hasattr(self, 'error_label') and self.error_label is not None: # If the error label exists, destroy it
            self.error_label.destroy()
            self.error_label = None

        if self.product_selection.get() == "": # If the product selection is empty, initialize the error label
            self.init_error_label(3, "product")
        else:
            self.delete()

    def delete(self):
        '''
        Deletes a product from the database
        '''
        product =self.product_selection.get() # Get the product from the product selection
        product_id = product.split(":")[0] # Get the product ID from the product
        dao.delete_product(connection, product_id) # Delete the product from the database
        self.delete_frame.destroy() # Destroy the delete frame
        self.init_buttons() # Reinitialize the buttons
        self.init_table(dao.get_all_products(connection)) # Reinitialize the table

    def init_error_label(self, r, field, reason = "empty"):
        '''
        Initializes the error labels

        Parameters:
        r: the row to put the error label
        field: the field that is in error
        reason: the reason why the field is in error (default is empty)
        '''
        if field == "name": # If the name field is in error, initialize the error label
            self.error_label = tk.Label(self.add_frame, text="Name cannot be empty", fg = "red")
            self.error_label.grid(row=r, column=4, columnspan=4)
        if field == "uom": # If the uom field is in error, initialize the error label
            self.error_label = tk.Label(self.add_frame, text="Unit of Measure cannot be empty", fg = "red")
            self.error_label.grid(row=r, column=4, columnspan=4)
        if field == "price": # If the price field is in error, initialize the error label
            if reason == "empty": # If the price field is empty, initialize the error label
                self.error_label = tk.Label(self.add_frame, text="Price per Unit cannot be empty", fg = "red")
                self.error_label.grid(row=r, column=4, columnspan=4)
            if reason == "not_digit": # If the price field is not a number, initialize the error label
                self.error_label = tk.Label(self.add_frame, text="Price per Unit must be a number", fg = "red")
                self.error_label.grid(row=r, column=4, columnspan=4)
        if field == "product": # If the product field is in error, initialize the error label
            self.error_label = tk.Label(self.delete_frame, text="Please select a product to delete", fg = "red")
            self.error_label.grid(row=r, column=4, columnspan=4)

    def blank_spaces(self, r, cols, frame):
        '''
        Creates blank spaces in the form
        '''
        if frame == "add": # If the frame is the add frame, create blank spaces
            blank_space = tk.Label(self.add_frame, text="", width=2)
        elif frame == "delete": # If the frame is the delete frame, create blank spaces
            blank_space = tk.Label(self.delete_frame, text="", width=2)
        for col in cols: # Loop through the columns to create blank spaces
            blank_space.grid(row=r, column=col, columnspan=2)

def main():
    '''
    Main function that creates the main window and executes the main GUI loop
    '''
    root = tk.Tk() # Create the root window
    window = Window(root) # Create the main window object with the root window
    root.mainloop() # Execute the main GUI loop

if __name__ == "__main__":
    main()
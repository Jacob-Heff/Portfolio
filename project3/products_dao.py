def get_all_products(connection):
    '''
    Returns a list of all products in the database

    Parameters:
    connection: the connection to the database

    Returns:
    response: a list of all products in the database (product_id, product_name, price_per_unit, quantity_in_stock, uom_name)
    '''
    cursor = connection.cursor() # Create a cursor object using the connection

    query = ("SELECT products.product_id, products.name, products.price_per_unit, products.quantity_in_stock, uom.uom_name "
    "FROM products INNER JOIN uom ON products.uom_id=uom.uom_id;") # SQL query to get all products

    cursor.execute(query) # Execute the query

    response = [] # Initialize an empty list to store the results

    for(product_id, name, price_per_unit, quantity_in_stock, uom_name) in cursor: # Iterate through the query results
        response.append(
            [
                product_id, 
                name,
                price_per_unit,
                uom_name,
                quantity_in_stock
            ]
        )
    return response # Return the list of products

def get_product_list(connection):
    '''
    Returns a list of all products in the database

    Parameters:
    connection: the connection to the database

    Returns:
    response: a list of all products in the database (product_id: product_name)
    '''
    cursor = connection.cursor() # Create a cursor object using the connection

    query = ("SELECT products.product_id, products.name FROM products") # SQL query to get all products

    cursor.execute(query) # Execute the query

    response = [] # Initialize an empty list to store the results

    for(product_id, name) in cursor: # Iterate through the query results
        product_id = str(product_id) + ": " # Convert the product_id to a string and add a colon
        response.append(
                product_id + name # Append the product_id and name to the list
        )
    return response # Return the list of products

def get_uom_list(connection):
    '''
    Returns a list of all units of measurement in the database

    Parameters:
    connection: the connection to the database

    Returns:
    response: a list of all units of measurement in the database
    '''
    cursor = connection.cursor() # Create a cursor object using the connection

    query = ("SELECT uom.uom_name FROM uom") # SQL query to get all units of measurement

    cursor.execute(query) # Execute the query

    response = [] # Initialize an empty list to store the results

    for uom_name in cursor: # Iterate through the query results
        response.append(uom_name
        )
    return response # Return the list of units of measurement

def uom_name_to_uom_id(connection, uom_name):
    '''
    Returns the unit of measurement ID for a given unit of measurement name

    Parameters:
    connection: the connection to the database
    uom_name: the name of the unit of measurement

    Returns:
    cursor[0]: the unit of measurement ID
    '''
    cursor = connection.cursor() # Create a cursor object using the connection

    query = ("SELECT uom_id FROM uom WHERE uom_name='" + uom_name + "'") # SQL query to get the unit of measurement ID

    cursor.execute(query) # Execute the query

    cursor = cursor.fetchone() # Get the first result

    return cursor[0] # Return the unit of measurement ID

def insert_new_product(connection, product):
    '''
    Inserts a new product into the database

    Parameters:
    connection: the connection to the database
    product: a dictionary containing the product name, unit of measurement ID, price per unit, and quantity in stcok
    '''

    cursor = connection.cursor() # Create a cursor object using the connection

    query = ("INSERT INTO products" 
            "(name, uom_id, price_per_unit, quantity_in_stock)" 
            "VALUES (%s, %s, %s, %s)") # SQL query to insert a new product
    
    data = (product['product_name'], product['uom_id'], product['price_per_unit'], product['quantity_in_stock']) # Data to insert into the query

    cursor.execute(query, data) # Execute the query
    connection.commit() # Commit the changes to the database

def delete_product(connection, product_id):
    '''
    Deletes a product from the database
    
    Parameters:
    connection: the connection to the database
    product_id: the ID of the product to delete
    '''
    cursor = connection.cursor() # Create a cursor object using the connection

    query = ("DELETE FROM products WHERE product_id=" + str(product_id)) # SQL query to delete a product

    cursor.execute(query) # Execute the query

    connection.commit() # Commit the changes to the database

def get_column_count(connection, table_name):
    '''
    Returns the number of columns in a table

    Parameters:
    connection: the connection to the database
    table_name: the name of the table

    Returns:
    count: the number of columns in the table
    '''
    cursor = connection.cursor() # Create a cursor object using the connection
    query = """
    SELECT COUNT(*) 
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE TABLE_SCHEMA = %s 
    AND TABLE_NAME = %s;
    """ # SQL query to get the number of columns in a table
    
    cursor.execute(query, (connection.database, table_name)) # Execute the query
    count = cursor.fetchone()[0] # Get the first result
    return count # Return the number of columns
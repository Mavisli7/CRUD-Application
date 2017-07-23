import csv

file_path ="data/products.csv"
headers=["id","name","aisle","department","price"]
products=[]

def read_products():
    '''
    read the products from csv file
    '''
    with open(file_path, "r") as csv_file:
        reader=csv.DictReader(csv_file)
        for Ordered_Dict in reader:
            products.append(dict(Ordered_Dict))

def welcome():
    '''
    welcome message
    '''
    username=input("Please input your username: ")
    print("-----------------------------------")
    print("PRODUCTS APPLICATION")
    print("-----------------------------------")
    print("Welcome @" + username + "!")
    print("\n")
    print("There are" +str(len(products)) +"products in the database. Please select an operation: ")
    print("\n")
    print("    Operation | description")
    print("    --------- | -----------------")
    print("    'List'    | Display a list of product identifiers and names.")
    print("    'Show'    | Show information about a product.")
    print("    'Create'  | Add a new product.")
    print("    'Update'  | Edit an existing product.")
    print("    'Destroy' | Delete an existing product.")

def list_function():
    '''
    list the products
    '''
    print("THERE ARE " + str(len(products))+" PRODUCTS: ")
    for product in products:
        print("+ " + str(product))

def input_find_product():
    '''
    input find a product
    '''
    user_input=input("OK. Please specify the product's identifier: ")
    selected_products=[product for product in products if product['id'] == user_input]
    if selected_products:
        return selected_products[0]
    else:
        print("Product Not Found")
        return None

def show_function():
    '''
    show a product from user input
    '''
    selected_product = input_find_product()
    if selected_product:
        print("SHOWING A PRODUCT HERE!")
        print(selected_product)

def get_new_id(products):
    '''
    product a new id for created product
    '''
    ids=[]
    for product in products:
        ids.append(int(product['id']))
    return max(ids)+1

def create_function():
    '''
    create a product and write to file
    '''
    print("OK. Please specify the product's information...")
    new_product=dict.fromkeys(headers)
    new_product['id']=str(get_new_id(products))
    for header in headers[1:]:
        new_product[header]=input("    {0} :".format(header))
    print("CREATING A PRODUCT HERE!")
    print(new_product)
    products.append(new_product)
    write_products()

def update_function():
    '''
    update a product and write to file
    '''
    selected_product = input_find_product()
    if selected_product:
        print("OK. Please specify the product's information...")
        for header in headers[1:]:
            selected_product[header]=input("Change '{0}' from '{1}' to: ".format(header, selected_product[header]))
        print("UPDATING A PRODUCT HERE!")
        print(selected_product)
        write_products()

def destroy_function():
    '''
    destroy a product and write to file
    '''
    selected_product = input_find_product()
    if selected_product:
        print("DESTROYING A PRODUCT HERE!")
        print(selected_product)
        del products[products.index(selected_product)]
        write_products()

def write_products():
    '''
    write products to csv file
    '''
    with open(file_path,'w', newline='') as csv_file:
        writer=csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

#1. read products
read_products()

#2. Welcome message
welcome()

#3. Begin service
while True:
    user_input=input()
    if user_input.title() == "List":
        list_function()
    elif user_input.title() == "Show":
        show_function()
    elif user_input.title() == "Create":
        create_function()
    elif user_input.title() == "Update":
        update_function()
    elif user_input.title() == "Destroy":
        destroy_function()
    elif user_input.title() == "Exit":
        print("Thanks for the visit, see you next time.")
        break
    else:
        user_input=input("Operation not supported, please try again: ")

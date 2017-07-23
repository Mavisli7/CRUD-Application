import csv

#file_path ="data/products.csv"
file_path ="/Users/mavisup/Desktop/nyu-info-2335-70-201706/projects/crud-app/products.csv"

products=[]
with open(file_path, "r") as csv_file:
    reader=csv.DictReader(csv_file)
    for Ordered_Dict in reader:
        products.append(dict(Ordered_Dict))

products_count=len(products)
headers=["id","name","aisle","department","price"]

#Welcome Message
username=input("Please input your username: ")
print("-----------------------------------")
print("PRODUCTS APPLICATION")
print("-----------------------------------")
print("Welcome @" + username + "!")
print("\n")
print("There are" +str(products_count) +"products in the database. Please select an operation: ")
print("\n")
print("    Operation | description")
print("    --------- | -----------------")
print("    'List'    | Display a list of product identifiers and names.")
print("    'Show'    | Show information about a product.")
print("    'Create'  | Add a new product.")
print("    'Update'  | Edit an existing product.")
print("    'Destroy' | Delete an existing product.")


#Write csvfile function
def write_row():
    with open(file_path,'w', newline='') as csv_file:
        writer=csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

#5 Functions
def list_function():
    print("THERE ARE" + str(products_count)+"PRODUCTS: ")
    for product in products:
        print("+ " + str(product))

def show_function():
    show_input=input("OK. Please specify the product's identifier: ")
    show_product=[product for product in products if product['id'] == show_input]
    if show_product:
        print("SHOWING A PRODUCT HERE!")
        print(show_product)
    else:
        print("Product Not Found")

def max_id(products):
    ids=[]
    for product in products:
        ids.append(int(product['id']))
    return max(ids)

def create_function():
    print("OK. Please specify the product's information...")
    new_product=dict.fromkeys(headers)
    new_product['id']=str(max_id(products)+1)
    for header in headers[1:]:
        new_product[header]=input("    {0} :".format(header))
    print("CREATING A PRODUCT HERE!")
    print(new_product)
    products.append(new_product)
    write_row()

def update_function():
    update_input=input("OK. Please specify the product's identifier: ")
    update_product=[product for product in products if product['id'] == update_input]
    if update_product:
        update_product=update_product[0]
        print("OK. Please specify the product's information...")
        for header in headers[1:]:
            update_product[header]=input("    change '{0}' from '{1}' to: ".format(header,update_product[header]))
        print("UPDATING A PRODUCT HERE!")
        print(update_product)
        write_row()
    else:
        print("Product Not Found")


def destroy_function():
    destroy_input=input("OK. Please specify the product's identifier: ")
    destroy_product=[product for product in products if product['id']==destroy_input][0]
    if destroy_product:
        print("DESTROYING A PRODUCT HERE!")
        print(destroy_product[0])
        del products[products.index(destroy_product[0])]
        write_row()
    else:
        print("COULDN'T FIND A PRODUCT WITH IDENTIFIER",destroy_input)


user_input=input(" ")

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

else:
    user_input=input("OOOPS SORRY! Please try again: ")

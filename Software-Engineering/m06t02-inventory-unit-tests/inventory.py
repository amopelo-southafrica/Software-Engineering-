class Shoe():
    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    def get_cost(self):
        total_cost = self.cost
        return total_cost
    
    def get_product(self):
        product_name = self.product
        return product_name

    def get_quantity(self):
        total_quantity = self.quantity
        return total_quantity
    
    def description(self):
        return f"{self.product} - R{self.cost:}\n Quantity:{self.quantity}Code:{self.code}\n Country:{self.country}"
    
clean_data = []
def read_shoes_data():
#Take the data from the file
    with open('inventory.txt','r') as file:
#Store each line from the data in a list 
        for shoe in file[1:]:
            shoe_details = shoe.split(",")
            country = shoe_details[0]
            code =shoe_details[1]
            product =shoe_details[2]
            cost =shoe_details[3]
            quantity =shoe_details[4]
            shoes = Shoe(country,code,product,cost,quantity)
            clean_data.append(shoes)
#For each line create a shoe object
def capture_shoes():
#Get data about a shoe
    country_user = input("Enter the country of the shoe:")
    code_user = input("Enter the product code:")
    product_user = input("Enter the product:")
    cost_user= int(input("Enter the cost of the shoe:"))
    quantity_user = int(input("Enter the quantities of the shoes:"))
    shoe_2 = Shoe(country_user,code_user,product_user,cost_user,quantity_user)
    new_shoe = clean_data.append(shoe_2)
    print(shoe_2)
    
def view_all():
    for shoe in clean_data:
        print(f'{shoe}\n')


def re_stock():
    sorted_list = []
    for numbers in clean_data:
        quantities = numbers[4]
        sorted_list.append(quantities)
    small_number = len(min(sorted_list))
    for index, small in enumerate(small_number, start=1):
        try:
            print(f'{small} is the remaining quantity for a shoe at shoe number {index}.')
            user_quantatity = int(input("Enter quantity to add:"))
        except ValueError:
            print("Oops! That was not a entry. Please enter a number")

#Add the quantites to that shoe object
    total_quantity = clean_data[index].get_quantity() + user_quantatity
    clean_data[index].quantity = total_quantity
    print("New quantity updated")

def search_shoe(target,items=clean_data):
    target_item = int(input("SKU:\n e.g SKU:84923"))
#Use the search function
    for index in range(len(items)): 
        if items[index] == target: 
            return index  
    result = search_shoe(target = target_item) 
    print(result)

def value_per_item():
#Take each item
    values_list = []
    for item in clean_data:
#Get the total
        total_value = item.get_cost()* item.get_quantity()
#Store in a list
        value_list = values_list.append(total_value)
#Print the output
        print(f'This is the value for {item.product()}:{total_value}')

def highest_qty():
#Get the item with the highest quantity
    items__list = []
    for items in clean_data:
        quantities_list = items.get_quantity()
        items__list.append(quantities_list) 
    big_quantity = max(items__list)
#Once found, find out which product
    index_postion = clean_data.index(big_quantity)
    biggest_quantity = index_postion
#Show the user it is on sale, for the store
    print(f'{biggest_quantity} should be listed for on sale')

#==========Main Menu=============
#Start with an introduction to the program
def show_menu():
    while True:
        print("Welcome Nike Manager." \
        "\n This program is designed to help you manage, track, and review warehouse " \
        "stock-taking sessions efficiently.\n It gives you a clear overview of inventory levels," \
       " highlights discrepancies, and supports faster, more organised decision-making during stock checks." \
    "\n With this system, you can: " \
    "\na.Record and review stock-taking sessions" \
    "\nb.Monitor available stock quantities." \
    "\nc.Identify shortages or excess stock quickly" \
    "\nd.Improve delivery planning and warehouse organisation")
#List the options and what these options can do

        print("\n Choose an option from the menu:" \
        "\n 1. Load inventory data from file" \
        "\n 2. Capture new shoe stock"\
        "\n 3. View all shoes in inventory" \
        "\n 4. Restock lowest quantity item " \
        "\n 5. Search for a shoe by code" \
        "\n 6. View value per item "\
        "\n 7. View item with highest quantity (On Sale)\n 0. Exit program")
#If they choose a certain option display the output
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            search_shoe()
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "0":
            print("Exiting system. Stock data secured.")
            
        else:
            print("Invalid selection. Please try again.")
            break
 
#Start the menu
show_menu()

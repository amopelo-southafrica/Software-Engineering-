class Shoe():
    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    def get_cost(self):
        total_cost = int(self.cost)
        return total_cost
    
    def get_product(self):
        product_name = self.product
        return product_name
    
    def get_code(self):
        product_code = self.code
        return product_code

    def get_quantity(self):
        total_quantity = int(self.quantity)
        return total_quantity
    
    def __str__(self):
        return f"{self.product} - R{self.cost:}\n Quantity:{self.quantity}Code:{self.code}\n Country:{self.country}"

                                    #----------Loads data from the file----------#
clean_data = []
def read_shoes_data():
    try:
        with open('inventory.txt','r') as file:
            next(file)             
            for shoe in file:
                shoe_details = shoe.split(",")
                country = shoe_details[0]
                code =shoe_details[1]
                product =shoe_details[2]
                cost =shoe_details[3]
                quantity =shoe_details[4]
                shoes = Shoe(country,code,product,cost,quantity)
                clean_data.append(shoes)
    except FileNotFoundError:
        print("Error: {file} not found.")
                                   #----------Captures new information about a new shoe----------#
def capture_shoes():
    print("\nAdd a New Shoe to Inventory")
    print("-" * 30)
    country_user = input("Manufacturing country (e.g. South Africa):")
    code_user = input("Unique product code (e.g. SKU1234): ")
    product_user = input("Product name (e.g. Nike Air Force 1):")
    cost_user= int(input("Unit cost (ZAR, numbers only): "))
    quantity_user = int(input("Initial stock quantity: "))
    shoe_2 = Shoe(country_user,code_user,product_user,cost_user,quantity_user)
    new_shoe = clean_data.append(shoe_2)
    print("Oops! That was not a valid entry. Try again...")
    print("\nShoe successfully added to inventory:")
    print(shoe_2)
                                 #----------Views all shoes in the stocklist----------#
def view_all():
    if not clean_data:
        print("Inventory is empty.")
        return
    for shoe in clean_data:
        print("\nCurrent Inventory:\n")
        print("=" * 30)
        print(f'{shoe}\n')
        print( f"-" * 30)

                                #----------Requests for a restock on the lowest quantity----------#
def re_stock():
    if not clean_data:
        print("Inventory is empty. Nothing to restock.")
        return
    lowest_shoe = None
    for shoe in clean_data:
        if lowest_shoe is None or shoe.get_quantity() < lowest_shoe.get_quantity():
            lowest_shoe = shoe
    print(f'{lowest_shoe.get_product()} has the lowest number of shoes in the stocklist. Quantities:{lowest_shoe.get_quantity()}')

    quantity_update = int(input("Please enter the number of new quantities:"))
    lowest_num = lowest_shoe.get_quantity()+ quantity_update
    print( f"-" * 30)
    print(f'New quantity for {lowest_shoe.get_product()}: {lowest_num}')
    print( f"-" * 30)

                                #----------Searches for a specific shoe ----------#
def search_shoe():
    if not clean_data:
        print("Inventory is empty.")
        return
    target = input("Enter the product code to search for: ")

    for shoe in clean_data:
        if shoe.get_code() == target:
            print("\n Product found:")
            print(f'{target} : {shoe.get_product()}')
            return

    print("\n No product found with that code.")

                                #----------Calculates the total value for each shoe----------#
def value_per_item():
    if not clean_data:
        print("Inventory is empty.")
        return
    for shoe in clean_data:
        total_quantities = shoe.get_quantity()
        total_cost = shoe.get_cost()
        total_value = total_quantities * total_cost
        shoe_name = shoe.get_product() 

        print(f'{shoe_name}\n Total Stock Value: R{total_value}')
        print( f"-" * 30)

                                #----------Requests for a sale on the highest number of shoes----------#
def highest_qty():
    if not clean_data:
        print("Inventory is empty.")
        return
    highest_shoe = None

    for shoe in clean_data:
        if highest_shoe is None or shoe.get_quantity() > highest_shoe.get_quantity():
            highest_shoe = shoe

    print(f"\nSale Recommendation:\n")
    print(f"{highest_shoe.get_product()} has the highest stock level ")
    print(f"({highest_shoe.get_quantity()} units).\n")
    print(f"Consider marking this item as ON SALE.")
                                    #==========Main Menu=============#
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

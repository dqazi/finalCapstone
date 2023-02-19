
class Shoe:
    #define constructor method for the shoe class
    def __init__(self, country, code, product, cost, quantity):
        #assign values passed in as arguments to the objects properties
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
#define the function get_cost to get the cost of the shoe and return the cost property of the object
    def get_cost(self):
        return self.cost
 #define the function get_quantity to get the quality of the shoe  and return quantity property of the object
    def get_quantity(self):
        return self.quantity
#define the string representation of the shoe object and return a formatted string witht he objects properties 
    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"

#create a shoe list
shoes_list = []

#define the function read_shoes_data - to read the inventory.txt file and populate the shoes_list with shoe objects 
def read_shoes_data(shoes_list):
    try:
       #open file and store its content in the file variable 
        with open("inventory.txt") as file:
            #read all lines in the file
            lines = file.readlines()
            #enumerate through each line, if currnet line is the first line, skip it
            for i, line in enumerate(lines):
                if i == 0:
                    continue
                #split the line by comma and assign resulting values to the correspondant variables
                country, code, product, cost, quantity = line.strip().split(",")
                #convert string to float data
                cost = float(cost)
                #convert string to int data
                quantity = int(quantity)
                #create shoe object using the extracted data
                shoe = Shoe(country, code, product, cost, quantity)
                #add the shoe object data to the list
                shoes_list.append(shoe)
                #print confirmation of list being added
            print("Data from inventory.txt file load successfully!")
     #exception error occure if reading the file. - will print the line with error message       
    except Exception as e:
        print(f"An error occurred: {e}")

#define function capture_shoe - print all shoe objects in the shoes_list
def capture_shoes(shoes_list):
    #get user to input various data for the new shoe
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost £: "))
    quantity = int(input("Enter quantity: "))
    #create a new shoe object using the entered data
    new_shoe = Shoe(country, code, product, cost, quantity)
    #append the new shoe object to the shoes_list
    shoes_list.append(new_shoe)
    try:
        #open inventory.txt in append
        with open("inventory.txt", "a") as file:
            #write the the new information to txt file & print confirmation
            file.write(f"\n{country},{code},{product},{cost},{quantity}")
            print(f'{product} data saved to inventory.txt file successfully!')
    except Exception as e:
        print(f"An error occurred: {e}")


#define function view_all - print all shoe objects in the shoe_list
def view_all(shoes_list):
    for shoe in shoes_list:
        print(shoe)

#defire function re_stock - finds shoe with  lowest quantitiy and allows user to add quantity 
def re_stock():
    #set lowest quantity to positive infinity
    lowest_quantity = float("inf")
    #initalise the lowest quantity shoe to none
    lowest_quantity_shoe = None
    #iterate through the shoes_list 
    for shoe in shoes_list:
       # if the current shoe has a lower quantity than the current lowest_quality 
        if shoe.get_quantity() < lowest_quantity:
            #update the lowest_quantity to the current shoes quantity 
            lowest_quantity = shoe.get_quantity()
            #update the lowest_quantity_shoe to the current shoe
            lowest_quantity_shoe = shoe
    #print the lowest quantity shoe
    print("The shoe with the lowest quantity is:")
    print(lowest_quantity_shoe)
#ask user if they want to increase the amout of shoes 
    answer = input("Do you want to add to the quantity of this shoe? (y/n)")
    if answer.lower() == "y":
        #request user to enter amount of stock they want to add
        add_quantity = int(input("How many do you want to add? "))
        lowest_quantity_shoe.quantity += add_quantity

         # update the inventory.txt file with the new quantity
        try:
            with open("inventory.txt", "w") as file:
                # write the header
                file.write("country,code,product,cost,quantity\n")
                # write the shoe data
                for shoe in shoes_list:
                    line = f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n"
                    file.write(line)
            print("Inventory updated successfully!")

        except Exception as e:
            print(f"An error occurred while updating the inventory: {e}")
    else:
        print("No change to inventory made")


#define function search_shoe.
def search_shoe(code):
    #user inputs shoe code
    shoe_code = input('''Please enter corresponding shoe code to search:
    ''')
    #iterate through shoe list 
    for shoe in shoes_list:
        #check if the code of current shoe in loop matches the input shoe code
        if shoe.code == shoe_code:
            #if it matches, print the related shoe detail
            print (shoe)
            return
    #if the loop finishes wihtout a matching shoe- print message        
    print("Error - Shoe Not Found.")

# define value_per_item function
def value_per_item(shoes_list):
    #loop through the list of shoes
    for shoe in shoes_list:
        #calculate the value of the stock for each shoe by multiplying cost by quantity
        value = shoe.cost * shoe.quantity
        #Print the product name and total stock value
        print(f"{shoe.product}: Total Stock Value = £{value}")

#define highest_qty function
def highest_qty(shoes_list):
    #set variable highest_quantity to keep track of the highest quantity of shoes
    highest_quantity = 0
    # set a variable 'highest_quantity_shoe' to keep track of the shoe with the highest quantity
    highest_quantity_shoe = None
    #loop through the list of shoes
    for shoe in shoes_list:
        #check if the quantity of the current shoe in the loop is higher than the current highest quantity
        if shoe.quantity > highest_quantity:
            #if the current shoe in the loop has a higher quantity than update the highest quantity
            highest_quantity = shoe.quantity
            #update the shoe witht he highest quantity
            highest_quantity_shoe = shoe
#print message with the shoe witht he highest quantity 
    print(f'''The shoe with the highest quantity is:
    {highest_quantity_shoe}''')
    


print(">>WELCOME TO THE SHOE INVENTORY MANAGEMENT SYSTEM<<")
#Create a while loop for the menu to run

#read data from the inventory txt file when programme starts
read_shoes_data(shoes_list)
while True:
    #load up data from the 
    
    print('''\n MENU
    1. Capture Shoes
    2. View All Shoes
    3. Re-Stock Shoes
    4. Search Shoe
    5. Calculate Value per Item
    6. Determine Highest Quantity
    7. Exit''')
    
    #try to run the following functions dependant on the input from the user    
    try:
        choice = int(input("Please enter your choice [1-8]: "))
      
        if choice == 1:
            capture_shoes(shoes_list)
        elif choice == 2:
            view_all(shoes_list)
        elif choice == 3:
            re_stock()
        elif choice == 4:
            search_shoe(shoes_list)
        elif choice == 5:
            value_per_item(shoes_list)
        elif choice == 6:
            highest_qty(shoes_list)
        elif choice == 7 :
            print(" See Ya!")
            break
        else:
            print("please enter between 1-8")
    #except value error if user inputs non-accepted character        
    except ValueError:
        print("No Letters, Numbers Between 1-8 Only")       
        
        
    
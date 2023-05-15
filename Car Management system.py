class User():
    def __init__(self, userID):
        self.userID = userID

    def login(self):
        self.username = input("Please enter your username: ")
        self.password = input("Please enter your password: ")  
        for line in open("database.txt","r").readlines(): # Read the lines
            login_info = line.split() # Split on the space, and store the results in a list of two strings
            if self.username == login_info[0] and self.password == login_info[1]:
                print("welcome!", self.username)
                print("The id of the user is ", self.userID)
                return True
        print("Invalid credentials.")
        return False

#Inheriting properties and attribute from user class
class Customer(User):
    def __init__(self, balance, userID):
        super().__init__(userID) #using overidding method
        # will take the input from the user
        self.cus_name = str(input("Enter your name: "))
        self.phone = str(input("Enter your phone number "))
        self.cus_email = str(input("Enter your email: "))
        self.balance = balance

    def register_customer(self):
        self.username = input("Please create your username ")
        self.password = input("Please create your password ")
        #the user can write and append 
        file = open("database.txt","a") 
        file.write(self.username)
        file.write(" ")
        file.write(self.password)
        file.write("\n")
        file.close()
        print(f'\nThe following customer {self.username} has been registered ')
        print("\nPress 3 to book a ride")

    def register(self):
        #The details of the customer are being displayed
        print("\nCustomer details:")
        print("The name of customer is ", self.cus_name)
        print("The phone number of customer is ", self.phone)
        print("The customer email is ", self.cus_email)
        print("The balance of customer that has been entered ", self.balance)
        print("The id of the user generated is ", self.userID)
        
#Inheriting properties and attribute from user class
class Admin(User):
    def __init__(self, name, rating, phone, userID):
        super().__init__(userID) #using overriding method
        self.name = name
        self.rating = rating
        self.phone = phone
    
    def Details(self):
        print("\nAdmin (driver) information: ")
        print(f'The name of the driver is {self.name} \nThe rating of the driver is {self.rating} \nThe phone of the driver is {self.phone} ')
        print(f'The user id displaying to the driver is {self.userID} ')

class Booking():
    def __init__(self, date, time, credit, cash, balance, userID, vehical):
        self.pickup = str(input("Enter pick up location: "))
        self.dropoff = str(input("Enter a drop off of location: "))
        #setting up the attributes
        self.date = date
        self.time = time 
        self.credit = credit
        self.cash = cash
        self.obj_book = Customer(balance, userID) #Taking customer class as composite
        self.obj_vehical = vehical #Taking vehical class as zggeratation

    def book(self):
        print("\nBooking info: ")
        print(f'The pick up location is {self.pickup} ')
        print(f'The drop off location is {self.dropoff} ')
        print(f'The current date {self.date} ')
        print(f'The current time is {self.time} ')
        print(f'The amount in credit is {self.credit} ')
        print(f'The amount in cash is {self.cash} ')
        self.obj_book.register() #Will display the attributes from the Customer class defined in function register
        print("\nPress 4 to view driver information")

class Credit():
    def __init__(self, credit):
        self.credit = credit
        self.credit_no = str(input("Enter the credit number: "))
        self.credit_exp = str(input("Enter expiry date for credit card: "))

    def Details(self):
        print(f'The credit card number is {self.credit_no} ')
        print(f'The expiration date for the credit card is {self.credit_exp} ')
        print(f'The amount in credit card is {self.credit} ')

class Payment():
    def __init__(self, tax, credit, balance, userID,):
        self.cost = 1500
        self.tax = tax
        self.balance = balance
        self.userID = userID
        self.obj_payemnt = Credit(credit) #taking credit class as composite

    def details(self):
        print("\n")
        print(f'The cost for the trip is {self.cost} ')
        print(f'The tax charged is {self.tax} ')
        print(f'The credit if the user has entered is {self.obj_payemnt.credit}')

    def totalcost(self):
        self.totalcost = (self.tax + self.cost) #Calculating the total cost
        self.remain_balance = (self.balance - self.totalcost) #Calculating the remaining balance
        print("\n")
        print(f'The total cost for the trip is {self.totalcost} ')
        print(f'This is your remaining balance {self.remain_balance} ')

class Vehical():
    def __init__(self,lists):
        self.type = lists

    def avaliable(self):
        print("\nThe vehicals avaliable currently are: ")
        for i in self.type: #creating a loop in order to display vehical type from list
            print(i)
        
    def choose(self, vehicals):
        if vehicals in self.type: #checking if the satatement holds true
            print(f'\nThe vehical selected {vehicals}')
        else:
            print("Invalid option")

#Inherating properties and attributes from vehical class
class Auto(Vehical):
    def __init__(self, model, num, lists):
        super().__init__(lists)
        self.model = model
        self.num = num

    def Display(self):
        print(f'The model of the auto is {self.model} \nThe number of the auto is {self.num} ')
#Inherting properties and attributes from vehical class
class Bike(Vehical):
    def __init__(self, model, num, lists):
        super().__init__(lists)
        self.model = model
        self.num = num     

    def Display(self):
        print(f'Bike model is {self.model} \nThe number is {self.num} ')   

 #inheriting from vehical class   
class Car(Vehical):
    def __init__(self, car_lists, lists):
        super().__init__(lists)
        self.car = car_lists
        

    def Display(self):
        print("\nThe car currently avaliable is: \n")
        print(self.car)
        
def main():
#Definig the menu
        print("\nWelcome to cab booking system - Uber")
        print("Select your options:")
        print()
        print("[1] User ")
        print("[2] customer registration")
        print("[3] booking registration")
        print("[4] Admin (driver) details")
        print("[5] Auto information")
        print("[6] Bike information")
        print("[7] Car information")
        print("[8] Confrim Payment")
        print("[9] Cancel ride")
        print("[10] Exit")
        print()
main()

loop = 1
# I have defined this globally incase we have to use it in other objects
obj_6 = Vehical(["Auto","Bike","Car"])

#The loop has been started
while loop == 1 :

    #Will take option from user as input in the form of integers
    option = int(input("Enter an option: "))

    if option == 1:

        obj_1 = User("zh-21456")
        obj_1.login()

    elif option == 2:
        obj_2 = Customer(2100, "zh-21456")
        obj_2.register()
        obj_2.register_customer()
        
    elif option == 3:
        vehical = Vehical(["Auto", "Bike", "Car"])
        obj_3 = Booking("21-02-2011", "12:00Pm", 1400 ,1500, 2100, "zh-21456", vehical)
        obj_6.avaliable()
        # Will display the correct vehical entered
        vehical.choose(input("Select a vehical: "))
        obj_3.book()  

    elif option == 4:
        obj_admin = Admin("Zoriaz", "4.5", "0303-1234899", "zh-21456")
        obj_admin.Details()
        print("\nPress 5 , 6 , 7 to view your vehical info") #After above data has been printed and displayed this shall be printed and displayed afterwards

    elif option == 5:
        obj_7 = Auto("CNG", "1233-234",["Auto", "Bike", "Car"])
        obj_7.Display()

    elif option == 6:

        obj_8 = Bike("Honda", "231-900",["Auto", "Bike", "Car"])
        obj_8.Display()

    elif option == 7:
        obj_9 = Car("Hyundai Elentra - 223-444",["Auto", "Bike", "Car"])
        obj_9.Display()

    elif option == 8:
        obj_5 = Payment(12.48, 1200, 2100, "zh-21456")
        obj_5.details()
        obj_5.totalcost()

    elif option == 9:
        print("Your ride has been successfully cancelled")

    elif option == 10:
        print("Thank you for selecting your services with us")
        #The value has been set to zero in order to stop the loop
        loop = 0
    #For printing error message incase any value outside to that decribed in the menu above has been entered    
    else:
        print("Invalid option try again")


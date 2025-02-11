#! /usr/bin/python3

#9.1 restauraunt
print("9.1 restaurant: ")

class Restaurant:
    """model a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_resaurant(self):
        """prints restaurant info"""
        print(f"This restaurant ({self.restaurant_name}) serves {self.cuisine_type}")
        
    def open_restaurant(self):
        print(f"This restaurant ({self.restaurant_name}) is now open!")
        
restaurant = Restaurant("Whitakers", "Sushi")
restaurant.describe_resaurant()
restaurant.open_restaurant()


#9.2 three restaurants
print("9.2 three restaurants: ")
restaurant1 = Restaurant("Pumpkintown general store", "Breakfast")
restaurant2 = Restaurant("Chic-Fil-A", "Chicken")
restaurant3 = Restaurant("Menkoi", "Ramen")
restaurant1.describe_resaurant()
restaurant2.describe_resaurant()
restaurant3.describe_resaurant()


#9.3 users
print("9.3 users:")
class User:
    """model a user"""
    def __init__(self, fname, lname, username, age, account_type):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.age = age
        self.accout_type = account_type
    
    def describe_user(self):
        print(f"See your profile details below: ")
        print(f"NAME: {self.fname.title()} {self.lname.title()}")
        print(f"USERNAME: {self.username}")
        print(f"ACCOUNT TYPE: {self.accout_type}")
        
    def greet_user(self):
        print(f"Hello, {self.fname.title()}!")
        
user1 = User("mikayla", "hubbard", "mhubbard", 21, "admin")
user1.greet_user()
user1.describe_user()    

user2 = User("luis", "martinez-meraz", "lmartinez", 22, "user")
user2.greet_user()
user2.describe_user()  

user3 = User("Freza", "Thompson", "freza125", 13, "user")
user3.greet_user()
user3.describe_user()  

#9.4 number served
print("9.4 number served:")
class Restaurant2:
    """model a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_resaurant(self):
        """prints restaurant info"""
        print(f"This restaurant ({self.restaurant_name}) serves {self.cuisine_type}")
        print(f"This restaurant has served {self.number_served} people")
        
    def open_restaurant(self):
        print(f"This restaurant ({self.restaurant_name}) is now open!")
        
    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        
    def increment_number_served(self, number):
        self.number_served += abs(number)
    
restaurant4 = Restaurant2("Stravinsky's", "Russion")
restaurant4.describe_resaurant()
restaurant4.set_number_served(8)
restaurant4.describe_resaurant() 
restaurant4.increment_number_served(1)
restaurant4.describe_resaurant()


#9.5 login attempts
print("9.5 login attempts:")
class User2:
    """model a user"""
    def __init__(self, fname, lname, username, age, account_type):
        self.fname = fname
        self.lname = lname
        self.username = username
        self.age = age
        self.accout_type = account_type
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"See your profile details below: ")
        print(f"NAME: {self.fname.title()} {self.lname.title()}")
        print(f"USERNAME: {self.username}")
        print(f"ACCOUNT TYPE: {self.accout_type}")
        
    def greet_user(self):
        print(f"Hello, {self.fname.title()}!")
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        
user1 = User2("mikayla", "hubbard", "mhubbard", 21, "admin")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

#9.6 ice cream stand
print("9.6 ices cream stand")
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        
        
    def display_flavors(self, flavors):
        print("Here are the available flavors:")
        for flavor in flavors:
            print(f"- {flavor}")
            
oconee_restaurant = IceCreamStand("Deb's Ice Cream", "Ice Cream")
oconee_restaurant.display_flavors(["chocolate", "vanilla"])

#9.7 admin
print("9.7 admin:")
class Admin2(User):
    def __init__(self, fname, lname, username, age, account_type):
        super().__init__(fname, lname, username, age, account_type)
        self.privleges = ["can add post", "can delete post", "ban ban user", "can see statistics"]
        
    def describe_privledges(self):
        print("Admin Privledges:")
        for privlege in self.privleges:
            print(f"- {privlege}")
            
admin1 = Admin2("mikayla", "hubbard", "mhubbard", 21, "admin")
admin1.describe_privledges()

#9.8 privleges
print("9.8 privleges:")
class Privleges:
    def __init__(self):
        self.privleges = ["can add post", "can delete post", "can ban user", "can see statistices"]
        
    def describe_privledges(self):
        print("Admin Privledges:")
        for privlege in self.privleges:
            print(f"- {privlege}")
            
class Admin3(User):
    def __init__(self, fname, lname, username, age, account_type):
        super().__init__(fname, lname, username, age, account_type)
        self.privleges = Privleges()
    
            
admin1 = Admin3("mikayla", "hubbard", "mhubbard", 21, "admin")
admin1.privleges.describe_privledges()
        
#9.9 battery upgrade
print("9.9 battery upgrade:")
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")
        
    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()

#9.10 imported Restaurant
print("9.10 imported Restaurant:")
from chapter9imports import Restaurant3 as R3
chronicles = R3("chronicles cafe", "sandwiches")
chronicles.describe_resaurant()

#9.11 imported admin
print("9.11 imported Admin:")
from chapter9imports import Admin4
new_admin = Admin4("charlie", "charleson", "ccharlie", 24, "admin")
new_admin.privleges.describe_privledges()

#9.12 multiple modules
from chapter9adminImports import Admin5
new_admin2 = Admin5("lin", "Lapiz", "llapiz", 31, "admin")
new_admin2.privleges.describe_privledges()

#9.13 dice
print("9.13 dice:")
from random import randint, choice
class Die:
    def __init__(self):
        self.sides = 6
        
    def roll(self):
        roll = randint(1, self.sides)
        print(roll)

print("6 sided:")
die = Die()
for number in range(10):
    die.roll()    
print("10 sided:")
die2 = Die()
die2.sides = 10
for number in range(10):
    die2.roll()    
print("20 sided:")
die3 = Die()
die3.sides = 20
for number in range(10):
    die3.roll()    
    
#9.14 lottery
print("9.14 lottery:")
list = ["2", "18", "91", "95", "96", "86", "44", "59", "12", "61", "k", "a", "e", "n", "s"]

def generate_number(list): 
    winning = "" 
    for number in range(4):
        win = choice(list)
        winning += f" {win}"
    return winning.title()
    
print(f"Any ticket matching these four number/letters wins a prize: {generate_number(list)}")


#9.15 lottery analysis
print("9.15 lottery analysis:")
my_ticket = generate_number(list)
winning_ticket = generate_number(list)
count = 1;
while my_ticket != winning_ticket:
    winning_ticket = generate_number(list)
    count += 1
    
print(f"The loop ran {count} times in order to get me a winning ticket")

#9.16 python module of the week
print("9.16 python module of the week")

#https://pymotw.com/3/time/index.html
import textwrap
import time
#you can get the current time
print(f"the time is {time.ctime()}")
#you can calculate a future time
later = time.time() + (20 * 60)
print(f"In 20 minutes it will be {time.ctime(later)}")
#this pauses the program for half a second
time.sleep(.5)
#this is how you access specific parts of the time, like year, month, hour etc.
print(f"The year is {time.gmtime().tm_year}")

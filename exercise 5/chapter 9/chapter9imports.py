class Restaurant3:
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
  
class User3:
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
        
class Privleges2:
    def __init__(self):
        self.privleges = ["can add post", "can delete post", "can ban user", "can see statistices"]
        
    def describe_privledges(self):
        print("Admin Privledges:")
        for privlege in self.privleges:
            print(f"- {privlege}")
            
class Admin4(User3):
    def __init__(self, fname, lname, username, age, account_type):
        super().__init__(fname, lname, username, age, account_type)
        self.privleges = Privleges2()

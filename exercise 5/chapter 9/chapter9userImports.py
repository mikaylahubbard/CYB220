class User4:
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
        

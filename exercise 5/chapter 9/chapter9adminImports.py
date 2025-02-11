from chapter9userImports import User4
class Privleges3:
    def __init__(self):
        self.privleges = ["can add post", "can delete post", "can ban user", "can see statistices"]
        
    def describe_privledges(self):
        print("Admin Privledges:")
        for privlege in self.privleges:
            print(f"- {privlege}")
            
class Admin5(User4):
    def __init__(self, fname, lname, username, age, account_type):
        super().__init__(fname, lname, username, age, account_type)
        self.privleges = Privleges3()

#! /usr/bin/python3

#10.1 learning python
print("10.1 learning python:")
from pathlib import Path

pythonPath = Path('learningPython.txt')
contents = pythonPath.read_text()
print(contents)
lines = contents.splitlines()
for line in lines:
    print(f"\n{line}")
    
#alternate way of opeing a file, as done in the slides
with open('learningPython.txt') as file:
    contents = file.read()
    print(contents)

#10.2 learning C
print("10.2 learning C: ")
c = contents.replace('python', 'C')
print(c)

#10.3 simpler code
print("10.3 simpler code")
pythonContents = Path('learningPython.txt').read_text()
for line in pythonContents.splitlines():
    print(line)
    
print(pythonContents.replace('python', 'C'))

#10.4 guest
print("10.4 guest:")
name = input("Please write your name: ")
path = Path('name.txt')
path.write_text(name)

#10.5 Guest Book
print("10.5 guest book:")
path = Path('guestBook.txt')
contents = ""
active = True
while active:
    name = input("Please enter a name to add to the guest book (q to quit): ")
    if name == 'q':
        active = False
        break
    else:
        contents += f"\n{name}"
path.write_text(contents)

#10.6 addition
print("10.6 addition:")
print("Adding 2 numbers")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
try:
    answer = int(num1) + int(num2)
except ValueError:
    print("Can't add a letter! Please only enter numbers :)")
else:
    print(f"{num1} + {num2} = {answer}")
    
#10.7 addition calculator
print("10.7 addition calculator:")
active = True
while active:
    print("\nCalculate the sum of 2 numbers. Enter 'q' at anytime to quit")
    num1 = input("Enter the first number: ")
    if num1 == 'q':
        active = False
        break
    num2 = input("Enter the second number: ")
    if num2 == 'q':
        active = False
        break
    try:
        answer = int(num1) + int(num2)
    except ValueError:
        print("Can't add a letter! Please only enter numbers :)")
    else:
        print(f"{num1} + {num2} = {answer}")
        
#10.8 cats and dogs
print("10.8 cats and dogs:")
filenames = ['cats.txttt', 'dogs.txt']
for file in filenames:
    path = Path(file)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file '{path}' does not exist :()")
    else:
        print(contents)
    
#10.9 silent cats and dogs
print("10.9 silent cats and dogs:")
for file in filenames:
    path = Path(file)
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        print(contents)

#10.10 common words
# https://gutenberg.org/ebooks/75341
# https://gutenberg.org/ebooks/75289 

print("10.10 common words:")
filenames = ['theDreadfulDragonOfHayHill.txt', ]

path = Path('theDreadfulDragonOfHayHill.txt')
contents = path.read_text()
count = contents.lower().count('the ')
print(count)

#10.11 favorite number
print("10.11 favorite number: ")
import json


def storeFavoriteNumber():
    num = input("Enter your favorite number: ")
    filename = 'favoriteNumber.json'
    with open(filename, "w") as f:
        json.dump(num, f)
        
def readFavoriteNumber():
    filename = 'favoriteNumber.json'
    with open(filename) as f:
        num = json.load(f)
        print(f"Your favorite number is {num}")
        
storeFavoriteNumber()
readFavoriteNumber()

#10.12 favorite number remembered
print("10.12 favorite number remembered")
def favoriteNumber():
    filename = 'favoriteNumber2.json'
    try: 
        with open(filename) as f:
            num = json.load(f)
    except:
        num = input("Enter your favorite number: ")
        with open(filename, "w") as f:
            json.dump(num, f)
    else:
        print(f"Your favoite number is {num}")    

favoriteNumber()

#10.13 user dictionary
print("10.13 User dictionary:")

def get_stored_dictionary(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        dictionary = json.loads(contents)
        return dictionary
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    age = input("what is your age? ")
    account_type = input("What is the account type? ")
    dictionary = {
        'username': username,
        'age': age,
        'account_type': account_type
        }
    contents = json.dumps(dictionary)
    path.write_text(contents)
    return username

def greet_user():
    """Greet the user by name."""
    path = Path('username2.json')
    dictionary = get_stored_dictionary(path)
    username = dictionary['username']
    if username:
        print(f"Welcome back, {username}!")
        print("Your info: ")
        for k, v in dictionary.items():
            print(f"{k}: {v}")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()

#10.14 verify user
print("10.14 verify user: ")

def get_stored_dictionary2(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        dictionary = json.loads(contents)
        return dictionary
    else:
        return None

def get_new_username2(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    age = input("what is your age? ")
    account_type = input("What is the account type? ")
    dictionary = {
        'username': username,
        'age': age,
        'account_type': account_type
        }
    contents = json.dumps(dictionary)
    path.write_text(contents)
    return username

def greet_user2():
    """Greet the user by name."""
    path = Path('username2.json')
    dictionary = get_stored_dictionary2(path)
    username = dictionary['username']
    if username:
        correct = input(f"Is this the correct username (y/n): {username}: ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            print("Your info: ")
            for k, v in dictionary.items():
                print(f"{k}: {v}")
        else:
            username = get_new_username2(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username2(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user2()

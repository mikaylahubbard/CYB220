import string
import secrets

#chars = string.ascii_letters + string.digits + string.punctuation
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
special = string.punctuation
#string.printable

#num_chars = int(input("How many characters would you like your password to be?: "))

num_upper = int(input("How many uppercase letters do you want? "))
num_lower = int(input("How many lowercase letters do you want? "))
num_digits = int(input("How many digits  do you want? "))
num_special = int(input("How many special characters do you want? "))
contents = ""

for num in range(num_upper):
    contents += secrets.choice(upper)
for num in range(num_lower):
    contents += secrets.choice(lower)
for num in range(num_digits):
    contents += secrets.choice(digits)
for num in range(num_special):
    contents += secrets.choice(special)

length = len(contents)


password = [None] * length
#randomly swap the indexes

for character in contents:
        indicis = [i for i, x in enumerate(password) if x == None]
        new_position = secrets.choice(indicis)
        password[new_position] = character


password = ''.join(password)
print(password)

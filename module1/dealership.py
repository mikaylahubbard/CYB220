#! /usr/bin/python3
import random
#Mikayla Hubbard - CYB 220 - Exercise 1 Part 2

# This is a program to store new vehicle inventory and assist with monthly payments
# Create variable of your favorite car brand
brand = "subaru"
# Create list of 5 of their models from cheapest to most expensive
models = ["impreza", "legacy", "crosstrek", "outback", "forester"]
# Append a 6th model to the list
models.append("ascent")
# Create list of 5 standard colors for all models
colors = ["black silica", "magnetite grey metallic", "daybreak blue pearl", "offshore blue metallic", "pure red"]
# Replace your last color with a different color
colors[-1] = "crystal white pearl"
# Create variable of the current new year models
year = 2025
# Create MSRP constant number (not string) of each of the models
IMPREZA = 22995
LEGACY = 25010
CROSSTREK = 25810
OUTBACK = 29010
FORESTER = 29810
ASCENT = 38910
# Create a constant number (not string) for total months in 4yr, 5yr, and 6yr loans
MONTHS_FOUR = 4*12
MONTHS_FIVE = 5*12
MONTHS_SIX = 6*12
# Create a variable for the guest's name. Be courteous in your upcoming messages :)
guest_name = "milton hershey"
# Create message variable (with f-string) welcoming customer to your new car store
message = f"Hi, {guest_name.title()}! Welcome to the {brand.title()} dealership :)"
# Create awesome banner with your brand/name/dealership, however you want to welcome customers
line1 = ":'######::'##::::'##:'########:::::'###::::'########::'##::::'##:"
line2 = "'##... ##: ##:::: ##: ##.... ##:::'## ##::: ##.... ##: ##:::: ##:"
line3 = " ##:::..:: ##:::: ##: ##:::: ##::'##:. ##:: ##:::: ##: ##:::: ##:"
line4 = ". ######:: ##:::: ##: ########::'##:::. ##: ########:: ##:::: ##:"
line5 = ":..... ##: ##:::: ##: ##.... ##: #########: ##.. ##::: ##:::: ##:"
line6 = "'##::: ##: ##:::: ##: ##:::: ##: ##.... ##: ##::. ##:: ##:::: ##:"
line7 = ". ######::. #######:: ########:: ##:::: ##: ##:::. ##:. #######::"
line8 = ":......::::.......:::........:::..:::::..::..:::::..:::.......:::"
banner = f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}\n{line8}\n"
# Print awesome banner and welcome message
print(banner)
print(message)
# Using title methods, print the number vehicles in alphabetical order, with the year and available colors.
alphabetical = sorted(models)
print("Models:")
for car in alphabetical:
    print(f"\t{car.title()}")

print(f"Year: {year}\nColor Options:")
for color in colors:
    print(f"\t{color.title()}")
    
# Create a variable that calculates a monthly payment (no interest) for 5yr/60months for the firstvehicle
mon_pay_5 = round(ASCENT/MONTHS_FIVE)

# and print that in a nice, kind message. Don't be rude/pushy to the customer :)
print(f"\nThe first option is the Ascent, which costs ${mon_pay_5} a month with our five year plan")
# Do the same thing, but give them 4yr and 6yr options for the same vehicle
mon_pay_4 = round(ASCENT/MONTHS_FOUR)
mon_pay_6 = round(ASCENT/MONTHS_SIX)
print(f"If you would like to consider a four year plan, the monthly payment would be ${mon_pay_4}. For a six year plan, this number would drop to ${mon_pay_6} a month")
# Lastly, give them a 5yr option for each of the other vehicles, just to see if they are interested
print(f"For a comparison, if you chose a five year plan with any of the other models, the monthly payment would be as follows:")
print(f"\tCrosstrek: ${round(CROSSTREK/MONTHS_FIVE)}\n\tForester: ${round(FORESTER/MONTHS_FIVE)}\n\tImpreza: ${round(IMPREZA/MONTHS_FIVE)}\n\tLegacy: ${round(LEGACY/MONTHS_FIVE)}\n\tOutback: ${round(OUTBACK/MONTHS_FIVE)}")


#Create 3 new features in this program. This can be building off of features (more loan options),
# discount for paying all cash, just ensure that it is utilizing the lessons learned in Module 2
# and not just simply printing strings. Math, lists, f-strings, must be involved.

#feature #1
#rich dude wants to buy them all, how much would it cose
total_cost = IMPREZA + LEGACY + CROSSTREK + OUTBACK + FORESTER + ASCENT
total_mon_5 = round(total_cost/MONTHS_FIVE)
print(f"\nOh, you're looking to spend a lot of money? As you wish. If you get one of each car model, the total cost would be ${total_cost} with a monthly payment of ${total_mon_5}")

#feature #2
#giving him a discount per car bought, how much would the total be now?
total_discount_cost = round(total_cost * .85)
total_mon_discount = round(total_discount_cost/MONTHS_FIVE)
print(f"\nHowever, we do have a discount where if you buy 2 or more cars, each car is 15 percent off")
print(f"In this case, your total cost would be ${total_discount_cost} with a monthly payment of ${total_mon_discount}")


#feature #3
#car showing, show the customer one each of the different cars, with a random color, including the price

print("\nHere are some of the cars you might be interested in:")

#these prices correspond with the cars via indexes
all_prices = [22995, 25010, 25810, 29010, 29810, 38910]

for index in range(6):
    car = models[index]
    price = all_prices[index]
    color = random.choice(colors)
    print(f"{index + 1}. This car is a {year} {car.title()}, of the color {color.title()}, and it costs ${price}")
    
print(f"\nThank you so much for visiting and taking a look at what we have to offer! Have a good day :)")


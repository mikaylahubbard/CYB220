#! /usr/bin/python3
#8.3 T-shirt
print("8.3 T-shirt:")
def make_shirt(size, text):
    print(f"Shirt size: {size}\nMessage: {text}")
    
make_shirt("M", "hello, world")
make_shirt(text="make tea, not war", size="XL")

#8.4 Large shirts
print("8.4 Large shirts:")
def make_shirt(size="L", text="I love python"):
    print(f"Shirt size: {size}\nMessage: {text}")
make_shirt()
make_shirt(size="M")
make_shirt("XL", "make tea, not war")

#8.5 Cities
print("8.5 Cities:")
def describe_city(name, country="the united states"):
    print(f"{name.title()} is in {country.title()}")
describe_city("new york")
describe_city("greenville")
describe_city("paris", "france")

#8.6 City Names
print("8.6 City Names:")
def city_country(name, country):
    return f"{name.title()}, {country.title()}"
london = city_country("london", "england")
bonn = city_country("bonn", "germany")
print(london)
print(bonn)
print(city_country("paris", "france"))

#8.7 Album
print("8.7 album: ")
def make_album(artist_name, album_title):
    album = {
        "artist_name": artist_name,
        "album_title": album_title,
    }
    return album
album1 = make_album("Stray Kids", "NOEASY")
album2 = make_album("Japanese Breakfast", "Jubilee")
album3 = make_album("Vitamin String Quartet", "Otaku")
print(album1)
print(album2)
print(album3)

def make_album2(artist_name, album_title, number_of_tracks=None):
    album = {
        "artist_name": artist_name,
        "album_title": album_title,
    }
    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks
    return album
        
album4 = make_album2("Colin Stetson", "The Menu", 14)
print(album4)

#8.8 User Albums
print("8.8 user albums")
active = True
while active:
    print("\nCreate an Album. Please give the artist name and album title. Enter 'q' at anytime to quit")
    name = input("Artist Name: ")
    if name == "q":
        active = False
        break
    title = input("Album Title: ")
    if title == "q":
        active = False
        break
    album = {
        "name": name,
        "title": title,
    }
    print(album)
    
#8.9 Messages
print("8.9 messages:")
def show_messages(list):
    for item in list:
        print(item)
messages = ["good morning sunshine, the earth says hello", "What is the air speed velocity of an unladen swallow?", "honey, where's my supersuit?"]
show_messages(messages)

#8.10 sending messages 
print("8.10 sending messages:")
sent_messages = []
def show_messages(list, sent):
    while list:
        item = list.pop()
        sent.append(item)
        print(item)
        
show_messages(messages, sent_messages)
print(messages)
print(sent_messages)
    
#8.11 Archived Messages
print("8.11 archived messages:")
messages = ["good morning sunshine, the earth says hello", "What is the air speed velocity of an unladen swallow?", "honey, where's my supersuit?"]
sent_messages = []
show_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)

#8.12 sandwiches
print("8.12 sandwiches:")
def make_sandwich(*sandwich_toppings):
    print(f"Making sandwich...\nThis sandwich contains the following:")
    for item in sandwich_toppings:
        print(f"\t-{item}")
    print("Sandwich Complete!")
    
make_sandwich("peanut butter", "jelly")
make_sandwich("turkey", "lettuce", "tomato", "mayo")
make_sandwich("chicken salad")

#8.13 user profile
print("8.13 user profile")
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Mikayla', 'Hubbard', school='Anderson Uiversity', major="Coding", year="Junior")
print(user_profile)

#8.14 cars
print("8.14 cars: ")
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

#8.15 printing models
#normally, this would be at the top, but putting it here for organization's sake
from printing_functions import *

print("8.15 printing models:")
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#8.16 imports
print("8.16 imports")
#normally, this would be at the top
import import_functions as import_functions
import_functions.city_country("Djibouti", "Djibouti")

from import_functions import city_country
print(city_country("Alexandria", "Egypt"))
from import_functions import describe_city as dc
dc("New York")
import import_functions as imfun
imfun.describe_city("Vienna", "Austria")
from import_functions import *
describe_city("Rio de Janero", "brazil")
print(city_country("Indianapolis", "United States"))

#8.17 styling funtions

print("8.17 styling functions: ")

#I shortened/tabbed these to make them more aligned with the styling
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Mikayla', 'Hubbard',  
    school='Anderson Uiversity', major="Coding", year="Junior")
print(user_profile)

messages = ["good morning sunshine, the earth says hello",
            "What is the air speed velocity of an unladen swallow?",
            "honey, where's my supersuit?"]
sent_messages = []
show_messages(messages[:], sent_messages)
print(messages)
print(sent_messages)

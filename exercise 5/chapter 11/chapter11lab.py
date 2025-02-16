#! /usr/bin/python3
#11.1 city country
print("11.1 city country: ")
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

#11.2 population
print("11.2 population")
def city_country_population(city, country, population):
    return f"{city.title()}, {country.title()} - population: {population}"


#ll.3 employee
print("11.3 employee: ")
class Employee:
    def __init__(self, fName, lName, salary):
        self.first_name = fName
        self.last_name = lName
        self.salary = salary
        
    def give_raise(self, amount=""):
        if amount == '':
            self.salary += 5000
        else:
            self.salary += amount
            


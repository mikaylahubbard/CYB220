class Restaurant:
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
    
restaurant4 = Restaurant("Stravinsky's", "Russian")
restaurant4.describe_resaurant()
restaurant4.set_number_served(8)
restaurant4.describe_resaurant() 
restaurant4.increment_number_served(1)
restaurant4.increment_number_served(4)
restaurant4.increment_number_served(2)

restaurant4.describe_resaurant()

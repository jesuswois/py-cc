# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.
class Restaurant:
    """
        Class specified in the exercise
    """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name.title()}, with a cuisine type of {self.cuisine_type}")

    def open_restaurent(self):
        print(f"The restaurant {self.restaurant_name} it's open!")

restaurant_1 = Restaurant("japan finnese","japanese")
restaurant_2 = Restaurant("magic water","thai")
restaurant_3 = Restaurant("eagles","american")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
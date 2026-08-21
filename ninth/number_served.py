# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166) . 
# Add an attribute called number_served with a default value of 0 . Create an 
# instance called restaurant from this class . Print the number of customers the 
# restaurant has served, and then change this value and print it again .
# Add a method called set_number_served() that lets you set the number 
# of customers that have been served . Call this method with a new number and 
# print the value again .
# Add a method called increment_number_served() that lets you increment 
# the number of customers who’ve been served . Call this method with any num
# ber you like that could represent how many customers were served in, say, a 
# day of business .
class Restaurant:
    """
        Class specified in the exercise
    """
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name.title()}, with a cuisine type of {self.cuisine_type}")
        print(f"Clients served: {self.number_served}")
    def open_restaurent(self):
        print(f"The restaurant {self.restaurant_name} it's open!")

    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self):
        self.number_served += 1

restaurant = Restaurant("the mariachis","mexican")
restaurant.describe_restaurant()
restaurant.open_restaurent()

restaurant.set_number_served(1321049)
restaurant.describe_restaurant()
restaurant.increment_number_served()
restaurant.describe_restaurant()